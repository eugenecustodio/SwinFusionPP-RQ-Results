"""Shared loader for the statistician's RQ1 analyses (read-only on package and raw predictions)."""
import glob, os, re
import numpy as np, pandas as pd

SCR = '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad'
RAW = SCR + '/b2dl/Thesis_Code_final_20261004/results/raw_predictions_v020'
PKG = '/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results'
ST = PKG + '/00_Shared/statistics_raw'
OUT = SCR + '/ch4/team/stats_out'
DS = ['ffpp_c23', 'ffpp_c40', 'celeb_df_v2', 'deeperforensics_1_0']
SEED = 20260930
B = 5000


def sig(z):
    return 1 / (1 + np.exp(-z))


def auc(y, s):
    r = pd.Series(s).rank().values
    n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


_op = None
def ops():
    global _op
    if _op is None:
        _op = pd.read_csv(ST + '/source_validation_operating_points_v020.csv')
    return _op


def load_cell(fam, reg, src, tgt):
    """Return DataFrame indexed by sorted video_id with label, clusters, per-seed logits s1..s3, ensemble z,
    plus frozen ensemble threshold (logit scale) and temperature."""
    d = f'{RAW}/{src}_to_{tgt}'
    seeds = []
    for k in (1, 2, 3):
        f = f'{d}/principal_{fam}_{src}_{reg}_s{k}_v002.video_predictions.parquet'
        x = pd.read_parquet(f)
        assert (x.analysis_status == 'analyzed').all()
        seeds.append(x.set_index('video_id').sort_index())
    ids = seeds[0].index
    for s in seeds:
        assert s.index.equals(ids)
    df = seeds[0][['label', 'dependency_cluster', 'source_group', 'global_cluster']].copy()
    for k, s in enumerate(seeds, 1):
        df[f's{k}'] = s['video_logit'].values
        df[f'pred{k}'] = s['predicted_class'].values
    df['z'] = df[['s1', 's2', 's3']].mean(axis=1)
    o = ops()
    e = o[(o.kind == 'three_seed_ensemble') & (o.family == fam) & (o.optimization_regimen == reg)
          & (o.condition == src) & (~o.run_id.str.endswith('__tta'))]
    assert len(e) == 1
    seedthr = []
    for k in (1, 2, 3):
        t = o[(o.kind == 'single_seed') & (o.family == fam) & (o.optimization_regimen == reg)
              & (o.condition == src) & (o.seed_slot == k)]
        assert len(t) == 1
        seedthr.append(float(t.threshold_logit.iloc[0]))
    return df, float(e.threshold_logit.iloc[0]), float(e.temperature.iloc[0]), seedthr


def threshold_metrics(y, pred):
    y = np.asarray(y).astype(int); pred = np.asarray(pred).astype(int)
    tp = int(((pred == 1) & (y == 1)).sum()); tn = int(((pred == 0) & (y == 0)).sum())
    fp = int(((pred == 1) & (y == 0)).sum()); fn = int(((pred == 0) & (y == 1)).sum())
    n = len(y)
    acc = (tp + tn) / n
    prec = tp / (tp + fp) if tp + fp else np.nan
    rec = tp / (tp + fn) if tp + fn else np.nan
    spec = tn / (tn + fp) if tn + fp else np.nan
    f1 = 2 * tp / (2 * tp + fp + fn) if (2 * tp + fp + fn) else np.nan
    bacc = (rec + spec) / 2
    return dict(accuracy=acc, precision=prec, recall=rec, specificity=spec, f1=f1, balanced_accuracy=bacc,
                tp=tp, tn=tn, fp=fp, fn=fn)


def average_precision(y, s):
    """Step-wise AP (sklearn average_precision_score definition)."""
    y = np.asarray(y).astype(int); s = np.asarray(s, float)
    order = np.argsort(-s, kind='mergesort')
    ys, ss = y[order], s[order]
    # distinct thresholds
    distinct = np.r_[np.where(np.diff(ss))[0], len(ss) - 1]
    tps = np.cumsum(ys)[distinct]; fps = (distinct + 1) - tps
    prec = tps / (tps + fps); rec = tps / ys.sum()
    rec_prev = np.r_[0, rec[:-1]]
    return float(np.sum((rec - rec_prev) * prec))


def rankavg(x):
    """Average ranks (scipy.stats.rankdata 'average'), numpy only."""
    x = np.asarray(x)
    sorter = np.argsort(x, kind='mergesort')
    inv = np.empty(sorter.size, dtype=np.intp); inv[sorter] = np.arange(sorter.size)
    xs = x[sorter]
    obs = np.r_[True, xs[1:] != xs[:-1]]
    dense = obs.cumsum()[inv]
    count = np.r_[np.nonzero(obs)[0], len(obs)]
    return 0.5 * (count[dense] + count[dense - 1] + 1)


def fauc(y, s):
    r = rankavg(s)
    n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def cluster_index(cl):
    uniq = sorted(set(cl.tolist()))
    return uniq, [np.flatnonzero(cl == c) for c in uniq]


def strata_of(y, uniq, idx):
    """Package rule ('class-preserving'): strata = clusters with no fake video first, then clusters with a fake."""
    hasf = np.array([y[i].max() == 1 for i in idx])
    return [g for g in (np.flatnonzero(~hasf), np.flatnonzero(hasf)) if len(g)]


def boot_draws(y, cl, seed=SEED, draws=B):
    """Yield video index arrays for each bootstrap draw, reproducing the package's stratified cluster bootstrap."""
    uniq, idx = cluster_index(cl)
    strata = strata_of(y, uniq, idx)
    rng = np.random.default_rng(seed)
    for _ in range(draws):
        pick = np.concatenate([g[rng.integers(0, len(g), len(g))] for g in strata])
        ii = np.concatenate([idx[p] for p in pick])
        yy = y[ii]
        if yy.min() == yy.max():
            continue
        yield ii


def rank_perm_p(y, a, b, cl, seed=SEED + 1, perms=B):
    """Rank-based cluster permutation test (Bandos et al. 2005), same loop/RNG as rerun_paired_tests.py."""
    ra, rb = rankavg(a), rankavg(b)
    obs = fauc(y, ra) - fauc(y, rb)
    uniq = sorted(set(cl.tolist()))
    code = pd.Series(cl).map({c: i for i, c in enumerate(uniq)}).values
    rng = np.random.default_rng(seed)
    extreme = 0
    for _ in range(perms):
        flips = rng.integers(0, 2, len(uniq))
        swap = flips[code].astype(bool)
        pa, pb = np.where(swap, rb, ra), np.where(swap, ra, rb)
        if abs(fauc(y, pa) - fauc(y, pb)) >= abs(obs) - 1e-15:
            extreme += 1
    return obs, (extreme + 1) / (perms + 1)


def holm(ps):
    ps = np.asarray(ps, float)
    order = np.argsort(ps, kind='mergesort')
    adj, run = np.empty(len(ps)), 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run
    return adj
