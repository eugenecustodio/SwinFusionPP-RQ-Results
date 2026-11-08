#!/usr/bin/env python3
"""Publication figure: paired ΔROC-AUC of SwinFusion++ against Swin-B and Video Swin-B.

Usage:  python paper_figure.py
Needs:  matplotlib, numpy
Writes: figures_recreated/paper/fig_paired_delta_auc.{pdf,png}
        figures_recreated/paper/paired_delta_auc_stats.csv

Intervals are the package's 95% class-preserving cluster-bootstrap intervals
(00_Shared/statistics_raw/paired_cluster_effects.csv). Filled markers mark
Holm-adjusted p < 0.05 within each family (RQ1 = within-dataset, RQ6 = transfer).

P_SOURCE selects the p-values behind the markers:
  "bootstrap"     two-sided cluster-bootstrap p from the same CSV (interim choice).
  "permutation"   the package's cluster permutation p. Not used: that test swaps raw
                  logits between models whose logit scales differ, so it is unreliable.
  <path to CSV>   a corrected file with columns family_rq, model_b, training_dataset,
                  test_dataset, p  (e.g. a rank-based permutation re-run).
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
OUT = HERE / "paper"
P_SOURCE = "bootstrap"
ALPHA = 0.05
BOOT_FLOOR = 2 / 5000  # smallest non-zero two-sided p with 5,000 draws

INK, INK2, MUTED, GRID, AXIS, BAND, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7", "#f5f4f1", "#ffffff"
BASELINES = {  # comparator -> (label, colour, marker); colours follow the model across all figures
    "swin_b__fixed_no_bo": ("vs Swin-B", "#eb6834", "s"),
    "video_swin_b__fixed_no_bo": ("vs Video Swin-B", "#1baf7a", "^"),
}
SHORT = {"ffpp_c23": "C23", "ffpp_c40": "C40", "celeb_df_v2": "CDF", "deeperforensics_1_0": "DFo"}
WITHIN = ["ffpp_c23", "ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]
TRANSFER = [("ffpp_c23", "ffpp_c40"), ("ffpp_c23", "celeb_df_v2"), ("ffpp_c23", "deeperforensics_1_0"),
            ("celeb_df_v2", "ffpp_c23"), ("celeb_df_v2", "ffpp_c40"), ("celeb_df_v2", "deeperforensics_1_0"),
            ("deeperforensics_1_0", "ffpp_c23"), ("deeperforensics_1_0", "ffpp_c40"),
            ("deeperforensics_1_0", "celeb_df_v2")]

plt.rcParams.update({
    "font.family": "Liberation Sans",   # Arial-metric; embeds as TrueType
    "font.size": 7,
    "axes.linewidth": 0.6,
    "axes.edgecolor": AXIS,
    "axes.labelcolor": INK,
    "xtick.color": AXIS,
    "ytick.color": AXIS,
    "xtick.labelcolor": INK2,
    "ytick.labelcolor": INK,
    "xtick.major.width": 0.6,
    "xtick.major.size": 2.5,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 7,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "axes.unicode_minus": True,
})


def read(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, run = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run
    return adj


def load():
    rows = [r for r in read(PKG / "00_Shared" / "statistics_raw" / "paired_cluster_effects.csv")
            if r["family_rq"] in ("RQ1", "RQ6") and r["model_a"] == "swinfusionpp__dataset_specific_bo"]
    if P_SOURCE == "bootstrap":
        raw = {id(r): max(float(r["bootstrap_two_sided_p"]), BOOT_FLOOR) for r in rows}
    elif P_SOURCE == "permutation":
        raw = {id(r): float(r["permutation_p"]) for r in rows}
    else:
        ext = {(x["family_rq"], x["model_b"], x["training_dataset"], x["test_dataset"]): float(x["p"])
               for x in read(P_SOURCE)}
        raw = {id(r): ext[(r["family_rq"], r["model_b"], r["training_dataset"], r["test_dataset"])] for r in rows}
    stats = {}
    for fam in ("RQ1", "RQ6"):
        members = [r for r in rows if r["family_rq"] == fam]
        for r, p_adj in zip(members, holm([raw[id(r)] for r in members])):
            stats[(r["model_b"], r["training_dataset"], r["test_dataset"])] = dict(
                family=fam, d=float(r["auc_difference"]), lo=float(r["ci_low"]), hi=float(r["ci_high"]),
                p=raw[id(r)], p_holm=p_adj, p_perm_holm_original=float(r["holm_adjusted_p"]),
                clusters=int(r["clusters"]), videos=int(r["eligible_videos"]))
    return stats


def panel(ax, conditions, stats, labels, title, lim, ticks, decimals):
    n = len(conditions)
    for y in range(n):
        if y % 2 == 0:
            ax.axhspan(y - 0.5, y + 0.5, color=BAND, lw=0, zorder=0)
    ax.axvline(0, color=MUTED, lw=0.7, zorder=1)
    for k, (base, (lbl, col, mk)) in enumerate(BASELINES.items()):
        dy = -0.17 if k == 0 else 0.17
        for y, (tr, te) in enumerate(conditions):
            s = stats[(base, tr, te)]
            sig = s["p_holm"] < ALPHA
            ax.plot([s["lo"], s["hi"]], [y + dy] * 2, color=col, lw=1.1, solid_capstyle="butt", zorder=2)
            ax.plot(s["d"], y + dy, marker=mk, ms=4.6 if mk == "s" else 5.2, ls="none", zorder=3,
                    mfc=col if sig else SURFACE, mec=col, mew=1.0)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_yticks(range(n), labels)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.set_xlim(-lim, lim)
    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _: "0" if abs(v) < 1e-12 else f"{v:+.{decimals}f}".replace("-", "−")))
    ax.grid(axis="x", color=GRID, lw=0.45, zorder=0)
    ax.set_axisbelow(True)
    ax.set_title(title, loc="left", fontsize=7.5, fontweight="bold", color=INK, pad=11)
    ax.text(0.0, 1.012, "← baseline better", transform=ax.transAxes, fontsize=6, color=MUTED,
            ha="left", va="bottom")
    ax.text(1.0, 1.012, "SwinFusion++ better →", transform=ax.transAxes, fontsize=6, color=MUTED,
            ha="right", va="bottom")


def main():
    stats = load()
    OUT.mkdir(parents=True, exist_ok=True)
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 4.55),
                                     gridspec_kw=dict(height_ratios=[len(WITHIN), len(TRANSFER)], hspace=0.42))
    fig.subplots_adjust(top=0.865)
    panel(ax_a, [(d, d) for d in WITHIN], stats, [SHORT[d] for d in WITHIN],
          "(a) Within-dataset", 0.0145, [-0.01, -0.005, 0, 0.005, 0.01], 3)
    panel(ax_b, TRANSFER, stats, [f"{SHORT[s]} → {SHORT[t]}" for s, t in TRANSFER],
          "(b) Cross-dataset, frozen transfer", 0.235, [-0.2, -0.1, 0, 0.1, 0.2], 1)
    ax_b.set_xlabel("ΔROC-AUC (SwinFusion++ − baseline), 95% CI", fontsize=7, labelpad=3)
    handles = [Line2D([], [], color=c, marker=m, ms=4.6 if m == "s" else 5.2, lw=1.1, mfc=c, mec=c, label=l)
               for l, c, m in BASELINES.values()]
    handles += [Line2D([], [], color=INK2, marker="o", ms=4.6, ls="none", mfc=INK2, mec=INK2,
                       label="Holm-adjusted p < 0.05"),
                Line2D([], [], color=INK2, marker="o", ms=4.6, ls="none", mfc=SURFACE, mec=INK2, mew=1.0,
                       label="Not significant")]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1.0), ncol=2, frameon=False,
               fontsize=6.5, handlelength=1.6, handletextpad=0.5, columnspacing=1.2, borderaxespad=0)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"fig_paired_delta_auc.{ext}")
    plt.close(fig)
    with open(OUT / "paired_delta_auc_stats.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["family_rq", "baseline", "training_dataset", "test_dataset", "delta_auc", "ci_low", "ci_high",
                    "p_" + (P_SOURCE if P_SOURCE in ("bootstrap", "permutation") else "rank_permutation"), "p_holm", "significant", "p_holm_original_permutation", "clusters", "videos"])
        for (base, tr, te), s in sorted(stats.items(), key=lambda kv: (kv[1]["family"], kv[0][1], kv[0][2], kv[0][0])):
            w.writerow([s["family"], base, tr, te, f"{s['d']:.4f}", f"{s['lo']:.4f}", f"{s['hi']:.4f}",
                        f"{s['p']:.4f}", f"{s['p_holm']:.4f}", s["p_holm"] < ALPHA,
                        f"{s['p_perm_holm_original']:.4f}", s["clusters"], s["videos"]])
    print("wrote", [str(p.relative_to(PKG)) for p in sorted(OUT.iterdir())])


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:  # optional override, e.g. paper/rank_permutation_p.csv
        P_SOURCE = sys.argv[1]
    main()
