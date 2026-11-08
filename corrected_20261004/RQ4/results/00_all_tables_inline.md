# RQ4 — writing package (v020)

> Does the hierarchical cross-attention between Swin and Video Swin improve detection performance compared to other spatio-temporal models such as CAST and TSFF-Net?

**Status:** Results complete.

## Table 1 — Hierarchical cross-attention vs matched controls (FF++ C23, 3 seeds, Holm)

### Recipe-matched ablation: SwinFusion++ and both controls on the same fixed recipe. Topology control: same stages, non-attentive exchange; capacity control: matched parameters, no exchange

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0019 | -0.0060 | 1.02e-04 | 0.2350 | 0.4699 | 280 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -3.06e-04 | -0.0019 | 8.67e-04 | 0.8446 | 0.8446 | 280 |

## Table 1c — Controls under frozen C23 → other-dataset transfer

### C23-trained SwinFusion++ (fixed) vs C23-trained controls on C40 / Celeb-DF / DeeperForensics test sets; source thresholds unchanged (A-18)

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | 0.0046 | -0.0072 | 0.0159 | 0.4387 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0219 | -0.0380 | -0.0064 | 0.0056 | 0.0280 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0020 | -0.0062 | 0.0016 | 0.2617 | 1.0000 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -2.99e-04 | -0.0113 | 0.0131 | 0.9656 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | 0.0416 | 0.0227 | 0.0612 | 4.00e-04 | 0.0024 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -3.32e-04 | -0.0047 | 0.0036 | 0.8706 | 1.0000 | 280 |

### Transfer metrics, C23-trained models

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C40 (LQ) | Capacity control | fixed_no_bo | 0.9763 | 0.9575 | 0.9906 | 0.9036 | 0.9593 | 0.8429 | 0.8973 | 0.9797 | 0.9739 | 0.0020 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | SwinFusion++ | fixed_no_bo | 0.9760 | 0.9575 | 0.9910 | 0.8857 | 0.9737 | 0.7929 | 0.8740 | 0.9796 | 0.9733 | 0.0017 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | Topology control | fixed_no_bo | 0.9780 | 0.9607 | 0.9916 | 0.9071 | 0.9597 | 0.8500 | 0.9015 | 0.9811 | 0.9755 | 0.0016 |
| FF++ C23 (HQ) | Celeb-DF v2 | Capacity control | fixed_no_bo | 0.8627 | 0.8012 | 0.9149 | 0.5920 | 0.9805 | 0.5374 | 0.6943 | 0.9748 | 0.8569 | 0.0154 |
| FF++ C23 (HQ) | Celeb-DF v2 | SwinFusion++ | fixed_no_bo | 0.8624 | 0.8052 | 0.9149 | 0.5941 | 0.9869 | 0.5362 | 0.6949 | 0.9752 | 0.8553 | 0.0076 |
| FF++ C23 (HQ) | Celeb-DF v2 | Topology control | fixed_no_bo | 0.8577 | 0.7977 | 0.9116 | 0.6370 | 0.9784 | 0.5919 | 0.7376 | 0.9738 | 0.8489 | 0.0139 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Capacity control | fixed_no_bo | 0.7846 | 0.7468 | 0.8212 | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.8042 | 0.7529 | 0.0603 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | SwinFusion++ | fixed_no_bo | 0.8261 | 0.7926 | 0.8603 | 0.5149 | 0.8750 | 0.0348 | 0.0670 | 0.8255 | 0.7973 | 0.0539 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Topology control | fixed_no_bo | 0.8481 | 0.8138 | 0.8813 | 0.5398 | 0.9444 | 0.0846 | 0.1553 | 0.8528 | 0.8200 | 0.0467 |

## Table 2 — Tier B component ablations (exploratory, single seed)

### ΔAUC = variant − full SwinFusion++ (same seed 260901, BO C23 parameters)

| comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p |
|---|---|---|---|---|---|
| tierb_one_directional vs full | -5.87e-04 | -0.0020 | 1.02e-04 | 1.0000 | 1.0000 |
| tierb_no_gate vs full | 6.63e-04 | -5.10e-04 | 0.0031 | 0.5159 | 1.0000 |
| tierb_no_agreement vs full | -7.65e-05 | -0.0012 | 0.0015 | 1.0000 | 1.0000 |
| tierb_stages_34_only vs full | -6.89e-04 | -0.0022 | 1.02e-04 | 1.0000 | 1.0000 |

### Tier B metrics

| variant | roc_auc | accuracy | precision | recall | f1 |
|---|---|---|---|---|---|
| full | 0.9970 | 0.9857 | 0.9857 | 0.9857 | 0.9857 |
| one_directional | 0.9965 | 0.9857 | 0.9789 | 0.9929 | 0.9858 |
| no_gate | 0.9977 | 0.9786 | 0.9718 | 0.9857 | 0.9787 |
| no_agreement | 0.9970 | 0.9893 | 0.9928 | 0.9857 | 0.9892 |
| stages_34_only | 0.9964 | 0.9714 | 0.9521 | 0.9929 | 0.9720 |

## Table 2c — Preliminary study: frozen-feature fusion heads (C23, single seed)

### Earlier pipeline; fixed encoders, 4-epoch heads

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison.

| model | train_condition | test_condition | roc_auc | f1 | accuracy | location |
|---|---|---|---|---|---|---|
| Full TLBG-HCA head (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9964 | 0.9857 | 0.9857 | Table 8 |
| Late concatenation head (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9952 | 0.9892 | 0.9893 | Table 8 |
| No-exchange head (capacity-matched) (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9964 | 0.9857 | 0.9857 | Table 8 |

## Table 3 — CAST and TSFF-Net published results

### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | family | model | train_condition | test_condition | metric_std | value | level | subset | location | primary_or_secondary | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | CAST | CAST-B0 | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7698 | video | unstated_or_other | arXiv v2 Table 4 (PDF p.32) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7492 | video | unstated_or_other | arXiv v2 Table 4 (PDF p.32) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 1.0000 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8629 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.6015 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9202 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8465 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9433 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5997 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9527 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9704 | video | deepfakes | arXiv v2 Table 5 (PDF p.35) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9995 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8243 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5988 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8641 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8216 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8864 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5813 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9560 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7710 | unstated | unstated_or_other | Table 5 (PDF p.12) | primary | Zhang et al. 2024 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | accuracy | 0.9689 | video | unstated_or_other | arXiv v2 Table 3 (PDF p.31) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | accuracy | 0.9757 | video | unstated_or_other | arXiv v2 Table 3 (PDF p.31) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9968 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5842 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8274 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8379 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8339 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9929 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5111 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7344 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7442 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5133 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9782 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7971 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9898 | video | unstated_or_other | arXiv v2 Table 3 (PDF p.31) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8750 | video | unstated_or_other | arXiv v2 Table 5 (PDF p.35) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8450 | video | unstated_or_other | arXiv v2 Table 5 (PDF p.35) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9861 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.6569 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7019 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8078 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7471 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9999 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5361 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7161 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7773 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.6217 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9797 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8336 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9949 | video | unstated_or_other | arXiv v2 Table 3 (PDF p.31) | primary | Thakre et al. 2026 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | ffpp_c23 | accuracy | 0.9770 | unstated | deepfakes | Table 3 (PDF p.11) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | ffpp_c23 | accuracy | 0.9100 | unstated | unstated_or_other | Table 3 (PDF p.11) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | ffpp_c23 | accuracy | 0.9890 | unstated | unstated_or_other | Table 3 (PDF p.11) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | ffpp_c23 | accuracy | 0.9000 | unstated | unstated_or_other | Table 3 (PDF p.11) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c40 | ffpp_c40 | accuracy | 0.8510 | unstated | deepfakes | Table 4 (PDF p.12) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c40 | ffpp_c40 | accuracy | 0.8310 | unstated | unstated_or_other | Table 4 (PDF p.12) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c40 | ffpp_c40 | accuracy | 0.7850 | unstated | unstated_or_other | Table 4 (PDF p.12) | primary | Zhang et al. 2024 |
| B | TSFF-Net | TSFF-Net | ffpp_c40 | ffpp_c40 | accuracy | 0.6600 | unstated | unstated_or_other | Table 4 (PDF p.12) | primary | Zhang et al. 2024 |

## Caveats

- Controls are matched internal comparisons (3 seeds); Tier B is exploratory single-seed evidence.
- CAST/TSFF-Net are published values under their own protocols (no retraining).
