# RQ6 — Results and Discussion

**RQ6.** Does SwinFusion++ improve deepfake detection performance compared to existing CNN- and transformer-based spatio-temporal models, both within datasets and across diverse datasets?

**Evidence used (state in the text).** This question synthesises RQ1–RQ4: (i) SwinFusion++ vs the internal Swin-B / Video Swin-B families within and across all four datasets (paired, Holm-corrected within the RQ6 transfer family); (ii) the locally reproduced CNN baselines (Xception, CNN–LSTM) from the preliminary study; (iii) published within- and cross-dataset values for CNN (Xception, I3D), recurrent (CNN-LSTM family), and transformer/fusion models (STIL, FTCN, ISTVT, TALL-Swin, SFormer, CAST, TSFF-Net), with comparability tiers and no statistical tests. Files: `results/table1_within.*`, `table2_directional.*`, `table2b_paired_rq6.*`, `table2c_preliminary_transfer.*`, `table3_published_cross.*`, `table4_published_within.*`, `fig1_matrix_swinfusionpp.png`.

---

## 1. Within datasets

| Dataset | SwinFusion++ AUC / Acc | Best internal baseline | Reproduced CNN (prelim.) | Best published (Tier A/B) |
|---|---|---|---|---|
| FF++ C23 | 0.9964 / 98.2% | Swin-B 0.9965 / Video Swin-B 98.9% | Xception 0.77; CNN-LSTM 0.79 | STIL Acc 98.6%, FTCN AUC 0.999, SFormer Acc 99.9% |
| FF++ C40 | **0.9941 / 96.1%** | Video Swin-B 0.9915 / 95.7% | Xception 0.81; CNN-LSTM 0.80 | STIL Acc 97.0%, Xception (XN-avg) 96.8% |
| Celeb-DF v2 | **0.9983 / 98.4%** | Video Swin-B 0.9958 / 98.3% | Xception 0.65 | STIL Acc 99.8%, Xception 99.4%, I3D 99.2% |
| DeeperForensics | 0.9954 / **98.5%** | Swin-B 0.9966 / 97.8% | Xception 0.998 (Acc 46%) | SFormer/I3D up to 100% |

## 2. Across datasets: SwinFusion++ directional matrix (ROC-AUC, frozen source thresholds)

| Train ↓ / Test → | FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics |
|---|---|---|---|---|
| **FF++ C23** | 0.9964 | **0.9862** | **0.8785** | 0.7316 |
| **Celeb-DF v2** | 0.8657 | 0.7345 | 0.9983 | 0.6824 |
| **DeeperForensics** | 0.7236 | 0.7067 | 0.5519 | 0.9954 |

Internal comparison across the nine transfer directions: SwinFusion++ has the highest point estimate in 4 (C23 → C40, C23 → Celeb-DF, Celeb-DF → DeeperForensics, DeeperForensics → C40), Video Swin-B in 4, Swin-B in 1. Significant after Holm correction: SwinFusion++ > Swin-B in four directions (C23 → DFo +0.164; Celeb-DF → DFo +0.081; DFo → C23 +0.112; DFo → C40 +0.110; all p = 0.004); Video Swin-B > SwinFusion++ on C23 → DeeperForensics (+0.111, p = 0.004). All other internal transfer differences are not significant.

## 3. Published cross-dataset results, FF++ C23 → Celeb-DF v2 (the field's standard generalisation test)

| Model | ROC-AUC | Tier |
|---|---|---|
| Xception | 0.653–0.737 | A/B |
| CAST-B5 / CAST-B0 | 0.749 / 0.770 | A |
| STIL (c40-trained) | 0.756 | B |
| TSFF-Net | 0.771 | B |
| I3D | 0.782 | A |
| Swin-B (as reported by TALL) | 0.831 | A |
| ISTVT | 0.841 | A |
| FTCN | 0.869 | A |
| **SwinFusion++ (ours, plain / flip-TTA)** | **0.879 / 0.885** | — |
| TALL-Swin | 0.908 | A |

FF++ C23 → DeeperForensics (published, all-manipulation FF++ training): FTCN 0.988, ISTVT 0.986, TALL-Swin 0.996, Xception 0.845 — versus SwinFusion++ 0.732 and Video Swin-B 0.842 on the authors' DeeperForensics binary construction (different target population and DeepFakes-only training; not comparable, see caveats).

Preliminary study (earlier pipeline), FF++ C23 → Celeb-DF: SwinFusion++ 0.873, Swin-B 0.905, Video Swin-B 0.905; → C40: 0.969 / 0.972 / 0.944.

---

## Interpretation

1. **Within datasets, SwinFusion++ is at the top of the field's reported range and best-or-equivalent internally.** It holds the best internal ROC-AUC on C40 and Celeb-DF and the best accuracy on three datasets; against the reproduced CNN and CNN-LSTM baselines it is 0.2–0.35 AUC higher on FF++ and Celeb-DF; against published transformer and fusion models (STIL, FTCN, SFormer, TALL-Swin) it is comparable within protocol differences. No internal within-dataset difference is statistically significant (ceiling effect).
2. **Across datasets, SwinFusion++ generalises best from the standard FF++ training condition and sits near the top of published FF++ → Celeb-DF results.** Its 0.879 (0.885 with the pre-declared flip-TTA variant) exceeds every published CNN, recurrent and fusion model in the record except TALL-Swin (0.908), including FTCN (0.869), which was designed for generalisation, and the other dual-stream/fusion designs CAST (≤ 0.77) and TSFF-Net (0.771). This is also a reversal of the preliminary study, where SwinFusion++ (0.873) trailed its own backbones (0.905).
3. **The improvement is not uniform across training sources.** When trained on Celeb-DF or DeeperForensics, SwinFusion++ transfers significantly better than Swin-B but is matched or exceeded by Video Swin-B in several directions, and all models degrade sharply (AUC 0.55–0.90, accuracy ≈ 50–70%). The RQ1 supplementary analysis shows that dataset-specific optimisation improved in-distribution results but reduced some transfers relative to the fixed-recipe SwinFusion++; generalisation from non-FF++ sources is therefore a limitation of the optimised configuration, not only of the architecture.
4. **DeeperForensics transfer is the weakest and least comparable cell.** FF++-trained models reach only 0.57–0.84 AUC on the authors' DeeperForensics construction (SwinFusion++ 0.73, Video Swin-B 0.84), far below published FF++ → DFo values (0.99), which use all four FF++ manipulations for training and the official DFo protocol. In addition, 382 of 402 DeeperForensics primary test videos share source lineage with FF++ rows (disclosed in the evaluation protocol), so this direction should be reported with that qualification and not used as a headline generalisation claim.
5. **Threshold transfer, not ranking, is the dominant failure mode under shift.** Across all transfer cells, precision stays high (≥ 0.9) while recall collapses (often < 10% on DeeperForensics and C40 targets), because the source-validation threshold is retained. ROC-AUC and PR-AUC remain the appropriate cross-dataset metrics; threshold-dependent metrics are reported for transparency and should be interpreted as operating-point mismatch shared by all models.

## Answer to RQ6

Yes, with qualifications. **Within datasets**, SwinFusion++ matches or exceeds the standalone Swin and Video Swin transformers (best ROC-AUC on FF++ C40 and Celeb-DF; best accuracy on three of four datasets; no significant internal differences) and substantially exceeds the reproduced CNN and CNN-LSTM baselines, placing it within the band of the strongest published spatio-temporal detectors. **Across datasets**, trained on FF++ C23 it achieves the best internal generalisation to C40 (0.986) and Celeb-DF (0.879, 0.885 with TTA), the latter above all published CNN, recurrent and fusion models in the record except TALL-Swin, and it significantly outperforms Swin-B in four transfer directions. It does not generalise uniformly better than Video Swin-B, which is significantly stronger on FF++ → DeeperForensics and competitive from Celeb-DF/DeeperForensics sources, and all models suffer threshold-transfer degradation. The overall conclusion is that SwinFusion++ is the best-performing or statistically equivalent detector within every dataset and the strongest FF++-trained generaliser by point estimate, while cross-dataset robustness remains condition-dependent.

**Limitations to state.** Published values are not protocol-matched (splits, manipulations, units); the DeeperForensics construction is the authors' audited subset with disclosed lineage overlap; only SwinFusion++ was Bayesian-optimised; thresholds were frozen on source validation (no target adaptation); FF++ test sets are small (280 videos, 70 clusters).

**Future work motivated by RQ6.** (a) Generalisation-targeted optimisation (leave-one-domain-out validation AUC or worst-domain AUC as the Bayesian objective, with a held-out final domain); (b) label-free threshold/calibration adaptation for deployment under shift; (c) knowledge distillation of SwinFusion++ into a single-stream student (e.g. Video Swin-B) to retain its accuracy at lower cost; (d) training the matched controls on C40/Celeb-DF to test cross-attention on harder data.
