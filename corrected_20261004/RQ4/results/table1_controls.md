### Recipe-matched ablation: SwinFusion++ and both controls on the same fixed recipe. Topology control: same stages, non-attentive exchange; capacity control: matched parameters, no exchange

*p-values corrected 2026-10-04: rank-based cluster permutation test (within-model ranks swapped per cluster), Holm within family. The original raw-logit test is in the original file.*

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0019 | -0.0060 | 1.02e-04 | 0.2350 | 0.4699 | 280 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -3.06e-04 | -0.0019 | 8.67e-04 | 0.8446 | 0.8446 | 280 |
