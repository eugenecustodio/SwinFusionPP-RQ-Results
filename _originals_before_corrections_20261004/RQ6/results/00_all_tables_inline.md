# RQ6 — writing package (v020)

> Does SwinFusion++ improve deepfake detection performance compared to existing CNN- and transformer-based spatio-temporal models, both within datasets and across diverse datasets?

**Status:** Results complete.

## Table 1 — Within-dataset synthesis (SwinFusion++ vs baselines)

### Plain variant

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

## Table 2 — Directional transfer (SwinFusion++ vs baselines)

### Cross-dataset, plain variant

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

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0811 | 0.0511 | 0.1130 | 2.00e-04 | 0.0036 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0189 | -0.0140 | 0.0499 | 0.3591 | 1.0000 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -0.0425 | -0.0806 | -0.0026 | 0.0118 | 0.1534 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0926 | 0.0263 | 0.1477 | 0.4989 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.1121 | 0.0724 | 0.1563 | 2.00e-04 | 0.0036 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.1103 | 0.0750 | 0.1501 | 2.00e-04 | 0.0036 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0105 | -0.0090 | 0.0315 | 0.7656 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.1638 | 0.1220 | 0.2096 | 2.00e-04 | 0.0036 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | 0.0123 | 0.0048 | 0.0211 | 0.3321 | 1.0000 | 280 |
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0221 | -0.0104 | 0.0573 | 0.2607 | 1.0000 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0390 | -0.0617 | -0.0179 | 0.0134 | 0.1608 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0285 | -0.0606 | 0.0070 | 0.2474 | 1.0000 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0482 | -0.1277 | 0.0138 | 0.3015 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0439 | -0.0770 | -0.0106 | 0.0476 | 0.5235 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0239 | -0.0127 | 0.0609 | 0.2807 | 1.0000 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0109 | -0.0086 | 0.0298 | 0.3703 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.1105 | -0.1374 | -0.0820 | 2.00e-04 | 0.0036 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | 0.0116 | 0.0040 | 0.0214 | 0.0586 | 0.5859 | 280 |

## Table 2c — Preliminary study: frozen C23-source transfer

### Earlier pipeline; DeeperForensics = full view

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison.

| model | train_condition | test_condition | roc_auc | roc_auc_ci_low | roc_auc_ci_high | f1 | accuracy | location |
|---|---|---|---|---|---|---|---|---|
| Swin-B (preliminary) | FF++ C23 (HQ) | Celeb-DF v2 | 0.9052 | 0.8958 | 0.9118 | 0.9315 | 0.8824 | Table 9 |
| Swin-B (preliminary) | FF++ C23 (HQ) | DeeperForensics-1.0 | 0.8002 | 0.7663 | 0.8350 | 0.3555 | 0.2809 | Table 9 |
| Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C40 (LQ) | 0.9719 | 0.9532 | 0.9878 | 0.8664 | 0.8821 | Table 9 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | Celeb-DF v2 | 0.8730 | 0.8549 | 0.8864 | 0.8821 | 0.8149 | Table 9 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | DeeperForensics-1.0 | 0.8021 | 0.7764 | 0.8317 | 0.2362 | 0.2055 | Table 9 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | FF++ C40 (LQ) | 0.9686 | 0.9522 | 0.9829 | 0.7686 | 0.8107 | Table 9 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | Celeb-DF v2 | 0.9045 | 0.8901 | 0.9138 | 0.9289 | 0.8824 | Table 9 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | DeeperForensics-1.0 | 0.7508 | 0.7175 | 0.7898 | 0.2110 | 0.1912 | Table 9 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C40 (LQ) | 0.9440 | 0.9190 | 0.9677 | 0.7182 | 0.7786 | Table 9 |

## Table 3 — Published cross-dataset results

### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | family | model | train_condition | test_condition | metric_std | value | level | subset | location | primary_or_secondary | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | CAST | CAST-B0 | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7698 | video | unstated_or_other | arXiv v2 Table 4 (PDF p.32) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7492 | video | unstated_or_other | arXiv v2 Table 4 (PDF p.32) | primary | Thakre et al. 2026 |
| A | FTCN | FTCN | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8690 | video | unstated_or_other | Table 3 (PDF p.6) | secondary (TALL paper; matches FTCN Table 4) | Xu et al. 2023 |
| A | FTCN | FTCN (+TT) | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8690 | video | not_applicable | Table 4 (PDF p.6) | primary | Zheng et al. 2021 |
| A | I3D | I3D (I3D-RGB*) | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7824 | video | not_applicable | Table 1 (PDF p.5) | original third-party run (TALL paper, own implementation) | Xu et al. 2023 |
| A | ISTVT | ISTVT | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8410 | video | all_four | TALL Table 3 (arXiv v3 PDF p.6) | secondary (reported in TALL, ICCV 2023) | Xu et al. 2023 |
| A | TALL-Swin | TALL-Swin | ffpp_c23 | celeb_df_v2 | roc_auc | 0.9079 | video | not_applicable | Table 1 and Table 3 (PDF p.5-6) | primary | Xu et al. 2023 |
| A | Xception | Xception | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7370 | video | unstated_or_other | Table 4 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| A | FTCN | FTCN (+TT) | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.9880 | video | not_applicable | Table 4 (PDF p.6) | primary | Zheng et al. 2021 |
| A | ISTVT | ISTVT | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.9860 | video | all_four | TALL Table 3 (arXiv v3 PDF p.6) | secondary (reported in TALL, ICCV 2023) | Xu et al. 2023 |
| A | TALL-Swin | TALL-Swin | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.9962 | video | not_applicable | Table 3 (PDF p.6) | primary | Xu et al. 2023 |
| A | Xception | Xception | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.8450 | video | unstated_or_other | Table 4 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| B | STIL | STIL | ffpp_c40 | celeb_df_v2 | roc_auc | 0.7558 | unstated | not_applicable | Table 3 (PDF p.6) | primary | Gu et al. 2021 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7710 | unstated | unstated_or_other | Table 5 (PDF p.12) | primary | Zhang et al. 2024 |
| B | Xception | Xception | ffpp_c23 | celeb_df_v2 | roc_auc | 0.6530 | frame | not_applicable | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c40 | celeb_df_v2 | roc_auc | 0.6550 | frame | not_applicable | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception-c40 | ffpp_c40 | celeb_df_v2 | roc_auc | 0.6550 | unstated | unstated_or_other | Table 3 (PDF p.6) | secondary (STIL paper, copied) | Gu et al. 2021 |

## Table 4 — Published within-dataset ROC-AUC (CNN and transformer spatio-temporal families)

### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | family | model | train_condition | test_condition | metric_std | value | level | subset | location | primary_or_secondary | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | FTCN | FTCN (+TT) | deeperforensics_1_0 | deeperforensics_1_0 | roc_auc | 1.0000 | video | unstated_or_other | Supplement Table 1 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
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
| A | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9990 | video | deepfakes | Table 2 (PDF p.6) | primary | Zheng et al. 2021 |
| A | FTCN | FTCN (+TT, L x1) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9810 | video | deepfakes | Table 8 (PDF p.8) | primary | Zheng et al. 2021 |
| A | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9390 | video | deepfakes | Table 2 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| B | Chen et al. 2022 | Chen et al. 2022 Xception + spatiotemporal attention + ConvLSTM (Xception-ConvLSTM/'Xception-LSTM') | celeb_df_v2 | celeb_df_v2 | roc_auc | 0.9991 | unstated | unstated_or_other | Hriez 2025 Table 6 (top-10 AUC, Celeb-DF; ref [157]), journal p.143972 (PDF p.16) | secondary (Hriez 2025 IEEE Access review) | Hriez et al. 2025 |
| B | I3D | I3D | celeb_df_v2 | celeb_df_v2 | roc_auc | 0.9759 | unstated | unstated_or_other | Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | secondary (Saikia et al. 2022 Table IV, copied from de Lima et al. 2020) | de Lima et al. 2020 |
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
| B | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9980 | video | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | TALL-Swin | TALL-Swin | ffpp_c23 | ffpp_c23 | roc_auc | 0.9987 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9970 | frame | deepfakes | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9630 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | FTCN | FTCN (+TT) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9830 | video | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | STIL | STIL | ffpp_c40 | ffpp_c40 | roc_auc | 0.9712 | unstated | deepfakes | Table 3 (PDF p.6) | primary | Gu et al. 2021 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9949 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9593 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9930 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9950 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9808 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9930 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9923 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9609 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9857 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9916 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9762 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9896 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9889 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9824 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9891 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9959 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9843 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9941 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | TALL-Swin | TALL-Swin | ffpp_c40 | ffpp_c40 | roc_auc | 0.9457 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | roc_auc | 0.9550 | frame | deepfakes | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | roc_auc | 0.8930 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | Xception | Xception-c40 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9550 | unstated | deepfakes | Table 3 (PDF p.6) | secondary (STIL paper, copied) | Gu et al. 2021 |

## Caveats

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.
