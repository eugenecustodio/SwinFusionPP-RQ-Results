# KEY_NUMBERS: printed strings for the Chapter 4 opening, 4.1.1–4.1.5 and the Chapter 3 amendment

Convention: `Tn rK [column]` = table CSV in `team/tables/`, 1-based data row K (header excluded, `__SPAN__` rows counted). Minus signs are U+2212. Copy strings exactly. Numbers not in a table cite their stats_out source.

## Opening (Evaluation Setting)

- FF++ C23: 280 videos (140 fake, 140 real), 70 clusters; clusters containing fakes: 70; coverage 100%, preprocessing failures 0 (T1_clusters_helper.csv; T1 by methodologist agrees)
- FF++ C40: 280 videos (140 fake, 140 real), 70 clusters; clusters containing fakes: 70; coverage 100%, preprocessing failures 0 (T1_clusters_helper.csv; T1 by methodologist agrees)
- Celeb-DF v2: 978 videos (843 fake, 135 real), 54 clusters; clusters containing fakes: 9; coverage 100%, preprocessing failures 0 (T1_clusters_helper.csv; T1 by methodologist agrees)
- DeeperForensics-1.0: 402 videos (201 fake, 201 real), 201 clusters; clusters containing fakes: 201; coverage 100%, preprocessing failures 0 (T1_clusters_helper.csv; T1 by methodologist agrees)
- Celeb-DF v2: 45 of the 54 clusters are single real videos; the 9 identity clusters hold 33–197 fakes each (stats_out/statistician_cdf_loo_identity.csv, fakes_per_cluster).
- DeeperForensics-1.0: 175 global lineage clusters vs 201 dependency clusters (T1_clusters_helper.csv).
- Celeb-DF v2 fake prevalence: 86.20% (T7 r5 span text); PR-AUC baselines 0.500 / 0.862 (T4 note).
- Coverage: 100% and 0 preprocessing failures in all 180 full-test seed × cell rows (heldout_seed_metrics_rq1_rq6.csv, plain, full_test).
- Rank-correction effect (architecture, 26 comparisons): removed one significant SwinFusion++ advantage, DFo → DFo vs Video Swin-B, Holm p < 0.005 → 1.000 (J5 r8); added two vs Swin-B: CDF → C23 0.342 → 0.018 (J5 r15) and DFo → CDF 1.000 → < 0.005 (J5 r25) [Holm (original) → Holm (rank)].
- Decisions changed by the correction: 10 of 65 RQ1/RQ6 comparisons (J5, "Decision changed?" = Yes). By family: architecture 3, configured system 5, optimization effect 2.
- Same 10 of 26 architecture comparisons significant under the final, pre-scoring (m = 27) and pooled (m = 26) partitions (J7; stats_out/statistician_holm_partitions.csv).
- Holm decisions from the stored paired-bootstrap p-values agreed with the rank test in 73 of 73 paired comparisons (65 RQ1/RQ6 + 8 RQ4 controls) (stats_out/statistician_r2_bootstrap_p_check.csv). Do not print any bootstrap p.
- Grouping-dependent result: BO − fixed within Celeb-DF v2, Holm p 0.021 (T9 r3) vs 0.077 pooled (T9 note; paired_tests_optionA.csv holm_sensitivity_pooled).
- Families: within-dataset architecture (m = 8), frozen-transfer architecture (m = 18), configured system (m = 8 / 18), optimization effect (m = 4 / 9).

## 4.1.1 In-distribution, fixed recipe

- ROC-AUC range over the 12 model × dataset cells: 0.9878 (T4 r6) to 0.9974 (T4 r14); both extremes are SwinFusion++ (C40 and DeeperForensics-1.0).
- Span T4 r1: "FF++ C23 — 280 videos (140 fake), 70 clusters"
  - T4 r2 SwinFusion++: AUC 0.9942 [0.9834, 0.9999]; PR-AUC 0.9963; Acc 97.86; Prec 98.55; Rec 97.14; Spec 98.57; F1 0.9784; FP 2; FN 4; seeds 0.9939 ± 0.0009
  - T4 r3 Swin-B: AUC 0.9965 [0.9906, 0.9999]; PR-AUC 0.9973; Acc 97.86; Prec 97.18; Rec 98.57; Spec 97.14; F1 0.9787; FP 4; FN 2; seeds 0.9965 ± 0.0007
  - T4 r4 Video Swin-B: AUC 0.9951 [0.9856, 1.0000]; PR-AUC 0.9967; Acc 98.93; Prec 99.28; Rec 98.57; Spec 99.29; F1 0.9892; FP 1; FN 2; seeds 0.9952 ± 0.0009
- Span T4 r5: "FF++ C40 — 280 videos (140 fake), 70 clusters"
  - T4 r6 SwinFusion++: AUC 0.9878 [0.9772, 0.9965]; PR-AUC 0.9896; Acc 94.64; Prec 93.71; Rec 95.71; Spec 93.57; F1 0.9470; FP 9; FN 6; seeds 0.9860 ± 0.0017
  - T4 r7 Swin-B: AUC 0.9883 [0.9777, 0.9960]; PR-AUC 0.9895; Acc 94.64; Prec 95.62; Rec 93.57; Spec 95.71; F1 0.9458; FP 6; FN 9; seeds 0.9875 ± 0.0013
  - T4 r8 Video Swin-B: AUC 0.9915 [0.9818, 0.9983]; PR-AUC 0.9933; Acc 95.71; Prec 95.71; Rec 95.71; Spec 95.71; F1 0.9571; FP 6; FN 6; seeds 0.9910 ± 0.0022
- Span T4 r9: "Celeb-DF v2 — 978 videos (843 fake), 54 clusters; all fakes in 9 identity clusters"
  - T4 r10 SwinFusion++: AUC 0.9951 [0.9905, 0.9995]; PR-AUC 0.9992; Acc 97.75; Prec 99.28; Rec 98.10; Spec 95.56; F1 0.9869; FP 6; FN 16; seeds 0.9939 ± 0.0022
  - T4 r11 Swin-B: AUC 0.9958 [0.9925, 0.9990]; PR-AUC 0.9993; Acc 95.40; Prec 99.63; Rec 95.02; Spec 97.78; F1 0.9727; FP 3; FN 42; seeds 0.9956 ± 0.0002
  - T4 r12 Video Swin-B: AUC 0.9958 [0.9915, 0.9994]; PR-AUC 0.9993; Acc 98.26; Prec 99.28; Rec 98.70; Spec 95.56; F1 0.9899; FP 6; FN 11; seeds 0.9954 ± 0.0003
- Span T4 r13: "DeeperForensics-1.0 — 402 videos (201 fake), 201 clusters"
  - T4 r14 SwinFusion++: AUC 0.9974 [0.9921, 1.0000]; PR-AUC 0.9980; Acc 98.76; Prec 100.00; Rec 97.51; Spec 100.00; F1 0.9874; FP 0; FN 5; seeds 0.9971 ± 0.0011
  - T4 r15 Swin-B: AUC 0.9966 [0.9892, 1.0000]; PR-AUC 0.9978; Acc 97.76; Prec 100.00; Rec 95.52; Spec 100.00; F1 0.9771; FP 0; FN 9; seeds 0.9968 ± 0.0009
  - T4 r16 Video Swin-B: AUC 0.9945 [0.9842, 0.9999]; PR-AUC 0.9966; Acc 97.01; Prec 99.48; Rec 94.53; Spec 99.50; F1 0.9694; FP 1; FN 11; seeds 0.9944 ± 0.0006
- Correct classifications (videos; computed as n − FP − FN from T4):
  - FF++ C23 (n = 280): SwinFusion++ 274, Swin-B 274, Video Swin-B 277 (T4 r2–r4)
  - FF++ C40 (n = 280): SwinFusion++ 265, Swin-B 265, Video Swin-B 268 (T4 r6–r8)
  - Celeb-DF v2 (n = 978): SwinFusion++ 956, Swin-B 933, Video Swin-B 961 (T4 r10–r12)
  - DeeperForensics-1.0 (n = 402): SwinFusion++ 397, Swin-B 393, Video Swin-B 390 (T4 r14–r16)
- T5 r1 FF++ C23 vs Swin-B: ΔAUC −0.0023 [−0.0079, +0.0009], raw p 0.461, Holm p 1.000
- T5 r2 FF++ C23 vs Video Swin-B: ΔAUC −0.0008 [−0.0031, +0.0002], raw p 0.254, Holm p 1.000
- T5 r3 FF++ C40 vs Swin-B: ΔAUC −0.0005 [−0.0076, +0.0061], raw p 0.907, Holm p 1.000
- T5 r4 FF++ C40 vs Video Swin-B: ΔAUC −0.0037 [−0.0101, +0.0013], raw p 0.198, Holm p 1.000
- T5 r5 Celeb-DF v2 vs Swin-B: ΔAUC −0.0007 [−0.0048, +0.0026], raw p 0.925, Holm p 1.000
- T5 r6 Celeb-DF v2 vs Video Swin-B: ΔAUC −0.0007 [−0.0033, +0.0012], raw p 0.774, Holm p 1.000
- T5 r7 DeeperForensics-1.0 vs Swin-B: ΔAUC +0.0009 [−0.0007, +0.0036], raw p 0.652, Holm p 1.000
- T5 r8 DeeperForensics-1.0 vs Video Swin-B: ΔAUC +0.0029 [−0.0005, +0.0085], raw p 0.299, Holm p 1.000
- All 8 within-dataset Holm p = 1.000; raw p 0.198 (T5 r4) to 0.925 (T5 r5). SwinFusion++ point estimate lower in 6 of 8 (T5 r1–r6).
- Envelope of the 8 paired intervals: lowest bound −0.0101 (T5 r4), highest +0.0085 (T5 r8) → print "each paired 95% interval lay between −0.011 and +0.009 AUC".
- MDD (α = 0.05/8): 0.0030–0.0123; headroom 0.0034–0.0117; MDD > headroom in 7 of 8 (exception FF++ C23 vs Video Swin-B: 0.0030 vs 0.0049, J6 r2) (J6).
- Supplementary within Δ, CDF → CDF vs Swin-B (J2 r5): ΔAcc +2.35 [+0.08, +5.10] pp; ΔRec +3.08 [+0.59, +5.99] pp; ΔF1 +0.0142 [+0.0005, +0.0318]
- Supplementary within Δ, DFo → DFo vs Video Swin-B (J2 r8): ΔAcc +1.74 [+0.50, +3.23] pp; ΔRec +2.99 [+0.50, +5.97] pp; ΔF1 +0.0180 [+0.0050, +0.0338]
- Within-dataset ΔAcc intervals excluding 0: 2 of 8, both higher for SwinFusion++ (above). Celeb-DF one carries the 9-cluster caveat.
- C40 seeds: SwinFusion++ 0.9874 / 0.9841 / 0.9865 vs Video Swin-B 0.9931 / 0.9913 / 0.9886 (J1 r5, r8); all 9 cross-seed pairings negative (−0.0089 to −0.0012; stats_out/statistician_seed_robustness.csv).

## 4.1.2 Frozen transfer, fixed recipe

- T6 r1 C23 → C40 vs Swin-B: SwinFusion++ 0.9760, comparator 0.9739, ΔAUC +0.0021 [−0.0068, +0.0103], raw p 0.631, Holm p 1.000
- T6 r2 C23 → C40 vs Video Swin-B: SwinFusion++ 0.9760, comparator 0.9746, ΔAUC +0.0014 [−0.0089, +0.0102], raw p 0.801, Holm p 1.000
- T6 r3 C23 → CDF vs Swin-B: SwinFusion++ 0.8624, comparator 0.8680, ΔAUC −0.0056 [−0.0282, +0.0201], raw p 0.693, Holm p 1.000
- T6 r4 C23 → CDF vs Video Swin-B: SwinFusion++ 0.8624, comparator 0.8676, ΔAUC −0.0052 [−0.0304, +0.0175], raw p 0.687, Holm p 1.000
- T6 r5 C23 → DFo vs Swin-B: SwinFusion++ 0.8261, comparator 0.5678, ΔAUC +0.2584 [+0.2133, +0.3046], raw p < 0.001, Holm p < 0.005
- T6 r6 C23 → DFo vs Video Swin-B: SwinFusion++ 0.8261, comparator 0.8421, ΔAUC −0.0159 [−0.0407, +0.0090], raw p 0.214, Holm p 1.000
- T6 r7 CDF → C23 vs Swin-B: SwinFusion++ 0.8958, comparator 0.8468, ΔAUC +0.0490 [+0.0200, +0.0770], raw p 0.002, Holm p 0.018
- T6 r8 CDF → C23 vs Video Swin-B: SwinFusion++ 0.8958, comparator 0.9047, ΔAUC −0.0089 [−0.0320, +0.0154], raw p 0.466, Holm p 1.000
- T6 r9 CDF → C40 vs Swin-B: SwinFusion++ 0.8384, comparator 0.7770, ΔAUC +0.0614 [+0.0339, +0.0918], raw p < 0.001, Holm p < 0.005
- T6 r10 CDF → C40 vs Video Swin-B: SwinFusion++ 0.8384, comparator 0.7630, ΔAUC +0.0754 [+0.0354, +0.1164], raw p < 0.001, Holm p < 0.005
- T6 r11 CDF → DFo vs Swin-B: SwinFusion++ 0.7233, comparator 0.6012, ΔAUC +0.1220 [+0.0933, +0.1544], raw p < 0.001, Holm p < 0.005
- T6 r12 CDF → DFo vs Video Swin-B: SwinFusion++ 0.7233, comparator 0.6603, ΔAUC +0.0630 [+0.0302, +0.0991], raw p < 0.001, Holm p 0.004
- T6 r13 DFo → C23 vs Swin-B: SwinFusion++ 0.8127, comparator 0.6115, ΔAUC +0.2012 [+0.1569, +0.2492], raw p < 0.001, Holm p < 0.005
- T6 r14 DFo → C23 vs Video Swin-B: SwinFusion++ 0.8127, comparator 0.7676, ΔAUC +0.0451 [+0.0077, +0.0816], raw p 0.019, Holm p 0.152
- T6 r15 DFo → C40 vs Swin-B: SwinFusion++ 0.7668, comparator 0.5964, ΔAUC +0.1705 [+0.1290, +0.2164], raw p < 0.001, Holm p < 0.005
- T6 r16 DFo → C40 vs Video Swin-B: SwinFusion++ 0.7668, comparator 0.6829, ΔAUC +0.0840 [+0.0439, +0.1229], raw p < 0.001, Holm p < 0.005
- T6 r17 DFo → CDF vs Swin-B: SwinFusion++ 0.5879, comparator 0.4593, ΔAUC +0.1286 [+0.0626, +0.1864], raw p < 0.001, Holm p < 0.005
- T6 r18 DFo → CDF vs Video Swin-B: SwinFusion++ 0.5879, comparator 0.6001, ΔAUC −0.0122 [−0.0917, +0.0487], raw p 0.793, Holm p 1.000
- vs Swin-B: significantly higher in 7 of 9 (ΔAUC +0.0490, T6 r7, to +0.2584, T6 r5); no detectable difference C23 → C40, C23 → CDF.
- vs Video Swin-B: significantly higher in 3 of 9 (CDF → C40 +0.0754 T6 r10; CDF → DFo +0.0630 T6 r12; DFo → C40 +0.0840 T6 r16); no detectable difference in 6; significantly lower in none.
- 5 negative point estimates (T6 r3, r4, r6, r8, r18); largest −0.0159 [−0.0407, +0.0090] (T6 r6). Widest lower bound −0.0917 (T6 r18, DFo → CDF vs Video Swin-B) → "−0.092".
- CI excludes 0 but not Holm-significant: DFo → C23 vs Video Swin-B +0.0451 [+0.0077, +0.0816], raw p 0.019, Holm p 0.152 (T6 r14).
- C23 → DFo: Swin-B 0.5678 [0.5250, 0.6105]; SwinFusion++ 0.8261 [0.7926, 0.8603]; Video Swin-B 0.8421 [0.8092, 0.8740] (J8 r3).
- C23 → DFo strict lineage-free subset (n = 60), seed means: SwinFusion++ 0.7356, Swin-B 0.5322, Video Swin-B 0.7874 (J3 r1, r3, r4); no interval.
- DFo → C23 and DFo → C40 strict subsets have n = 20 (J3 r5, r9): too small to check those wins.
- DFo → CDF: Swin-B 0.4593 [0.3970, 0.5259], SwinFusion++ 0.5879 [0.5210, 0.6592], Video Swin-B 0.6001 [0.5354, 0.6750] (J8 r9).
- Transfer ROC-AUC range, three fixed-recipe models: 0.4593 (Swin-B, DFo → CDF; T6 r17) to 0.9760 (SwinFusion++, C23 → C40; T6 r1). SwinFusion++ alone: 0.5879–0.9760.
- Seed sign agreement: 9 of the 10 significant differences agree in 9/9 cross-seed pairings; CDF → C40 vs Video Swin-B 8/9 (J7 r4).
- Celeb-DF leave-one-identity-out, DFo → CDF vs Swin-B: +0.1122 to +0.1477 (J7 r10).
- DFo-target results unchanged at 175 global lineage clusters (J7 "Holm p (DFo global clusters)"; stats_out/statistician_dfo_global_cluster.csv: no Holm decision changed in any family; CI bounds moved ≤ 0.0025).
- Mean transfer AUC (Appendix J only, J8 r10): 0.8099 / 0.7002 / 0.7848 / 0.7623 — NOT for the Chapter 4 text.

## 4.1.3 Threshold-dependent metrics under transfer

- Specificity range: 91.11–100.00% (T7; min = Swin-B C23 → CDF, T7 r7).
- Recall: 0.00–63.70% in all directions except C23 → C40 (79.29–87.14%, T7 r2–r4); 63.70 = Swin-B C23 → CDF (T7 r7).
- DFo → CDF accuracy 13.80–15.24% (T7 r34–r36), against 13.80% for calling every video real (1 − 0.862).
- From CDF and DFo sources every model made at most 60 positive calls (T7: Video Swin-B CDF → C23 TP 59 + FP 1, r16); recall 0.00–42.14%.
- Swin-B made no positive call in DFo → C23, DFo → C40 and DFo → CDF (precision and F1 "—"; T7 r27, r31, r35).
- SwinFusion++ never had the highest transfer accuracy, recall or F1 (point estimates; T7). Ties: CDF → C40 SwinFusion++ = Swin-B (52.14 / 4.29 / 0.0822), both below Video Swin-B.
- Supplementary ΔAcc intervals excluding 0 (J2; percentage points):
  - C23 → C40 vs Swin-B (J2 r9): ΔAcc −3.21 [−6.07, −0.36]; ΔF1 −0.0398 [−0.0751, −0.0053]
  - C23 → C40 vs Video Swin-B (J2 r10): ΔAcc −3.21 [−5.36, −1.07]; ΔF1 −0.0385 [−0.0656, −0.0137]
  - C23 → CDF vs Swin-B (J2 r11): ΔAcc −8.08 [−13.53, −1.78]; ΔF1 −0.0767 [−0.1340, −0.0198]
  - C23 → CDF vs Video Swin-B (J2 r12): ΔAcc −7.06 [−13.22, −1.17]; ΔF1 −0.0668 [−0.1446, −0.0110]
  - C23 → DFo vs Video Swin-B (J2 r14): ΔAcc −6.47 [−8.71, −4.23]; ΔF1 −0.2139 [−0.2826, −0.1441]
  - CDF → C23 vs Video Swin-B (J2 r16): ΔAcc −7.14 [−10.36, −4.29]; ΔF1 −0.1567 [−0.2208, −0.0972]
  - CDF → C23 vs Swin-B (J2 r15): ΔAcc +3.21 [+1.07, +5.71]; ΔF1 +0.0901 [+0.0352, +0.1535]
  - CDF → DFo vs Swin-B (J2 r19): ΔAcc +1.74 [+0.50, +3.23]; ΔF1 +0.0647 [+0.0195, +0.1126]
  - Count: 6 lower (first six above), 2 higher (last two), out of 18 transfer comparisons.

## 4.1.4 Configured system and optimization effect

- T8 r1 C23 → C23 vs Swin-B: BO 0.9964, comparator 0.9965, ΔAUC −0.0001 [−0.0027, +0.0017], raw p 0.945, Holm p 1.000
- T8 r2 C23 → C23 vs Video Swin-B: BO 0.9964, comparator 0.9951, ΔAUC +0.0014 [0.0000, +0.0037], raw p 0.189, Holm p 1.000
- T8 r3 C40 → C40 vs Swin-B: BO 0.9941, comparator 0.9883, ΔAUC +0.0058 [+0.0010, +0.0124], raw p 0.022, Holm p 0.178
- T8 r4 C40 → C40 vs Video Swin-B: BO 0.9941, comparator 0.9915, ΔAUC +0.0026 [−0.0026, +0.0090], raw p 0.485, Holm p 1.000
- T8 r5 CDF → CDF vs Swin-B: BO 0.9983, comparator 0.9958, ΔAUC +0.0024 [+0.0002, +0.0057], raw p 0.071, Holm p 0.500
- T8 r6 CDF → CDF vs Video Swin-B: BO 0.9983, comparator 0.9958, ΔAUC +0.0024 [+0.0001, +0.0058], raw p 0.204, Holm p 1.000
- T8 r7 DFo → DFo vs Swin-B: BO 0.9954, comparator 0.9966, ΔAUC −0.0012 [−0.0041, +0.0007], raw p 0.531, Holm p 1.000
- T8 r8 DFo → DFo vs Video Swin-B: BO 0.9954, comparator 0.9945, ΔAUC +0.0008 [−0.0030, +0.0050], raw p 0.774, Holm p 1.000
- T8 r9 C23 → C40 vs Swin-B: BO 0.9862, comparator 0.9739, ΔAUC +0.0123 [+0.0048, +0.0211], raw p < 0.001, Holm p 0.010
- T8 r10 C23 → C40 vs Video Swin-B: BO 0.9862, comparator 0.9746, ΔAUC +0.0116 [+0.0040, +0.0214], raw p 0.001, Holm p 0.015
- T8 r11 C23 → CDF vs Swin-B: BO 0.8785, comparator 0.8680, ΔAUC +0.0105 [−0.0090, +0.0315], raw p 0.268, Holm p 1.000
- T8 r12 C23 → CDF vs Video Swin-B: BO 0.8785, comparator 0.8676, ΔAUC +0.0109 [−0.0086, +0.0298], raw p 0.366, Holm p 1.000
- T8 r13 C23 → DFo vs Swin-B: BO 0.7316, comparator 0.5678, ΔAUC +0.1638 [+0.1220, +0.2096], raw p < 0.001, Holm p < 0.005
- T8 r14 C23 → DFo vs Video Swin-B: BO 0.7316, comparator 0.8421, ΔAUC −0.1105 [−0.1374, −0.0820], raw p < 0.001, Holm p < 0.005
- T8 r15 CDF → C23 vs Swin-B: BO 0.8657, comparator 0.8468, ΔAUC +0.0189 [−0.0140, +0.0499], raw p 0.228, Holm p 1.000
- T8 r16 CDF → C23 vs Video Swin-B: BO 0.8657, comparator 0.9047, ΔAUC −0.0390 [−0.0617, −0.0179], raw p < 0.001, Holm p 0.005
- T8 r17 CDF → C40 vs Swin-B: BO 0.7345, comparator 0.7770, ΔAUC −0.0425 [−0.0806, −0.0026], raw p 0.025, Holm p 0.197
- T8 r18 CDF → C40 vs Video Swin-B: BO 0.7345, comparator 0.7630, ΔAUC −0.0285 [−0.0606, +0.0070], raw p 0.107, Holm p 0.747
- T8 r19 CDF → DFo vs Swin-B: BO 0.6824, comparator 0.6012, ΔAUC +0.0811 [+0.0511, +0.1130], raw p < 0.001, Holm p < 0.005
- T8 r20 CDF → DFo vs Video Swin-B: BO 0.6824, comparator 0.6603, ΔAUC +0.0221 [−0.0104, +0.0573], raw p 0.189, Holm p 1.000
- T8 r21 DFo → C23 vs Swin-B: BO 0.7236, comparator 0.6115, ΔAUC +0.1121 [+0.0724, +0.1563], raw p < 0.001, Holm p < 0.005
- T8 r22 DFo → C23 vs Video Swin-B: BO 0.7236, comparator 0.7676, ΔAUC −0.0439 [−0.0770, −0.0106], raw p 0.016, Holm p 0.144
- T8 r23 DFo → C40 vs Swin-B: BO 0.7067, comparator 0.5964, ΔAUC +0.1103 [+0.0750, +0.1501], raw p < 0.001, Holm p < 0.005
- T8 r24 DFo → C40 vs Video Swin-B: BO 0.7067, comparator 0.6829, ΔAUC +0.0239 [−0.0127, +0.0609], raw p 0.193, Holm p 1.000
- T8 r25 DFo → CDF vs Swin-B: BO 0.5519, comparator 0.4593, ΔAUC +0.0926 [+0.0263, +0.1477], raw p 0.002, Holm p 0.022
- T8 r26 DFo → CDF vs Video Swin-B: BO 0.5519, comparator 0.6001, ΔAUC −0.0482 [−0.1277, +0.0138], raw p 0.168, Holm p 1.000
- Configured system within: 0 of 8 Holm-significant (smallest Holm p 0.178, T8 r3). Transfer vs Swin-B: 6 of 9 significant (T8 r9, r13, r19, r21, r23, r25); vs Video Swin-B: higher on C23 → C40 (T8 r10), lower on C23 → DFo (T8 r14) and CDF → C23 (T8 r16).
- T9 r1 C23 → C23: BO 0.9964, fixed 0.9942, ΔAUC +0.0022 [+0.0001, +0.0058], raw p 0.074, Holm p 0.148
- T9 r2 C40 → C40: BO 0.9941, fixed 0.9878, ΔAUC +0.0063 [+0.0018, +0.0118], raw p < 0.001, Holm p 0.002
- T9 r3 CDF → CDF: BO 0.9983, fixed 0.9951, ΔAUC +0.0031 [+0.0005, +0.0060], raw p 0.007, Holm p 0.021
- T9 r4 DFo → DFo: BO 0.9954, fixed 0.9974, ΔAUC −0.0021 [−0.0051, 0.0000], raw p 0.115, Holm p 0.148
- T9 r5 C23 → C40: BO 0.9862, fixed 0.9760, ΔAUC +0.0102 [+0.0043, +0.0182], raw p < 0.001, Holm p < 0.005
- T9 r6 C23 → CDF: BO 0.8785, fixed 0.8624, ΔAUC +0.0161 [+0.0018, +0.0301], raw p 0.054, Holm p 0.109
- T9 r7 C23 → DFo: BO 0.7316, fixed 0.8261, ΔAUC −0.0946 [−0.1218, −0.0662], raw p < 0.001, Holm p < 0.005
- T9 r8 CDF → C23: BO 0.8657, fixed 0.8958, ΔAUC −0.0302 [−0.0589, −0.0042], raw p 0.022, Holm p 0.066
- T9 r9 CDF → C40: BO 0.7345, fixed 0.8384, ΔAUC −0.1039 [−0.1416, −0.0662], raw p < 0.001, Holm p < 0.005
- T9 r10 CDF → DFo: BO 0.6824, fixed 0.7233, ΔAUC −0.0409 [−0.0649, −0.0170], raw p 0.001, Holm p 0.005
- T9 r11 DFo → C23: BO 0.7236, fixed 0.8127, ΔAUC −0.0891 [−0.1239, −0.0526], raw p < 0.001, Holm p 0.002
- T9 r12 DFo → C40: BO 0.7067, fixed 0.7668, ΔAUC −0.0601 [−0.0868, −0.0313], raw p < 0.001, Holm p < 0.005
- T9 r13 DFo → CDF: BO 0.5519, fixed 0.5879, ΔAUC −0.0360 [−0.0780, +0.0025], raw p 0.093, Holm p 0.109
- Optimization effect: significant gains C40 → C40 (T9 r2), CDF → CDF (T9 r3, grouping-dependent), C23 → C40 (T9 r5); significant losses in 5 transfer directions, −0.0409 (T9 r10) to −0.1039 (T9 r9): C23 → DFo, CDF → C40, CDF → DFo, DFo → C23, DFo → C40.
- BO trial counts and best validation AUCs are NOT in these tables (methodologist / 00_Shared/bayesian_optimisation).

## 4.1.5 Answer to RQ1: reuse the strings above. Agreed sentences use: 7 of 9; 3 of 9; −0.092; −0.011 and +0.009; 7 of 8; 6 of 18; 2.

## Chapter 3 amendment paragraph (D2_final.txt)

- Pre-scoring specification date: September 30, 2026 (decision A-07, autonomous_decisions_v020.md); 5,000 draws; 5,000 permutations; seed 20260930 (not printed).
- 10 of 65 RQ1/RQ6 decisions changed by the correction (J5); among 26 architecture comparisons, 1 removed and 2 added (J5; see Opening section for rows).
- 73 of 73 bootstrap-decision agreement, including the 8 RQ4 control comparisons (stats_out/statistician_r2_bootstrap_p_check.csv).
- Six families: m = 8, 18, 8, 18, 4, 9; pooled architecture family m = 26; pre-scoring partition m = 12 / 27 (A-16).
- Grouping-dependent: 0.021 vs 0.077 (T9 r3; T9 note).
- DeeperForensics-1.0 lineage clusters: 175 instead of 201; Celeb-DF v2: 9 identity clusters; nine cross-seed pairings.
- McNemar: Celeb-DF v2 clusters hold up to 207 videos; FF++ clusters 4; DeeperForensics-1.0 clusters 2 (T1_clusters_helper.csv; Round 1 memo A-1).
