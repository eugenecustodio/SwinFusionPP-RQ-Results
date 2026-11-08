| Condition | Comparison | ΔAUC [95% CI] | p (unadjusted) | p_Holm | Holm family |
|---|---|---|---|---|---|
| C23 → C40 | SwinFusion++ (fixed recipe) − Capacity control | −0.0003 [−0.0047, +0.0036] | 0.871 | 1.000 | RQ4_controls_transfer (m=6) |
| C23 → C40 | SwinFusion++ (fixed recipe) − Topology control | −0.0020 [−0.0062, +0.0016] | 0.262 | 1.000 | RQ4_controls_transfer (m=6) |
| C23 → Celeb-DF | SwinFusion++ (fixed recipe) − Capacity control | −0.0003 [−0.0113, +0.0131] | 0.966 | 1.000 | RQ4_controls_transfer (m=6) |
| C23 → Celeb-DF | SwinFusion++ (fixed recipe) − Topology control | +0.0046 [−0.0072, +0.0159] | 0.439 | 1.000 | RQ4_controls_transfer (m=6) |
| C23 → DFo | SwinFusion++ (fixed recipe) − Capacity control | +0.0416 [+0.0227, +0.0612] | <0.001 | **0.002** ✔ | RQ4_controls_transfer (m=6) |
| C23 → DFo | SwinFusion++ (fixed recipe) − Topology control | −0.0219 [−0.0380, −0.0064] | 0.006 | **0.028** ✘ | RQ4_controls_transfer (m=6) |

RQ4 matched controls, frozen transfer from FF++ C23 (unchanged by Option A). p-values: rank-based cluster permutation test (5,000 permutations), Holm-adjusted within the named family. ✔ / ✘ = first model significantly better / worse (p_Holm < 0.05).
