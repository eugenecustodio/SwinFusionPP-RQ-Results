| Condition | Comparison | ΔAUC [95% CI] | p (unadjusted) | p_Holm | Holm family |
|---|---|---|---|---|---|
| C23 → C40 | SwinFusion++ (fixed recipe) − Swin-B | +0.0021 [−0.0068, +0.0103] | 0.631 | 1.000 | RQ6_architecture (m=18) |
| C23 → C40 | SwinFusion++ (fixed recipe) − Video Swin-B | +0.0014 [−0.0089, +0.0102] | 0.801 | 1.000 | RQ6_architecture (m=18) |
| C23 → Celeb-DF | SwinFusion++ (fixed recipe) − Swin-B | −0.0056 [−0.0282, +0.0201] | 0.693 | 1.000 | RQ6_architecture (m=18) |
| C23 → Celeb-DF | SwinFusion++ (fixed recipe) − Video Swin-B | −0.0052 [−0.0304, +0.0175] | 0.687 | 1.000 | RQ6_architecture (m=18) |
| C23 → DFo | SwinFusion++ (fixed recipe) − Swin-B | +0.2584 [+0.2133, +0.3046] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| C23 → DFo | SwinFusion++ (fixed recipe) − Video Swin-B | −0.0159 [−0.0407, +0.0090] | 0.214 | 1.000 | RQ6_architecture (m=18) |
| Celeb-DF → C23 | SwinFusion++ (fixed recipe) − Swin-B | +0.0490 [+0.0200, +0.0770] | 0.002 | **0.018** ✔ | RQ6_architecture (m=18) |
| Celeb-DF → C23 | SwinFusion++ (fixed recipe) − Video Swin-B | −0.0089 [−0.0320, +0.0154] | 0.466 | 1.000 | RQ6_architecture (m=18) |
| Celeb-DF → C40 | SwinFusion++ (fixed recipe) − Swin-B | +0.0614 [+0.0339, +0.0918] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| Celeb-DF → C40 | SwinFusion++ (fixed recipe) − Video Swin-B | +0.0754 [+0.0354, +0.1164] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| Celeb-DF → DFo | SwinFusion++ (fixed recipe) − Swin-B | +0.1220 [+0.0933, +0.1544] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| Celeb-DF → DFo | SwinFusion++ (fixed recipe) − Video Swin-B | +0.0630 [+0.0302, +0.0991] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| DFo → C23 | SwinFusion++ (fixed recipe) − Swin-B | +0.2012 [+0.1569, +0.2492] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| DFo → C23 | SwinFusion++ (fixed recipe) − Video Swin-B | +0.0451 [+0.0077, +0.0816] | 0.019 | 0.152 | RQ6_architecture (m=18) |
| DFo → C40 | SwinFusion++ (fixed recipe) − Swin-B | +0.1705 [+0.1290, +0.2164] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| DFo → C40 | SwinFusion++ (fixed recipe) − Video Swin-B | +0.0840 [+0.0439, +0.1229] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| DFo → Celeb-DF | SwinFusion++ (fixed recipe) − Swin-B | +0.1286 [+0.0626, +0.1864] | <0.001 | **0.004** ✔ | RQ6_architecture (m=18) |
| DFo → Celeb-DF | SwinFusion++ (fixed recipe) − Video Swin-B | −0.0122 [−0.0917, +0.0487] | 0.793 | 1.000 | RQ6_architecture (m=18) |

Principal transfer family (fixed recipe vs fixed recipe). p-values: rank-based cluster permutation test (5,000 permutations), Holm-adjusted within the named family. ✔ / ✘ = first model significantly better / worse (p_Holm < 0.05).
