# RQ1 — writing package (v020)

> To what extent does SwinFusion++ improve video-level deepfake detection performance compared with standalone Swin Transformer and standalone Video Swin Transformer under in-distribution and cross-dataset evaluation, in terms of Accuracy, Precision, Recall, F1-Score, and ROC-AUC?

**Status:** Results complete.

## Table 1 — SwinFusion++ vs standalone Swin-B and Video Swin-B (within-dataset)

### Three-seed mean-logit ensembles; SwinFusion++ = BO-selected training parameters, baselines = shared fixed recipe

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.9965 | 0.9906 | 0.9999 | 0.9786 | 0.9718 | 0.9857 | 0.9787 | 0.9973 | 0.9965 | 6.71e-04 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.9964 | 0.9886 | 1.0000 | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9975 | 0.9966 | 6.44e-04 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.9951 | 0.9856 | 1.0000 | 0.9893 | 0.9928 | 0.9857 | 0.9892 | 0.9967 | 0.9952 | 8.68e-04 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.9883 | 0.9777 | 0.9960 | 0.9464 | 0.9562 | 0.9357 | 0.9458 | 0.9895 | 0.9875 | 0.0013 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9941 | 0.9875 | 0.9989 | 0.9607 | 0.9388 | 0.9857 | 0.9617 | 0.9945 | 0.9923 | 0.0017 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.9915 | 0.9818 | 0.9983 | 0.9571 | 0.9571 | 0.9571 | 0.9571 | 0.9933 | 0.9910 | 0.0022 |
| Celeb-DF v2 | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.9958 | 0.9925 | 0.9990 | 0.9540 | 0.9963 | 0.9502 | 0.9727 | 0.9993 | 0.9956 | 2.28e-04 |
| Celeb-DF v2 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.9983 | 0.9963 | 1.0000 | 0.9836 | 0.9976 | 0.9834 | 0.9904 | 0.9997 | 0.9974 | 8.49e-04 |
| Celeb-DF v2 | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.9958 | 0.9915 | 0.9994 | 0.9826 | 0.9928 | 0.9870 | 0.9899 | 0.9993 | 0.9954 | 2.75e-04 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.9966 | 0.9892 | 1.0000 | 0.9776 | 1.0000 | 0.9552 | 0.9771 | 0.9978 | 0.9968 | 8.53e-04 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.9954 | 0.9874 | 1.0000 | 0.9851 | 1.0000 | 0.9701 | 0.9848 | 0.9968 | 0.9952 | 0.0016 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.9945 | 0.9842 | 0.9999 | 0.9701 | 0.9948 | 0.9453 | 0.9694 | 0.9966 | 0.9944 | 6.34e-04 |

## Table 2 — Paired tests, SwinFusion++ vs baselines (RQ1 family, Holm)

### ΔAUC = SwinFusion++ − baseline

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0024 | 1.52e-04 | 0.0057 | 0.0714 | 0.4997 | 978 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -0.0012 | -0.0041 | 6.69e-04 | 0.5307 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -1.02e-04 | -0.0027 | 0.0017 | 0.9450 | 1.0000 | 280 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0058 | 9.69e-04 | 0.0124 | 0.0222 | 0.1776 | 280 |
| Celeb-DF v2 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0024 | 1.43e-04 | 0.0058 | 0.2038 | 1.0000 | 978 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 8.42e-04 | -0.0030 | 0.0050 | 0.7736 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0014 | 0.0000 | 0.0037 | 0.1886 | 1.0000 | 280 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0026 | -0.0026 | 0.0090 | 0.4847 | 1.0000 | 280 |

## Table 3 — Cross-dataset (directional transfer)

### Source thresholds unchanged; full target tests with v020 lineage-overlap disclosure

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.9739 | 0.9572 | 0.9885 | 0.9179 | 0.9606 | 0.8714 | 0.9139 | 0.9793 | 0.9713 | 0.0059 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9862 | 0.9739 | 0.9959 | 0.9357 | 0.9766 | 0.8929 | 0.9328 | 0.9882 | 0.9850 | 0.0012 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.9746 | 0.9570 | 0.9893 | 0.9179 | 0.9756 | 0.8571 | 0.9125 | 0.9786 | 0.9741 | 0.0025 |
| FF++ C23 (HQ) | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.8680 | 0.8086 | 0.9184 | 0.6748 | 0.9781 | 0.6370 | 0.7716 | 0.9762 | 0.8618 | 0.0131 |
| FF++ C23 (HQ) | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.8785 | 0.8253 | 0.9256 | 0.6738 | 0.9695 | 0.6418 | 0.7723 | 0.9783 | 0.8702 | 0.0039 |
| FF++ C23 (HQ) | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.8676 | 0.8251 | 0.9108 | 0.6646 | 0.9831 | 0.6216 | 0.7616 | 0.9763 | 0.8660 | 0.0026 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.5678 | 0.5250 | 0.6105 | 0.5274 | 0.9231 | 0.0597 | 0.1121 | 0.6282 | 0.5686 | 0.0182 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.7316 | 0.7015 | 0.7638 | 0.5199 | 0.9000 | 0.0448 | 0.0853 | 0.7458 | 0.6968 | 0.0534 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.8421 | 0.8092 | 0.8740 | 0.5796 | 0.9706 | 0.1642 | 0.2809 | 0.8542 | 0.8379 | 0.0245 |
| Celeb-DF v2 | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.8468 | 0.8129 | 0.8814 | 0.6036 | 1.0000 | 0.2071 | 0.3432 | 0.8684 | 0.8444 | 0.0108 |
| Celeb-DF v2 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.8657 | 0.8283 | 0.9038 | 0.6357 | 1.0000 | 0.2714 | 0.4270 | 0.8950 | 0.8663 | 0.0108 |
| Celeb-DF v2 | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.9047 | 0.8739 | 0.9340 | 0.7071 | 0.9833 | 0.4214 | 0.5900 | 0.9194 | 0.8996 | 0.0178 |
| Celeb-DF v2 | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.7770 | 0.7430 | 0.8102 | 0.5214 | 1.0000 | 0.0429 | 0.0822 | 0.7879 | 0.7747 | 0.0054 |
| Celeb-DF v2 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7345 | 0.6961 | 0.7741 | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.7836 | 0.7282 | 0.0227 |
| Celeb-DF v2 | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.7630 | 0.7201 | 0.8035 | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.8024 | 0.7515 | 0.0526 |
| Celeb-DF v2 | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.6012 | 0.5624 | 0.6408 | 0.5100 | 1.0000 | 0.0199 | 0.0390 | 0.6671 | 0.5971 | 0.0176 |
| Celeb-DF v2 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.6824 | 0.6488 | 0.7178 | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.7257 | 0.6727 | 0.0146 |
| Celeb-DF v2 | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.6603 | 0.6130 | 0.7048 | 0.5348 | 1.0000 | 0.0697 | 0.1302 | 0.7051 | 0.6503 | 0.0142 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.6115 | 0.5774 | 0.6466 | 0.5000 | — | 0.0000 | — | 0.6287 | 0.5970 | 0.0437 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.7236 | 0.6918 | 0.7579 | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.7138 | 0.6681 | 0.0503 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.7676 | 0.7358 | 0.8021 | 0.5107 | 0.8000 | 0.0286 | 0.0552 | 0.7756 | 0.7560 | 0.0244 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.5964 | 0.5592 | 0.6330 | 0.5000 | — | 0.0000 | — | 0.6191 | 0.5840 | 0.0389 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7067 | 0.6758 | 0.7410 | 0.5000 | — | 0.0000 | — | 0.6937 | 0.6599 | 0.0337 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.6829 | 0.6430 | 0.7265 | 0.5071 | 1.0000 | 0.0143 | 0.0282 | 0.6995 | 0.6751 | 0.0235 |
| DeeperForensics-1.0 | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.4593 | 0.3970 | 0.5259 | 0.1380 | — | 0.0000 | — | 0.8414 | 0.4545 | 0.0305 |
| DeeperForensics-1.0 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.5519 | 0.4954 | 0.6128 | 0.1380 | — | 0.0000 | — | 0.8749 | 0.5533 | 0.0104 |
| DeeperForensics-1.0 | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.6001 | 0.5354 | 0.6750 | 0.1524 | 0.9375 | 0.0178 | 0.0349 | 0.9018 | 0.5948 | 0.0158 |

### Paired transfer tests (RQ6 family, Holm)

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0811 | 0.0511 | 0.1130 | 2.00e-04 | 0.0036 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0189 | -0.0140 | 0.0499 | 0.2284 | 1.0000 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -0.0425 | -0.0806 | -0.0026 | 0.0246 | 0.1968 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0926 | 0.0263 | 0.1477 | 0.0022 | 0.0220 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.1121 | 0.0724 | 0.1563 | 2.00e-04 | 0.0036 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.1103 | 0.0750 | 0.1501 | 2.00e-04 | 0.0036 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0105 | -0.0090 | 0.0315 | 0.2677 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.1638 | 0.1220 | 0.2096 | 2.00e-04 | 0.0036 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0123 | 0.0048 | 0.0211 | 8.00e-04 | 0.0096 | 280 |
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0221 | -0.0104 | 0.0573 | 0.1894 | 1.0000 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0390 | -0.0617 | -0.0179 | 4.00e-04 | 0.0052 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0285 | -0.0606 | 0.0070 | 0.1068 | 0.7475 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0482 | -0.1277 | 0.0138 | 0.1682 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0439 | -0.0770 | -0.0106 | 0.0160 | 0.1440 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0239 | -0.0127 | 0.0609 | 0.1932 | 1.0000 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0109 | -0.0086 | 0.0298 | 0.3655 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.1105 | -0.1374 | -0.0820 | 2.00e-04 | 0.0036 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0116 | 0.0040 | 0.0214 | 0.0014 | 0.0154 | 280 |

## Table 4 — Pre-declared flip-TTA variant of SwinFusion++ (descriptive)

### Labelled variant (A-13); the main results and tests use the plain variant

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.9965 | 0.9889 | 1.0000 | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9975 | 0.9965 | 7.22e-04 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9855 | 0.9722 | 0.9957 | 0.9321 | 0.9690 | 0.8929 | 0.9294 | 0.9874 | 0.9844 | 0.0018 |
| FF++ C23 (HQ) | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.8847 | 0.8275 | 0.9356 | 0.6677 | 0.9796 | 0.6275 | 0.7650 | 0.9792 | 0.8779 | 0.0058 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.7338 | 0.7040 | 0.7672 | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.7425 | 0.7007 | 0.0566 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9937 | 0.9865 | 0.9988 | 0.9607 | 0.9388 | 0.9857 | 0.9617 | 0.9942 | 0.9915 | 0.0020 |
| Celeb-DF v2 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.8665 | 0.8287 | 0.9039 | 0.6250 | 1.0000 | 0.2500 | 0.4000 | 0.8947 | 0.8670 | 0.0116 |
| Celeb-DF v2 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7360 | 0.6980 | 0.7754 | 0.5250 | 1.0000 | 0.0500 | 0.0952 | 0.7862 | 0.7321 | 0.0237 |
| Celeb-DF v2 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.9983 | 0.9966 | 0.9999 | 0.9796 | 0.9976 | 0.9786 | 0.9880 | 0.9997 | 0.9977 | 8.41e-04 |
| Celeb-DF v2 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.6827 | 0.6487 | 0.7188 | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.7270 | 0.6736 | 0.0136 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.7268 | 0.6963 | 0.7607 | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.7160 | 0.6712 | 0.0513 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7085 | 0.6776 | 0.7431 | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.6977 | 0.6618 | 0.0349 |
| DeeperForensics-1.0 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.5537 | 0.4951 | 0.6180 | 0.1380 | — | 0.0000 | — | 0.8750 | 0.5520 | 0.0171 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.9956 | 0.9881 | 1.0000 | 0.9876 | 1.0000 | 0.9751 | 0.9874 | 0.9969 | 0.9954 | 0.0016 |

## Supplementary S1 — Recipe-matched comparison (all models on the shared fixed recipe)

### Architecture-only check: identical training recipe for every model

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.9965 | 0.9906 | 0.9999 | 0.9786 | 0.9718 | 0.9857 | 0.9787 | 0.9973 | 0.9965 | 6.71e-04 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | SwinFusion++ | fixed_no_bo | 0.9942 | 0.9834 | 0.9999 | 0.9786 | 0.9855 | 0.9714 | 0.9784 | 0.9963 | 0.9939 | 8.57e-04 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.9951 | 0.9856 | 1.0000 | 0.9893 | 0.9928 | 0.9857 | 0.9892 | 0.9967 | 0.9952 | 8.68e-04 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.9883 | 0.9777 | 0.9960 | 0.9464 | 0.9562 | 0.9357 | 0.9458 | 0.9895 | 0.9875 | 0.0013 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | SwinFusion++ | fixed_no_bo | 0.9878 | 0.9772 | 0.9965 | 0.9464 | 0.9371 | 0.9571 | 0.9470 | 0.9896 | 0.9860 | 0.0017 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.9915 | 0.9818 | 0.9983 | 0.9571 | 0.9571 | 0.9571 | 0.9571 | 0.9933 | 0.9910 | 0.0022 |
| Celeb-DF v2 | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.9958 | 0.9925 | 0.9990 | 0.9540 | 0.9963 | 0.9502 | 0.9727 | 0.9993 | 0.9956 | 2.28e-04 |
| Celeb-DF v2 | Celeb-DF v2 | SwinFusion++ | fixed_no_bo | 0.9951 | 0.9905 | 0.9995 | 0.9775 | 0.9928 | 0.9810 | 0.9869 | 0.9992 | 0.9939 | 0.0022 |
| Celeb-DF v2 | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.9958 | 0.9915 | 0.9994 | 0.9826 | 0.9928 | 0.9870 | 0.9899 | 0.9993 | 0.9954 | 2.75e-04 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.9966 | 0.9892 | 1.0000 | 0.9776 | 1.0000 | 0.9552 | 0.9771 | 0.9978 | 0.9968 | 8.53e-04 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | SwinFusion++ | fixed_no_bo | 0.9974 | 0.9921 | 1.0000 | 0.9876 | 1.0000 | 0.9751 | 0.9874 | 0.9980 | 0.9971 | 0.0011 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.9945 | 0.9842 | 0.9999 | 0.9701 | 0.9948 | 0.9453 | 0.9694 | 0.9966 | 0.9944 | 6.34e-04 |

### Paired, within (RQ1_secondary, Holm)

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -7.21e-04 | -0.0048 | 0.0026 | 0.9252 | 1.0000 | 978 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 8.66e-04 | -6.93e-04 | 0.0036 | 0.6525 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0023 | -0.0079 | 8.67e-04 | 0.4607 | 1.0000 | 280 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -4.59e-04 | -0.0076 | 0.0061 | 0.9068 | 1.0000 | 280 |
| Celeb-DF v2 | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -6.90e-04 | -0.0033 | 0.0012 | 0.7740 | 1.0000 | 978 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0029 | -5.45e-04 | 0.0085 | 0.2987 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -8.16e-04 | -0.0031 | 2.04e-04 | 0.2539 | 1.0000 | 280 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0037 | -0.0101 | 0.0013 | 0.1976 | 1.0000 | 280 |
| Celeb-DF v2 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0031 | 4.98e-04 | 0.0060 | 0.0070 | 0.0770 | 978 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0021 | -0.0051 | 0.0000 | 0.1152 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0022 | 5.10e-05 | 0.0058 | 0.0742 | 0.7419 | 280 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0063 | 0.0018 | 0.0118 | 6.00e-04 | 0.0072 | 280 |

### Paired, transfer (RQ6_secondary, Holm)

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.1220 | 0.0933 | 0.1544 | 2.00e-04 | 0.0054 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.0490 | 0.0200 | 0.0770 | 0.0020 | 0.0240 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.0614 | 0.0339 | 0.0918 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.1286 | 0.0626 | 0.1864 | 2.00e-04 | 0.0054 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.2012 | 0.1569 | 0.2492 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.1705 | 0.1290 | 0.2164 | 2.00e-04 | 0.0054 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0056 | -0.0282 | 0.0201 | 0.6927 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.2584 | 0.2133 | 0.3046 | 2.00e-04 | 0.0054 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.0021 | -0.0068 | 0.0103 | 0.6313 | 1.0000 | 280 |
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0630 | 0.0302 | 0.0991 | 4.00e-04 | 0.0060 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0089 | -0.0320 | 0.0154 | 0.4661 | 1.0000 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0754 | 0.0354 | 0.1164 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0122 | -0.0917 | 0.0487 | 0.7932 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0451 | 0.0077 | 0.0816 | 0.0190 | 0.2090 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0840 | 0.0439 | 0.1229 | 2.00e-04 | 0.0054 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0052 | -0.0304 | 0.0175 | 0.6875 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0159 | -0.0407 | 0.0090 | 0.2136 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0014 | -0.0089 | 0.0102 | 0.8006 | 1.0000 | 280 |
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0409 | -0.0649 | -0.0170 | 0.0012 | 0.0156 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0302 | -0.0589 | -0.0042 | 0.0220 | 0.2200 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.1039 | -0.1416 | -0.0662 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0360 | -0.0780 | 0.0025 | 0.0934 | 0.7471 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0891 | -0.1239 | -0.0526 | 4.00e-04 | 0.0060 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0601 | -0.0868 | -0.0313 | 2.00e-04 | 0.0054 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0161 | 0.0018 | 0.0301 | 0.0544 | 0.4895 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0946 | -0.1218 | -0.0662 | 2.00e-04 | 0.0054 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0102 | 0.0043 | 0.0182 | 2.00e-04 | 0.0054 | 280 |

## Table 5 — Preliminary study (earlier pipeline): within-dataset ensembles

### Values as fractions; shows the change from the earlier pipeline

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison.

| model | train_condition | test_condition | roc_auc | roc_auc_ci_low | roc_auc_ci_high | f1 | accuracy | location |
|---|---|---|---|---|---|---|---|---|
| Swin-B (preliminary) | Celeb-DF v2 | Celeb-DF v2 | 0.9824 | 0.9785 | 0.9835 | 0.9433 | 0.9092 | Table 4 |
| Swin-B (preliminary) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9989 | 0.9974 | 0.9999 | 0.9940 | 0.9891 | Table 4 |
| Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9930 | 0.9824 | 1.0000 | 0.9856 | 0.9857 | Table 4 |
| Swin-B (preliminary) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.9917 | 0.9817 | 0.9987 | 0.9712 | 0.9714 | Table 4 |
| SwinFusion++ (preliminary) | Celeb-DF v2 | Celeb-DF v2 | 0.9724 | 0.9680 | 0.9746 | 0.9561 | 0.9278 | Table 4 |
| SwinFusion++ (preliminary) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9990 | 0.9970 | 1.0000 | 0.9844 | 0.9719 | Table 4 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9965 | 0.9921 | 0.9994 | 0.9712 | 0.9714 | Table 4 |
| SwinFusion++ (preliminary) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.9854 | 0.9727 | 0.9952 | 0.9420 | 0.9429 | Table 4 |
| Video Swin-B (preliminary) | Celeb-DF v2 | Celeb-DF v2 | 0.9749 | 0.9710 | 0.9770 | 0.9414 | 0.9057 | Table 4 |
| Video Swin-B (preliminary) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9989 | 0.9970 | 0.9999 | 0.9861 | 0.9748 | Table 4 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9972 | 0.9923 | 0.9999 | 0.9784 | 0.9786 | Table 4 |
| Video Swin-B (preliminary) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.9930 | 0.9864 | 0.9979 | 0.9577 | 0.9571 | Table 4 |

## Table 6 — Published standalone Swin-B results (context)

### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | model | train_condition | test_condition | metric_std | value | level | location | source |
|---|---|---|---|---|---|---|---|---|
| A | Swin-B (baseline, context only) | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8313 | video | Table 1 (PDF p.5) | Xu et al. 2023 |

## Caveats

- SwinFusion++ training parameters were selected by Bayesian optimisation on source validation; the baselines use the shared fixed recipe (disclose this). Supplementary S1 gives the recipe-matched comparison.
- Transfer uses source operating points unchanged; overlap-free subsets are secondary (see results/metrics_v020).
- Three seeds per configuration; uncertainty is cluster-bootstrap over dependency clusters, not over seeds.
