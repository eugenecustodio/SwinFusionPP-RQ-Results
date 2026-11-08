### C23-trained SwinFusion++ (fixed) vs C23-trained controls on C40 / Celeb-DF / DeeperForensics test sets; source thresholds unchanged (A-18)

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | 0.0046 | -0.0072 | 0.0159 | 0.4691 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0219 | -0.0380 | -0.0064 | 0.0148 | 0.0740 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0020 | -0.0062 | 0.0016 | 0.2667 | 1.0000 | 280 |
| FF++ C23 (HQ) | Celeb-DF v2 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -2.99e-04 | -0.0113 | 0.0131 | 0.9804 | 1.0000 | 978 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | 0.0416 | 0.0227 | 0.0612 | 6.00e-04 | 0.0036 | 402 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -3.32e-04 | -0.0047 | 0.0036 | 0.8868 | 1.0000 | 280 |
