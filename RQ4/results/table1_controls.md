### Recipe-matched ablation: SwinFusion++ and both controls on the same fixed recipe. Topology control: same stages, non-attentive exchange; capacity control: matched parameters, no exchange

| training | test | comparison | delta_auc | ci_low | ci_high | permutation_p | holm_p | videos |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0019 | -0.0060 | 1.02e-04 | 0.0150 | 0.0300 | 280 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -3.06e-04 | -0.0019 | 8.67e-04 | 0.7109 | 0.7109 | 280 |
