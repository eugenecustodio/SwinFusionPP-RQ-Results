"""Figure data for the methodologist: fig12_forest.csv (26 principal ΔAUCs) and roc_points.csv (ROC curves +
frozen operating points, 13 cells x 3 fixed-recipe ensembles). Validated against the package before writing."""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_fmt import *

pt = paired_tests()
ens = pd.read_csv(ST + '/three_seed_mean_logit_ensemble.csv'); ens = ens[ens.variant == 'plain']
data = load_all()

# ---- fig12_forest.csv ----
rows, order = [], 0
for panel, cells in [('within', WITHIN), ('transfer', TRANSFER)]:
    for src, tgt in cells:
        for b in ['SwinB', 'VSB']:
            r = get_test(pt, 'SF++F', b, src, tgt)
            fam = r.family_optionA
            df_a = data[('SF++F', src, tgt)]['df']; df_b = data[(b, src, tgt)]['df']
            y = df_a.label.values.astype(int)
            d = fauc(y, df_a.z.values) - fauc(y, df_b.z.values)
            assert abs(d - r.auc_difference) < 1e-12
            order += 1
            rows.append(dict(order=order, panel=panel, family=FAMNAME[fam], training=src, test=tgt,
                             condition_label=LONG[src] if src == tgt else cond(src, tgt), comparator=MLABEL[b],
                             delta_auc=r.auc_difference, ci_low=r.ci_low, ci_high=r.ci_high, raw_p=r.permutation_p_rank,
                             holm_p=r.holm_optionA, holm_significant=bool(r.holm_optionA < 0.05),
                             ci_excludes_zero=bool(r.ci_low > 0 or r.ci_high < 0),
                             delta_str=sgn(r.auc_difference), ci_str=ci(r.ci_low, r.ci_high), raw_p_str=p_raw(r.permutation_p_rank),
                             holm_p_str=p_holm(r.holm_optionA, FAMM[fam])))
f12 = pd.DataFrame(rows)
assert len(f12) == 26 and f12.holm_significant.sum() == 10
f12.to_csv(TAB + '/fig12_forest.csv', index=False)
print('fig12_forest.csv', len(f12), 'rows; significant', int(f12.holm_significant.sum()))

# ---- roc_points.csv ----
def roc_curve_pts(y, s):
    order_ = np.argsort(-s, kind='mergesort')
    ys, ss = y[order_], s[order_]
    distinct = np.r_[np.where(np.diff(ss))[0], len(ss) - 1]
    tps = np.cumsum(ys)[distinct]; fps = (distinct + 1) - tps
    P, N = ys.sum(), len(ys) - ys.sum()
    return np.r_[0, fps / N], np.r_[0, tps / P], np.r_[np.inf, ss[distinct]]

rrows = []
for src, tgt in CELLS:
    for mk in ['SF++F', 'SwinB', 'VSB']:
        D = data[(mk, src, tgt)]; df = D['df']
        y = df.label.values.astype(int); z = df.z.values
        fpr, tpr, th = roc_curve_pts(y, z)
        a = fauc(y, z)
        assert abs(np.trapezoid(tpr, fpr) - a) < 1e-12, (mk, src, tgt)
        e = ens[(ens.family == MODELS[mk][0]) & (ens.optimization_regimen == MODELS[mk][1]) & (ens.training_dataset == src) & (ens.test_dataset == tgt)].iloc[0]
        assert abs(a - e.roc_auc) < 1e-12
        tm = threshold_metrics(y, df.pred.values)
        op_fpr, op_tpr = tm['fp'] / (tm['fp'] + tm['tn']), tm['tp'] / (tm['tp'] + tm['fn'])
        assert abs(op_tpr - e.recall) < 1e-12 and abs(op_fpr - (1 - e.specificity)) < 1e-12
        # operating point lies on the curve
        assert np.any((np.abs(fpr - op_fpr) < 1e-12) & (np.abs(tpr - op_tpr) < 1e-12))
        base = dict(panel='within' if src == tgt else 'transfer', training=src, test=tgt,
                    cell_label=LONG[src] if src == tgt else cond(src, tgt), model=MLABEL[mk], auc=a, auc_str=num(a))
        for f_, t_, h_ in zip(fpr, tpr, th):
            rrows.append(dict(base, point_type='curve', fpr=f_, tpr=t_, threshold_logit=h_))
        rrows.append(dict(base, point_type='operating_point', fpr=op_fpr, tpr=op_tpr, threshold_logit=D['thr']))
roc = pd.DataFrame(rrows)
roc.to_csv(TAB + '/roc_points.csv', index=False)
print('roc_points.csv', len(roc), 'rows;', roc[roc.point_type == 'operating_point'].shape[0], 'operating points; all AUCs and operating points validated')
