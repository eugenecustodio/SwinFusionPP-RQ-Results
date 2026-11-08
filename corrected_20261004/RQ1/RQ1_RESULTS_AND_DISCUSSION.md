# RQ1 — Results and Discussion

> **Corrected 2026-10-04.** Paired-test p-values were re-computed with a rank-based cluster permutation test: each model's ensemble logits are converted to within-model ranks before the cluster-level swap. The original test swapped raw logits between models whose logit scales differ, which made its p-values unreliable. ΔAUC values, bootstrap intervals and all metrics are unchanged. Corrected statistics: `00_Shared/statistics_raw/paired_cluster_effects_rank_corrected.csv`. Changed conclusions: the C23 → C40 advantage is now significant against both baselines; SwinFusion++ beats Swin-B in six transfer directions (was four); Video Swin-B is also significantly better on Celeb-DF → C23. Within-dataset results are unchanged (no significant differences).

**RQ1.** To what extent does SwinFusion++ improve video-level deepfake detection performance compared with standalone Swin Transformer and standalone Video Swin Transformer under in-distribution and cross-dataset evaluation, in terms of Accuracy, Precision, Recall, F1-Score, and ROC-AUC?

**Setup (state in the text).** SwinFusion++ = the Bayesian-optimised configuration (training parameters selected on source validation only). Swin-B and Video Swin-B use the shared fixed recipe. All numbers are video-level, held-out test sets, three-seed mean-logit ensembles, decision thresholds frozen on source validation before any test scoring. ROC-AUC intervals are 95% cluster-bootstrap intervals (5,000 draws over dependency clusters); paired tests are rank-based cluster permutation tests (within-model ranks swapped per cluster) with Holm correction within the RQ1 (within-dataset) and RQ6 (transfer) families. Files: `results/table1_within.*`, `table2_paired_within.*`, `table3_transfer.*`, `table3b_paired_transfer.*`, `table4_tta_variant.*`, `supp_s1_*`, `fig1_within_ci.png`, `fig2_transfer_*.png`.

---

## 1. In-distribution (within-dataset) results

| Test set | Model | ROC-AUC [95% CI] | Accuracy | Precision | Recall | F1 | Seed AUC mean ± SD |
|---|---|---|---|---|---|---|---|
| FF++ C23 | **SwinFusion++** | 0.9964 [0.9886, 1.0000] | 98.21% | 97.87% | 98.57% | 0.9822 | 0.9966 ± 0.0006 |
| FF++ C23 | Swin-B | **0.9965** [0.9906, 0.9999] | 97.86% | 97.18% | 98.57% | 0.9787 | 0.9965 ± 0.0007 |
| FF++ C23 | Video Swin-B | 0.9951 [0.9856, 1.0000] | **98.93%** | **99.28%** | 98.57% | **0.9892** | 0.9952 ± 0.0009 |
| FF++ C40 | **SwinFusion++** | **0.9941** [0.9875, 0.9989] | **96.07%** | 93.88% | **98.57%** | **0.9617** | 0.9923 ± 0.0017 |
| FF++ C40 | Swin-B | 0.9883 [0.9777, 0.9960] | 94.64% | 95.62% | 93.57% | 0.9458 | 0.9875 ± 0.0013 |
| FF++ C40 | Video Swin-B | 0.9915 [0.9818, 0.9983] | 95.71% | **95.71%** | 95.71% | 0.9571 | 0.9910 ± 0.0022 |
| Celeb-DF v2 | **SwinFusion++** | **0.9983** [0.9963, 1.0000] | **98.36%** | **99.76%** | 98.34% | **0.9904** | 0.9974 ± 0.0008 |
| Celeb-DF v2 | Swin-B | 0.9958 [0.9925, 0.9990] | 95.40% | 99.63% | 95.02% | 0.9727 | 0.9956 ± 0.0002 |
| Celeb-DF v2 | Video Swin-B | 0.9958 [0.9915, 0.9994] | 98.26% | 99.28% | **98.70%** | 0.9899 | 0.9954 ± 0.0003 |
| DeeperForensics | **SwinFusion++** | 0.9954 [0.9874, 1.0000] | **98.51%** | 100.00% | **97.01%** | **0.9848** | 0.9952 ± 0.0016 |
| DeeperForensics | Swin-B | **0.9966** [0.9892, 1.0000] | 97.76% | 100.00% | 95.52% | 0.9771 | 0.9968 ± 0.0009 |
| DeeperForensics | Video Swin-B | 0.9945 [0.9842, 0.9999] | 97.01% | 99.48% | 94.53% | 0.9694 | 0.9944 ± 0.0006 |

**Paired tests (RQ1 family, Holm-corrected)** — SwinFusion++ minus baseline, ΔROC-AUC:

| Dataset | vs Swin-B | vs Video Swin-B |
|---|---|---|
| FF++ C23 | −0.0001 [−0.0027, +0.0017], p_Holm = 1.00 | +0.0014 [+0.0000, +0.0037], p_Holm = 1.00 |
| FF++ C40 | +0.0058 [+0.0010, +0.0124], p_Holm = 0.18 | +0.0026 [−0.0026, +0.0090], p_Holm = 1.00 |
| Celeb-DF v2 | +0.0024 [+0.0002, +0.0057], p_Holm = 0.50 | +0.0024 [+0.0001, +0.0058], p_Holm = 1.00 |
| DeeperForensics | −0.0012 [−0.0041, +0.0007], p_Holm = 1.00 | +0.0008 [−0.0030, +0.0050], p_Holm = 1.00 |

### Interpretation

1. **SwinFusion++ obtains the highest ROC-AUC on the two harder conditions, FF++ C40 (0.9941) and Celeb-DF v2 (0.9983), and the highest accuracy and F1 on three of the four conditions (C40, Celeb-DF, DeeperForensics).** On Celeb-DF every individual SwinFusion++ seed (0.9965–0.9982) exceeded every baseline seed (≤ 0.9958), and the model is the most balanced: 98.3% of fakes detected with 98.5% of real videos passed, whereas Swin-B misses more fakes (recall 95.0%) and Video Swin-B rejects more real videos (specificity 95.6%).
2. **On FF++ C23 and DeeperForensics the three models are statistically indistinguishable.** All AUCs lie between 0.9945 and 0.9966 with overlapping intervals; on C23 Video Swin-B has the best accuracy (98.93%) by one or two videos out of 280. These conditions are near the performance ceiling, so small differences are within sampling noise.
3. **No within-dataset difference reaches significance after Holm correction** (smallest adjusted p = 0.18, C40 vs Swin-B), although the point estimates and some unadjusted bootstrap intervals favour SwinFusion++ on C40 and Celeb-DF (e.g. +0.0058 [+0.0010, +0.0124] vs Swin-B on C40). The honest statement is therefore: *SwinFusion++ is the best or statistically equivalent model within every dataset, with its clearest point-estimate advantages on compressed (C40) and high-quality face-swap (Celeb-DF) content.*
4. **Seed stability.** SwinFusion++'s seed-to-seed standard deviation (0.0006–0.0017) is comparable to the baselines'; its advantage on Celeb-DF is consistent across seeds rather than driven by one lucky run.

---

## 2. Cross-dataset (frozen transfer) results

Source weights, ensemble membership, calibration and thresholds are carried unchanged to the target dataset; no target labels are used for any decision. ROC-AUC (plain variant):

| Trained on → tested on | **SwinFusion++** | Swin-B | Video Swin-B | Best |
|---|---|---|---|---|
| FF++ C23 → FF++ C40 | **0.9862** [0.9739, 0.9959] | 0.9739 | 0.9746 | SwinFusion++ |
| FF++ C23 → Celeb-DF v2 | **0.8785** [0.8253, 0.9256] | 0.8680 | 0.8676 | SwinFusion++ |
| FF++ C23 → DeeperForensics | 0.7316 [0.7015, 0.7638] | 0.5678 | **0.8421** | Video Swin-B |
| Celeb-DF → FF++ C23 | 0.8657 | 0.8468 | **0.9047** | Video Swin-B |
| Celeb-DF → FF++ C40 | 0.7345 | **0.7770** | 0.7630 | Swin-B |
| Celeb-DF → DeeperForensics | **0.6824** | 0.6012 | 0.6603 | SwinFusion++ |
| DeeperForensics → FF++ C23 | 0.7236 | 0.6115 | **0.7676** | Video Swin-B |
| DeeperForensics → FF++ C40 | **0.7067** | 0.5964 | 0.6829 | SwinFusion++ |
| DeeperForensics → Celeb-DF | 0.5519 | 0.4593 | **0.6001** | Video Swin-B |

**Paired transfer tests (RQ6 family, Holm-corrected), SwinFusion++ minus baseline:**

| Direction | vs Swin-B | vs Video Swin-B |
|---|---|---|
| C23 → C40 | **+0.0123 [+0.0048, +0.0211], p_Holm = 0.010** | **+0.0116 [+0.0040, +0.0214], p_Holm = 0.015** |
| C23 → Celeb-DF | +0.0105 [−0.0090, +0.0315], p_Holm = 1.00 | +0.0109 [−0.0086, +0.0298], p_Holm = 1.00 |
| C23 → DeeperForensics | **+0.1638 [+0.1220, +0.2096], p_Holm = 0.004** | **−0.1105 [−0.1374, −0.0820], p_Holm = 0.004** |
| Celeb-DF → C23 | +0.0189 [−0.0140, +0.0499], p_Holm = 1.00 | **−0.0390 [−0.0617, −0.0179], p_Holm = 0.005** |
| Celeb-DF → C40 | −0.0425 [−0.0806, −0.0026], p_Holm = 0.20 | −0.0285 [−0.0606, +0.0070], p_Holm = 0.75 |
| Celeb-DF → DeeperForensics | **+0.0811 [+0.0511, +0.1130], p_Holm = 0.004** | +0.0221 [−0.0104, +0.0573], p_Holm = 1.00 |
| DeeperForensics → C23 | **+0.1121 [+0.0724, +0.1563], p_Holm = 0.004** | −0.0439 [−0.0770, −0.0106], p_Holm = 0.14 |
| DeeperForensics → C40 | **+0.1103 [+0.0750, +0.1501], p_Holm = 0.004** | +0.0239 [−0.0127, +0.0609], p_Holm = 1.00 |
| DeeperForensics → Celeb-DF | **+0.0926 [+0.0263, +0.1477], p_Holm = 0.022** | −0.0482 [−0.1277, +0.0138], p_Holm = 1.00 |

**FF++ C23 → Celeb-DF v2, full metrics (978 videos: 843 fake, 135 real):**

| Model | ROC-AUC | PR-AUC | Acc | Precision | Recall | Specificity | F1 |
|---|---|---|---|---|---|---|---|
| SwinFusion++ | **0.8785** | **0.9783** | 67.38% | 96.95% | **64.18%** | 87.41% | **0.7723** |
| Swin-B | 0.8680 | 0.9762 | **67.48%** | 97.81% | 63.70% | 91.11% | 0.7716 |
| Video Swin-B | 0.8676 | 0.9763 | 66.46% | **98.31%** | 62.16% | **93.33%** | 0.7616 |

The pre-declared horizontal-flip TTA variant of SwinFusion++ (reported descriptively, `table4_tta_variant.*`) reaches 0.8847 [0.8275, 0.9356] on this direction.

### Interpretation

1. **From the standard FF++ training condition, SwinFusion++ generalises best.** It has the highest AUC for compression shift (C23 → C40: 0.9862, +0.012 over both baselines, with accuracy 93.6% vs 91.8%) and for the cleanest cross-dataset test, C23 → Celeb-DF (0.8785 vs 0.868), where the Celeb-DF test set has no recorded identity overlap with FF++ training data. The compression-shift lead is significant against both baselines after Holm correction (p_Holm = 0.010 vs Swin-B, 0.015 vs Video Swin-B); the C23 → Celeb-DF lead is not (p_Holm = 1.00; the intervals overlap), so it is a best point estimate, not an established difference.
2. **Transfer is condition-dependent and SwinFusion++ is not uniformly superior.** It significantly outperforms Swin-B in six directions (C23 → C40, C23 → DeeperForensics, Celeb-DF → DeeperForensics, DeeperForensics → C23, DeeperForensics → C40, DeeperForensics → Celeb-DF; p_Holm 0.004–0.022) and Video Swin-B in one (C23 → C40), but is significantly *worse* than Video Swin-B on C23 → DeeperForensics (−0.11 AUC) and Celeb-DF → C23 (−0.039 AUC, p_Holm = 0.005), and Video Swin-B has the higher point estimate in four of the nine directions. Temporal evidence alone (Video Swin-B) transfers particularly well to and from DeeperForensics, whose manipulations alter motion more than texture.
3. **Accuracy, precision, recall and F1 collapse under transfer for every model** (accuracy 50–70% in most directions; recall near zero when FF++- or Celeb-DF-trained models are applied to DeeperForensics). This is a threshold-transfer effect, not a ranking failure: ROC-AUC remains informative while the source-validation threshold no longer sits at the target score distribution. On C23 → Celeb-DF, SwinFusion++ catches the most fakes (541/843) while flagging slightly more real videos (17/135) than the baselines. Recalibrating on the target domain would require target labels and was deliberately not done.
4. **The optimisation trades generalisation for in-distribution accuracy.** The supplementary recipe-matched analysis (`supp_s1_*`) shows that Bayesian optimisation significantly improved SwinFusion++ within C40 (+0.0063, p_Holm = 0.007) and on C23 → C40 (+0.0102, p_Holm = 0.005), but that the fixed-recipe SwinFusion++ transfers significantly better from Celeb-DF and DeeperForensics (e.g. DeeperForensics → C23: 0.8127 fixed vs 0.7236 optimised, p_Holm = 0.006) and to DeeperForensics from C23 and Celeb-DF. Dataset-specific optimisation fits the source domain more tightly.

---

## 3. Answer to RQ1

SwinFusion++ improves video-level detection over the standalone Swin-B and Video Swin-B *modestly and condition-dependently*. In-distribution it is the best or statistically equivalent model on every dataset, with the highest ROC-AUC on FF++ C40 (0.9941) and Celeb-DF v2 (0.9983) and the highest accuracy/F1 on three of four datasets, but no within-dataset difference survives multiplicity correction because all models operate near ceiling. Under frozen cross-dataset evaluation from FF++ it attains the best compression-shift generalisation (0.9862, significantly better than both baselines) and the best FF++ → Celeb-DF generalisation by point estimate (0.8785, not significant), and significantly outperforms Swin-B in six transfer directions, while Video Swin-B generalises significantly better from FF++ to DeeperForensics and from Celeb-DF to FF++ C23 and remains a strong, cheaper competitor. Threshold-dependent metrics degrade for all models under transfer.

**Comparison with the preliminary study.** In the earlier pipeline SwinFusion++ did not exceed its constituent encoders (C40 AUC 0.985 vs 0.993; Celeb-DF 0.972 vs 0.982; C23 → Celeb-DF 0.873 vs 0.905). With the revised face-processing cache, seven locked evaluation anchors, three-seed ensembles and dataset-specific optimisation, it now leads on both of those conditions and on FF++ → Celeb-DF. The two studies use different test populations, so this is a change in pattern rather than a paired before/after estimate (`table5_preliminary_within.*`).

**Limitations to state.** Only SwinFusion++ was Bayesian-optimised (baselines used the fixed recipe; recipe-matched results are supplementary); FF++ and DeeperForensics test rows share source lineage with other conditions' training/validation rows (disclosed in the evaluation protocol; Celeb-DF test has zero recorded overlap); FF++ test sets contain 280 videos in 70 dependency clusters, which limits statistical power at ceiling-level performance.
