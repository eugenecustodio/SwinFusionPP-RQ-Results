"""Probe: which bootstrap variant reproduces the package's stored ensemble AUC CI and paired ΔAUC CI?"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *

ens = pd.read_csv(ST + '/three_seed_mean_logit_ensemble.csv'); ens = ens[ens.variant == 'plain']
pair = pd.read_csv(ST + '/paired_cluster_effects.csv')
print(sorted(pd.read_csv(ST + '/cluster_bootstrap_intervals.csv').seed_slot.astype(str).unique()))

def variants(df, col):
    y = df.label.values.astype(int); cl = df[col].values
    uniq = np.array(sorted(set(cl.tolist())))
    idx = {c: np.flatnonzero(cl == c) for c in uniq}
    return y, uniq, idx

def boot(df, scorefn, col='dependency_cluster', mode='integers', seed=SEED, strat=False):
    y, uniq, idx = variants(df, col)
    rng = np.random.default_rng(seed)
    K = len(uniq)
    out = []
    if strat:
        hasf = np.array([y[idx[c]].max() == 1 for c in uniq]); hasr = np.array([y[idx[c]].min() == 0 for c in uniq])
        groups = [np.flatnonzero(hasf), np.flatnonzero(~hasf)]
    for b in range(B):
        if strat:
            pick = np.concatenate([g[rng.integers(0, len(g), len(g))] for g in groups if len(g)])
        elif mode == 'integers':
            pick = rng.integers(0, K, K)
        else:
            pick = rng.choice(K, size=K, replace=True)
        ii = np.concatenate([idx[uniq[p]] for p in pick])
        yy = y[ii]
        if yy.min() == yy.max():
            continue
        out.append(scorefn(yy, ii))
    return np.array(out)

for (fam, reg, src, tgt) in [('swin_b', 'fixed_no_bo', 'ffpp_c23', 'ffpp_c23'), ('swinfusionpp', 'fixed_no_bo', 'celeb_df_v2', 'celeb_df_v2'),
                             ('swinfusionpp', 'fixed_no_bo', 'ffpp_c23', 'deeperforensics_1_0')]:
    df, thr, T, _ = load_cell(fam, reg, src, tgt)
    z = df.z.values
    r = ens[(ens.family == fam) & (ens.optimization_regimen == reg) & (ens.training_dataset == src) & (ens.test_dataset == tgt)].iloc[0]
    print(fam, reg, src, tgt, 'stored AUC', r.roc_auc, 'mine', auc(df.label.values, z), 'stored CI', r.roc_auc_ci_low, r.roc_auc_ci_high)
    for mode, strat in [('integers', False), ('choice', False), ('integers', True)]:
        d = boot(df, lambda yy, ii: auc(yy, z[ii]), mode=mode, strat=strat)
        for q in ['linear']:
            print('   ', mode, 'strat' if strat else '', len(d), np.quantile(d, [0.025, 0.975]))

# paired
for (src, tgt) in [('ffpp_c23', 'ffpp_c23'), ('celeb_df_v2', 'celeb_df_v2')]:
    a, *_ = load_cell('swinfusionpp', 'fixed_no_bo', src, tgt)
    b, *_ = load_cell('swin_b', 'fixed_no_bo', src, tgt)
    za, zb = a.z.values, b.z.values
    r = pair[(pair.model_a == 'swinfusionpp__fixed_no_bo') & (pair.model_b == 'swin_b__fixed_no_bo') & (pair.training_dataset == src) & (pair.test_dataset == tgt)].iloc[0]
    print('pair', src, tgt, 'stored', r.auc_difference, r.ci_low, r.ci_high, r.bootstrap_two_sided_p)
    for mode, strat in [('integers', False), ('choice', False), ('integers', True)]:
        d = boot(a, lambda yy, ii: auc(yy, za[ii]) - auc(yy, zb[ii]), mode=mode, strat=strat)
        print('   ', mode, 'strat' if strat else '', len(d), np.quantile(d, [0.025, 0.975]), 2*min((d<=0).mean(), (d>=0).mean()))
