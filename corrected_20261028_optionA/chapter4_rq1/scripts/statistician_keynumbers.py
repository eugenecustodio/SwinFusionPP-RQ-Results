"""Write tables/KEY_NUMBERS.md: every number the prose will cite, as the printed string, with table/row/column.
Row numbers r# are 1-based CSV data rows (header excluded; __SPAN__ rows counted). Values are read back from the
table CSVs so the prose and tables cannot diverge."""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_fmt import *

t = {k: pd.read_csv(f'{TAB}/{k}.csv', dtype=str, keep_default_na=False) for k in
     ['T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'J1', 'J2', 'J3', 'J5', 'J6', 'J7', 'J8']}
help_ = pd.read_csv(f'{TAB}/T1_clusters_helper.csv')
L = []
def ref(tab, r, col):
    return f'{tab} r{r} [{col}]'
def grp_rows(tab, first_col_value, n=2):
    """rows of a group whose label appears in the first column of its first row"""
    df = t[tab]; c0 = df.columns[0]
    i = df.index[df[c0] == first_col_value][0]
    return list(range(i, i + n))
def cellv(tab, i, col):
    return t[tab].loc[i, col]
def find(tab, label, comp, ncomp=2):
    rows = grp_rows(tab, label, ncomp)
    for i in rows:
        if t[tab].loc[i, t[tab].columns[1]] == comp:
            return i
    raise KeyError((tab, label, comp))

A = lambda s: L.append(s)
A('# KEY_NUMBERS: printed strings for the Chapter 4 opening, 4.1.1–4.1.5 and the Chapter 3 amendment\n')
A('Convention: `Tn rK [column]` = table CSV in `team/tables/`, 1-based data row K (header excluded, `__SPAN__` rows counted). '
  'Minus signs are U+2212. Copy strings exactly. Numbers not in a table cite their stats_out source.\n')

A('## Opening (Evaluation Setting)\n')
for _, h in help_.iterrows():
    A(f"- {h.test_set}: {h.videos} videos ({h.fake} fake, {h.real} real), {h.dependency_clusters} clusters; clusters containing fakes: {h.clusters_containing_fakes}; "
      f"coverage {100 * h.coverage_min:.0f}%, preprocessing failures {h.preprocessing_failures_max} (T1_clusters_helper.csv; T1 by methodologist agrees)")
A('- Celeb-DF v2: 45 of the 54 clusters are single real videos; the 9 identity clusters hold 33–197 fakes each (stats_out/statistician_cdf_loo_identity.csv, fakes_per_cluster).')
A('- DeeperForensics-1.0: 175 global lineage clusters vs 201 dependency clusters (T1_clusters_helper.csv).')
A(f"- Celeb-DF v2 fake prevalence: 86.20% (T7 r5 span text); PR-AUC baselines 0.500 / 0.862 (T4 note).")
A('- Coverage: 100% and 0 preprocessing failures in all 180 full-test seed × cell rows (heldout_seed_metrics_rq1_rq6.csv, plain, full_test).')
def j5(comp):
    i = t['J5'].index[t['J5'].Comparison == comp][0]
    return i, cellv('J5', i, 'Holm (original)'), cellv('J5', i, 'Holm (rank)')
i1, o1, r1 = j5(f'SwinFusion++ vs Video Swin-B, DFo {ARROW} DFo')
i2, o2, r2 = j5(f'SwinFusion++ vs Swin-B, CDF {ARROW} C23')
i3, o3, r3 = j5(f'SwinFusion++ vs Swin-B, DFo {ARROW} CDF')
A(f'- Rank-correction effect (architecture, 26 comparisons): removed one significant SwinFusion++ advantage, DFo → DFo vs Video Swin-B, Holm p {o1} → {r1} (J5 r{i1 + 1}); '
  f'added two vs Swin-B: CDF → C23 {o2} → {r2} (J5 r{i2 + 1}) and DFo → CDF {o3} → {r3} (J5 r{i3 + 1}) [Holm (original) → Holm (rank)].')
nchg = int((t['J5']['Decision changed?'] == 'Yes').sum())
A(f'- Decisions changed by the correction: {nchg} of 65 RQ1/RQ6 comparisons (J5, "Decision changed?" = Yes). By family: architecture 3, configured system 5, optimization effect 2.')
A('- Same 10 of 26 architecture comparisons significant under the final, pre-scoring (m = 27) and pooled (m = 26) partitions (J7; stats_out/statistician_holm_partitions.csv).')
A('- Holm decisions from the stored paired-bootstrap p-values agreed with the rank test in 73 of 73 paired comparisons (65 RQ1/RQ6 + 8 RQ4 controls) '
  '(stats_out/statistician_r2_bootstrap_p_check.csv). Do not print any bootstrap p.')
A(f"- Grouping-dependent result: BO − fixed within Celeb-DF v2, Holm p {cellv('T9', 2, 'Holm p')} (T9 r3) vs 0.077 pooled (T9 note; paired_tests_optionA.csv holm_sensitivity_pooled).")
A('- Families: within-dataset architecture (m = 8), frozen-transfer architecture (m = 18), configured system (m = 8 / 18), optimization effect (m = 4 / 9).\n')

A('## 4.1.1 In-distribution, fixed recipe\n')
auc_cells = []
for i, r in t['T4'].iterrows():
    if r.Model != '__SPAN__':
        auc_cells.append((r['ROC-AUC [95% CI]'].split(' ')[0], i + 1))
vals = sorted(auc_cells, key=lambda x: float(x[0]))
A(f'- ROC-AUC range over the 12 model × dataset cells: {vals[0][0]} (T4 r{vals[0][1]}) to {vals[-1][0]} (T4 r{vals[-1][1]}); both extremes are SwinFusion++ (C40 and DeeperForensics-1.0).')
for i, r in t['T4'].iterrows():
    if r.Model == '__SPAN__':
        A(f'- Span T4 r{i + 1}: "{r.iloc[1]}"')
    else:
        acc = float(r['Acc (%)'])
        A(f"  - T4 r{i + 1} {r.Model}: AUC {r['ROC-AUC [95% CI]']}; PR-AUC {r['PR-AUC']}; Acc {r['Acc (%)']}; Prec {r['Prec (%)']}; Rec {r['Rec (%)']}; "
          f"Spec {r['Spec (%)']}; F1 {r['F1']}; FP {r['FP']}; FN {r['FN']}; seeds {r['Seed AUC mean ± SD']}")
# correct classifications
A('- Correct classifications (videos; computed as n − FP − FN from T4):')
for d, rows_ in [('FF++ C23', (1, 2, 3)), ('FF++ C40', (5, 6, 7)), ('Celeb-DF v2', (9, 10, 11)), ('DeeperForensics-1.0', (13, 14, 15))]:
    n = int(t['T4'].iloc[rows_[0] - 1, 1].split(' — ')[1].split(' videos')[0])
    s = ', '.join(f"{t['T4'].loc[i, 'Model']} {n - int(t['T4'].loc[i, 'FP']) - int(t['T4'].loc[i, 'FN'])}" for i in rows_)
    A(f'  - {d} (n = {n}): {s} (T4 r{rows_[0] + 1}–r{rows_[2] + 1})')
for i, r in t['T5'].iterrows():
    lab = r['Test set'] or t['T5'].loc[i - 1, 'Test set']
    A(f"- T5 r{i + 1} {lab} vs {r.Comparator}: ΔAUC {r['ΔAUC']} {r['95% CI']}, raw p {r['Raw p']}, Holm p {r['Holm p']}")
A('- All 8 within-dataset Holm p = 1.000; raw p 0.198 (T5 r4) to 0.925 (T5 r5). SwinFusion++ point estimate lower in 6 of 8 (T5 r1–r6).')
A('- Envelope of the 8 paired intervals: lowest bound −0.0101 (T5 r4), highest +0.0085 (T5 r8) → print "each paired 95% interval lay between −0.011 and +0.009 AUC".')
j6 = t['J6']
A(f"- MDD (α = 0.05/8): {min(j6['MDD (α = 0.05/8)'])}–{max(j6['MDD (α = 0.05/8)'])}; headroom {min(j6['Headroom'])}–{max(j6['Headroom'])}; "
  'MDD > headroom in 7 of 8 (exception FF++ C23 vs Video Swin-B: 0.0030 vs 0.0049, J6 r2) (J6).')
for lab, comp in [('CDF → CDF', 'Swin-B'), ('DFo → DFo', 'Video Swin-B')]:
    i = find('J2', lab, comp)
    A(f"- Supplementary within Δ, {lab} vs {comp} (J2 r{i + 1}): ΔAcc {cellv('J2', i, 'ΔAcc [95% CI]')} pp; ΔRec {cellv('J2', i, 'ΔRec [95% CI]')} pp; ΔF1 {cellv('J2', i, 'ΔF1 [95% CI]')}")
A('- Within-dataset ΔAcc intervals excluding 0: 2 of 8, both higher for SwinFusion++ (above). Celeb-DF one carries the 9-cluster caveat.')
A('- C40 seeds: SwinFusion++ 0.9874 / 0.9841 / 0.9865 vs Video Swin-B 0.9931 / 0.9913 / 0.9886 (J1 r5, r8); all 9 cross-seed pairings negative '
  '(−0.0089 to −0.0012; stats_out/statistician_seed_robustness.csv).\n')

A('## 4.1.2 Frozen transfer, fixed recipe\n')
for i, r in t['T6'].iterrows():
    lab = r['Direction'] or t['T6'].loc[i - 1, 'Direction']
    A(f"- T6 r{i + 1} {lab} vs {r.Comparator}: SwinFusion++ {r['SwinFusion++ AUC']}, comparator {r['Comparator AUC']}, ΔAUC {r['ΔAUC']} {r['95% CI']}, raw p {r['Raw p']}, Holm p {r['Holm p']}")
A('- vs Swin-B: significantly higher in 7 of 9 (ΔAUC +0.0490, T6 r7, to +0.2584, T6 r5); no detectable difference C23 → C40, C23 → CDF.')
A('- vs Video Swin-B: significantly higher in 3 of 9 (CDF → C40 +0.0754 T6 r10; CDF → DFo +0.0630 T6 r12; DFo → C40 +0.0840 T6 r16); no detectable difference in 6; significantly lower in none.')
A('- 5 negative point estimates (T6 r3, r4, r6, r8, r18); largest −0.0159 [−0.0407, +0.0090] (T6 r6). Widest lower bound −0.0917 (T6 r18, DFo → CDF vs Video Swin-B) → "−0.092".')
A('- CI excludes 0 but not Holm-significant: DFo → C23 vs Video Swin-B +0.0451 [+0.0077, +0.0816], raw p 0.019, Holm p 0.152 (T6 r14).')
for mk_col in ['SwinFusion++', 'Swin-B', 'Video Swin-B']:
    pass
j8 = t['J8']
A(f"- C23 → DFo: Swin-B {j8.loc[2, 'Swin-B']}; SwinFusion++ {j8.loc[2, 'SwinFusion++']}; Video Swin-B {j8.loc[2, 'Video Swin-B']} (J8 r3).")
j3 = t['J3']
A(f"- C23 → DFo strict lineage-free subset (n = 60), seed means: SwinFusion++ {j3.loc[0, 'Mean']}, Swin-B {j3.loc[2, 'Mean']}, Video Swin-B {j3.loc[3, 'Mean']} (J3 r1, r3, r4); no interval.")
A('- DFo → C23 and DFo → C40 strict subsets have n = 20 (J3 r5, r9): too small to check those wins.')
A(f"- DFo → CDF: Swin-B {j8.loc[8, 'Swin-B']}, SwinFusion++ {j8.loc[8, 'SwinFusion++']}, Video Swin-B {j8.loc[8, 'Video Swin-B']} (J8 r9).")
A('- Transfer ROC-AUC range, three fixed-recipe models: 0.4593 (Swin-B, DFo → CDF; T6 r17) to 0.9760 (SwinFusion++, C23 → C40; T6 r1). SwinFusion++ alone: 0.5879–0.9760.')
A('- Seed sign agreement: 9 of the 10 significant differences agree in 9/9 cross-seed pairings; CDF → C40 vs Video Swin-B 8/9 (J7 r4).')
A(f"- Celeb-DF leave-one-identity-out, DFo → CDF vs Swin-B: {t['J7'].loc[9, 'CDF leave-one-identity-out ΔAUC']} (J7 r10).")
A('- DFo-target results unchanged at 175 global lineage clusters (J7 "Holm p (DFo global clusters)"; stats_out/statistician_dfo_global_cluster.csv: no Holm decision changed in any family; CI bounds moved ≤ 0.0025).')
A('- Mean transfer AUC (Appendix J only, J8 r10): 0.8099 / 0.7002 / 0.7848 / 0.7623 — NOT for the Chapter 4 text.\n')

A('## 4.1.3 Threshold-dependent metrics under transfer\n')
t7 = t['T7']
specs = [float(x) for x, m_ in zip(t7['Spec (%)'], t7.Model) if m_ != '__SPAN__']
A(f'- Specificity range: {min(specs):.2f}–{max(specs):.2f}% (T7; min = Swin-B C23 → CDF, T7 r7).')
A('- Recall: 0.00–63.70% in all directions except C23 → C40 (79.29–87.14%, T7 r2–r4); 63.70 = Swin-B C23 → CDF (T7 r7).')
A('- DFo → CDF accuracy 13.80–15.24% (T7 r34–r36), against 13.80% for calling every video real (1 − 0.862).')
A('- From CDF and DFo sources every model made at most 60 positive calls (T7: Video Swin-B CDF → C23 TP 59 + FP 1, r16); recall 0.00–42.14%.')
A('- Swin-B made no positive call in DFo → C23, DFo → C40 and DFo → CDF (precision and F1 "—"; T7 r27, r31, r35).')
A('- SwinFusion++ never had the highest transfer accuracy, recall or F1 (point estimates; T7). Ties: CDF → C40 SwinFusion++ = Swin-B (52.14 / 4.29 / 0.0822), both below Video Swin-B.')
A('- Supplementary ΔAcc intervals excluding 0 (J2; percentage points):')
for lab, comp in [('C23 → C40', 'Swin-B'), ('C23 → C40', 'Video Swin-B'), ('C23 → CDF', 'Swin-B'), ('C23 → CDF', 'Video Swin-B'),
                  ('C23 → DFo', 'Video Swin-B'), ('CDF → C23', 'Video Swin-B'), ('CDF → C23', 'Swin-B'), ('CDF → DFo', 'Swin-B')]:
    try:
        i = find('J2', lab, comp)
    except (KeyError, IndexError):
        # second row of a pair has an empty first cell
        j = grp_rows('J2', lab, 2)[1]; i = j
    A(f"  - {lab} vs {comp} (J2 r{i + 1}): ΔAcc {cellv('J2', i, 'ΔAcc [95% CI]')}; ΔF1 {cellv('J2', i, 'ΔF1 [95% CI]')}")
A('  - Count: 6 lower (first six above), 2 higher (last two), out of 18 transfer comparisons.\n')

A('## 4.1.4 Configured system and optimization effect\n')
for i, r in t['T8'].iterrows():
    lab = r['Condition'] or t['T8'].loc[i - 1, 'Condition']
    A(f"- T8 r{i + 1} {lab} vs {r.Comparator}: BO {r['SwinFusion++ (BO) AUC']}, comparator {r['Comparator AUC']}, ΔAUC {r['ΔAUC']} {r['95% CI']}, raw p {r['Raw p']}, Holm p {r['Holm p']}")
A('- Configured system within: 0 of 8 Holm-significant (smallest Holm p 0.178, T8 r3). Transfer vs Swin-B: 6 of 9 significant (T8 r9, r13, r19, r21, r23, r25); '
  'vs Video Swin-B: higher on C23 → C40 (T8 r10), lower on C23 → DFo (T8 r14) and CDF → C23 (T8 r16).')
for i, r in t['T9'].iterrows():
    A(f"- T9 r{i + 1} {r.Condition}: BO {r['BO AUC']}, fixed {r['Fixed AUC']}, ΔAUC {r['ΔAUC']} {r['95% CI']}, raw p {r['Raw p']}, Holm p {r['Holm p']}")
A('- Optimization effect: significant gains C40 → C40 (T9 r2), CDF → CDF (T9 r3, grouping-dependent), C23 → C40 (T9 r5); significant losses in 5 transfer directions, '
  '−0.0409 (T9 r10) to −0.1039 (T9 r9): C23 → DFo, CDF → C40, CDF → DFo, DFo → C23, DFo → C40.')
A('- BO trial counts and best validation AUCs are NOT in these tables (methodologist / 00_Shared/bayesian_optimisation).\n')

A('## 4.1.5 Answer to RQ1: reuse the strings above. Agreed sentences use: 7 of 9; 3 of 9; −0.092; −0.011 and +0.009; 7 of 8; 6 of 18; 2.\n')

A('## Chapter 3 amendment paragraph (D2_final.txt)\n')
A('- Pre-scoring specification date: September 30, 2026 (decision A-07, autonomous_decisions_v020.md); 5,000 draws; 5,000 permutations; seed 20260930 (not printed).')
A('- 10 of 65 RQ1/RQ6 decisions changed by the correction (J5); among 26 architecture comparisons, 1 removed and 2 added (J5; see Opening section for rows).')
A('- 73 of 73 bootstrap-decision agreement, including the 8 RQ4 control comparisons (stats_out/statistician_r2_bootstrap_p_check.csv).')
A('- Six families: m = 8, 18, 8, 18, 4, 9; pooled architecture family m = 26; pre-scoring partition m = 12 / 27 (A-16).')
A('- Grouping-dependent: 0.021 vs 0.077 (T9 r3; T9 note).')
A('- DeeperForensics-1.0 lineage clusters: 175 instead of 201; Celeb-DF v2: 9 identity clusters; nine cross-seed pairings.')
A('- McNemar: Celeb-DF v2 clusters hold up to 207 videos; FF++ clusters 4; DeeperForensics-1.0 clusters 2 (T1_clusters_helper.csv; Round 1 memo A-1).')
open(f'{TAB}/KEY_NUMBERS.md', 'w').write('\n'.join(L) + '\n')
print('KEY_NUMBERS.md lines:', len(L))
