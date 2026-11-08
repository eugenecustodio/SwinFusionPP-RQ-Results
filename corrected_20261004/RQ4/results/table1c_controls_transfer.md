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
