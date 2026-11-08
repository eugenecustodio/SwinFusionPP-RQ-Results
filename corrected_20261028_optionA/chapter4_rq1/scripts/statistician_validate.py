"""Step 1: prove the loader and resampling code reproduce the package before any new number is reported.
Checks, for the 65 RQ1/RQ6 paired tests in paired_tests_optionA.csv: ΔAUC, paired cluster-bootstrap CI and
rank-permutation p (all exact), and the Option A Holm values. Also checks the 39 ensemble AUC CIs of the
fixed-recipe Swin-B / Video Swin-B / SwinFusion++ cells and the per-seed AUCs (plain, full_test).
Writes stats_out/statistician_validation.csv."""
import sys, time
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *

t0 = time.time()
pt = pd.read_csv(PKG + '/corrected_20261028_optionA/paired_tests_optionA.csv')
pt = pt[pt.family_optionA.str.startswith(('RQ1', 'RQ6'))].copy()
ens = pd.read_csv(ST + '/three_seed_mean_logit_ensemble.csv'); ens = ens[ens.variant == 'plain']
seedm = pd.read_csv(ST + '/heldout_seed_metrics_rq1_rq6.csv')
seedm = seedm[(seedm.variant == 'plain') & (seedm.subset == 'full_test')]
cache = {}
def cell(key, src, tgt):
    fam, reg = key.split('__')
    k = (fam, reg, src, tgt)
    if k not in cache:
        cache[k] = load_cell(fam, reg, src, tgt)
    return cache[k]

rows = []
for _, r in pt.iterrows():
    A, *_ = cell(r.model_a, r.training_dataset, r.test_dataset)
    Bm, *_ = cell(r.model_b, r.training_dataset, r.test_dataset)
    assert A.index.equals(Bm.index) and (A.label == Bm.label).all()
    y = A.label.values.astype(int); cl = A.dependency_cluster.values
    za, zb = A.z.values, Bm.z.values
    d = np.array([fauc(y[ii], za[ii]) - fauc(y[ii], zb[ii]) for ii in boot_draws(y, cl)])
    lo, hi = np.quantile(d, [0.025, 0.975])
    obs, p = rank_perm_p(y, za, zb, cl)
    rows.append(dict(check='paired_test', family=r.family_optionA, model_a=r.model_a, model_b=r.model_b,
                     training=r.training_dataset, test=r.test_dataset,
                     stored_delta=r.auc_difference, my_delta=obs, stored_ci_low=r.ci_low, my_ci_low=lo,
                     stored_ci_high=r.ci_high, my_ci_high=hi, stored_p=r.permutation_p_rank, my_p=p,
                     ok=bool(abs(obs - r.auc_difference) < 1e-12 and abs(lo - r.ci_low) < 1e-12 and abs(hi - r.ci_high) < 1e-12 and abs(p - r.permutation_p_rank) < 1e-12)))
val = pd.DataFrame(rows)
# Holm within Option A families
for fam, g in val.groupby('family'):
    val.loc[g.index, 'my_holm'] = holm(g.my_p.values)
val = val.merge(pt[['family_optionA', 'model_a', 'model_b', 'training_dataset', 'test_dataset', 'holm_optionA']]
                .rename(columns={'family_optionA': 'family', 'training_dataset': 'training', 'test_dataset': 'test'}),
                on=['family', 'model_a', 'model_b', 'training', 'test'])
val['ok'] = val.ok & (abs(val.my_holm - val.holm_optionA) < 1e-12)

erows = []
for _, r in ens[ens.family.isin(['swin_b', 'video_swin_b', 'swinfusionpp'])].iterrows():
    A, thr, T, st = cell(f'{r.family}__{r.optimization_regimen}', r.training_dataset, r.test_dataset)
    y = A.label.values.astype(int); z = A.z.values
    a = np.array([fauc(y[ii], z[ii]) for ii in boot_draws(y, A.dependency_cluster.values)])
    lo, hi = np.quantile(a, [0.025, 0.975])
    ok = abs(fauc(y, z) - r.roc_auc) < 1e-12 and abs(lo - r.roc_auc_ci_low) < 1e-12 and abs(hi - r.roc_auc_ci_high) < 1e-12
    sm = seedm[(seedm.family == r.family) & (seedm.optimization_regimen == r.optimization_regimen)
               & (seedm.training_dataset == r.training_dataset) & (seedm.test_dataset == r.test_dataset)].sort_values('seed_slot')
    mine = [fauc(y, A[f's{k}'].values) for k in (1, 2, 3)]
    ok_seed = np.allclose(mine, sm.roc_auc.values, atol=1e-12) and abs(np.mean(mine) - r.seed_auc_mean) < 1e-12 and abs(np.std(mine, ddof=1) - r.seed_auc_sd) < 1e-12
    erows.append(dict(check='ensemble_auc_ci_and_seed_auc', family=r.family, model_a=f'{r.family}__{r.optimization_regimen}',
                      training=r.training_dataset, test=r.test_dataset, stored_delta=r.roc_auc, my_delta=fauc(y, z),
                      stored_ci_low=r.roc_auc_ci_low, my_ci_low=lo, stored_ci_high=r.roc_auc_ci_high, my_ci_high=hi,
                      ok=bool(ok and ok_seed)))
out = pd.concat([val, pd.DataFrame(erows)], ignore_index=True)
out.to_csv(OUT + '/statistician_validation.csv', index=False)
print(out.groupby('check').ok.agg(['size', 'sum']))
print('failures:'); print(out[~out.ok][['check', 'family', 'model_a', 'training', 'test']])
print(f'{time.time() - t0:.0f}s')
