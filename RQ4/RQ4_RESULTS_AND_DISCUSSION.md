# RQ4 — Results and Discussion

**RQ4.** Does the hierarchical cross-attention between Swin and Video Swin improve detection performance compared to other spatio-temporal models such as CAST and TSFF-Net?

**Evidence used (state in the text).** Three layers: (i) **matched controls** — SwinFusion++ (fixed recipe) vs a *topology control* (same stages, alignment and joint readout, exchange block removed) and a *capacity control* (same parameter count ±5%, per-stream layers with no cross-stream attention), all trained on FF++ C23 with the identical fixed recipe, three seeds each, evaluated on the C23 test set and under frozen transfer to C40, Celeb-DF and DeeperForensics; (ii) **Tier B ablations** — four one-change variants of the Bayesian-optimised SwinFusion++ (one-directional attention, no gates, no |S−V|/S⊙V agreement features, exchange only in stages 3–4), single exploratory seed, C23 test set, paired against the full model with the same seed; (iii) **published CAST and TSFF-Net** results as context, plus the preliminary study's frozen-feature fusion-head experiment. Paired effects are ΔAUC with 95% cluster-bootstrap intervals and cluster permutation tests, Holm-corrected within each family. Files: `results/table1_controls.*`, `table1b_controls_metrics.*`, `table1c_controls_transfer.*`, `table1d_controls_transfer_metrics.*`, `table2_tier_b.*`, `table2b_tier_b_metrics.*`, `table2c_preliminary_fusion_heads.*`, `table3_cast_tsff_published.*`, `fig1_controls_forest.png`, `fig1b_controls_transfer_forest.png`, `fig2_tier_b_forest.png`.

---

## 1. Matched controls (fixed recipe, FF++ C23 training)

**Within FF++ C23 (280 test videos, three-seed ensembles)**

| Model | ROC-AUC [95% CI] | Accuracy | F1 |
|---|---|---|---|
| SwinFusion++ (fixed recipe, full cross-attention) | 0.9942 [0.9834, 0.9999] | 97.86% | 0.9784 |
| Capacity control (same size, no exchange) | 0.9945 [0.9848, 0.9999] | **98.57%** | **0.9856** |
| Topology control (no exchange block) | **0.9962** [0.9888, 1.0000] | 98.21% | 0.9821 |

Paired (SwinFusion++ − control, RQ4_controls family): vs capacity −0.0003 [−0.0019, +0.0009], p_Holm = 0.71; vs topology −0.0019 [−0.0060, +0.0001], p_Holm = 0.03 (interval touches zero; permutation and bootstrap disagree, so not treated as established).

**Frozen transfer from C23 (RQ4_controls_transfer family)**

| Target | SwinFusion++ (fixed) | Capacity control | Topology control | Δ vs capacity | Δ vs topology |
|---|---|---|---|---|---|
| FF++ C40 | 0.9760 | 0.9763 | 0.9780 | −0.0003, p_Holm = 1.00 | −0.0020, p_Holm = 1.00 |
| Celeb-DF v2 | 0.8624 | 0.8627 | 0.8577 | −0.0003, p_Holm = 1.00 | +0.0046, p_Holm = 1.00 |
| DeeperForensics | 0.8261 | 0.7846 | 0.8481 | **+0.0416 [+0.0227, +0.0612], p_Holm = 0.004** | −0.0219 [−0.0380, −0.0064], p_Holm = 0.07 |

## 2. Tier B ablations (Bayesian-optimised SwinFusion++, FF++ C23 test, single seed)

| Variant | ROC-AUC | Accuracy | F1 | ΔAUC vs full [95% CI] | p_Holm |
|---|---|---|---|---|---|
| Full SwinFusion++ (same seed) | 0.9970 | 98.57% | 0.9857 | — | — |
| One-directional attention (S ← V only) | 0.9965 | 98.57% | 0.9858 | −0.0006 [−0.0020, +0.0001] | 1.00 |
| No gates (all gates = 1) | 0.9977 | 97.86% | 0.9787 | +0.0007 [−0.0005, +0.0031] | 1.00 |
| No agreement features (no |S−V|, S⊙V) | 0.9970 | 98.93% | 0.9892 | −0.0001 [−0.0012, +0.0015] | 1.00 |
| Exchange in stages 3–4 only | 0.9964 | 97.14% | 0.9720 | −0.0007 [−0.0022, +0.0001] | 1.00 |

## 3. Published CAST / TSFF-Net and the preliminary fusion-head experiment

| Model | Setting | ROC-AUC |
|---|---|---|
| CAST (Thakre et al.; B0/B5 variants) | FF++ C23 within (several configurations) | 0.58–1.00 (main configuration ≈ 0.95–1.00; multiscale variant lower) |
| CAST-B0 / CAST-B5 | FF++ C23 → Celeb-DF | 0.770 / 0.749 |
| TSFF-Net (Zhang et al. 2024) | FF++ C23 → Celeb-DF | 0.771 (Tier B) |
| **SwinFusion++ (ours)** | FF++ C23 within / C23 → Celeb-DF | **0.996 / 0.879** |
| Preliminary study, frozen C23 features (single seed): full TLBG-HCA vs capacity-matched no-exchange head | C23 test | 0.9964 vs 0.9964 (identical); late concatenation 0.9952 |

---

## Interpretation

1. **Within FF++ C23, cross-attention gives no measurable advantage over matched controls.** The three fixed-recipe fusion variants differ by ≤ 0.002 AUC and by one to two videos in accuracy; the capacity control (identical parameter count, no cross-stream attention) is statistically indistinguishable from the full model (Δ = −0.0003, p_Holm = 0.71), and the topology control is nominally slightly better. This replicates the preliminary study's frozen-feature finding (full = no-exchange = 0.9964) under end-to-end training with three seeds. C23 is at the performance ceiling, so the test has limited sensitivity: the result is "no detectable difference", not equivalence.
2. **Under transfer, cross-attention shows one significant benefit.** Generalising from C23 to DeeperForensics, the full model outperforms the same-size capacity control by +0.042 AUC (p_Holm = 0.004) — the strictest comparison, because only the exchange mechanism differs. This indicates that cross-stream attention can contribute transferable evidence on motion-altering manipulations. However, the topology control (no exchange block at all) is nominally better still on that direction (−0.022, not significant), and on C40 and Celeb-DF all three are tied. The mechanism-specific evidence is therefore mixed: positive against matched capacity, not against the simplest joint readout.
3. **No single component of the optimised SwinFusion++ is shown to be essential on C23.** All four Tier B ablations lie within ±0.0007 AUC of the full model (all p_Holm = 1.00); removing the agreement features or the gates did not reduce ranking performance, and restricting exchange to stages 3–4 cost 0.0007 AUC and 1.4 accuracy points. These are single-seed, ceiling-level results and are descriptive only.
4. **Relative to other spatio-temporal fusion models, SwinFusion++ compares favourably in generalisation.** On FF++ C23 → Celeb-DF, SwinFusion++ (0.879) exceeds the published CAST (0.75–0.77) and TSFF-Net (0.771) values by a wide margin; within FF++ C23 it (0.996) is at or above CAST's best configurations. CAST's own ablations report a benefit from CNN–Transformer cross-attention, whereas our Swin/Video-Swin controls mostly do not; the two studies test different representations and controls and need not agree. Published comparisons are context under their own protocols.
5. **What explains SwinFusion++'s performance, then?** The controls show that most of the system-level gain comes from (a) jointly reading both encoders' stage-wise features (including their difference and product) and (b) the dataset-specific optimisation (RQ1 supplementary: +0.0063 AUC on C40, p_Holm = 0.002). Cross-attention adds measurable value in one generalisation setting and is otherwise not separable from these factors.

## Answer to RQ4

Hierarchical cross-attention between Swin-B and Video Swin-B does **not** produce a measurable in-distribution improvement over matched topology or capacity controls on FF++ C23, and none of the four component ablations changes C23 performance detectably. It does yield one significant transfer advantage over the capacity-matched no-exchange control (C23 → DeeperForensics, +0.042 AUC), and the complete SwinFusion++ system generalises substantially better from FF++ to Celeb-DF than the published CAST and TSFF-Net cross-attention/fusion models. The defensible conclusion is that SwinFusion++'s advantage is a property of the dual-stream, jointly read, optimised system rather than demonstrably of cross-attention alone; the ceiling effect on C23 limits the sensitivity of the mechanism test.

**Limitations to state.** Controls were trained only on C23 and only under the fixed recipe (they were not Bayesian-optimised); Tier B ablations are single-seed; C23 within-dataset performance is at ceiling; CAST and TSFF-Net were not retrained under the common protocol. Future work: Bayesian-optimise the controls, train them on C40/Celeb-DF, test attention on harder data, and inspect learned gate values/attention maps to see whether the exchange paths are actually used.
