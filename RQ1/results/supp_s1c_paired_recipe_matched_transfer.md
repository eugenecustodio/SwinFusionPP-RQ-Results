### Paired, transfer (RQ6_secondary, Holm)

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.1220 | 0.0933 | 0.1544 | 2.00e-04 | 0.0054 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.0490 | 0.0200 | 0.0770 | 0.0342 | 0.4787 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.0614 | 0.0339 | 0.0918 | 0.0018 | 0.0288 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.1286 | 0.0626 | 0.1864 | 0.3157 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.2012 | 0.1569 | 0.2492 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.1705 | 0.1290 | 0.2164 | 2.00e-04 | 0.0054 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0056 | -0.0282 | 0.0201 | 0.8628 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.2584 | 0.2133 | 0.3046 | 2.00e-04 | 0.0054 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | 0.0021 | -0.0068 | 0.0103 | 0.8286 | 1.0000 | 280 |
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0630 | 0.0302 | 0.0991 | 2.00e-04 | 0.0054 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0089 | -0.0320 | 0.0154 | 0.4503 | 1.0000 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0754 | 0.0354 | 0.1164 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0122 | -0.0917 | 0.0487 | 0.8956 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0451 | 0.0077 | 0.0816 | 0.0558 | 0.7253 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0840 | 0.0439 | 0.1229 | 2.00e-04 | 0.0054 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0052 | -0.0304 | 0.0175 | 0.8768 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0159 | -0.0407 | 0.0090 | 0.3451 | 1.0000 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | 0.0014 | -0.0089 | 0.0102 | 0.9476 | 1.0000 | 280 |
| Celeb-DF v2 | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0409 | -0.0649 | -0.0170 | 0.0220 | 0.3299 | 402 |
| Celeb-DF v2 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0302 | -0.0589 | -0.0042 | 0.0678 | 0.8134 | 280 |
| Celeb-DF v2 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.1039 | -0.1416 | -0.0662 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0360 | -0.0780 | 0.0025 | 0.7117 | 1.0000 | 978 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0891 | -0.1239 | -0.0526 | 2.00e-04 | 0.0054 | 280 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0601 | -0.0868 | -0.0313 | 6.00e-04 | 0.0102 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0161 | 0.0018 | 0.0301 | 0.3135 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0946 | -0.1218 | -0.0662 | 2.00e-04 | 0.0054 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | 0.0102 | 0.0043 | 0.0182 | 0.2833 | 1.0000 | 280 |
