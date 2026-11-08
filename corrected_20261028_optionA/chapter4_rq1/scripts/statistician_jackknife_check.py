"""Diagnostic: delete-one-cluster jackknife SE vs stratified cluster-bootstrap SE of ΔAUC, for all 65 RQ1/RQ6 tests.
A ratio well above 1 indicates the percentile bootstrap interval is likely too narrow (few effective clusters).
Writes stats_out/statistician_jackknife_vs_bootstrap.csv."""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *
tm = pd.read_csv(OUT + '/statistician_threshold_metrics.csv')
tm = tm[(tm.kind == 'paired_delta') & (tm.metric == 'auc')]
M = {'SF++F': ('swinfusionpp', 'fixed_no_bo'), 'SwinB': ('swin_b', 'fixed_no_bo'), 'VSB': ('video_swin_b', 'fixed_no_bo'), 'SF++BO': ('swinfusionpp', 'dataset_specific_bo')}
rows = []
for r in tm.itertuples():
    A, *_ = load_cell(*M[r.model], r.training, r.test); Bm, *_ = load_cell(*M[r.versus], r.training, r.test)
    y = A.label.values.astype(int); cl = A.dependency_cluster.values
    uniq = sorted(set(cl.tolist()))
    th = []
    for c in uniq:
        k = cl != c
        th.append(fauc(y[k], A.z.values[k]) - fauc(y[k], Bm.z.values[k]))
    th = np.array(th); G = len(uniq)
    se_j = np.sqrt((G - 1) / G * ((th - th.mean()) ** 2).sum())
    rows.append(dict(family=r.family, training=r.training, test=r.test, model=r.model, versus=r.versus, clusters=G,
                     delta_auc=r.estimate, se_boot=r.se_boot, se_jackknife=se_j, ratio_jack_over_boot=se_j / r.se_boot,
                     boot_ci_low=r.ci_low, boot_ci_high=r.ci_high))
d = pd.DataFrame(rows)
d.to_csv(OUT + '/statistician_jackknife_vs_bootstrap.csv', index=False)
print(d.groupby('test').ratio_jack_over_boot.describe().round(3))
