#!/usr/bin/env python3
"""Re-run the paired ensemble tests with a rank-based cluster permutation test.

Usage:  python rerun_paired_tests.py <path/to/raw_predictions_v020>
Needs:  numpy, scipy, pyarrow
Writes: figures_recreated/paper/rank_permutation_results.csv   (all comparisons, both tests)
        figures_recreated/paper/rank_permutation_p.csv         (input for paper_figure.py P_SOURCE)

Mirrors scripts/rq1_rq6_early_v020.py (ensembles_and_stats + paired_tests) and
scripts/cluster_stats_v020.py exactly (same video order, same seeds, same 5,000
permutations), with one change: each model's ensemble logits are converted to
within-model ranks before the cluster-level swap (Bandos, Rockette & Gur, 2005).
ROC-AUC is rank-invariant, so every observed ΔAUC is unchanged; only the null
distribution is fixed. The original raw-logit test is recomputed alongside as a
self-check: its p-values must equal the package CSV before the new ones are trusted.
Only aggregate statistics are written.
"""
import csv
import re
import sys
from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
from scipy.stats import rankdata

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
OUT = HERE / "paper"
PERMUTATIONS = 5000
SEED = 20260930

PRIMARY = [("swinfusionpp__dataset_specific_bo", "swin_b__fixed_no_bo"),
           ("swinfusionpp__dataset_specific_bo", "video_swin_b__fixed_no_bo")]
SECONDARY = [("swinfusionpp__fixed_no_bo", "swin_b__fixed_no_bo"),
             ("swinfusionpp__fixed_no_bo", "video_swin_b__fixed_no_bo"),
             ("swinfusionpp__dataset_specific_bo", "swinfusionpp__fixed_no_bo")]
CONTROLS = [("swinfusionpp__fixed_no_bo", "topology_control__fixed_no_bo"),
            ("swinfusionpp__fixed_no_bo", "capacity_control__fixed_no_bo")]
RUN = re.compile(r"^principal_(?P<family>.+)_(?P<cond>ffpp_c23|ffpp_c40|celeb_df_v2|deeperforensics_1_0)_"
                 r"(?P<regimen>fixed_no_bo|dataset_specific_bo)_s(?P<slot>[123])_v002$")


def family_of(pair, within):
    if pair in PRIMARY:
        return "RQ1" if within else "RQ6"
    if pair in SECONDARY:
        return "RQ1_secondary" if within else "RQ6_secondary"
    return "RQ4_controls" if within else "RQ4_controls_transfer"


def auc(labels, scores):
    """Mann-Whitney ROC-AUC with average ranks for ties (identical to sklearn's roc_auc_score)."""
    r = rankdata(scores)
    pos = labels == 1
    n1 = pos.sum()
    n0 = len(labels) - n1
    return (r[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def permutation_p(labels, a, b, clusters, seed=SEED + 1, permutations=PERMUTATIONS):
    """Same loop and RNG stream as cluster_stats_v020.cluster_permutation_test."""
    observed = auc(labels, a) - auc(labels, b)
    unique = sorted(set(clusters.tolist()))
    index = {c: np.flatnonzero(clusters == c) for c in unique}
    rng = np.random.default_rng(seed)
    extreme = 0
    for _ in range(permutations):
        swap = np.zeros(len(labels), dtype=bool)
        for c, flip in zip(unique, rng.integers(0, 2, len(unique))):
            if flip:
                swap[index[c]] = True
        pa, pb = np.where(swap, b, a), np.where(swap, a, b)
        if abs(auc(labels, pa) - auc(labels, pb)) >= abs(observed) - 1e-15:
            extreme += 1
    return observed, (extreme + 1) / (permutations + 1)


def holm(ps):
    order = np.argsort(ps)
    adj, run = np.empty(len(ps)), 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run
    return adj.tolist()


def load_ensembles(raw_dir):
    groups = {}
    for path in sorted(Path(raw_dir).glob("*_to_*/*.video_predictions.parquet")):
        run_id = path.name[: -len(".video_predictions.parquet")]
        if run_id.endswith("__tta"):
            continue
        m = RUN.match(run_id)
        if not m:
            continue
        source, target = path.parent.name.split("_to_")
        key = f"{m['family']}__{m['regimen']}"
        groups.setdefault((key, source, target), {})[int(m["slot"])] = pq.read_table(path).to_pylist()
    ensembles = {}
    for (key, source, target), seeds in groups.items():
        if sorted(seeds) != [1, 2, 3]:
            continue  # single-seed runs (Tier B) are not part of these families
        base = {p["video_id"]: p for p in seeds[1]}
        ids = sorted(base)
        labels = np.array([base[i]["label"] for i in ids])
        clusters = np.array([base[i]["dependency_cluster"] for i in ids])
        logits = [np.array([{p["video_id"]: p["video_logit"] for p in seeds[s]}[i] for i in ids]) for s in (1, 2, 3)]
        ensembles[(key, source, target)] = (ids, labels, clusters, np.mean(logits, axis=0))
    return ensembles


def main(raw_dir):
    if not Path(raw_dir).is_dir() or not any(Path(raw_dir).glob("*_to_*/*.video_predictions.parquet")):
        sys.exit(f"No prediction files found in {raw_dir}. Expected <source>_to_<target>/*.video_predictions.parquet "
                 f"(was the download step run with real credentials?).")
    ensembles = load_ensembles(raw_dir)
    print(f"loaded {len(ensembles)} three-seed ensembles")
    reference = {(r["family_rq"], r["model_a"], r["model_b"], r["training_dataset"], r["test_dataset"]): r
                 for r in csv.DictReader(open(PKG / "00_Shared" / "statistics_raw" / "paired_cluster_effects.csv"))}
    rows = []
    for key_a, key_b in PRIMARY + SECONDARY + CONTROLS:
        for (key, source, target), (ids, labels, clusters, a) in sorted(ensembles.items()):
            if key != key_a or (key_b, source, target) not in ensembles:
                continue
            ids_b, _, _, b = ensembles[(key_b, source, target)]
            if ids_b != ids:
                raise RuntimeError("paired_video_sets_differ")
            fam = family_of((key_a, key_b), source == target)
            obs, p_raw = permutation_p(labels, a, b, clusters)
            _, p_rank = permutation_p(labels, rankdata(a), rankdata(b), clusters)
            ref = reference[(fam, key_a, key_b, source, target)]
            rows.append(dict(family_rq=fam, model_a=key_a, model_b=key_b, training_dataset=source, test_dataset=target,
                             auc_difference=obs, ci_low=float(ref["ci_low"]), ci_high=float(ref["ci_high"]),
                             bootstrap_two_sided_p=float(ref["bootstrap_two_sided_p"]),
                             permutation_p_original_csv=float(ref["permutation_p"]),
                             permutation_p_original_recomputed=p_raw, permutation_p_rank=p_rank,
                             check_delta=abs(obs - float(ref["auc_difference"])) < 1e-9,
                             check_original_p=abs(p_raw - float(ref["permutation_p"])) < 1e-12,
                             clusters=len(set(clusters.tolist())), videos=len(ids)))
            print(f"{fam:22} {key_a[:24]:24} vs {key_b[:26]:26} {source:>20} -> {target:<20} "
                  f"d={obs:+.4f}  p_orig={p_raw:.4f}  p_rank={p_rank:.4f}", flush=True)
    for fam in sorted({r["family_rq"] for r in rows}):
        members = [r for r in rows if r["family_rq"] == fam]
        for r, adj in zip(members, holm([r["permutation_p_rank"] for r in members])):
            r["holm_rank"] = adj
        for r, adj in zip(members, holm([r["permutation_p_original_recomputed"] for r in members])):
            r["holm_original"] = adj
    ok_d = all(r["check_delta"] for r in rows)
    ok_p = all(r["check_original_p"] for r in rows)
    print(f"\nself-check: {len(rows)} comparisons | ΔAUC matches CSV: {ok_d} | original p reproduced: {ok_p}")
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "rank_permutation_results.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    with open(OUT / "rank_permutation_p.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["family_rq", "model_b", "training_dataset", "test_dataset", "p"])
        for r in rows:
            if r["family_rq"] in ("RQ1", "RQ6"):
                w.writerow([r["family_rq"], r["model_b"], r["training_dataset"], r["test_dataset"], r["permutation_p_rank"]])
    if not (ok_d and ok_p):
        print("WARNING: reconstruction does not match the package; do not use the rank p-values.")
        sys.exit(2)
    changed = [r for r in rows if (r["holm_rank"] < 0.05) != (r["holm_original"] < 0.05)]
    print(f"conclusions that change at Holm 0.05: {len(changed)}")
    for r in changed:
        print(f"  {r['family_rq']:22} {r['model_a'][:24]} vs {r['model_b'][:26]} {r['training_dataset']} -> "
              f"{r['test_dataset']}: Holm original {r['holm_original']:.3f} -> rank {r['holm_rank']:.3f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
