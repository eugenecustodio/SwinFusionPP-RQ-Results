# RQ6 — Results and Discussion

> **Option A framing (2026-10-28).** This version follows the analysis plan in Chapter 3 of the manuscript and decision D-25.
> - **Internal comparisons** use the **fixed-recipe** SwinFusion++, Swin-B and Video Swin-B (the principal architecture evidence).
> - **Comparisons with published and reproduced external models** use the **BO-selected SwinFusion++ (configured system)**, as RQ2 does, with the fixed-recipe value shown alongside.
>
> Paired p-values are the rank-based cluster permutation tests (2026-10-04 correction), Holm-adjusted within each family listed in `../paired_tests_optionA.csv`. Also corrected here: STIL accuracies (C23 99.6%, C40 98.2%), the C23 → Celeb-DF AUC (0.8785 → 0.878), and the preliminary-study comparison, which is now described as a change in pattern rather than a reversal.

**RQ6.** Does SwinFusion++ improve deepfake detection performance compared to existing CNN- and transformer-based spatio-temporal models, both within datasets and across diverse datasets?

**Evidence used (state in the text).** This question synthesizes RQ1–RQ4:
1. **Internal transformer encoders.** SwinFusion++ vs Swin-B and Video Swin-B under the identical fixed recipe, within and across all four datasets. These use paired rank-based cluster permutation tests, Holm-corrected within the RQ1_architecture (8 tests) and RQ6_architecture (18 tests) families.
2. **Configured system.** The BO-selected SwinFusion++, reported separately.
3. **Reproduced CNN baselines.** Xception and the CNN–LSTM, both from the preliminary study.
4. **Published values.** Within- and cross-dataset values for CNN models (Xception, I3D), recurrent models (CNN–LSTM family), and transformer/fusion models (STIL, FTCN, ISTVT, TALL-Swin, SFormer, CAST, TSFF-Net). They carry comparability tiers and are not tested statistically.

Files: `results/table1_within_architecture.*`, `table1b_within_configured_system.*`, `table2_directional_matrix_fixed.*`, `table2b_directional_matrix_bo.*`, `table3_transfer_auc.*`, `table3_transfer_all_metrics.*`, `table3b_paired_transfer_architecture.*`, `table3c_paired_transfer_configured_system.*`; published and preliminary tables unchanged in `../../RQ6/results/` (`table2c_preliminary_transfer.*`, `table3_published_cross.*`, `table4_published_within.*`); figures in `../figures/RQ6/`.

---

## 1. Within datasets

| Dataset | SwinFusion++ (fixed recipe) AUC / Acc | Best fixed-recipe encoder | SwinFusion++ (BO-selected) AUC / Acc | Reproduced CNN (prelim.) | Best published (Tier A/B) |
|---|---|---|---|---|---|
| FF++ C23 | 0.9942 / 97.9% | Swin-B 0.9965; Video Swin-B Acc 98.9% | 0.9964 / 98.2% | Xception 0.77; CNN–LSTM 0.79 | STIL Acc 99.6%, SFormer Acc 99.9%, FTCN AUC 0.999, TALL-Swin AUC 0.999 (B) |
| FF++ C40 | 0.9878 / 94.6% | Video Swin-B 0.9915 / 95.7% | **0.9941 / 96.1%** | Xception 0.81; CNN–LSTM 0.80 | STIL Acc 98.2%, SFormer Acc 98.2%, Xception (XN-avg) 96.8–97.1%; best AUC FTCN 0.983 (B) |
| Celeb-DF v2 | 0.9951 / 97.8% | Video Swin-B 0.9958 / 98.3% | **0.9983 / 98.4%** | Xception 0.65 | STIL Acc 99.8%, Xception 99.4%, I3D 99.2% |
| DeeperForensics | **0.9974 / 98.8%** | Swin-B 0.9966 / 97.8% | 0.9954 / 98.5% | Xception 0.998 (Acc 46%) | SFormer/I3D up to 100% |

No within-dataset difference between SwinFusion++ and either encoder is significant, under the fixed recipe or for the BO-selected configuration (all p_Holm ≥ 0.18).

## 2. Across datasets

**Directional ROC-AUC matrix, SwinFusion++ (fixed recipe); frozen source thresholds.** The diagonal is within-dataset.

| Train ↓ / Test → | FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics |
|---|---|---|---|---|
| **FF++ C23** | *0.9942* | 0.9760 | 0.8624 | 0.8261 |
| **Celeb-DF v2** | 0.8958 | 0.8384 | *0.9951* | 0.7233 |
| **DeeperForensics** | 0.8127 | 0.7668 | 0.5879 | *0.9974* |

The BO-selected matrix (`table2b_directional_matrix_bo.*`) is higher on C23 → C40 (0.9862) and C23 → Celeb-DF (0.8785), and lower in the other seven directions.

**Internal comparison across the nine transfer directions (principal, fixed recipe).**
- **Best point estimate:** SwinFusion++ in 5 directions (C23 → C40, Celeb-DF → C40, Celeb-DF → DeeperForensics, DeeperForensics → C23, DeeperForensics → C40), Video Swin-B in 3 and Swin-B in 1.
- **SwinFusion++ > Swin-B, significant after Holm correction in seven directions:**
  - C23 → DeeperForensics: +0.258;
  - Celeb-DF → C23: +0.049, p = 0.018;
  - Celeb-DF → C40: +0.061;
  - Celeb-DF → DeeperForensics: +0.122;
  - DeeperForensics → C23: +0.201;
  - DeeperForensics → C40: +0.170;
  - DeeperForensics → Celeb-DF: +0.129.

  All are at p = 0.004 except where stated.
- **SwinFusion++ > Video Swin-B, significant in three directions:** Celeb-DF → C40 (+0.075), Celeb-DF → DeeperForensics (+0.063) and DeeperForensics → C40 (+0.084), all p = 0.004.
- **No direction in which an encoder is significantly better than SwinFusion++.**
- **Mean transfer AUC (descriptive):** SwinFusion++ 0.810, Video Swin-B 0.785, Swin-B 0.700.

**Configured system (BO-selected).**
- Significantly better than Swin-B in six directions, and than Video Swin-B on C23 → C40 (+0.012, p = 0.015).
- Significantly worse than Video Swin-B on C23 → DeeperForensics (−0.111, p = 0.004) and Celeb-DF → C23 (−0.039, p = 0.005).
- Mean transfer AUC 0.762.

## 3. Published cross-dataset results, FF++ C23 → Celeb-DF v2 (the field's standard generalization test)

| Model | ROC-AUC | Tier |
|---|---|---|
| Xception | 0.653–0.737 | A/B |
| CAST-B5 / CAST-B0 | 0.749 / 0.770 | A |
| STIL (c40-trained) | 0.756 | B |
| TSFF-Net | 0.771 | B |
| I3D | 0.782 | A |
| Swin-B (as reported by TALL) | 0.831 | A |
| ISTVT | 0.841 | A |
| **SwinFusion++ (ours, fixed recipe)** | **0.862** | — |
| FTCN | 0.869 | A |
| **SwinFusion++ (ours, BO-selected; plain / flip-TTA)** | **0.878 / 0.885** | — |
| TALL-Swin | 0.908 | A |

**FF++ C23 → DeeperForensics (published).** FTCN 0.988, ISTVT 0.986, TALL-Swin 0.996 and Xception 0.845 were all trained on all FF++ manipulations. Ours are SwinFusion++ 0.826 (fixed recipe) / 0.732 (BO-selected) and Video Swin-B 0.842, on the authors' DeeperForensics binary construction. The target population and DeepFakes-only training differ, so these values are not comparable (see the caveats below).

**Preliminary study (earlier pipeline), FF++ C23 → Celeb-DF:** SwinFusion++ 0.873, Swin-B 0.905, Video Swin-B 0.905. FF++ C23 → C40: 0.969 / 0.972 / 0.944.

---

## Interpretation

1. **Within datasets, SwinFusion++ matches the standalone transformers and clearly exceeds the reproduced CNN baselines.**
   - **Against the encoders:** under matched training it is statistically indistinguishable from Swin-B and Video Swin-B on all four datasets (ceiling effect).
   - **Against the reproduced CNN and CNN–LSTM baselines:** it is 0.18–0.35 AUC higher on FF++ and Celeb-DF.
   - **Against published transformer and fusion models (STIL, FTCN, SFormer, TALL-Swin):** it is comparable within protocol differences. The BO-selected configuration has the highest C40 ROC-AUC in the record (0.994; fixed recipe 0.988, also above FTCN's 0.983). In accuracy it is one to two points below the best published values on C23, C40 and Celeb-DF.
2. **Across datasets, the architectural advantage appears under distribution shift.** With identical training, SwinFusion++ is never significantly worse than either encoder, beats Swin-B in seven of nine directions and Video Swin-B in three, and has the highest mean transfer AUC. The advantage is concentrated in transfers from Celeb-DF and DeeperForensics sources. From the standard FF++ C23 source, the three are tied on C40 and Celeb-DF.
3. **Against published FF++ → Celeb-DF results, SwinFusion++ sits near the top of the record.**
   - **Fixed recipe (0.862):** above every CNN, recurrent and fusion model listed except FTCN (0.869) and TALL-Swin (0.908). That includes ISTVT, I3D, CAST (≤ 0.77) and TSFF-Net (0.771).
   - **BO-selected configuration (0.878; 0.885 with TTA):** above all but TALL-Swin.
   - **The top of the ranking is unresolved.** Both 95% intervals ([0.805, 0.915] and [0.825, 0.926]) contain ISTVT, FTCN and TALL-Swin, and the protocols differ.
   - **Relation to the preliminary study.** There, SwinFusion++ (0.873) trailed its own backbones (0.905). Under the matched recipe it is now level with them (0.862 vs 0.868). Most of that change comes from the encoders dropping rather than from SwinFusion++ rising. The test populations also differ (859 vs 978 videos), so this is a change in pattern, not an improvement.
4. **The optimization regimen matters as much as the architecture for transfer.** The BO-selected configuration improves in-distribution AUC and compression transfer (C23 → C40) but significantly lowers five other directions relative to the fixed recipe (RQ1, §4). Dataset-specific tuning on source-validation AUC therefore trades generalization for in-distribution fit.
5. **DeeperForensics transfer is the least comparable cell.** FF++-trained models reach 0.57–0.85 AUC on the authors' DeeperForensics construction, far below the published FF++ → DeeperForensics values (0.99). Those values use all four FF++ manipulations for training and the official DeeperForensics protocol. In addition, 382 of 402 DeeperForensics primary test videos share source lineage with FF++ rows (disclosed in the evaluation protocol). This direction should be reported with that qualification and not used as a headline generalization claim.
6. **Threshold transfer, not ranking, is the dominant failure mode under shift.**
   - **The pattern:** across transfer cells, precision stays high (≥ 0.9 in most cells) while recall collapses (often < 10% on DeeperForensics and C40 targets), because the source-validation threshold is retained.
   - **What to report:** ROC-AUC and PR-AUC remain the appropriate cross-dataset metrics. Threshold-dependent metrics are reported for transparency and reflect an operating-point mismatch shared by all models.
7. **Against the evaluation criterion in Chapter 3,** a model is "strong" only if it (a) performs competitively within each in-distribution benchmark, (b) remains stable across FF++ quality levels, and (c) transfers better to unseen datasets than competing baselines. Under the matched recipe:
   - **(a) is met:** ROC-AUC 0.988–0.997 on every benchmark.
   - **(b) is met:** 0.988 within C40 and 0.976 for C23 → C40, on par with the encoders.
   - **(c) is met against Swin-B** (seven of nine directions) **and partly against Video Swin-B:** better in three, tied in six, worse in none.

## Hypothesis decision

H0: *SwinFusion++ does not improve deepfake detection performance compared to existing CNN- or transformer-based spatio-temporal models.*

- **H0 is rejected against the reproduced CNN baselines.** Margins are 0.18–0.35 AUC within datasets. The formal paired test (preliminary study, C40, vs the CNN–LSTM) gives ΔAUC +0.18, Holm p = 0.0004.
- **H0 is rejected against the standalone transformer encoders under cross-dataset transfer** in the directions listed in §2: seven against Swin-B and three against Video Swin-B.
- **H0 is not rejected within datasets against Swin-B or Video Swin-B** (all p_Holm = 1.00). It is also not rejected for transfer from FF++ C23 to C40 and Celeb-DF.
- **Published models cannot be tested.** The protocols are not matched, so no hypothesis decision is made against them.

## Answer to RQ6

**Partly, and mainly across datasets.**
- **Within datasets:** SwinFusion++ performs at the level of the standalone Swin and Video Swin transformers (statistically indistinguishable under identical training) and substantially exceeds the reproduced CNN and CNN–LSTM baselines. That places it within the band of the strongest published spatio-temporal detectors.
- **Across datasets, under identical training:** it is never significantly worse than either transformer encoder and is significantly better than Swin-B in seven of nine transfer directions and Video Swin-B in three. It has the highest mean transfer ROC-AUC (0.810).
- **On FF++ → Celeb-DF:** it reaches 0.862 (fixed recipe) and 0.878 (BO-selected configuration). That is above all published CNN, recurrent and fusion models in the record except FTCN and/or TALL-Swin, with overlapping intervals.
- **Where the improvement shows:** it is concentrated in transfer from Celeb-DF and DeeperForensics sources. From FF++ C23 the encoders are tied with it.
- **The BO-selected configuration** trades several transfer directions for higher in-distribution scores.
- **Thresholds:** all models suffer threshold-transfer degradation.

**Overall:** SwinFusion++ improves cross-dataset robustness relative to its standalone encoders under matched training, without an in-distribution gain.

**Limitations to state.**
- **Published values are not protocol-matched** (splits, manipulations, units).
- **The DeeperForensics construction** is the authors' audited subset, with disclosed lineage overlap.
- **Unequal optimization:** only SwinFusion++ was Bayesian-optimized, with 8 trials for Celeb-DF and DeeperForensics.
- **No target adaptation:** thresholds were frozen on source validation.
- **Small test sets:** FF++ has 280 videos in 70 clusters.
- **Controls trained only on C23:** the matched controls (RQ4) were trained only on FF++ C23. The transfer advantage from Celeb-DF and DeeperForensics sources therefore cannot yet be attributed to cross-attention.

**Future work motivated by RQ6.**
- **(a) Generalization-targeted optimization:** use leave-one-domain-out validation AUC or worst-domain AUC as the Bayesian objective, with a held-out final domain.
- **(b) Deployment under shift:** label-free threshold and calibration adaptation.
- **(c) Distillation:** distill SwinFusion++ into a single-stream student (e.g. Video Swin-B) to retain its robustness at lower cost.
- **(d) Controls on other sources:** train the matched controls on C40, Celeb-DF and DeeperForensics to test whether the transfer advantage from those sources comes from cross-attention.
