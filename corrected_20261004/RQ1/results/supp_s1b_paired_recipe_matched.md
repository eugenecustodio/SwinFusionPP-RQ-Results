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
