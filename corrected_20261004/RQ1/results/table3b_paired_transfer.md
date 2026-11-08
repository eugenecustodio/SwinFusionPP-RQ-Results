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
