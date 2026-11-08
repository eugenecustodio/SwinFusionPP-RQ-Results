"""Supplementary RQ1 analyses (post hoc, statistician round 1). Run statistician_validate.py first.
All resampling reuses the package's stratified dependency-cluster bootstrap (seed 20260930, 5,000 draws) and the
rank-based cluster permutation (seed 20260931, 5,000 permutations) unless stated. Ensemble = mean of 3 seed logits,
decision = z >= frozen source-validation ensemble threshold (reproduces all 52 stored confusion matrices).
Outputs in stats_out/:
  statistician_threshold_metrics.csv     per-model point + 95% CI, and paired Δ + 95% CI (Acc, Prec, Rec, F1, Spec)
  statistician_within_sensitivity.csv    SE, minimum detectable ΔAUC and headroom for the 8 within-dataset tests
  statistician_dfo_global_cluster.csv    DeeperForensics-target tests re-run with global_cluster (175 clusters)
  statistician_holm_partitions.csv       26 architecture tests under three Holm partitions
  statistician_seed_robustness.csv       cross-seed sign agreement of ΔAUC
  statistician_cdf_loo_identity.csv      Celeb-DF-target tests with each fake-bearing identity cluster removed
  statistician_mean_transfer.csv         unweighted mean transfer AUC with a joint cluster-bootstrap CI
"""
import sys, time
from statistics import NormalDist
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *

t0 = time.time()
CELLS = [(d, d) for d in DS] + [('ffpp_c23', t) for t in ['ffpp_c40', 'celeb_df_v2', 'deeperforensics_1_0']] + \
        [('celeb_df_v2', t) for t in ['ffpp_c23', 'ffpp_c40', 'deeperforensics_1_0']] + \
        [('deeperforensics_1_0', t) for t in ['ffpp_c23', 'ffpp_c40', 'celeb_df_v2']]
MODELS = {'SF++F': ('swinfusionpp', 'fixed_no_bo'), 'SwinB': ('swin_b', 'fixed_no_bo'),
          'VSB': ('video_swin_b', 'fixed_no_bo'), 'SF++BO': ('swinfusionpp', 'dataset_specific_bo')}
ARCH = [('SF++F', 'SwinB'), ('SF++F', 'VSB')]
CONF = [('SF++BO', 'SwinB'), ('SF++BO', 'VSB')]
OPT = [('SF++BO', 'SF++F')]
MET = ['accuracy', 'precision', 'recall', 'specificity', 'f1']
data = {}
for src, tgt in CELLS:
    for m, (fam, reg) in MODELS.items():
        df, thr, T, st = load_cell(fam, reg, src, tgt)
        df['pred'] = (df.z.values >= thr).astype(int)
        data[(m, src, tgt)] = (df, thr, st)

def fam_name(src, tgt, kind):
    return {'arch': 'RQ1_architecture', 'conf': 'RQ1_configured_system', 'opt': 'RQ1_optimization_effect'}[kind] if src == tgt else \
           {'arch': 'RQ6_architecture', 'conf': 'RQ6_configured_system', 'opt': 'RQ6_optimization_effect'}[kind]

# ---------------- 1. threshold metrics: per-model and paired-difference CIs (same draws as ΔAUC) ----------------
tm_rows, sens_rows = [], []
for src, tgt in CELLS:
    base = data[('SF++F', src, tgt)][0]
    y = base.label.values.astype(int); cl = base.dependency_cluster.values
    preds = {m: data[(m, src, tgt)][0].pred.values for m in MODELS}
    zs = {m: data[(m, src, tgt)][0].z.values for m in MODELS}
    for m in MODELS:
        assert data[(m, src, tgt)][0].index.equals(base.index)
    point = {m: threshold_metrics(y, preds[m]) for m in MODELS}
    draws = {m: {k: [] for k in MET + ['auc']} for m in MODELS}
    for ii in boot_draws(y, cl):
        yy = y[ii]
        for m in MODELS:
            tmv = threshold_metrics(yy, preds[m][ii])
            for k in MET:
                draws[m][k].append(tmv[k])
            draws[m]['auc'].append(fauc(yy, zs[m][ii]))
    draws = {m: {k: np.array(v, float) for k, v in dd.items()} for m, dd in draws.items()}
    for m in MODELS:
        for k in MET + ['auc']:
            v = draws[m][k]
            est = point[m][k] if k != 'auc' else fauc(y, zs[m])
            tm_rows.append(dict(kind='per_model', training=src, test=tgt, model=m, versus='', metric=k, estimate=est,
                                ci_low=np.nanquantile(v, 0.025), ci_high=np.nanquantile(v, 0.975),
                                undefined_draws=int(np.isnan(v).sum()), clusters=len(set(cl.tolist())), videos=len(y)))
    for kind, pairs in [('arch', ARCH), ('conf', CONF), ('opt', OPT)]:
        for a, b in pairs:
            for k in MET + ['auc']:
                v = draws[a][k] - draws[b][k]
                est = (point[a][k] - point[b][k]) if k != 'auc' else fauc(y, zs[a]) - fauc(y, zs[b])
                tm_rows.append(dict(kind='paired_delta', family=fam_name(src, tgt, kind), training=src, test=tgt, model=a,
                                    versus=b, metric=k, estimate=est, ci_low=np.nanquantile(v, 0.025),
                                    ci_high=np.nanquantile(v, 0.975), se_boot=np.nanstd(v, ddof=1),
                                    undefined_draws=int(np.isnan(v).sum()), clusters=len(set(cl.tolist())), videos=len(y),
                                    ci_excludes_zero=bool(np.nanquantile(v, 0.025) > 0 or np.nanquantile(v, 0.975) < 0)))
            if kind == 'arch' and src == tgt:
                v = draws[a]['auc'] - draws[b]['auc']
                se = np.std(v, ddof=1)
                zb = NormalDist().inv_cdf(0.80)
                sens_rows.append(dict(test=tgt, model=a, versus=b, clusters=len(set(cl.tolist())), videos=len(y),
                                      auc_baseline=fauc(y, zs[b]), headroom_1_minus_auc_baseline=1 - fauc(y, zs[b]),
                                      delta_auc=fauc(y, zs[a]) - fauc(y, zs[b]),
                                      ci_low=np.quantile(v, 0.025), ci_high=np.quantile(v, 0.975), se_boot=se,
                                      mdd80_alpha05=(NormalDist().inv_cdf(0.975) + zb) * se,
                                      mdd80_holm_first_step=(NormalDist().inv_cdf(1 - 0.05 / 16) + zb) * se))
    print('cell done', src, tgt, f'{time.time() - t0:.0f}s', flush=True)
tm = pd.DataFrame(tm_rows)
tm.to_csv(OUT + '/statistician_threshold_metrics.csv', index=False)
sens = pd.DataFrame(sens_rows)
sens['mdd_exceeds_headroom'] = sens.mdd80_holm_first_step > sens.headroom_1_minus_auc_baseline
sens.to_csv(OUT + '/statistician_within_sensitivity.csv', index=False)

# sanity: ΔAUC CIs from this loop must equal the package CIs (same draws)
pt = pd.read_csv(PKG + '/corrected_20261028_optionA/paired_tests_optionA.csv')
key = {'SF++F': 'swinfusionpp__fixed_no_bo', 'SwinB': 'swin_b__fixed_no_bo', 'VSB': 'video_swin_b__fixed_no_bo', 'SF++BO': 'swinfusionpp__dataset_specific_bo'}
chk = tm[(tm.kind == 'paired_delta') & (tm.metric == 'auc')].copy()
chk['model_a'] = chk.model.map(key); chk['model_b'] = chk.versus.map(key)
chk = chk.merge(pt, left_on=['model_a', 'model_b', 'training', 'test'], right_on=['model_a', 'model_b', 'training_dataset', 'test_dataset'])
assert len(chk) == 65 and np.allclose(chk.ci_low_x, chk.ci_low_y, atol=1e-12) and np.allclose(chk.ci_high_x, chk.ci_high_y, atol=1e-12)
print('ΔAUC CIs in the threshold-metric loop match the package for all 65 tests')

# ---------------- 2. DeeperForensics-target tests at the global_cluster level ----------------
g_rows = []
for src, tgt in CELLS:
    if tgt != 'deeperforensics_1_0':
        continue
    for kind, pairs in [('arch', ARCH), ('conf', CONF), ('opt', OPT)]:
        for a, b in pairs:
            A = data[(a, src, tgt)][0]; Bm = data[(b, src, tgt)][0]
            y = A.label.values.astype(int)
            for col in ['dependency_cluster', 'global_cluster']:
                cl = A[col].values
                v = np.array([fauc(y[ii], A.z.values[ii]) - fauc(y[ii], Bm.z.values[ii]) for ii in boot_draws(y, cl)])
                obs, p = rank_perm_p(y, A.z.values, Bm.z.values, cl)
                g_rows.append(dict(family=fam_name(src, tgt, kind), training=src, test=tgt, model=a, versus=b, cluster_col=col,
                                   clusters=len(set(cl.tolist())), delta_auc=obs, ci_low=np.quantile(v, 0.025),
                                   ci_high=np.quantile(v, 0.975), perm_p=p))
g = pd.DataFrame(g_rows)
# re-Holm Option A families with the global-cluster p substituted for the DFo-target tests
pt['m_a'] = pt.model_a.map({v: k for k, v in key.items()}); pt['m_b'] = pt.model_b.map({v: k for k, v in key.items()})
gg = g[g.cluster_col == 'global_cluster'].set_index(['family', 'training', 'test', 'model', 'versus']).perm_p
rq = pt[pt.family_optionA.str.startswith(('RQ1', 'RQ6'))].copy()
rq['p_global'] = [gg.get((r.family_optionA, r.training_dataset, r.test_dataset, r.m_a, r.m_b), r.permutation_p_rank) for r in rq.itertuples()]
for fam, grp in rq.groupby('family_optionA'):
    rq.loc[grp.index, 'holm_global'] = holm(grp.p_global.values)
g = g.merge(rq[['family_optionA', 'training_dataset', 'test_dataset', 'm_a', 'm_b', 'holm_optionA', 'holm_global']],
            left_on=['family', 'training', 'test', 'model', 'versus'], right_on=['family_optionA', 'training_dataset', 'test_dataset', 'm_a', 'm_b'])
g = g.drop(columns=['family_optionA', 'training_dataset', 'test_dataset', 'm_a', 'm_b'])
g.to_csv(OUT + '/statistician_dfo_global_cluster.csv', index=False)
rq['changed_global'] = (rq.holm_optionA < 0.05) != (rq.holm_global < 0.05)
print('global-cluster: Holm conclusions changed in any RQ1/RQ6 family:', int(rq.changed_global.sum()))
print('DFo global sensitivity done', f'{time.time() - t0:.0f}s', flush=True)

# ---------------- 3. Holm partitions for the 26 architecture tests ----------------
ar = pt[pt.family_optionA.isin(['RQ1_architecture', 'RQ6_architecture'])].copy()
ar['holm_pooled_RQ1_26'] = holm(ar.permutation_p_rank.values)
prev = pt.copy()
for fam, grp in prev.groupby('family_rq'):
    prev.loc[grp.index, 'holm_prev_recomputed'] = holm(grp.permutation_p_rank.values)
ar = ar.merge(prev[['model_a', 'model_b', 'training_dataset', 'test_dataset', 'family_rq', 'holm_prev_recomputed']],
              on=['model_a', 'model_b', 'training_dataset', 'test_dataset', 'family_rq'])
assert np.allclose(ar.holm_prev_recomputed, ar.holm_previous_family)
ar = ar[['family_optionA', 'family_rq', 'm_a', 'm_b', 'training_dataset', 'test_dataset', 'auc_difference', 'ci_low', 'ci_high',
         'permutation_p_rank', 'holm_optionA', 'holm_previous_family', 'holm_pooled_RQ1_26']]
for c in ['holm_optionA', 'holm_previous_family', 'holm_pooled_RQ1_26']:
    ar['sig_' + c] = ar[c] < 0.05
ar['monte_carlo_se_raw_p'] = np.sqrt(ar.permutation_p_rank * (1 - ar.permutation_p_rank) / B)
ar.to_csv(OUT + '/statistician_holm_partitions.csv', index=False)
print('Holm partitions: sig counts', ar[['sig_holm_optionA', 'sig_holm_previous_family', 'sig_holm_pooled_RQ1_26']].sum().to_dict())

# ---------------- 4. seed robustness ----------------
s_rows = []
for src, tgt in CELLS:
    for kind, pairs in [('arch', ARCH), ('conf', CONF), ('opt', OPT)]:
        for a, b in pairs:
            A = data[(a, src, tgt)][0]; Bm = data[(b, src, tgt)][0]
            y = A.label.values.astype(int)
            ens_d = fauc(y, A.z.values) - fauc(y, Bm.z.values)
            sa = [fauc(y, A[f's{k}'].values) for k in (1, 2, 3)]
            sb = [fauc(y, Bm[f's{k}'].values) for k in (1, 2, 3)]
            cross = np.array([x - w for x in sa for w in sb])
            s_rows.append(dict(family=fam_name(src, tgt, kind), training=src, test=tgt, model=a, versus=b, ensemble_delta=ens_d,
                               seed_mean_a=np.mean(sa), seed_sd_a=np.std(sa, ddof=1), seed_min_a=min(sa), seed_max_a=max(sa),
                               seed_mean_b=np.mean(sb), seed_sd_b=np.std(sb, ddof=1), seed_min_b=min(sb), seed_max_b=max(sb),
                               seedmean_delta=np.mean(sa) - np.mean(sb), cross_seed_min=cross.min(), cross_seed_max=cross.max(),
                               cross_seed_same_sign_as_ensemble=int((np.sign(cross) == np.sign(ens_d)).sum()), cross_seed_pairs=9,
                               ensemble_minus_seedmean_a=fauc(y, A.z.values) - np.mean(sa)))
sr = pd.DataFrame(s_rows)
sr = sr.merge(pt[['m_a', 'm_b', 'training_dataset', 'test_dataset', 'holm_optionA']], left_on=['model', 'versus', 'training', 'test'],
              right_on=['m_a', 'm_b', 'training_dataset', 'test_dataset']).drop(columns=['m_a', 'm_b', 'training_dataset', 'test_dataset'])
sr.to_csv(OUT + '/statistician_seed_robustness.csv', index=False)

# ---------------- 5. Celeb-DF target: leave one fake-bearing identity cluster out ----------------
l_rows = []
for src, tgt in CELLS:
    if tgt != 'celeb_df_v2':
        continue
    for kind, pairs in [('arch', ARCH), ('conf', CONF), ('opt', OPT)]:
        for a, b in pairs:
            A = data[(a, src, tgt)][0]; Bm = data[(b, src, tgt)][0]
            y = A.label.values.astype(int); cl = A.dependency_cluster.values
            fclus = sorted(set(cl[y == 1].tolist()))
            loo = []
            for c in fclus:
                keep = cl != c
                loo.append(fauc(y[keep], A.z.values[keep]) - fauc(y[keep], Bm.z.values[keep]))
            l_rows.append(dict(family=fam_name(src, tgt, kind), training=src, test=tgt, model=a, versus=b,
                               fake_bearing_clusters=len(fclus), fakes_per_cluster='/'.join(str(int(((cl == c) & (y == 1)).sum())) for c in fclus),
                               delta_auc=fauc(y, A.z.values) - fauc(y, Bm.z.values), loo_min=min(loo), loo_max=max(loo),
                               loo_same_sign=int(sum(np.sign(loo) == np.sign(fauc(y, A.z.values) - fauc(y, Bm.z.values))))))
pd.DataFrame(l_rows).merge(pt[['m_a', 'm_b', 'training_dataset', 'test_dataset', 'holm_optionA']], left_on=['model', 'versus', 'training', 'test'],
    right_on=['m_a', 'm_b', 'training_dataset', 'test_dataset']).drop(columns=['m_a', 'm_b', 'training_dataset', 'test_dataset']) \
    .to_csv(OUT + '/statistician_cdf_loo_identity.csv', index=False)

# ---------------- 6. unweighted mean transfer AUC over the 9 directions, joint cluster bootstrap ----------------
TR = [c for c in CELLS if c[0] != c[1] and c[0] != 'ffpp_c40']
assert len(TR) == 9
groups = {'ffpp': [c for c in TR if c[1] in ('ffpp_c23', 'ffpp_c40')], 'celeb': [c for c in TR if c[1] == 'celeb_df_v2'],
          'dfo': [c for c in TR if c[1] == 'deeperforensics_1_0']}
prep = {}
for gname, cells in groups.items():
    ref = data[('SF++F',) + cells[0]][0]
    uniq, _ = cluster_index(ref.dependency_cluster.values)
    for c in cells:
        df = data[('SF++F',) + c][0]
        assert sorted(set(df.dependency_cluster)) == uniq  # FF++ C23 and C40 test sets share the same 70 pair clusters
    yref = ref.label.values.astype(int)
    idx_ref = [np.flatnonzero(ref.dependency_cluster.values == u) for u in uniq]
    strata = strata_of(yref, uniq, idx_ref)
    per_cell = {c: [np.flatnonzero(data[('SF++F',) + c][0].dependency_cluster.values == u) for u in uniq] for c in cells}
    prep[gname] = (strata, per_cell)
rng = np.random.default_rng(20261030)
mean_draws = {m: [] for m in ['SF++F', 'SwinB', 'VSB', 'SF++BO']}
for _ in range(B):
    sums = {m: 0.0 for m in mean_draws}
    for gname, (strata, per_cell) in prep.items():
        pick = np.concatenate([s[rng.integers(0, len(s), len(s))] for s in strata])
        for c, idxs in per_cell.items():
            ii = np.concatenate([idxs[p] for p in pick])
            for m in mean_draws:
                df = data[(m,) + c][0]
                sums[m] += fauc(df.label.values[ii].astype(int), df.z.values[ii])
    for m in mean_draws:
        mean_draws[m].append(sums[m] / 9)
md = {m: np.array(v) for m, v in mean_draws.items()}
pt_mean = {m: np.mean([fauc(data[(m,) + c][0].label.values.astype(int), data[(m,) + c][0].z.values) for c in TR]) for m in md}
mrows = [dict(quantity=f'mean transfer AUC {m}', estimate=pt_mean[m], ci_low=np.quantile(md[m], 0.025), ci_high=np.quantile(md[m], 0.975)) for m in md]
for a, b in [('SF++F', 'SwinB'), ('SF++F', 'VSB'), ('SF++BO', 'SF++F'), ('SF++BO', 'VSB')]:
    v = md[a] - md[b]
    mrows.append(dict(quantity=f'mean transfer ΔAUC {a} - {b}', estimate=pt_mean[a] - pt_mean[b], ci_low=np.quantile(v, 0.025),
                      ci_high=np.quantile(v, 0.975), share_draws_le_0=float((v <= 0).mean())))
pd.DataFrame(mrows).to_csv(OUT + '/statistician_mean_transfer.csv', index=False)
print(pd.DataFrame(mrows).round(4).to_string())
print(f'done {time.time() - t0:.0f}s')
