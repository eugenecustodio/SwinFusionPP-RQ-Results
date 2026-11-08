# RQ1 — Results and Discussion

> **Option A framing (2026-10-28).** This version follows the analysis plan in Chapter 3 of the manuscript and decision D-25 (2026-09-30). The **fixed-recipe comparison is the principal architecture evidence**: Swin-B, Video Swin-B and SwinFusion++ trained with the identical non-BO recipe. The **BO-selected SwinFusion++ is reported separately as a configured system**, together with the optimization effect (BO-selected minus fixed-recipe SwinFusion++). Each comparison type is its own Holm family. Paired p-values are the rank-based cluster permutation tests from the 2026-10-04 correction. ΔAUC values, intervals and metrics are unchanged. All families: `../paired_tests_optionA.csv`.

**RQ1.** To what extent does SwinFusion++ improve video-level deepfake detection performance compared with standalone Swin Transformer and standalone Video Swin Transformer under in-distribution and cross-dataset evaluation, in terms of Accuracy, Precision, Recall, F1-Score, and ROC-AUC?

**Setup (state in the text).**
- **Principal architecture comparison.** Swin-B, Video Swin-B and SwinFusion++ were all trained with the same predefined fixed (non-BO) recipe and evaluated on the same video-level held-out test sets.
- **Configured-system comparison.** SwinFusion++'s training parameters were also selected by Bayesian optimization (BO) on source validation only. That configuration is compared with the same fixed-recipe baselines and is interpreted as configured-system performance with unequal optimization effort.
- **Ensembles and thresholds.** All results are three-seed mean-logit ensembles, with decision thresholds frozen on source validation before any test scoring.
- **Statistics.** ROC-AUC intervals are 95% cluster-bootstrap intervals (5,000 draws over dependency clusters). Paired tests are rank-based cluster permutation tests with Holm correction within each family:
  - RQ1_architecture (8 within-dataset tests);
  - RQ6_architecture (18 transfer tests);
  - RQ1/RQ6_configured_system (8 / 18);
  - RQ1/RQ6_optimization_effect (4 / 9).

Files: `results/table1_within_architecture.*`, `table1b_within_configured_system.*`, `table2_paired_within_architecture.*`, `table2b_paired_within_configured_system.*`, `table3_transfer_auc.*`, `table3_transfer_all_metrics.*`, `table3b_paired_transfer_architecture.*`, `table3c_paired_transfer_configured_system.*`, `table4_tta_variant.*`; figures in `../figures/RQ1/`.

---

## 1. In-distribution results — principal fixed-recipe comparison

| Test set | Model | ROC-AUC [95% CI] | Accuracy | Precision | Recall | Specificity | F1 | Seed AUC mean ± SD |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 | SwinFusion++ | 0.9942 [0.9834, 0.9999] | 97.86% | 98.55% | 97.14% | 98.57% | 0.9784 | 0.9939 ± 0.0009 |
| FF++ C23 | Swin-B | **0.9965** [0.9906, 0.9999] | 97.86% | 97.18% | **98.57%** | 97.14% | 0.9787 | 0.9965 ± 0.0007 |
| FF++ C23 | Video Swin-B | 0.9951 [0.9856, 1.0000] | **98.93%** | **99.28%** | **98.57%** | **99.29%** | **0.9892** | 0.9952 ± 0.0009 |
| FF++ C40 | SwinFusion++ | 0.9878 [0.9772, 0.9965] | 94.64% | 93.71% | **95.71%** | 93.57% | 0.9470 | 0.9860 ± 0.0017 |
| FF++ C40 | Swin-B | 0.9883 [0.9777, 0.9960] | 94.64% | 95.62% | 93.57% | **95.71%** | 0.9458 | 0.9875 ± 0.0013 |
| FF++ C40 | Video Swin-B | **0.9915** [0.9818, 0.9983] | **95.71%** | **95.71%** | **95.71%** | **95.71%** | **0.9571** | 0.9910 ± 0.0022 |
| Celeb-DF v2 | SwinFusion++ | 0.9951 [0.9905, 0.9995] | 97.75% | 99.28% | 98.10% | 95.56% | 0.9869 | 0.9939 ± 0.0022 |
| Celeb-DF v2 | Swin-B | **0.9958** [0.9925, 0.9990] | 95.40% | **99.63%** | 95.02% | **97.78%** | 0.9727 | 0.9956 ± 0.0002 |
| Celeb-DF v2 | Video Swin-B | **0.9958** [0.9915, 0.9994] | **98.26%** | 99.28% | **98.70%** | 95.56% | **0.9899** | 0.9954 ± 0.0003 |
| DeeperForensics | SwinFusion++ | **0.9974** [0.9921, 1.0000] | **98.76%** | **100.00%** | **97.51%** | **100.00%** | **0.9874** | 0.9971 ± 0.0011 |
| DeeperForensics | Swin-B | 0.9966 [0.9892, 1.0000] | 97.76% | **100.00%** | 95.52% | **100.00%** | 0.9771 | 0.9968 ± 0.0009 |
| DeeperForensics | Video Swin-B | 0.9945 [0.9842, 0.9999] | 97.01% | 99.48% | 94.53% | 99.50% | 0.9694 | 0.9944 ± 0.0006 |

**Paired tests (RQ1_architecture family, m = 8, Holm-corrected).** ΔROC-AUC = SwinFusion++ minus baseline, all three trained with the fixed recipe:

| Dataset | vs Swin-B | vs Video Swin-B |
|---|---|---|
| FF++ C23 | −0.0023 [−0.0079, +0.0009], p_Holm = 1.00 | −0.0008 [−0.0031, +0.0002], p_Holm = 1.00 |
| FF++ C40 | −0.0005 [−0.0076, +0.0061], p_Holm = 1.00 | −0.0037 [−0.0101, +0.0013], p_Holm = 1.00 |
| Celeb-DF v2 | −0.0007 [−0.0048, +0.0026], p_Holm = 1.00 | −0.0007 [−0.0033, +0.0012], p_Holm = 1.00 |
| DeeperForensics | +0.0009 [−0.0007, +0.0036], p_Holm = 1.00 | +0.0029 [−0.0005, +0.0085], p_Holm = 1.00 |

### Interpretation

1. **Under matched training, the three architectures are statistically indistinguishable within every dataset.**
   - **Ranking performance.** All nine AUCs lie between 0.9878 and 0.9974, every interval overlaps, and all eight adjusted p-values are 1.00.
   - **Point estimates are within 0.004 AUC.** SwinFusion++ is highest on DeeperForensics (0.9974, with the best accuracy, 98.76%, and F1, 0.9874). It is slightly below one or both encoders on C23, C40 and Celeb-DF.
2. **Accuracy differs by only a few videos.**
   - **C23:** SwinFusion++ ties Swin-B (97.86%), and Video Swin-B is ahead by three videos out of 280.
   - **C40:** SwinFusion++ again ties Swin-B (94.64%).
   - **Celeb-DF:** SwinFusion++ (97.75%) lies between Swin-B (95.40%) and Video Swin-B (98.26%).

   These conditions are near the performance ceiling, so the test has little power to separate the models. The correct reading is "no detectable difference", not equivalence.
3. **Seed stability is comparable across models.** SwinFusion++'s seed-to-seed SD (0.0009–0.0022) is similar to the baselines'.

---

## 2. Cross-dataset (frozen transfer) results — principal fixed-recipe comparison

Source weights, ensemble membership, calibration and thresholds are carried unchanged to the target; no target labels are used for any decision. ROC-AUC (plain variant):

| Trained on → tested on | SwinFusion++ | Swin-B | Video Swin-B | Best |
|---|---|---|---|---|
| FF++ C23 → FF++ C40 | **0.9760** [0.9575, 0.9910] | 0.9739 | 0.9746 | SwinFusion++ |
| FF++ C23 → Celeb-DF v2 | 0.8624 [0.8052, 0.9149] | **0.8680** | 0.8676 | Swin-B |
| FF++ C23 → DeeperForensics | 0.8261 [0.7926, 0.8603] | 0.5678 | **0.8421** | Video Swin-B |
| Celeb-DF → FF++ C23 | 0.8958 [0.8663, 0.9253] | 0.8468 | **0.9047** | Video Swin-B |
| Celeb-DF → FF++ C40 | **0.8384** [0.8056, 0.8725] | 0.7770 | 0.7630 | SwinFusion++ |
| Celeb-DF → DeeperForensics | **0.7233** [0.6869, 0.7604] | 0.6012 | 0.6603 | SwinFusion++ |
| DeeperForensics → FF++ C23 | **0.8127** [0.7802, 0.8475] | 0.6115 | 0.7676 | SwinFusion++ |
| DeeperForensics → FF++ C40 | **0.7668** [0.7322, 0.8032] | 0.5964 | 0.6829 | SwinFusion++ |
| DeeperForensics → Celeb-DF | 0.5879 [0.5210, 0.6592] | 0.4593 | **0.6001** | Video Swin-B |
| **Mean over the nine directions (descriptive)** | **0.810** | 0.700 | 0.785 | |

**Paired transfer tests (RQ6_architecture family, m = 18, Holm-corrected), SwinFusion++ minus baseline:**

| Direction | vs Swin-B | vs Video Swin-B |
|---|---|---|
| C23 → C40 | +0.0021 [−0.0068, +0.0103], p_Holm = 1.00 | +0.0014 [−0.0089, +0.0102], p_Holm = 1.00 |
| C23 → Celeb-DF | −0.0056 [−0.0282, +0.0201], p_Holm = 1.00 | −0.0052 [−0.0304, +0.0175], p_Holm = 1.00 |
| C23 → DeeperForensics | **+0.2584 [+0.2133, +0.3046], p_Holm = 0.004** | −0.0159 [−0.0407, +0.0090], p_Holm = 1.00 |
| Celeb-DF → C23 | **+0.0490 [+0.0200, +0.0770], p_Holm = 0.018** | −0.0089 [−0.0320, +0.0154], p_Holm = 1.00 |
| Celeb-DF → C40 | **+0.0614 [+0.0339, +0.0918], p_Holm = 0.004** | **+0.0754 [+0.0354, +0.1164], p_Holm = 0.004** |
| Celeb-DF → DeeperForensics | **+0.1220 [+0.0933, +0.1544], p_Holm = 0.004** | **+0.0630 [+0.0302, +0.0991], p_Holm = 0.004** |
| DeeperForensics → C23 | **+0.2012 [+0.1569, +0.2492], p_Holm = 0.004** | +0.0451 [+0.0077, +0.0816], p_Holm = 0.15 |
| DeeperForensics → C40 | **+0.1705 [+0.1290, +0.2164], p_Holm = 0.004** | **+0.0840 [+0.0439, +0.1229], p_Holm = 0.004** |
| DeeperForensics → Celeb-DF | **+0.1286 [+0.0626, +0.1864], p_Holm = 0.004** | −0.0122 [−0.0917, +0.0487], p_Holm = 1.00 |

**FF++ C23 → Celeb-DF v2, full metrics (978 videos: 843 fake, 135 real):**

| Model | ROC-AUC | PR-AUC | Acc | Precision | Recall | Specificity | F1 |
|---|---|---|---|---|---|---|---|
| SwinFusion++ | 0.8624 | 0.9752 | 59.41% | **98.69%** | 53.62% | **95.56%** | 0.6949 |
| Swin-B | **0.8680** | 0.9762 | **67.48%** | 97.81% | **63.70%** | 91.11% | **0.7716** |
| Video Swin-B | 0.8676 | **0.9763** | 66.46% | 98.31% | 62.16% | 93.33% | 0.7616 |

### Interpretation

1. **Under matched training, SwinFusion++ transfers better than Swin-B in most directions and is never significantly worse than either encoder.**
   - **Against Swin-B:** significantly better in seven of nine directions (+0.049 to +0.258 AUC; p_Holm 0.004–0.018).
   - **Against Video Swin-B:** significantly better in three (Celeb-DF → C40 +0.075, Celeb-DF → DeeperForensics +0.063, DeeperForensics → C40 +0.084; all p_Holm = 0.004).
   - **Never significantly worse:** none of its six negative point estimates is significant; the largest is −0.016 against Video Swin-B on C23 → DeeperForensics.
   - **Best and average performance:** it has the highest AUC of the three in five directions and the highest mean transfer AUC (0.810 vs 0.785 for Video Swin-B and 0.700 for Swin-B; descriptive).
2. **The advantage depends on the training source.**
   - **Trained on Celeb-DF or DeeperForensics:** SwinFusion++ is significantly better than Swin-B in all six directions and better than Video Swin-B in three of them.
   - **Trained on the standard FF++ C23 condition:** the three models are statistically tied on C40 (0.976 vs 0.974–0.975) and Celeb-DF (0.862 vs 0.868), where the Celeb-DF test set has no recorded identity overlap with FF++ training data.
   - **C23 → DeeperForensics:** Swin-B collapses (0.568), while both models with a temporal stream hold up (SwinFusion++ 0.826, Video Swin-B 0.842). Temporal evidence appears to be what transfers in this direction.
3. **Accuracy, precision, recall and F1 collapse under transfer for every model.** Accuracy is 50–70% in most directions, and recall is near zero when FF++- or Celeb-DF-trained models are applied to DeeperForensics.
   - **This is a threshold-transfer effect, not a ranking failure.** ROC-AUC remains informative, but the source-validation threshold no longer sits at the target score distribution.
   - **C23 → Celeb-DF is an example:** SwinFusion++'s retained threshold is the most conservative. It has the highest precision and specificity (6 false alarms out of 135 real videos), but the lowest recall (53.6%) and accuracy (59.4%).
   - **Recalibrating on the target** would require target labels and was deliberately not done.

---

## 3. Configured-system comparison: BO-selected SwinFusion++ vs the fixed-recipe baselines

This comparison has unequal optimization effort. It measures configured-system performance and is not, by itself, evidence for the architecture (manuscript, Chapter 3).

**In-distribution (RQ1_configured_system, m = 8):**

| Test set | SwinFusion++ (BO-selected) AUC [95% CI] / Acc / F1 | Δ vs Swin-B, p_Holm | Δ vs Video Swin-B, p_Holm |
|---|---|---|---|
| FF++ C23 | 0.9964 [0.9886, 1.0000] / 98.21% / 0.9822 | −0.0001, 1.00 | +0.0014, 1.00 |
| FF++ C40 | 0.9941 [0.9875, 0.9989] / 96.07% / 0.9617 | +0.0058, 0.18 | +0.0026, 1.00 |
| Celeb-DF v2 | 0.9983 [0.9963, 1.0000] / 98.36% / 0.9904 | +0.0024, 0.50 | +0.0024, 1.00 |
| DeeperForensics | 0.9954 [0.9874, 1.0000] / 98.51% / 0.9848 | −0.0012, 1.00 | +0.0008, 1.00 |

**Frozen transfer (RQ6_configured_system, m = 18):**
- **Against Swin-B:** the BO-selected configuration is significantly better in six directions: C23 → C40, C23 → DeeperForensics, Celeb-DF → DeeperForensics, DeeperForensics → C23, DeeperForensics → C40 and DeeperForensics → Celeb-DF (p_Holm 0.004–0.022).
- **Against Video Swin-B:**
  - It is significantly better on C23 → C40 (0.9862 vs 0.9746, +0.0116, p_Holm = 0.015).
  - It is significantly worse on C23 → DeeperForensics (0.7316 vs 0.8421, −0.1105, p_Holm = 0.004) and Celeb-DF → C23 (0.8657 vs 0.9047, −0.0390, p_Holm = 0.005).
- **C23 → Celeb-DF:** its AUC of 0.8785 [0.8253, 0.9256] is the highest of all models, but not significantly (p_Holm = 1.00). With the pre-declared flip TTA it is 0.8847.

## 4. Optimization effect: BO-selected minus fixed-recipe SwinFusion++

| Condition | Δ AUC [95% CI] | p_Holm | Family |
|---|---|---|---|
| Within FF++ C23 | +0.0022 [+0.0001, +0.0058] | 0.15 | RQ1_optimization_effect (m = 4) |
| Within FF++ C40 | **+0.0063 [+0.0018, +0.0118]** | **0.002** | RQ1_optimization_effect |
| Within Celeb-DF v2 | **+0.0031 [+0.0005, +0.0060]** | **0.021** | RQ1_optimization_effect |
| Within DeeperForensics | −0.0021 [−0.0051, +0.0000] | 0.15 | RQ1_optimization_effect |
| C23 → C40 | **+0.0102 [+0.0043, +0.0182]** | **0.002** | RQ6_optimization_effect (m = 9) |
| C23 → Celeb-DF | +0.0161 [+0.0018, +0.0301] | 0.11 | RQ6_optimization_effect |
| C23 → DeeperForensics | **−0.0946 [−0.1218, −0.0662]** | **0.002** | RQ6_optimization_effect |
| Celeb-DF → C23 | −0.0302 [−0.0589, −0.0042] | 0.066 | RQ6_optimization_effect |
| Celeb-DF → C40 | **−0.1039 [−0.1416, −0.0662]** | **0.002** | RQ6_optimization_effect |
| Celeb-DF → DeeperForensics | **−0.0409 [−0.0649, −0.0170]** | **0.005** | RQ6_optimization_effect |
| DeeperForensics → C23 | **−0.0891 [−0.1239, −0.0526]** | **0.002** | RQ6_optimization_effect |
| DeeperForensics → C40 | **−0.0601 [−0.0868, −0.0313]** | **0.002** | RQ6_optimization_effect |
| DeeperForensics → Celeb-DF | −0.0360 [−0.0780, +0.0025] | 0.11 | RQ6_optimization_effect |

**Interpretation.** Dataset-specific Bayesian optimization fits the source domain more tightly.
- **Gains:** it significantly raised in-distribution AUC on C40 and Celeb-DF and improved compression transfer (C23 → C40).
- **Losses:** it significantly lowered five other transfer directions, by 0.04–0.10 AUC.

The BO objective was source-validation AUC, so this trade-off is expected. It explains why the BO-selected configuration's transfer losses to Video Swin-B do not appear under the matched recipe.

*Sensitivity note.* Within Celeb-DF, the optimization effect is significant when the four within-dataset BO-vs-fixed tests form their own family (p_Holm = 0.021). It is not significant when they are pooled with the eight fixed-recipe-vs-baseline tests, as in the 2026-10-04 grouping (p_Holm = 0.077). No other conclusion depends on the grouping.

---

## 5. Answer to RQ1

**In-distribution, under the principal fixed-recipe comparison, SwinFusion++ does not measurably improve detection over standalone Swin-B or Video Swin-B.** All three reach ROC-AUC 0.988–0.997 on the four datasets and no difference is significant (all p_Holm = 1.00). Accuracy, precision, recall and F1 differ by a few videos, which is consistent with a performance ceiling.

**Under frozen cross-dataset evaluation, SwinFusion++ improves on the standalone encoders.**
- **Against Swin-B:** significantly better in seven of nine transfer directions.
- **Against Video Swin-B:** significantly better in three.
- **Never significantly worse** than either encoder.
- **Highest mean transfer ROC-AUC** (0.810, vs 0.785 for Video Swin-B and 0.700 for Swin-B).

The gain comes mainly from training on Celeb-DF and DeeperForensics. From FF++ C23 to C40 and to Celeb-DF, the three models are tied. Threshold-dependent metrics degrade for all models under transfer because source thresholds are retained.

**The BO-selected configuration (configured system) shows the cost of tuning for the source domain.**
- **Gains:** it reaches the highest in-distribution ROC-AUC on C40 (0.9941) and Celeb-DF (0.9983), and the best compression transfer (0.9862, significantly above both encoders).
- **Losses:** it gives up transfer from the other sources and is significantly worse than Video Swin-B on two directions.

**Comparison with the preliminary study.** In the earlier pipeline, SwinFusion++ did not exceed its constituent encoders: C40 AUC 0.985 vs 0.993, Celeb-DF 0.972 vs 0.982, and C23 → Celeb-DF 0.873 vs 0.905.
- **Within datasets and from FF++ C23, the pattern persists under the matched recipe** (C40 0.988 vs 0.992; Celeb-DF 0.995 vs 0.996; C23 → Celeb-DF 0.862 vs 0.868). However, the gaps are now small and not significant.
- **What is new is the transfer from Celeb-DF and DeeperForensics sources,** which the preliminary study did not evaluate.
- **The two studies use different test populations** (`table5_preliminary_within.*` in `../../RQ1/results/`), so this is a change in pattern, not a paired before/after estimate.

**Limitations to state.**
- **Unequal optimization:** only SwinFusion++ was Bayesian-optimized. The BO studies used 12 trials for C23 and C40 and 8 for Celeb-DF and DeeperForensics, below the 12–20 the manuscript declared.
- **Shared source lineage:** FF++ and DeeperForensics test rows share source lineage with other conditions' training/validation rows (disclosed in the evaluation protocol). The Celeb-DF test set has zero recorded overlap.
- **Limited power at the ceiling:** FF++ test sets contain 280 videos in 70 dependency clusters.
- **Only three seeds per model.**
