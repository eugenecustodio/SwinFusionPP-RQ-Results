"""Production tables T4–T9 and J1–J8 (pre-rounded print strings) + notes + T1 helper.
Every value is recomputed from raw predictions and asserted against the package CSVs, or read from the package
(per-seed, TTA, strict-subset values) after cross-checks. Supplementary values come from statistician_rq1_analyses.py
outputs (stats_out/), which were validated in Round 1."""
import sys, json
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_fmt import *

SPAN = '__SPAN__'
pt = paired_tests()
ens_all = pd.read_csv(ST + '/three_seed_mean_logit_ensemble.csv')
ens = ens_all[ens_all.variant == 'plain']
seedm = pd.read_csv(ST + '/heldout_seed_metrics_rq1_rq6.csv')
data = load_all()

def E(mk, src, tgt, variant='plain'):
    e = ens_all[(ens_all.variant == variant) & (ens_all.family == MODELS[mk][0]) & (ens_all.optimization_regimen == MODELS[mk][1])
                & (ens_all.training_dataset == src) & (ens_all.test_dataset == tgt)]
    assert len(e) == 1
    return e.iloc[0]

# ---------- recompute + assert ensemble metrics ----------
M = {}
for (mk, src, tgt), D in data.items():
    df = D['df']; y = df.label.values.astype(int)
    tm = threshold_metrics(y, df.pred.values)
    tm['auc'] = fauc(y, df.z.values); tm['ap'] = average_precision(y, df.z.values)
    e = E(mk, src, tgt)
    if tm['tp'] + tm['fp'] == 0:  # package (and this table) treat F1 as undefined when no video is called fake
        assert np.isnan(e.f1); tm['f1'] = np.nan
    for k_m, k_e in [('auc', 'roc_auc'), ('ap', 'pr_auc'), ('accuracy', 'accuracy'), ('recall', 'recall'), ('specificity', 'specificity'), ('f1', 'f1')]:
        if k_m == 'f1' and np.isnan(tm['f1']):
            continue
        assert abs(tm[k_m] - e[k_e]) < 1e-12, (mk, src, tgt, k_m)
    if not np.isnan(tm['precision']):
        assert abs(tm['precision'] - e.precision) < 1e-12
    assert (tm['tp'], tm['fp'], tm['tn'], tm['fn']) == (e.tp, e.fp, e.tn, e.fn)
    tm['ci'] = (e.roc_auc_ci_low, e.roc_auc_ci_high)
    s = [fauc(y, df[f's{k}'].values) for k in (1, 2, 3)]
    assert abs(np.mean(s) - e.seed_auc_mean) < 1e-12 and abs(np.std(s, ddof=1) - e.seed_auc_sd) < 1e-12
    tm['seeds'] = s; tm['n'] = len(y); tm['nfake'] = int(y.sum()); tm['clusters'] = df.dependency_cluster.nunique()
    tm['fake_clusters'] = df[df.label == 1].dependency_cluster.nunique()
    M[(mk, src, tgt)] = tm
print('ensemble metrics recomputed and asserted for', len(M), 'cells')

def span_within(d):
    t = M[('SF++F', d, d)]
    s = f"{LONG[d]} — {t['n']} videos ({t['nfake']} fake), {t['clusters']} clusters"
    if d == 'celeb_df_v2':
        s += f"; all fakes in {t['fake_clusters']} identity clusters"
    return s

def prec_str(t):
    pos = t['tp'] + t['fp']
    if pos == 0:
        return '—'
    return pct(t['precision']) + ('†' if pos < 10 else '')

def write(name, rows, cols, note):
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(f'{TAB}/{name}.csv', index=False)
    assert len(note.split()) < 90, (name, len(note.split()))
    open(f'{TAB}/{name}_note.txt', 'w').write(note + '\n')
    return df

ABBR = ('C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0.')
CDFNOTE = 'Celeb-DF v2 intervals are approximate: all 843 fake videos lie in 9 identity clusters.'
CIN = ('95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity.')
PN = ('Raw p: two-sided rank-based cluster permutation test (5,000 permutations); Holm p: Holm-adjusted within the family; '
      '"< 0.005" marks the smallest attainable adjusted value.')
T = {}

# ---------- T4 ----------
rows = []
for d in DS:
    rows.append([SPAN, span_within(d)] + [''] * 9)
    for mk in ['SF++F', 'SwinB', 'VSB']:
        t = M[(mk, d, d)]
        rows.append([MLABEL[mk], f"{num(t['auc'])} {ci(*t['ci'], signed=False)}", num(t['ap']), pct(t['accuracy']), prec_str(t),
                     pct(t['recall']), pct(t['specificity']), num(t['f1']), str(t['fp']), str(t['fn']),
                     f"{num(np.mean(t['seeds']))} ± {num(np.std(t['seeds'], ddof=1))}"])
T['T4'] = write('T4', rows, ['Model', 'ROC-AUC [95% CI]', 'PR-AUC', 'Acc (%)', 'Prec (%)', 'Rec (%)', 'Spec (%)', 'F1', 'FP', 'FN', 'Seed AUC mean ± SD'],
    'Note. Three-seed mean-logit ensembles, fixed recipe; thresholds frozen on source validation. ROC-AUC intervals: ' + CIN +
    ' PR-AUC prevalence baselines: 0.500 (FF++, DFo), 0.862 (CDF). FPR = 1 − specificity; FNR = 1 − recall. '
    'Seed SD from three seeds is descriptive. ' + CDFNOTE)

# ---------- T5 ----------
rows = []
for d in DS:
    for i, b in enumerate(['SwinB', 'VSB']):
        r = get_test(pt, 'SF++F', b, d, d)
        rows.append([LONG[d] if i == 0 else '', MLABEL[b], sgn(r.auc_difference), ci(r.ci_low, r.ci_high), p_raw(r.permutation_p_rank), p_holm(r.holm_optionA, 8)])
T['T5'] = write('T5', rows, ['Test set', 'Comparator', 'ΔAUC', '95% CI', 'Raw p', 'Holm p'],
    'Note. ΔAUC = fixed-recipe SwinFusion++ minus comparator (three-seed ensembles). Intervals: ' + CIN +
    ' Raw p: two-sided rank-based cluster permutation test (5,000 permutations). Holm p: within-dataset architecture family '
    '(m = 8; file label RQ1_architecture). ' + CDFNOTE)

# ---------- T6 ----------
rows = []
for src, tgt in TRANSFER:
    for i, b in enumerate(['SwinB', 'VSB']):
        r = get_test(pt, 'SF++F', b, src, tgt)
        rows.append([cond(src, tgt) if i == 0 else '', MLABEL[b], num(M[('SF++F', src, tgt)]['auc']), num(M[(b, src, tgt)]['auc']),
                     sgn(r.auc_difference), ci(r.ci_low, r.ci_high), p_raw(r.permutation_p_rank), p_holm(r.holm_optionA, 18)])
T['T6'] = write('T6', rows, ['Direction', 'Comparator', 'SwinFusion++ AUC', 'Comparator AUC', 'ΔAUC', '95% CI', 'Raw p', 'Holm p'],
    'Note. X → Y: trained on X, tested on Y with frozen source weights, thresholds and temperatures. ' + ABBR +
    ' ΔAUC = fixed-recipe SwinFusion++ minus comparator. Intervals: ' + CIN + ' ' + PN +
    ' Family: frozen-transfer architecture (m = 18; file label RQ6_architecture). CDF-target intervals are approximate (9 fake-bearing clusters).')

# ---------- T7 ----------
rows = []
for src, tgt in TRANSFER:
    t0 = M[('SF++F', src, tgt)]
    rows.append([SPAN, f"{cond(src, tgt)} — {t0['n']} videos, fake prevalence {pct(t0['nfake'] / t0['n'])}%"] + [''] * 7)
    for mk in ['SF++F', 'SwinB', 'VSB']:
        t = M[(mk, src, tgt)]
        rows.append([MLABEL[mk], num(t['ap']), pct(t['accuracy']), prec_str(t), pct(t['recall']), pct(t['specificity']),
                     '—' if np.isnan(t['f1']) else num(t['f1']), str(t['tp']), str(t['fp'])])
T['T7'] = write('T7', rows, ['Model', 'PR-AUC', 'Acc (%)', 'Prec (%)', 'Rec (%)', 'Spec (%)', 'F1', 'TP', 'FP'],
    'Note. Fixed-recipe three-seed ensembles at frozen source-validation thresholds; no target labels were used. ' + ABBR +
    ' Precision and F1: "—" = no positive calls (undefined); † = fewer than 10 positive calls. PR-AUC baseline equals the fake prevalence. '
    'Descriptive; no tests. Paired differences: Table J2.')

# ---------- T8 ----------
rows = []
for src, tgt in CELLS:
    for i, b in enumerate(['SwinB', 'VSB']):
        r = get_test(pt, 'SF++BO', b, src, tgt)
        rows.append([cond(src, tgt) if i == 0 else '', MLABEL[b], num(M[('SF++BO', src, tgt)]['auc']), num(M[(b, src, tgt)]['auc']),
                     sgn(r.auc_difference), ci(r.ci_low, r.ci_high), p_raw(r.permutation_p_rank), p_holm(r.holm_optionA, FAMM[r.family_optionA])])
T['T8'] = write('T8', rows, ['Condition', 'Comparator', 'SwinFusion++ (BO) AUC', 'Comparator AUC', 'ΔAUC', '95% CI', 'Raw p', 'Holm p'],
    'Note. Configured system: BO-selected SwinFusion++ minus fixed-recipe comparator; optimization effort is unequal. '
    'X → X = within-dataset. ' + ABBR + ' Intervals: ' + CIN + ' ' + PN +
    ' Families: configured system within (m = 8) and transfer (m = 18). CDF-target intervals are approximate.')

# ---------- T9 ----------
rows = []
for src, tgt in CELLS:
    r = get_test(pt, 'SF++BO', 'SF++F', src, tgt)
    rows.append([cond(src, tgt), num(M[('SF++BO', src, tgt)]['auc']), num(M[('SF++F', src, tgt)]['auc']), sgn(r.auc_difference),
                 ci(r.ci_low, r.ci_high), p_raw(r.permutation_p_rank), p_holm(r.holm_optionA, FAMM[r.family_optionA])])
T['T9'] = write('T9', rows, ['Condition', 'BO AUC', 'Fixed AUC', 'ΔAUC', '95% CI', 'Raw p', 'Holm p'],
    'Note. Optimization effect: BO-selected minus fixed-recipe SwinFusion++. X → X = within-dataset. ' + ABBR + ' Intervals: ' + CIN +
    ' ' + PN + ' Families: within (m = 4) and transfer (m = 9). CDF → CDF is grouping-dependent: Holm p = 0.077 when pooled with the 8 architecture tests.')

# ---------- J1 per-seed ----------
sp = seedm[(seedm.subset == 'full_test') & (seedm.variant == 'plain')]
rows = []
for src, tgt in CELLS:
    for i, mk in enumerate(['SF++F', 'SF++BO', 'SwinB', 'VSB']):
        g = sp[(sp.family == MODELS[mk][0]) & (sp.optimization_regimen == MODELS[mk][1]) & (sp.training_dataset == src) & (sp.test_dataset == tgt)].sort_values('seed_slot')
        assert np.allclose(g.roc_auc.values, M[(mk, src, tgt)]['seeds'], atol=1e-12)
        s = g.roc_auc.values
        rows.append([cond(src, tgt) if i == 0 else '', MLABEL[mk], num(s[0]), num(s[1]), num(s[2]), f'{num(s.mean())} ± {num(s.std(ddof=1))}', num(M[(mk, src, tgt)]['auc'])])
T['J1'] = write('J1', rows, ['Training → test', 'Model', 'Seed 1', 'Seed 2', 'Seed 3', 'Mean ± SD', 'Ensemble'],
    'Note. Video-level ROC-AUC of each training seed (260901, 260902, 260903) and of the three-seed mean-logit ensemble. '
    'X → X = within-dataset. ' + ABBR + ' SD from three seeds is descriptive and imprecise. Seeds are not resampled or tested.')

# ---------- J2 threshold-metric paired Δ ----------
thm = pd.read_csv(OUT + '/statistician_threshold_metrics.csv')
thm = thm[(thm.kind == 'paired_delta') & (thm.model == 'SF++F')]
rows = []
for src, tgt in CELLS:
    for i, b in enumerate(['SwinB', 'VSB']):
        g = thm[(thm.training == src) & (thm.test == tgt) & (thm.versus == b)].set_index('metric')
        ta, tb = M[('SF++F', src, tgt)], M[(b, src, tgt)]
        for k in ['accuracy', 'recall', 'f1', 'precision']:
            if not (np.isnan(ta[k]) or np.isnan(tb[k])):
                assert abs(g.loc[k, 'estimate'] - (ta[k] - tb[k])) < 1e-12
        cells = []
        for k in ['accuracy', 'precision', 'recall', 'f1']:
            if k == 'precision' and min(ta['tp'] + ta['fp'], tb['tp'] + tb['fp']) < 10:
                cells.append('n.e.'); continue
            if k == 'f1' and (np.isnan(ta['f1']) or np.isnan(tb['f1'])):
                cells.append('n.e.'); continue
            r = g.loc[k]
            if k == 'f1':
                cells.append(f'{sgn(r.estimate)} {ci(r.ci_low, r.ci_high)}')
            else:
                cells.append(f'{sgn(100 * r.estimate, 2)} {ci(100 * r.ci_low, 100 * r.ci_high, 2)}')
        rows.append([cond(src, tgt) if i == 0 else '', MLABEL[b]] + cells)
T['J2'] = write('J2', rows, ['Condition', 'Comparator', 'ΔAcc [95% CI]', 'ΔPrec [95% CI]', 'ΔRec [95% CI]', 'ΔF1 [95% CI]'],
    'Note. Supplementary, post hoc. Fixed-recipe SwinFusion++ minus comparator at frozen thresholds; accuracy, precision and recall in '
    'percentage points. Paired ' + CIN[:-1] + '; no p-values. n.e. = not estimable (precision: a model made fewer than 10 positive calls; F1: none). '
    'X → X = within-dataset. ' + ABBR + ' CDF intervals are approximate (9 fake-bearing clusters).')

# ---------- J3 strict subsets ----------
ss = seedm[(seedm.subset == 'strict_overlap_free') & (seedm.variant == 'plain')]
rows = []
for src, tgt in [('ffpp_c23', 'deeperforensics_1_0'), ('deeperforensics_1_0', 'ffpp_c23'), ('deeperforensics_1_0', 'ffpp_c40')]:
    for i, mk in enumerate(['SF++F', 'SF++BO', 'SwinB', 'VSB']):
        g = ss[(ss.family == MODELS[mk][0]) & (ss.optimization_regimen == MODELS[mk][1]) & (ss.training_dataset == src) & (ss.test_dataset == tgt)].sort_values('seed_slot')
        assert len(g) == 3 and g.analyzed_videos.nunique() == 1
        n = int(g.analyzed_videos.iloc[0]); s = g.roc_auc.values
        rows.append([f'{cond(src, tgt)} (n = {n})' if i == 0 else '', MLABEL[mk], num(s[0]), num(s[1]), num(s[2]), num(s.mean())])
T['J3'] = write('J3', rows, ['Direction (n)', 'Model', 'Seed 1', 'Seed 2', 'Seed 3', 'Mean'],
    'Note. Strict lineage-free subsets: target test videos whose lineage never appears in the source training or validation split. '
    'Per-seed ROC-AUC only; no ensemble, interval or test. Other directions are lineage-free on the full test set. ' + ABBR)

# ---------- J4 TTA ----------
rows = []
for src, tgt in CELLS:
    r = [cond(src, tgt)]
    for mk in ['SF++F', 'SwinB', 'VSB', 'SF++BO']:
        tt = E(mk, src, tgt, 'tta_flip')
        g = seedm[(seedm.subset == 'full_test') & (seedm.variant == 'tta_flip') & (seedm.family == MODELS[mk][0]) & (seedm.optimization_regimen == MODELS[mk][1])
                  & (seedm.training_dataset == src) & (seedm.test_dataset == tgt)]
        assert len(g) == 3 and abs(g.roc_auc.mean() - tt.seed_auc_mean) < 1e-12  # internal consistency of the package TTA values
        r += [num(M[(mk, src, tgt)]['auc']), num(tt.roc_auc)]
    rows.append(r)
T['J4'] = write('J4', rows, ['Condition', 'SwinFusion++ plain', 'SwinFusion++ TTA', 'Swin-B plain', 'Swin-B TTA', 'Video Swin-B plain', 'Video Swin-B TTA',
                             'SwinFusion++ (BO) plain', 'SwinFusion++ (BO) TTA'],
    'Note. Ensemble ROC-AUC without (plain) and with the predeclared horizontal-flip test-time augmentation (TTA), for all models. '
    'Plain values are used throughout Chapter 4. TTA values are from the package ensemble file (raw TTA predictions were not available for '
    're-computation). X → X = within-dataset. ' + ABBR)

# ---------- J5 rank correction ----------
rk = pd.read_csv(OUT + '/statistician_rank_correction_impact.csv')
famorder = list(FAMNAME)
rows = []
for fam in famorder:
    g = rk[rk.family_optionA == fam]
    for src, tgt in CELLS:
        for _, r in g[(g.training_dataset == src) & (g.test_dataset == tgt)].sort_values('model_b').iterrows():
            a, b = KEY2M[r.model_a], KEY2M[r.model_b]
            rows.append([FAMNAME[fam], f'{MLABEL[a]} vs {MLABEL[b]}, {cond(src, tgt)}', sgn(r.auc_difference),
                         p_raw(r.permutation_p_original_recomputed), p_holm(r.holm_rawlogit_optionA, FAMM[fam]),
                         p_raw(r.permutation_p_rank), p_holm(r.holm_optionA, FAMM[fam]), 'Yes' if r.conclusion_changed else 'No'])
assert len(rows) == 65 and sum(x[-1] == 'Yes' for x in rows) == 10
T['J5'] = write('J5', rows, ['Family', 'Comparison', 'ΔAUC', 'Raw-logit p', 'Holm (original)', 'Rank p', 'Holm (rank)', 'Decision changed?'],
    'Note. Original predeclared test: cluster permutation exchanging raw ensemble logits. Corrected test: cluster-level rank-based '
    'adaptation of Bandos et al. (2005). Both use 5,000 permutations and Holm adjustment within the six final families; ΔAUC is identical. '
    'Decision changed = significance at 0.05 after Holm adjustment differs. X → X = within-dataset. ' + ABBR)

# ---------- J6 within sensitivity ----------
ws = pd.read_csv(OUT + '/statistician_within_sensitivity.csv')
rows = []
for d in DS:
    for i, b in enumerate(['SwinB', 'VSB']):
        r = ws[(ws.test == d) & (ws.versus == b)].iloc[0]
        rows.append([LONG[d] if i == 0 else '', MLABEL[b], num(r.se_boot), num(r.mdd80_alpha05), num(r.mdd80_holm_first_step), num(r.headroom_1_minus_auc_baseline)])
T['J6'] = write('J6', rows, ['Test set', 'Comparator', 'SE(ΔAUC)', 'MDD (α = 0.05)', 'MDD (α = 0.05/8)', 'Headroom'],
    'Note. Supplementary, post hoc. SE: standard deviation of the 5,000 paired cluster-bootstrap ΔAUC draws. MDD: smallest ΔAUC '
    'detectable with 80% power by a two-sided normal-approximation test, (z + 0.84) × SE. Headroom: 1 − comparator ROC-AUC, the largest '
    'possible gain for SwinFusion++. MDD exceeds headroom in 7 of 8 comparisons at α = 0.05/8. ' + CDFNOTE)

# ---------- J7 robustness of the 10 significant architecture differences ----------
hp = pd.read_csv(OUT + '/statistician_holm_partitions.csv')
sr = pd.read_csv(OUT + '/statistician_seed_robustness.csv')
gl = pd.read_csv(OUT + '/statistician_dfo_global_cluster.csv'); gl = gl[gl.cluster_col == 'global_cluster']
lo = pd.read_csv(OUT + '/statistician_cdf_loo_identity.csv')
def p3(h, m):
    return p_holm(h, m)
rows = []
for src, tgt in TRANSFER:
    for b in ['SwinB', 'VSB']:
        r = get_test(pt, 'SF++F', b, src, tgt)
        if r.holm_optionA >= 0.05:
            continue
        h = hp[(hp.m_b == b) & (hp.training_dataset == src) & (hp.test_dataset == tgt)].iloc[0]
        s = sr[(sr.model == 'SF++F') & (sr.versus == b) & (sr.training == src) & (sr.test == tgt)].iloc[0]
        g = gl[(gl.model == 'SF++F') & (gl.versus == b) & (gl.training == src) & (gl.test == tgt)]
        l = lo[(lo.model == 'SF++F') & (lo.versus == b) & (lo.training == src) & (lo.test == tgt)]
        rows.append([f'{cond(src, tgt)} vs {MLABEL[b]}', p3(h.holm_optionA, 18), p3(h.holm_previous_family, 27), p3(h.holm_pooled_RQ1_26, 26),
                     f"{int(s.cross_seed_same_sign_as_ensemble)}/9", p3(g.holm_global.iloc[0], 18) if len(g) else '—',
                     f"{sgn(l.loo_min.iloc[0])} to {sgn(l.loo_max.iloc[0])}" if len(l) else '—'])
assert len(rows) == 10
T['J7'] = write('J7', rows, ['Comparison', 'Holm p (final, m = 18)', 'Holm p (pre-scoring, m = 27)', 'Holm p (pooled, m = 26)', 'Seed sign agreement',
                             'Holm p (DFo global clusters)', 'CDF leave-one-identity-out ΔAUC'],
    'Note. Supplementary. The ten fixed-recipe SwinFusion++ differences significant after Holm adjustment. Pre-scoring partition: grouping recorded '
    'before test scoring. Seed sign agreement: cross-seed pairings with the ensemble ΔAUC sign. DFo global clusters: 175 lineage clusters instead of 201. '
    '"< 0.005" marks the family floor; floors at m = 26/27 round to 0.005. ' + ABBR)

# ---------- J8 transfer AUC [CI] all four ----------
rows = []
for src, tgt in TRANSFER:
    rows.append([cond(src, tgt)] + [f"{num(M[(mk, src, tgt)]['auc'])} {ci(*M[(mk, src, tgt)]['ci'], signed=False)}" for mk in ['SF++F', 'SwinB', 'VSB', 'SF++BO']])
means = {mk: np.mean([M[(mk, s, t)]['auc'] for s, t in TRANSFER]) for mk in ['SF++F', 'SwinB', 'VSB', 'SF++BO']}
rows.append(['Unweighted mean (descriptive)'] + [num(means[mk]) for mk in ['SF++F', 'SwinB', 'VSB', 'SF++BO']])
T['J8'] = write('J8', rows, ['Direction', 'SwinFusion++', 'Swin-B', 'Video Swin-B', 'SwinFusion++ (BO)'],
    'Note. Ensemble ROC-AUC [95% CI] under frozen transfer; intervals: ' + CIN + ' ' + ABBR +
    ' The unweighted mean summarizes this grid only: directions share sources and test sets, the mean was not predeclared, '
    'and the registry rules out a collapsed generalization score; it supports no claim.')

# ---------- T1 helper (cluster columns) ----------
rows = []
for d in DS:
    t = M[('SF++F', d, d)]
    f = sp[sp.test_dataset == d]
    rows.append(dict(test_set=LONG[d], videos=t['n'], fake=t['nfake'], real=t['n'] - t['nfake'], dependency_clusters=t['clusters'],
                     clusters_containing_fakes=t['fake_clusters'], coverage_min=f.coverage.min(), preprocessing_failures_max=int(f.n_preprocessing_failed.max()),
                     global_lineage_clusters=data[('SF++F', d, d)]['df'].global_cluster.nunique()))
pd.DataFrame(rows).to_csv(TAB + '/T1_clusters_helper.csv', index=False)

json.dump({k: list(v.columns) for k, v in T.items()}, open(TAB + '/_columns.json', 'w'), indent=1)
print('tables written:', ', '.join(T))
