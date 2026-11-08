"""Which Option A Holm conclusions differ between the predeclared raw-logit permutation test and the rank-based
correction? Uses package CSVs only. Writes stats_out/statistician_rank_correction_impact.csv."""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *
pt = pd.read_csv(PKG + '/corrected_20261028_optionA/paired_tests_optionA.csv')
rc = pd.read_csv(ST + '/paired_cluster_effects_rank_corrected.csv')
m = pt.merge(rc[['model_a', 'model_b', 'training_dataset', 'test_dataset', 'permutation_p_original_recomputed']],
             on=['model_a', 'model_b', 'training_dataset', 'test_dataset'])
m = m[m.family_optionA.str.startswith(('RQ1', 'RQ6'))].copy()
for f, g in m.groupby('family_optionA'):
    m.loc[g.index, 'holm_rawlogit_optionA'] = holm(g.permutation_p_original_recomputed.values)
m['conclusion_changed'] = (m.holm_rawlogit_optionA < 0.05) != (m.holm_optionA < 0.05)
m.to_csv(OUT + '/statistician_rank_correction_impact.csv', index=False)
print(m.groupby('family_optionA').conclusion_changed.sum())
