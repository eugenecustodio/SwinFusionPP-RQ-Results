| Condition | Comparison | ΔAUC [95% CI] | p (unadjusted) | p_Holm | Holm family |
|---|---|---|---|---|---|
| FF++ C23 (HQ) | SwinFusion++ (BO-selected) − Swin-B | −0.0001 [−0.0027, +0.0017] | 0.945 | 1.000 | RQ1_configured_system (m=8) |
| FF++ C23 (HQ) | SwinFusion++ (BO-selected) − Video Swin-B | +0.0014 [+0.0000, +0.0037] | 0.189 | 1.000 | RQ1_configured_system (m=8) |
| FF++ C40 (LQ) | SwinFusion++ (BO-selected) − Swin-B | +0.0058 [+0.0010, +0.0124] | 0.022 | 0.178 | RQ1_configured_system (m=8) |
| FF++ C40 (LQ) | SwinFusion++ (BO-selected) − Video Swin-B | +0.0026 [−0.0026, +0.0090] | 0.485 | 1.000 | RQ1_configured_system (m=8) |
| Celeb-DF v2 | SwinFusion++ (BO-selected) − Swin-B | +0.0024 [+0.0002, +0.0057] | 0.071 | 0.500 | RQ1_configured_system (m=8) |
| Celeb-DF v2 | SwinFusion++ (BO-selected) − Video Swin-B | +0.0024 [+0.0001, +0.0058] | 0.204 | 1.000 | RQ1_configured_system (m=8) |
| DeeperForensics-1.0 | SwinFusion++ (BO-selected) − Swin-B | −0.0012 [−0.0041, +0.0007] | 0.531 | 1.000 | RQ1_configured_system (m=8) |
| DeeperForensics-1.0 | SwinFusion++ (BO-selected) − Video Swin-B | +0.0008 [−0.0030, +0.0050] | 0.774 | 1.000 | RQ1_configured_system (m=8) |
| FF++ C23 (HQ) | SwinFusion++ (BO-selected) − SwinFusion++ (fixed recipe) | +0.0022 [+0.0001, +0.0058] | 0.074 | 0.148 | RQ1_optimization_effect (m=4) |
| FF++ C40 (LQ) | SwinFusion++ (BO-selected) − SwinFusion++ (fixed recipe) | +0.0063 [+0.0018, +0.0118] | <0.001 | **0.002** ✔ | RQ1_optimization_effect (m=4) |
| Celeb-DF v2 | SwinFusion++ (BO-selected) − SwinFusion++ (fixed recipe) | +0.0031 [+0.0005, +0.0060] | 0.007 | **0.021** ✔ | RQ1_optimization_effect (m=4) |
| DeeperForensics-1.0 | SwinFusion++ (BO-selected) − SwinFusion++ (fixed recipe) | −0.0021 [−0.0051, +0.0000] | 0.115 | 0.148 | RQ1_optimization_effect (m=4) |

Configured-system family (BO-selected vs fixed-recipe baselines) and optimization-effect family (BO-selected vs fixed-recipe SwinFusion++), within-dataset. p-values: rank-based cluster permutation test (5,000 permutations), Holm-adjusted within the named family. ✔ / ✘ = first model significantly better / worse (p_Holm < 0.05).
