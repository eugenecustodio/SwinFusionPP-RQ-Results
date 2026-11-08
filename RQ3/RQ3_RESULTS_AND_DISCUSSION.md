# RQ3 — Results and Discussion

**RQ3.** How does the performance of SwinFusion++ compare to CNN-LSTM models on the FaceForensics++ (HQ/LQ) dataset?

**Evidence used (state in the text).** (i) SwinFusion++'s held-out FF++ C23 and C40 test results (video-level, three-seed ensembles, frozen thresholds). (ii) The representative CNN–LSTM (ImageNet ResNet-18 embeddings + one-layer LSTM, 256 hidden units) reproduced in the authors' preliminary study on the same FF++ DeepFakes conditions, including that study's protocol-eligible paired comparison on C40. (iii) Published CNN-LSTM-family results (Güera & Delp 2018; Sabir et al. 2019 recurrent-convolutional variants; Chen et al. 2022 Xception-ConvLSTM; Saikia et al. 2022) with comparability tiers. Files: `results/table1_ours.*`, `table1b_preliminary_baselines.*`, `table2_published_AB.*`, `table3_published_C.*`, `fig1_vs_published.png`.

---

## 1. SwinFusion++ vs the reproduced CNN–LSTM (FF++ DeepFakes)

| Condition | Model | ROC-AUC | Accuracy | F1 |
|---|---|---|---|---|
| FF++ C23 (HQ) | **SwinFusion++ (ours, test)** | **0.9964** | **98.21%** | **0.9822** |
| FF++ C23 (HQ) | CNN–LSTM (preliminary, seed 1701) | 0.7876 | 71.43% | 0.7452 |
| FF++ C40 (LQ) | **SwinFusion++ (ours, test)** | **0.9941** | **96.07%** | **0.9617** |
| FF++ C40 (LQ) | CNN–LSTM (preliminary, seed 1701) | 0.7984 | 70.71% | 0.7515 |

**Preliminary paired test (same pipeline, 280 common C40 videos, 70 dependency groups, seed-1701 single models):** SwinFusion++ − CNN–LSTM ΔAUC = **+0.1846** [0.1503, 0.2165], ΔF1 = **+0.1867** [0.1503, 0.2201], Holm-adjusted p = 0.0004. This remains the only formally eligible SwinFusion++-vs-recurrent inference; the C23 contrast in that study was exploratory because training cohorts differed.

## 2. Published CNN-LSTM-family results on FF++ (context)

| Family | Setting | Reported value | Tier |
|---|---|---|---|
| Sabir et al. 2019 (DenseNet/ResNet-50 + GRU/BiGRU, landmark alignment) | FF++ DeepFakes, c40/LQ, per-manipulation | Accuracy 87–97% (best ~96.9%, 5-frame BiGRU + alignment) | B (unit unstated) |
| Güera & Delp 2018 (InceptionV3 + LSTM) | Own 600-video web dataset, 20–80 frames | Accuracy ~94–97% | C |
| Chen et al. 2022 (Xception + spatio-temporal attention + ConvLSTM) | FF++ (various), DFDC, Celeb-DF | Accuracy up to ~99% within FF++ (settings vary) | B/C |
| Saikia et al. 2022 (optical-flow CNN + LSTM) | FF++ (subset unstated), Celeb-DF v1 counts, DFDC | Accuracy ~74–91%, AUC 0.73–0.91 | C |

Full rows with citations and notes are in `table2_published_AB.csv` and `table3_published_C.csv`.

---

## Interpretation

1. **SwinFusion++ exceeds the reproduced CNN–LSTM by a large margin on both FF++ conditions:** +0.21 AUC and +27 accuracy points on C23, +0.20 AUC and +25 points on C40. The preliminary study's paired test on C40 (ΔAUC +0.18, p = 0.0004) is the formal statistical support; the current SwinFusion++ (0.9941 on C40) is slightly stronger than the seed-1701 model used in that test (0.9830), so the gap has not narrowed.
2. **The margin reflects representation and pretraining as much as architecture.** The recurrent baseline uses ImageNet ResNet-18 features and a short LSTM with a 15-epoch budget; SwinFusion++ uses two large pretrained Swin backbones and a 30-epoch optimised schedule. The result therefore establishes that SwinFusion++ as a configured system outperforms this representative CNN–LSTM, not that recurrence is intrinsically inadequate.
3. **Published recurrent detectors are reported under non-matched protocols.** The strongest, Sabir et al.'s aligned BiGRU variants (≈96–97% accuracy on FF++ c40 DeepFakes) and Chen et al.'s attention-ConvLSTM, approach SwinFusion++'s C40 accuracy (96.1%) in their own settings, but with unstated evaluation units and different splits. SwinFusion++'s advantage over the *published* CNN-LSTM family is therefore clear against the older/simpler designs (Güera & Delp, Saikia et al.) and comparable-to-better against the best aligned recurrent models; no statistical claim is made for the latter.
4. **Compression (C40) is where temporal transformers help most.** The reproduced CNN–LSTM loses little between C23 and C40 because it is weak on both; SwinFusion++ retains 0.994 AUC under heavy compression, where frame-level texture cues degrade and the Video Swin stream's motion evidence remains available.

## Answer to RQ3

On FF++ DeepFakes HQ (C23) and LQ (C40), SwinFusion++ (ROC-AUC 0.996 / 0.994, accuracy 98.2% / 96.1%) substantially outperforms the locally reproduced CNN–LSTM baseline (0.788 / 0.798, 71.4% / 70.7%), with the preliminary study's protocol-eligible paired test on C40 confirming a significant advantage (ΔAUC +0.18, Holm p = 0.0004). Relative to published CNN-LSTM-family results, SwinFusion++ is clearly superior to early convolutional-recurrent designs and at least comparable to the best aligned recurrent models, under the caveat that published protocols are not matched.

**Limitations to state.** The reproduced CNN–LSTM is a single representative implementation (one seed, earlier pipeline) with a smaller pretrained backbone and budget; its numbers are from the preliminary study's test population (same FF++ split size, 280 videos) rather than re-run under the current pipeline; published comparisons are descriptive only.
