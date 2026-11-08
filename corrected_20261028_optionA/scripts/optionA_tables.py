"""Build Option A (fixed recipe = principal architecture comparison) tables from the package CSVs.
Usage: python optionA_tables.py <package_root> <out_root>"""
import csv, sys, os, collections, json
PKG, OUT = sys.argv[1], sys.argv[2]
ST = os.path.join(PKG, '00_Shared', 'statistics_raw')
DS = {'ffpp_c23': 'FF++ C23 (HQ)', 'ffpp_c40': 'FF++ C40 (LQ)', 'celeb_df_v2': 'Celeb-DF v2', 'deeperforensics_1_0': 'DeeperForensics-1.0'}
SH = {'ffpp_c23': 'C23', 'ffpp_c40': 'C40', 'celeb_df_v2': 'Celeb-DF', 'deeperforensics_1_0': 'DFo'}
WITHIN = ['ffpp_c23', 'ffpp_c40', 'celeb_df_v2', 'deeperforensics_1_0']
TRANSFER = [('ffpp_c23', 'ffpp_c40'), ('ffpp_c23', 'celeb_df_v2'), ('ffpp_c23', 'deeperforensics_1_0'),
            ('celeb_df_v2', 'ffpp_c23'), ('celeb_df_v2', 'ffpp_c40'), ('celeb_df_v2', 'deeperforensics_1_0'),
            ('deeperforensics_1_0', 'ffpp_c23'), ('deeperforensics_1_0', 'ffpp_c40'), ('deeperforensics_1_0', 'celeb_df_v2')]
MODELS = [('swinfusionpp', 'fixed_no_bo', 'SwinFusion++ (fixed recipe)'), ('swin_b', 'fixed_no_bo', 'Swin-B'),
          ('video_swin_b', 'fixed_no_bo', 'Video Swin-B'), ('swinfusionpp', 'dataset_specific_bo', 'SwinFusion++ (BO-selected)')]
LBL = {'swinfusionpp__fixed_no_bo': 'SwinFusion++ (fixed recipe)', 'swinfusionpp__dataset_specific_bo': 'SwinFusion++ (BO-selected)',
       'swin_b__fixed_no_bo': 'Swin-B', 'video_swin_b__fixed_no_bo': 'Video Swin-B',
       'topology_control__fixed_no_bo': 'Topology control', 'capacity_control__fixed_no_bo': 'Capacity control'}

ens = {}
for r in csv.DictReader(open(os.path.join(ST, 'three_seed_mean_logit_ensemble.csv'))):
    ens[(r['family'], r['optimization_regimen'], r['training_dataset'], r['test_dataset'], r['variant'])] = r

def holm(ps):
    m = len(ps); order = sorted(range(m), key=lambda i: ps[i]); adj = [0] * m; run = 0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (m - rank) * ps[i])); adj[i] = run
    return adj

# ---- Option A families ----
pr = list(csv.DictReader(open(os.path.join(ST, 'paired_cluster_effects_rank_corrected.csv'))))
def famA(r):
    a, b = r['model_a'], r['model_b']; within = r['training_dataset'] == r['test_dataset']
    if r['family_rq'].startswith('RQ4'): return r['family_rq'], 'control (recipe-matched)'
    if a == 'swinfusionpp__fixed_no_bo' and b in ('swin_b__fixed_no_bo', 'video_swin_b__fixed_no_bo'):
        return ('RQ1_architecture' if within else 'RQ6_architecture'), 'principal (fixed recipe vs fixed recipe)'
    if a == 'swinfusionpp__dataset_specific_bo' and b in ('swin_b__fixed_no_bo', 'video_swin_b__fixed_no_bo'):
        return ('RQ1_configured_system' if within else 'RQ6_configured_system'), 'configured system (BO-selected vs fixed recipe)'
    if a == 'swinfusionpp__dataset_specific_bo' and b == 'swinfusionpp__fixed_no_bo':
        return ('RQ1_optimization_effect' if within else 'RQ6_optimization_effect'), 'optimization effect (BO-selected vs fixed SwinFusion++)'
    raise SystemExit('unmapped ' + str(r))
fam = collections.defaultdict(list)
for i, r in enumerate(pr):
    f, role = famA(r); r['family_optionA'] = f; r['role_optionA'] = role; fam[f].append(i)
for f, idx in fam.items():
    for a, i in zip(holm([float(pr[i]['permutation_p_rank']) for i in idx]), idx): pr[i]['holm_optionA'] = a
# sensitivity: pooled configured+optimization families (as the old secondary pooling)
pool = collections.defaultdict(list)
for i, r in enumerate(pr):
    f = r['family_optionA']
    key = f.replace('_optimization_effect', '_configured_system') if 'optimization' in f else f
    pool[key].append(i)
for f, idx in pool.items():
    for a, i in zip(holm([float(pr[i]['permutation_p_rank']) for i in idx]), idx): pr[i]['holm_sensitivity_pooled'] = a
counts = {f: len(v) for f, v in fam.items()}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'paired_tests_optionA.csv'), 'w', newline='') as fh:
    cols = ['family_optionA', 'role_optionA', 'family_rq', 'model_a', 'model_b', 'training_dataset', 'test_dataset', 'auc_difference', 'ci_low', 'ci_high',
            'permutation_p_rank', 'holm_optionA', 'holm_rank', 'holm_sensitivity_pooled', 'clusters', 'videos']
    w = csv.writer(fh); w.writerow([c if c != 'holm_rank' else 'holm_previous_family' for c in cols])
    for r in pr: w.writerow([r[c] for c in cols])

def P(r, k): return float(r[k])
def pct(x): return '—' if x in ('', 'nan') else '%.2f%%' % (100 * float(x))
def f4(x): return '—' if x in ('', 'nan') else '%.4f' % float(x)
def pval(x): return '%.3f' % x if x >= 0.001 else '<0.001'
def sgn(x): return ('+' if x >= 0 else '−') + '%.4f' % abs(x)
def write(rel, header, rows_csv, md_header, rows_md, note=''):
    path = os.path.join(OUT, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path + '.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(header); w.writerows(rows_csv)
    with open(path + '.md', 'w') as fh:
        fh.write('| ' + ' | '.join(md_header) + ' |\n|' + '---|' * len(md_header) + '\n')
        for row in rows_md: fh.write('| ' + ' | '.join(row) + ' |\n')
        if note: fh.write('\n' + note + '\n')

MCOLS = ['roc_auc', 'roc_auc_ci_low', 'roc_auc_ci_high', 'pr_auc', 'accuracy', 'precision', 'recall', 'specificity', 'f1', 'seed_auc_mean', 'seed_auc_sd', 'analyzed_videos', 'clusters']
def metric_rows(pairs, models, variant='plain'):
    rc, rm = [], []
    for tr, te in pairs:
        for fam_, reg, lab in models:
            r = ens[(fam_, reg, tr, te, variant)]
            rc.append([DS[tr], DS[te], lab, reg, variant] + [r[c] for c in MCOLS])
            rm.append([SH[tr] + ' → ' + SH[te] if tr != te else DS[te], lab,
                       '%s [%s, %s]' % (f4(r['roc_auc']), f4(r['roc_auc_ci_low']), f4(r['roc_auc_ci_high'])),
                       pct(r['accuracy']), pct(r['precision']), pct(r['recall']), pct(r['specificity']), f4(r['f1']),
                       '%s ± %s' % (f4(r['seed_auc_mean']), f4(r['seed_auc_sd']))])
    return rc, rm
HC = ['training', 'test', 'model', 'regimen', 'variant'] + MCOLS
HM = ['Condition', 'Model', 'ROC-AUC [95% CI]', 'Accuracy', 'Precision', 'Recall', 'Specificity', 'F1', 'Seed AUC mean ± SD']
fixed3, bo = MODELS[:3], [MODELS[3]]
for rq in ('RQ1', 'RQ6'):
    rc, rm = metric_rows([(d, d) for d in WITHIN], fixed3)
    write(f'{rq}/results/table1_within_architecture', HC, rc, HM, rm, 'Principal architecture comparison: all three models trained with the identical fixed (non-BO) recipe. Three-seed mean-logit ensembles; thresholds frozen on source validation.')
    rc, rm = metric_rows([(d, d) for d in WITHIN], bo + fixed3[1:])
    write(f'{rq}/results/table1b_within_configured_system', HC, rc, HM, rm, 'Configured-system comparison: BO-selected SwinFusion++ against the fixed-recipe Swin-B and Video Swin-B (unequal optimization effort).')
rc, rm = metric_rows(TRANSFER, MODELS)
for rq in ('RQ1', 'RQ6'):
    write(f'{rq}/results/table3_transfer_all_metrics', HC, rc, HM, rm, 'Frozen transfer: source weights, ensemble, calibration and threshold applied unchanged to the target.')
# AUC-only transfer summary
rcs, rms = [], []
for tr, te in TRANSFER:
    vals = [ens[(f_, g, tr, te, 'plain')] for f_, g, _ in MODELS]
    best = max(range(3), key=lambda k: float(vals[k]['roc_auc']))
    rcs.append([DS[tr], DS[te]] + sum([[v['roc_auc'], v['roc_auc_ci_low'], v['roc_auc_ci_high']] for v in vals], []))
    cells = ['%s [%s, %s]' % (f4(v['roc_auc']), f4(v['roc_auc_ci_low']), f4(v['roc_auc_ci_high'])) for v in vals]
    cells[best] = '**' + cells[best].replace(' [', '** [', 1)
    rms.append([SH[tr] + ' → ' + SH[te]] + cells + [MODELS[best][2]])
for rq in ('RQ1', 'RQ6'):
    write(f'{rq}/results/table3_transfer_auc', ['training', 'test'] + sum([[m[2] + ' AUC', m[2] + ' CI low', m[2] + ' CI high'] for m in MODELS], []), rcs,
          ['Train → Test'] + [m[2] for m in MODELS] + ['Best of the three fixed-recipe models'], rms,
          'Bold = highest of the three fixed-recipe models (the principal comparison). The BO-selected column is the configured system.')
# directional matrices
for reg, lab, nm in (('fixed_no_bo', 'SwinFusion++ (fixed recipe)', 'table2_directional_matrix_fixed'), ('dataset_specific_bo', 'SwinFusion++ (BO-selected)', 'table2b_directional_matrix_bo')):
    rc, rm = [], []
    for tr in ['ffpp_c23', 'celeb_df_v2', 'deeperforensics_1_0']:
        row = []
        for te in WITHIN:
            k = ('swinfusionpp', reg, tr, te, 'plain'); row.append(ens[k]['roc_auc'] if k in ens else '')
        rc.append([DS[tr]] + row); rm.append(['**' + DS[tr] + '**'] + [('*%s*' % f4(v) if te == tr else f4(v)) if v else 'not run' for v, te in zip(row, WITHIN)])
    write(f'RQ6/results/{nm}', ['training'] + [DS[t] for t in WITHIN], rc, ['Train ↓ / Test →'] + [DS[t] for t in WITHIN], rm, f'{lab}, ROC-AUC. Diagonal (italic) = within-dataset.')
# paired tables
def paired_tbl(rel, fams, note):
    sel = [r for r in pr if r['family_optionA'] in fams]
    order = {(tr, te): i for i, (tr, te) in enumerate([(d, d) for d in WITHIN] + TRANSFER)}
    sel.sort(key=lambda r: (fams.index(r['family_optionA']), order[(r['training_dataset'], r['test_dataset'])], r['model_b']))
    rc = [[r['family_optionA'], DS[r['training_dataset']], DS[r['test_dataset']], LBL[r['model_a']], LBL[r['model_b']], r['auc_difference'], r['ci_low'], r['ci_high'],
           r['permutation_p_rank'], r['holm_optionA'], counts[r['family_optionA']], r['videos'], r['clusters']] for r in sel]
    rm = []
    for r in sel:
        h = float(r['holm_optionA']); d = float(r['auc_difference'])
        mark = (' ✔' if d > 0 else ' ✘') if h < 0.05 else ''
        cond = DS[r['test_dataset']] if r['training_dataset'] == r['test_dataset'] else SH[r['training_dataset']] + ' → ' + SH[r['test_dataset']]
        rm.append([cond, LBL[r['model_a']] + ' − ' + LBL[r['model_b']], '%s [%s, %s]' % (sgn(d), sgn(float(r['ci_low'])), sgn(float(r['ci_high']))),
                   pval(float(r['permutation_p_rank'])), ('**%s**' % pval(h) if h < 0.05 else pval(h)) + mark, r['family_optionA'] + ' (m=%d)' % counts[r['family_optionA']]])
    write(rel, ['family', 'training', 'test', 'model_a', 'model_b', 'delta_auc', 'ci_low', 'ci_high', 'permutation_p_rank', 'holm_p', 'family_size', 'videos', 'clusters'], rc,
          ['Condition', 'Comparison', 'ΔAUC [95% CI]', 'p (unadjusted)', 'p_Holm', 'Holm family'], rm,
          note + ' p-values: rank-based cluster permutation test (5,000 permutations), Holm-adjusted within the named family. ✔ / ✘ = first model significantly better / worse (p_Holm < 0.05).')
for rq in ('RQ1',):
    paired_tbl('RQ1/results/table2_paired_within_architecture', ['RQ1_architecture'], 'Principal RQ1 family (within-dataset, fixed recipe vs fixed recipe).')
    paired_tbl('RQ1/results/table2b_paired_within_configured_system', ['RQ1_configured_system', 'RQ1_optimization_effect'], 'Configured-system family (BO-selected vs fixed-recipe baselines) and optimization-effect family (BO-selected vs fixed-recipe SwinFusion++), within-dataset.')
for rq in ('RQ1', 'RQ6'):
    paired_tbl(f'{rq}/results/table3b_paired_transfer_architecture', ['RQ6_architecture'], 'Principal transfer family (fixed recipe vs fixed recipe).')
    paired_tbl(f'{rq}/results/table3c_paired_transfer_configured_system', ['RQ6_configured_system', 'RQ6_optimization_effect'], 'Configured-system and optimization-effect families, frozen transfer.')
paired_tbl('RQ4/results/table1_controls', ['RQ4_controls'], 'RQ4 matched controls, within FF++ C23 (unchanged by Option A).')
paired_tbl('RQ4/results/table1c_controls_transfer', ['RQ4_controls_transfer'], 'RQ4 matched controls, frozen transfer from FF++ C23 (unchanged by Option A).')
# TTA (descriptive)
rc, rm = metric_rows([(d, d) for d in WITHIN] + TRANSFER, [MODELS[0], MODELS[3]], variant='tta_flip')
write('RQ1/results/table4_tta_variant', HC, rc, HM, rm, 'Pre-declared horizontal-flip TTA variant (A-13), descriptive only; both SwinFusion++ regimens.')
# summary json for writing
summ = {'family_sizes': counts, 'tests': [{k: r[k] for k in ('family_optionA', 'model_a', 'model_b', 'training_dataset', 'test_dataset', 'auc_difference', 'ci_low', 'ci_high', 'permutation_p_rank', 'holm_optionA', 'holm_rank', 'holm_sensitivity_pooled')} for r in pr]}
# (summary json for drafting removed)
print('family sizes:', counts)
# RQ2 published table: flag the six SFormer Table 4 cross-compression cells mislabelled as train == test
src = os.path.join(PKG, 'RQ2', 'results', 'table2_published_AB.csv')
rows = list(csv.DictReader(open(src, newline='')))
for r in rows:
    flag = r['model'] == 'SFormer' and r['location'].startswith('Table 4') and 'Cross-compression' in r['protocol_notes']
    r['optionA_20261028_note'] = ('EXCLUDE from within-dataset ranges: off-diagonal cross-compression cell of SFormer Table 4 '
                                  '(diagonal = Table 3 values 99.9 / 98.15); train/test labels in this row are wrong') if flag else ''
dst = os.path.join(OUT, 'RQ2', 'results', 'table2_published_AB.csv'); os.makedirs(os.path.dirname(dst), exist_ok=True)
w = csv.DictWriter(open(dst, 'w', newline=''), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('RQ2 published rows flagged:', sum(1 for r in rows if r['optionA_20261028_note']))
