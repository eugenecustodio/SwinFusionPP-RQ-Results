"""Round 2 checks: (1) identify the formula of the package's bootstrap_two_sided_p; (2) Holm decisions from
bootstrap p vs rank p in Option A families; (3) configured-system/optimization decisions under the
pre-scoring and pooled partitions. Writes stats_out/statistician_r2_bootstrap_p_check.csv."""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *
pt = pd.read_csv(PKG + '/corrected_20261028_optionA/paired_tests_optionA.csv')
rc = pd.read_csv(ST + '/paired_cluster_effects_rank_corrected.csv')
m = pt.merge(rc[['model_a', 'model_b', 'training_dataset', 'test_dataset', 'bootstrap_two_sided_p']],
             on=['model_a', 'model_b', 'training_dataset', 'test_dataset'])
# (1) formula probe on 6 tests
cands = {}
for r in m.head(12).itertuples():
    fa, ra = r.model_a.split('__'); fb, rb = r.model_b.split('__')
    A, *_ = load_cell(fa, ra, r.training_dataset, r.test_dataset); Bm, *_ = load_cell(fb, rb, r.training_dataset, r.test_dataset)
    y = A.label.values.astype(int)
    d = np.array([fauc(y[ii], A.z.values[ii]) - fauc(y[ii], Bm.z.values[ii]) for ii in boot_draws(y, A.dependency_cluster.values)])
    f = {'2min_le_ge': 2 * min((d <= 0).mean(), (d >= 0).mean()), '2min_lt_gt': 2 * min((d < 0).mean(), (d > 0).mean()),
         'centered_abs': (np.abs(d - d.mean()) >= abs(r.auc_difference)).mean(),
         'centered_abs_obs': (np.abs(d - r.auc_difference) >= abs(r.auc_difference)).mean(),
         '2min_lt_gt_cap1': min(1, 2 * min((d < 0).mean(), (d > 0).mean()))}
    for k, v in f.items():
        cands.setdefault(k, []).append(abs(v - r.bootstrap_two_sided_p) < 1e-12)
print({k: f'{sum(v)}/{len(v)}' for k, v in cands.items()})
# (2) Holm decisions
for fam, g in m.groupby('family_optionA'):
    m.loc[g.index, 'holm_boot_optionA'] = holm(g.bootstrap_two_sided_p.values)
m['same_decision'] = (m.holm_boot_optionA < 0.05) == (m.holm_optionA < 0.05)
print('bootstrap-p Holm decisions identical:', int(m.same_decision.sum()), '/', len(m), '| bootstrap p == 0:', int((m.bootstrap_two_sided_p == 0).sum()))
m.to_csv(OUT + '/statistician_r2_bootstrap_p_check.csv', index=False)
# (3) partitions for non-architecture families
for c in ['holm_previous_family', 'holm_sensitivity_pooled']:
    ch = m[(m.holm_optionA < 0.05) != (m[c] < 0.05)]
    print(c, 'changed:', len(ch)); print(ch[['family_optionA', 'model_a', 'model_b', 'training_dataset', 'test_dataset', 'holm_optionA', c]].to_string())
