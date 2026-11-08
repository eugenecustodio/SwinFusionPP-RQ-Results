# RQ2 — Results and Discussion

> **Corrected 2026-10-04.** Paired-test p-values were re-computed with a rank-based cluster permutation test: each model's ensemble logits are converted to within-model ranks before the cluster-level swap. The original test swapped raw logits between models whose logit scales differ, which made its p-values unreliable. ΔAUC values, bootstrap intervals and all metrics are unchanged. Corrected statistics: `00_Shared/statistics_raw/paired_cluster_effects_rank_corrected.csv`. This file also corrects published values: TALL-Swin's row previously showed Xception's numbers as reported in the TALL paper; STIL's accuracies were misquoted (C23 99.6%, C40 98.2%); I3D, SFormer and FTCN C40 values were missing.

**RQ2.** What is the performance of SwinFusion++ relative to established baselines when evaluated on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0?

**Evidence used (state in the text).** Three sources, kept separate: (i) SwinFusion++'s own held-out test results (video-level, three-seed ensembles, frozen thresholds); (ii) the Xception baseline reproduced locally in the authors' preliminary study (same four datasets, seed 1701, earlier pipeline); (iii) published values for Xception, I3D, STIL, FTCN, TALL-Swin and SFormer, extracted from the original papers with a comparability tier (A = same dataset/compression, video-level, DeepFakes subset; B = same dataset but unit or subset differs/unstated; C = other data, context only). I3D and SFormer were blocked in the preliminary study (no verified local run), so they appear as published values only. No statistical test is made against published numbers; they come from different splits, frame sampling, face crops and evaluation units. Files: `results/table1_ours.*`, `table1b_preliminary_baselines.*`, `table2_published_AB.*`, `table3_published_C.*`, `fig1_vs_published.png`.

---

## 1. SwinFusion++ (ours, held-out test)

| Dataset | ROC-AUC [95% CI] | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|---|
| FF++ DeepFakes C23 (HQ) | 0.9964 [0.9886, 1.0000] | 98.21% | 97.87% | 98.57% | 0.9822 |
| FF++ DeepFakes C40 (LQ) | 0.9941 [0.9875, 0.9989] | 96.07% | 93.88% | 98.57% | 0.9617 |
| Celeb-DF v2 | 0.9983 [0.9963, 1.0000] | 98.36% | 99.76% | 98.34% | 0.9904 |
| DeeperForensics-1.0 (binary construction) | 0.9954 [0.9874, 1.0000] | 98.51% | 100.00% | 97.01% | 0.9848 |

## 2. Locally reproduced baseline (preliminary study, same four datasets)

| Dataset | Xception ROC-AUC | Xception Acc | Xception F1 | SwinFusion++ (now) ROC-AUC |
|---|---|---|---|---|
| FF++ C23 | 0.7725 | 69.64% | 0.6886 | **0.9964** |
| FF++ C40 | 0.8109 | 74.29% | 0.7429 | **0.9941** |
| Celeb-DF v2 | 0.6480 | 84.17%* | 0.9140* | **0.9983** |
| DeeperForensics-1.0 | 0.9978 | 46.00% | 0.5821 | 0.9954 |

\*Xception predicted "fake" for every Celeb-DF video (balanced accuracy 0.50); its accuracy/F1 reflect the 84% fake prevalence, not discrimination. On DeeperForensics it ranked well (AUC 0.998) but its threshold produced 1,288 false negatives (accuracy 46%).

## 3. Published values (Tier A/B, within-dataset, video-level unless noted)

| Model | FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics |
|---|---|---|---|---|
| **SwinFusion++ (ours)** | **AUC 0.996 / Acc 98.2%** | **AUC 0.994 / Acc 96.1%** | **AUC 0.998 / Acc 98.4%** | **AUC 0.995 / Acc 98.5%** |
| Xception (published) | Acc 98.9–100% (XN-avg) | Acc 96.8–97.1% (XN-avg) | Acc 99.4% | Acc 77–100% (DFo benchmark, varies by setting) |
| I3D (published) | Acc 92.9% | Acc 91.1% | Acc 99.2% | Acc 79–100% |
| STIL (published) | Acc 99.6% (DF) | Acc 98.2% / AUC 0.971 (Tier B) | Acc 99.8% | — |
| FTCN (published) | AUC 0.981–0.999; Acc 97.9–99.1% (Tier B) | AUC 0.983 (Tier B) | — | AUC 1.000 (within) |
| TALL-Swin (published) | Acc 98.7% / AUC 0.999 (Tier B) | Acc 92.8% / AUC 0.946 (Tier B) | — | — |
| SFormer (published) | Acc 84–99.9% (several settings) | Acc 59–98.2% (several settings) | Acc 95–99.1% | Acc 99.7–100% |

Full rows with citations, locations, units and subsets are in `table2_published_AB.csv`; Tier C rows (DFDC, Celeb-DF v1 counts, own data) are in `table3_published_C.csv`.

---

## Interpretation

1. **Against the locally reproduced Xception, SwinFusion++ is far stronger on FF++ and Celeb-DF** (ROC-AUC 0.996 / 0.994 / 0.998 vs 0.77 / 0.81 / 0.65). On DeeperForensics both rank near-perfectly (0.995 vs 0.998), but Xception's retained threshold failed (46% accuracy) while SwinFusion++ delivered 98.5% accuracy with no false positives. These are the only cross-family numbers obtained under a shared face-processing pipeline; they differ in pretraining, training budget and capacity, so they support "SwinFusion++ exceeds this reproduced Xception", not an architecture-only claim.
2. **Against published results, SwinFusion++ is competitive with, but in accuracy slightly below, the strongest reported within-dataset values.** In ROC-AUC its C40 value (0.994) is above every published C40 AUC in the record (FTCN 0.983, STIL 0.971, Xception 0.955, TALL-Swin 0.946), and its C23 value (0.996) lies within the published range (FTCN 0.981–0.999; TALL-Swin 0.999, Tier B). In accuracy it sits one to two points below the best published values: C23 98.2% vs 98.7–100% (TALL-Swin, Xception XN-avg, STIL, SFormer); C40 96.1% vs 98.2% (STIL, SFormer) and 96.8–97.1% (Xception XN-avg), though above TALL-Swin (92.8%) and I3D (91.1%); Celeb-DF 98.4% vs 99.1–99.8% (SFormer, I3D, Xception, STIL). These margins are small relative to the protocol differences described next.
3. **Why these comparisons are context, not a leaderboard.** Published numbers were obtained on different test splits (often the official FF++ split with all 140 test videos per manipulation, sometimes all four manipulations pooled), with different face crops, frame counts and sometimes frame-level rather than video-level scoring. Accuracy also depends on the operating point, which published papers rarely freeze in advance. SwinFusion++'s numbers come from a pre-registered-style protocol (sealed inference, thresholds frozen on validation, identity-cluster-aware intervals). The appropriate claim is "close to the best published results under a stricter protocol", not "better than model X".
4. **DeeperForensics requires care.** Within-dataset scores are near ceiling for every method (published I3D/Xception reach 100% in some DFo settings; SwinFusion++ 0.995 AUC / 98.5% accuracy). The retained DeeperForensics binary construction is the authors' audited subset, not the official benchmark protocol, so published DFo values are Tier A only in dataset identity.

## Answer to RQ2

On the FF++ DeepFakes HQ/LQ subsets, Celeb-DF v2 and the DeeperForensics-1.0 construction, SwinFusion++ reaches ROC-AUC 0.994–0.998 and accuracy 96.1–98.5%, substantially above the locally reproduced Xception baseline on FF++ and Celeb-DF, and close to the best published results for I3D, STIL, FTCN, TALL-Swin and SFormer under their own protocols: the highest C40 ROC-AUC in the record, but one to two accuracy points below the best published values on C23, C40 and Celeb-DF. The clearest advantage over established CNN baselines appears on compressed (C40) and high-quality face-swap (Celeb-DF) content; on DeeperForensics all strong methods are near ceiling. Published comparisons are descriptive context under non-matched protocols.

**Limitations to state.** Only one cross-family baseline (Xception) and one recurrent baseline (RQ3) were reproduced locally, both in the earlier preliminary pipeline; I3D and SFormer have no verified local numbers; published values are not protocol-matched and no inference is drawn from them.
