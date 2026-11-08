# RQ3 — Results and Discussion

> **Option A framing (2026-10-28).** Following Chapter 3, comparisons with external models use the **BO-selected SwinFusion++ (configured system)**; fixed-recipe values (the RQ1 principal architecture evidence) are shown for reference. Also corrected:
> - Chen et al. 2022 is Tier C, because only secondary survey quotes are available.
> - Saikia et al.'s FF++ AUC range is 0.75–0.91; the 0.73 is a Celeb-DF value.
> - The comparison with early recurrent designs is narrowed to Saikia et al., because Güera & Delp report on different data.
> - Sabir et al.'s own ablation is summarized.

> **Corrected 2026-10-04.** Paired-test p-values were re-computed with a rank-based cluster permutation test: each model's ensemble logits are converted to within-model ranks before the cluster-level swap. The original test swapped raw logits between models whose logit scales differ, which made its p-values unreliable. ΔAUC values, bootstrap intervals and all metrics are unchanged. Corrected statistics: `00_Shared/statistics_raw/paired_cluster_effects_rank_corrected.csv`.

**RQ3.** How does the performance of SwinFusion++ compare to CNN-LSTM models on the FaceForensics++ (HQ/LQ) dataset?

**Evidence used (state in the text).** (i) SwinFusion++'s held-out FF++ C23 and C40 test results (video-level, three-seed ensembles, frozen thresholds). (ii) The representative CNN–LSTM (ImageNet ResNet-18 embeddings + one-layer LSTM, 256 hidden units) reproduced in the authors' preliminary study on the same FF++ DeepFakes conditions, including that study's protocol-eligible paired comparison on C40. (iii) Published CNN-LSTM-family results (Güera & Delp 2018; Sabir et al. 2019 recurrent-convolutional variants; Chen et al. 2022 Xception-ConvLSTM; Saikia et al. 2022) with comparability tiers. Files: `results/table1_ours.*`, `table1b_preliminary_baselines.*`, `table2_published_AB.*`, `table3_published_C.*`, `fig1_vs_published.png`.

---

## 1. SwinFusion++ vs the reproduced CNN–LSTM (FF++ DeepFakes)

| Condition | Model | ROC-AUC | Accuracy | F1 |
|---|---|---|---|---|
| FF++ C23 (HQ) | **SwinFusion++ (ours, BO-selected)** | **0.9964** | **98.21%** | **0.9822** |
| FF++ C23 (HQ) | SwinFusion++ (ours, fixed recipe) | 0.9942 | 97.86% | 0.9784 |
| FF++ C23 (HQ) | CNN–LSTM (preliminary, seed 1701) | 0.7876 | 71.43% | 0.7452 |
| FF++ C40 (LQ) | **SwinFusion++ (ours, BO-selected)** | **0.9941** | **96.07%** | **0.9617** |
| FF++ C40 (LQ) | SwinFusion++ (ours, fixed recipe) | 0.9878 | 94.64% | 0.9470 |
| FF++ C40 (LQ) | CNN–LSTM (preliminary, seed 1701) | 0.7984 | 70.71% | 0.7515 |

**Preliminary paired test (same pipeline, 280 common C40 videos, 70 dependency groups, seed-1701 single models):** SwinFusion++ − CNN–LSTM ΔAUC = **+0.1846** [0.1503, 0.2165], ΔF1 = **+0.1867** [0.1503, 0.2201], Holm-adjusted p = 0.0004. This remains the only formally eligible SwinFusion++-vs-recurrent inference; the C23 contrast in that study was exploratory because training cohorts differed.

## 2. Published CNN-LSTM-family results on FF++ (context)

| Family | Setting | Reported value | Tier |
|---|---|---|---|
| Sabir et al. 2019 (DenseNet/ResNet-50 + GRU/BiGRU, landmark alignment; GRU, not LSTM) | FF++ DeepFakes, c40/LQ | DeepFakes subset: accuracy 91.7–96.9%, ROC-AUC 0.989–0.996 (best 96.9% / 0.996, 5-frame recurrent with alignment); single-frame variants up to 96.4% / 0.995 | B (unit unstated) |
| Güera & Delp 2018 (InceptionV3 + LSTM) | Own 600-video web dataset, 20–80 frames | Accuracy ~94–97% | C |
| Chen et al. 2022 (Xception + spatio-temporal attention + ConvLSTM) | FF++ (various), DFDC, Celeb-DF | Accuracy up to ~99% within FF++ (settings vary; available only as secondary survey quotes) | C |
| Saikia et al. 2022 (optical-flow CNN + LSTM) | FF++ (subset unstated), Celeb-DF v1 counts, DFDC | Accuracy ~74–91%; AUC 0.75–0.91 on FF++ (0.73 on Celeb-DF) | C |

Full rows with citations and notes are in `table2_published_AB.csv` and `table3_published_C.csv`.

---

## Interpretation

1. **SwinFusion++ exceeds the reproduced CNN–LSTM by a large margin on both FF++ conditions:** +0.21 AUC and +27 accuracy points on C23, +0.20 AUC and +25 points on C40 (BO-selected; the fixed recipe gives +0.21 / +26 and +0.19 / +24). The preliminary study's paired test on C40 (ΔAUC +0.18, p = 0.0004) is the formal statistical support; both current SwinFusion++ models (BO-selected 0.9941, fixed recipe 0.9878 on C40) are stronger than the seed-1701 model used in that test (0.9830), so the gap has not narrowed.
2. **The margin reflects representation and pretraining as much as architecture.** The recurrent baseline uses ImageNet ResNet-18 features and a short LSTM with a 15-epoch budget; SwinFusion++ uses two large pretrained Swin backbones and a 30-epoch optimized schedule. The result therefore establishes that SwinFusion++ as a configured system outperforms this representative CNN–LSTM, not that recurrence is intrinsically inadequate.
3. **Published recurrent detectors are reported under non-matched protocols.** The strongest, Sabir et al.'s aligned recurrent variants, report 96.9% accuracy and ROC-AUC 0.996 on FF++ c40 DeepFakes, slightly above SwinFusion++'s C40 values (BO-selected 96.1%, 0.994; fixed recipe 94.6%, 0.988), though with unstated evaluation units, different splits and GRU rather than LSTM recurrence; Chen et al.'s attention-ConvLSTM is reported at similar accuracy, but only through secondary survey quotes (Tier C). Sabir et al.'s own ablation shows that most of their gain comes from face alignment rather than recurrence (single-frame DenseNet 94.5% → with alignment 96.4% → with BiGRU 96.9%). SwinFusion++'s advantage over the *published* CNN-recurrent family is therefore clear against the optical-flow CNN–LSTM of Saikia et al. (Güera & Delp report on a different, web-collected dataset and cannot be ranked) but not against the best aligned recurrent models, with which it is comparable; no statistical claim is made for either.
4. **Compression (C40).** The reproduced CNN–LSTM loses little between C23 and C40 because it is weak on both. SwinFusion++ retains 0.994 AUC (BO-selected; 0.988 fixed recipe) under heavy compression. Under the matched recipe, however, it does not exceed the standalone encoders on C40 (Swin-B 0.988, Video Swin-B 0.992; RQ1), so this robustness cannot be attributed to the fusion design specifically.

## Answer to RQ3

On FF++ DeepFakes HQ (C23) and LQ (C40), SwinFusion++ (BO-selected: ROC-AUC 0.996 / 0.994, accuracy 98.2% / 96.1%; fixed recipe: 0.994 / 0.988, 97.9% / 94.6%) substantially outperforms the locally reproduced CNN–LSTM baseline (0.788 / 0.798, 71.4% / 70.7%), with the preliminary study's protocol-eligible paired test on C40 confirming a significant advantage (ΔAUC +0.18, Holm p = 0.0004). Relative to published CNN-LSTM-family results, SwinFusion++ is clearly superior to the optical-flow CNN–LSTM of Saikia et al. and comparable to, not better than, the best aligned recurrent models (Sabir et al.: 96.9% / 0.996 vs 96.1% / 0.994 on C40 DeepFakes, Tier B), under the caveat that published protocols are not matched.

**Limitations to state.** The reproduced CNN–LSTM is a single representative implementation (one seed, earlier pipeline) with a smaller pretrained backbone and budget; its numbers are from the preliminary study's test population (same FF++ split size, 280 videos) rather than re-run under the current pipeline; published comparisons are descriptive only.
