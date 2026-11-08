# RQ2 expansion: review draft (accepted view)

## Chapter 1/3 sentences (final NEW text)
**C8:** «RQ2 will compare BO-selected SwinFusion++, with the fixed-recipe result alongside, with previously reported results for established frame-level, recurrent, 3D-convolutional, and spatio-temporal detectors, including Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer. RQ3 will compare SwinFusion++ on C23 and C40 with previously reported CNN–LSTM results.»

**C31:** «External baselines (Xception, I3D, STIL, FTCN with Temporal Transformer, TALL-Swin, SFormer, CNN–LSTM models, CAST, TSFF-Net, and the other previously reported detectors listed in Chapter 4) will not be retrained in this study; their previously reported results will be recorded with their datasets, protocols, and evaluation units.»

**C52:** «they are grouped according to the kind of evidence they emphasize and the kind of comparison they make possible. Previously reported results will be given for the subset with values on the datasets of this study: frame-level detectors (Xception, MesoNet, Face X-ray, F3-Net, FDFL, Multi-attention, RECCE, and the face-warping-artifact detectors D-FWA and DSP-FWA); recurrent models (CNN–LSTM models, ResNet+LSTM, CNN–GRU, and Two-branch); 3D-convolutional and video-recognition models (C3D, I3D, TSN, TEI, and ADDNet-3D); spatio-temporal detectors (S-MIL, STIL, FTCN, and LipForensics); and transformer-based and fusion models (ViViT, VTN, VidTr, DFDT, ADT, M2TR, ISTVT, TALL-Swin, SFormer, CAST, and TSFF-Net).»


## RQ2 section
[NEW] ## Research Question 2: SwinFusion++ Compared With Established Baselines
[NEW] RQ2 asked: What is the performance of SwinFusion++ relative to established baselines when evaluated on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0? Three kinds of evidence are kept separate. The first is the held-out performance of SwinFusion++; following the analysis plan, the BO-selected configuration is reported with the fixed-recipe result alongside. The second is the Xception baseline that the authors trained in their preliminary study (Custodio et al., 2026), the only established baseline that this group has run on these datasets; it used an earlier pipeline, a single seed, and partly different test populations. The third consists of previously reported results for established frame-level, recurrent, 3D-convolutional, and spatio-temporal detectors, taken from the comparison tables of X. Li et al. (2020), Gu et al. (2021), Jiang et al. (2020), Masi et al. (2020), Haliassos et al. (2021), and Xu et al. (2023) and from Rössler et al. (2019), Zheng et al. (2021), and Kingra et al. (2024). Every row of each table used is recorded in Appendix J, Table J9, and rows were left out of the chapter tables only by a stated category, never because of their values. No baseline was retrained in the present study, so none of these comparisons is paired and none is tested; they are descriptive.
[NEW] Two features of this study’s test sets further limit comparison with published values. The Celeb-DF v2 test set contains 978 videos split by target identity rather than the official 518-video test list, and the DeeperForensics-1.0 test set is this study’s construction of unperturbed manipulated videos and their FaceForensics++ source originals, which corresponds to the benchmark’s standard (undistorted) setting, although identical test lists cannot be verified; the benchmark’s distorted and hidden test settings are not comparable. Published results also come from their own splits, frame sampling, face crops, and operating points.
[NEW] The models and their original papers are as follows: frame-level detectors Xception (Chollet, 2017), MesoNet (Afchar et al., 2018), the face-warping detectors D-FWA and DSP-FWA (Y. Li &amp; Lyu, 2018), Face X-ray (L. Li et al., 2020), F3-Net (Qian et al., 2020), FDFL (J. Li et al., 2021), the multi-attentional detector (H. Zhao et al., 2021), RECCE (Cao et al., 2022), and Add-Net and ADDNet-3D (Zi et al., 2020); recurrent models built on long short-term memory (Hochreiter &amp; Schmidhuber, 1997), including a ResNet+LSTM baseline (He et al., 2016), a gated recurrent CNN–GRU (Sabir et al., 2019), and the two-branch recurrent network (Masi et al., 2020); 3D-convolutional and video-recognition models C3D (Tran et al., 2015), I3D (Carreira &amp; Zisserman, 2017), TSN (L. Wang et al., 2016), and TEI (Z. Liu et al., 2020); and spatio-temporal detectors and video transformers S-MIL-T (X. Li et al., 2020), STIL (Gu et al., 2021), FTCN (Zheng et al., 2021), LipForensics (Haliassos et al., 2021), DFDT (Khormali &amp; Yuan, 2022), ADT (P. Wang et al., 2022), M2TR (J. Wang et al., 2022), VTN (Neimark et al., 2021), VidTr (Y. Zhang et al., 2021), ViViT (Arnab et al., 2021), ISTVT (C. Zhao et al., 2023), TALL-Swin (Xu et al., 2023), and SFormer (Kingra et al., 2024). DeepRhythm (Qi et al., 2020) is listed in Table J9 only, because the value quoted for it by Gu et al. (2021) does not match its original paper.
[NEW] SwinFusion++ and the Preliminary-Study Xception Baseline
[NEW] Table 9 places SwinFusion++ beside the Xception baseline of the preliminary study.
[NEW] #### Table 9. SwinFusion++ and the Preliminary-Study Xception Baseline
[NEW] | Model | Test videos (fake %) | ROC-AUC [95% CI] | Acc (%) | Rec (%) | Spec (%) | F1 |
| --- | --- | --- | --- | --- | --- | --- |
[NEW] | FF++ C23 — this study: 280 videos (50.00% fake) |
[NEW] | SwinFusion++ (BO-selected) | 280 (50.00) | 0.9964 [0.9886, 1.0000] | 98.21 | 98.57 | 97.86 | 0.9822 |
[NEW] | SwinFusion++ (fixed recipe) | 280 (50.00) | 0.9942 [0.9834, 0.9999] | 97.86 | 97.14 | 98.57 | 0.9784 |
[NEW] | Xception (preliminary study) | 280 (50.00) | 0.7725 | 69.64 | 67.14 | 72.14 | 0.6886 |
[NEW] | FF++ C40 — this study: 280 videos (50.00% fake) |
[NEW] | SwinFusion++ (BO-selected) | 280 (50.00) | 0.9941 [0.9875, 0.9989] | 96.07 | 98.57 | 93.57 | 0.9617 |
[NEW] | SwinFusion++ (fixed recipe) | 280 (50.00) | 0.9878 [0.9772, 0.9965] | 94.64 | 95.71 | 93.57 | 0.9470 |
[NEW] | Xception (preliminary study) | 280 (50.00) | 0.8109 | 74.29 | 74.29 | 74.29 | 0.7429 |
[NEW] | Celeb-DF v2 — this study: 978 videos (86.20% fake); all fakes in 9 identity clusters |
[NEW] | SwinFusion++ (BO-selected) | 978 (86.20) | 0.9983 [0.9963, 1.0000] | 98.36 | 98.34 | 98.52 | 0.9904 |
[NEW] | SwinFusion++ (fixed recipe) | 978 (86.20) | 0.9951 [0.9905, 0.9995] | 97.75 | 98.10 | 95.56 | 0.9869 |
[NEW] | Xception (preliminary study) | 859 (84.17) | 0.6480 | 84.17* | 100.00* | 0.00* | 0.9140* |
[NEW] | DeeperForensics-1.0 — this study: 402 videos (50.00% fake) |
[NEW] | SwinFusion++ (BO-selected) | 402 (50.00) | 0.9954 [0.9874, 1.0000] | 98.51 | 97.01 | 100.00 | 0.9848 |
[NEW] | SwinFusion++ (fixed recipe) | 402 (50.00) | 0.9974 [0.9921, 1.0000] | 98.76 | 97.51 | 100.00 | 0.9874 |
[NEW] | Xception (preliminary study) | 2,385 (91.61) | 0.9978 | 46.00† | 41.05† | 100.00† | 0.5821† |
[NEW] Note. SwinFusion++: three-seed ensembles, thresholds frozen on source validation; 95% percentile intervals from 5,000 stratified cluster-bootstrap draws (Celeb-DF v2 approximate). Xception: single seed, earlier pipeline (Custodio et al., 2026); no interval reported; recall and specificity derived from its reported accuracy and F1. Its Celeb-DF v2 and DeeperForensics-1.0 test sets differ from this study. *Every video labeled fake. †No false positives; 1,288 of 2,185 fake videos missed. Descriptive only; no tests.
[NEW] On FaceForensics++, where both studies used test sets of 280 videos (140 fake) drawn under the same source-pair split rule, SwinFusion++ reached ROC-AUC 0.9964 on C23 and 0.9941 on C40 (fixed recipe 0.9942 and 0.9878), against 0.7725 and 0.8109 for Xception. Its accuracy was 98.21% and 96.07% (fixed recipe 97.86% and 94.64%), against 69.64% and 74.29%. On Celeb-DF v2, SwinFusion++ reached ROC-AUC 0.9983 (fixed recipe 0.9951) on its 978-video test set, while Xception reached 0.6480 on its 859-video test set and labeled every video fake, so its 84.17% accuracy equals the share of fake videos. On DeeperForensics-1.0, both ranked videos almost perfectly (SwinFusion++ 0.9954, fixed recipe 0.9974; Xception 0.9978), but on very different populations: Xception’s test set held 2,385 videos, 91.61% of them fake and including perturbed variants, and at its threshold it missed 1,288 fake videos (accuracy 46.00%).
[NEW] SwinFusion++ therefore ranked videos far better than the preliminary-study Xception on FaceForensics++ C23 and C40 and much better on Celeb-DF v2, although on a different test population; on DeeperForensics-1.0 the two were similar. The two models differ in pipeline, training budget, pretraining, capacity, and number of seeds, so the comparison shows that SwinFusion++ exceeds this particular baseline on FaceForensics++ and Celeb-DF v2, not that the architecture alone accounts for the gap.
[NEW] Comparison With Previously Reported Results
[NEW] Table 10 lists the previously reported Tier A results, which use the same dataset, manipulation subset, compression, and video-level unit as this study, and Table 11 lists the Tier B results, which pool all four FaceForensics++ manipulations, leave the subset unstated, or score frames. Table J9 gives the full list of values considered and the reason for each exclusion.
[NEW] #### Table 10. Previously Reported Tier A Results on the Benchmarks of This Study
[NEW] | Model | FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics-1.0 |
| --- | --- | --- | --- | --- |
[NEW] | This study: three-seed ensembles, thresholds frozen on source validation |
[NEW] | SwinFusion++ (BO-selected) | Acc 98.21; AUC 0.9964 | Acc 96.07; AUC 0.9941 | Acc 98.36; AUC 0.9983 | Acc 98.51; AUC 0.9954 |
[NEW] | SwinFusion++ (fixed recipe) | Acc 97.86; AUC 0.9942 | Acc 94.64; AUC 0.9878 | Acc 97.75; AUC 0.9951 | Acc 98.76; AUC 0.9974 |
[NEW] | Previously reported, Tier A (each paper’s own split, frame sampling, and operating point) |
[NEW] | Xception | Acc 98.93–100.00ᵃᵇ | Acc 96.78–97.14ᵃᵇ | Acc 99.44ᵇ | Acc 100.00ᶜ |
[NEW] | D-FWA | — | — | Acc 98.58ᵇ | — |
[NEW] | CNN–LSTM | Acc 99.64ᵇ | Acc 96.43ᵇ | Acc 95.73ᵇ | — |
[NEW] | ResNet+LSTM | — | — | — | Acc 100.00ᶜ |
[NEW] | C3D | Acc 92.86ᵃ | Acc 89.29ᵃ | — | Acc 98.50ᶜ |
[NEW] | I3D | Acc 92.86ᵇ | Acc 91.07ᵇ | Acc 99.23ᵇ | Acc 100.00ᶜ |
[NEW] | TSN | — | — | — | Acc 99.25ᶜ |
[NEW] | TEI | Acc 97.86ᵃ | Acc 95.00ᵃ | Acc 99.12ᵃ | — |
[NEW] | S-MIL-T | Acc 99.64ᵇ | Acc 97.14ᵇ | Acc 98.84ᵇ | — |
[NEW] | ADDNet-3D | Acc 92.14ᵃ | Acc 90.36ᵃ | Acc 95.16ᵃ | — |
[NEW] | STIL | Acc 99.64ᵃ | Acc 98.21; AUC 0.9712ᵃ | Acc 99.78ᵃ | — |
[NEW] | SFormer | Acc 98.50–99.90ᵈ | Acc 94.82–98.15ᵈ | Acc 95.04–99.10ᵈ | Acc 99.67–100.00ᵈ |
[NEW] Note. Tier A only: FF++ DeepFakes subset at the stated compression, Celeb-DF v2, or the DeeperForensics-1.0 standard (undistorted) set; video level; values as printed; none was tested. Sources ᵃ and ᵇ use similar video-level protocols (16 and 20 test frames per video); their Xception values use frame-score averaging and differ between the two papers. The DeeperForensics-1.0 standard set has this study’s construction; identical test lists cannot be verified. Celeb-DF v2 test sets and fake shares differ (here 86.20% fake). SFormer values were not re-verified. ᵃGu et al. (2021); ᵇX. Li et al. (2020); ᶜJiang et al. (2020); ᵈKingra et al. (2024).
[NEW] #### Table 11. Previously Reported Tier B Results on FaceForensics++
[NEW] | Model | FF++ C23 Acc (%) | FF++ C23 AUC | FF++ C40 Acc (%) | FF++ C40 AUC | Setting | Source |
| --- | --- | --- | --- | --- | --- | --- |
[NEW] | This study (DeepFakes subset only; not like-for-like with the rows below) |
[NEW] | SwinFusion++ (BO-selected) | 98.21 | 0.9964 | 96.07 | 0.9941 | DeepFakes subset; video level | This study |
[NEW] | SwinFusion++ (fixed recipe) | 97.86 | 0.9942 | 94.64 | 0.9878 | DeepFakes subset; video level | This study |
[NEW] | Previously reported, Tier B (pooled manipulations, unstated subset, or frame level) |
[NEW] | MesoNet | 83.10‡ | — | 70.47‡ | — | All four manipulations; video level | ᵃ |
[NEW] | Xception | 95.73‡ | 0.9630 | 86.86 | 0.8930 | All four manipulations; video level | ᵃ |
[NEW] | Face X-ray | — | 0.8735 | — | 0.6160 | All four manipulations; video level | ᵃ |
[NEW] | Two-branch | 96.43 | — | 86.34 | — | All four manipulations; video level | ᵃ |
[NEW] | Add-Net | 96.78 | 0.9774 | 87.50 | 0.9101 | All four manipulations; video level | ᵃ |
[NEW] | F3-Net | 97.52 | 0.9810 | 90.43 | 0.9043 | All four manipulations; video level | ᵃ |
[NEW] | FDFL | 96.69 | 0.9930 | 89.00 | 0.9240 | All four manipulations; video level | ᵃ |
[NEW] | Multi-attentional | 97.60 | 0.9929 | 88.69 | 0.9040 | All four manipulations; video level | ᵃ |
[NEW] | RECCE | 97.06 | 0.9932 | 91.03 | 0.9502 | All four manipulations; video level | ᵃ |
[NEW] | LipForensics | 98.80 | 0.9970 | 94.20 | 0.9810 | All four manipulations; video level | ᵃ |
[NEW] | DFDT | 98.18 | 0.9926 | 92.67 | 0.9448 | All four manipulations; video level | ᵃ |
[NEW] | ADT | 92.05 | 0.9630 | 81.48 | 0.8252 | All four manipulations; video level | ᵃ |
[NEW] | M2TR (ST-M2TR) | — | 0.9942 | — | 0.9531 | All four manipulations; video level | ᵃ |
[NEW] | VTN | 98.47 | — | 94.02 | — | All four manipulations; video level | ᵃ |
[NEW] | VidTr | 97.42 | — | 92.12 | — | All four manipulations; video level | ᵃ |
[NEW] | ViViT (re-implemented) | 92.60 | — | 88.02 | — | All four manipulations; video level | ᵃ |
[NEW] | ISTVT (not re-verified) | 99.00 | — | 96.15 | — | All four manipulations; video level | ᵃ |
[NEW] | TALL-Swin | 98.65 | 0.9987 | 92.82 | 0.9457 | All four manipulations; video level | ᵃ |
[NEW] | LipForensics | 98.8 | 0.997 | 94.2 | 0.981 | All four manipulations; video level | ᵇ |
[NEW] | Xception | 97.0 | 0.993 | 89.0 | 0.920 | All four manipulations; video level | ᵇ |
[NEW] | Face X-ray | 78.4 | 0.978 | 34.2 | 0.773 | All four manipulations; video level | ᵇ |
[NEW] | CNN–GRU | 97.0 | 0.993 | 90.1 | 0.922 | All four manipulations; video level | ᵇ |
[NEW] | Two-branch | — | 0.9912 | — | 0.9110 | All four manipulations; video level; 700 test videos | ᶜ |
[NEW] | Xception | — | 0.9250 | — | 0.8675 | All four manipulations; video level; 700 test videos | ᶜ |
[NEW] | DSP-FWA | — | 0.5749 | — | 0.6234 | All four manipulations; video level; 700 test videos | ᶜ |
[NEW] | MesoNet | 95.26 | — | 89.52 | — | DeepFakes-specific detector; frame level | ᵈ |
[NEW] | Xception | 98.85 | — | 94.28 | — | DeepFakes-specific detector; frame level | ᵈ |
[NEW] | FTCN with Temporal Transformer | 99.1 | 0.998 | — | 0.983 | Subset not stated; video level; DeeperForensics-1.0 (own split): AUC 1.000 | ᵉ |
[NEW] Note. Tier B values as printed; none was tested, and none shares this study’s test videos or manipulation subset, so no row is comparable with SwinFusion++ like for like. A model reported by two papers has one row per source. ViViT was re-implemented by ᵃ; ISTVT was not re-verified against its original. ᵃ’s two-branch AUCs equal ᶜ’s frame-level values and are listed only in J9. ‡Equals Rössler et al.’s frame-level accuracy on all four manipulations. — = not reported. ᵃXu et al. (2023); ᵇHaliassos et al. (2021); ᶜMasi et al. (2020); ᵈRössler et al. (2019); ᵉZheng et al. (2021), supplement.
[NEW] In ROC-AUC, the only Tier A value is STIL’s 0.9712 on C40, below the 0.9941 of the BO-selected SwinFusion++ (fixed recipe 0.9878). The Tier B ROC-AUC values ranged from 0.5749 (DSP-FWA) to 0.9987 (TALL-Swin) on C23 and from 0.6160 (Face X-ray, as reported by Xu et al., 2023) to 0.983 (FTCN) on C40, while SwinFusion++ reached 0.9964 and 0.9941 (fixed recipe 0.9942 and 0.9878) on the DeepFakes subset alone; because the Tier B values pool manipulations or leave the subset unstated, they are not like-for-like.
[NEW] Accuracy is compared only for the Tier A values on balanced test sets: the two FaceForensics++ sets and the DeeperForensics-1.0 standard set. On FF++ C23, the reported accuracies ranged from 92.14% (ADDNet-3D) to 100.00% (Xception with frame-score averaging, as reported by X. Li et al., 2020), and on C40 from 89.29% (C3D) to 98.21% (STIL). The BO-selected SwinFusion++ reached 98.21% and 96.07%, 1.79 and 2.14 percentage points below the highest values; the fixed recipe was 2.14 and 3.57 points below. On the DeeperForensics-1.0 standard set, the reported accuracies ranged from 98.50% (C3D) to 100.00%, and SwinFusion++ (98.51%; fixed recipe 98.76%) lay within that range, near the ceiling. Celeb-DF v2 accuracies are not compared: this study’s test set is 86.20% fake, so calling every video fake would already score 86.20%, and the published test sets have other or unstated class balances.
[NEW] Under their own protocols, the published within-dataset results and those of SwinFusion++ therefore lie in the same high range on FaceForensics++ and near the ceiling on DeeperForensics-1.0; Celeb-DF v2 accuracies cannot be compared. Because no test videos, splits, or operating points are shared, the data support neither a claim that SwinFusion++ outperforms these established models nor the reverse.
[NEW] Answer to Research Question 2
[NEW] On the FaceForensics++ DeepFakes C23 and C40 subsets, Celeb-DF v2, and the DeeperForensics-1.0 construction, the BO-selected SwinFusion++ reached ROC-AUC of 0.9941 to 0.9983 and accuracy of 96.07% to 98.51% (fixed recipe 0.9878 to 0.9974 and 94.64% to 98.76%). It ranked videos far better than the Xception baseline of the preliminary study on FaceForensics++ and Celeb-DF v2 and similarly on DeeperForensics-1.0, a comparison limited by the different pipeline and, for the last two datasets, by different test populations. Against previously reported results for a wider set of established detectors, its FaceForensics++ ROC-AUC lay within the reported range on C23 and above it on C40, although almost all of these values are Tier B and not like-for-like; its accuracy on the balanced FaceForensics++ test sets was 1.79 to 2.14 percentage points below the highest Tier A values (fixed recipe 2.14 to 3.57); and on the DeeperForensics-1.0 standard set its accuracy lay within the reported range, near the ceiling. Because those results come from other splits and protocols, they place SwinFusion++ within the range of the listed methods on FaceForensics++ but cannot rank it against them.
[NEW] 

## New reference entries (in order)
[NEW] Afchar, D., Nozick, V., Yamagishi, J., &amp; Echizen, I. (2018). MesoNet: A compact facial video forgery detection network. In 2018 IEEE International Workshop on Information Forensics and Security (WIFS) (pp. 1–7). IEEE. https://doi.org/10.1109/WIFS.2018.8630761
[NEW] Bandos, A. I., Rockette, H. E., &amp; Gur, D. (2005). A permutation test sensitive to differences in areas for comparing ROC curves from a paired design. Statistics in Medicine, 24(18), 2873–2893. https://doi.org/10.1002/sim.2149
[NEW] Cao, J., Ma, C., Yao, T., Chen, S., Ding, S., &amp; Yang, X. (2022). End-to-end reconstruction-classification learning for face forgery detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4103–4112). https://doi.org/10.1109/CVPR52688.2022.00408
[NEW] Custodio, E. T., Degamo, M. K., Escueta, K. R. C., San Diego, D. A. E., &amp; Sarmiento, M. J. F. (2026). SwinFusion++: Face-aligned spatio-temporal Swin Transformer for deepfake detection [Unpublished manuscript]. College of Computer Studies and Systems, University of the East–Manila.
[NEW] He, K., Zhang, X., Ren, S., &amp; Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (pp. 770–778). https://doi.org/10.1109/CVPR.2016.90
[NEW] Hochreiter, S., &amp; Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735
[NEW] Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70.
[NEW] Khormali, A., &amp; Yuan, J.-S. (2022). DFDT: An end-to-end DeepFake detection framework using vision transformer. Applied Sciences, 12(6), Article 2953. https://doi.org/10.3390/app12062953
[NEW] Li, J., Xie, H., Li, J., Wang, Z., &amp; Zhang, Y. (2021). Frequency-aware discriminative feature learning supervised by single-center loss for face forgery detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 6454–6463). https://doi.org/10.1109/CVPR46437.2021.00639
[NEW] Li, L., Bao, J., Zhang, T., Yang, H., Chen, D., Wen, F., &amp; Guo, B. (2020). Face X-ray for more general face forgery detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 5000–5009). https://doi.org/10.1109/CVPR42600.2020.00505
[NEW] Li, X., Lang, Y., Chen, Y., Mao, X., He, Y., Wang, S., Xue, H., &amp; Lu, Q. (2020). Sharp multiple instance learning for DeepFake video detection. In Proceedings of the 28th ACM International Conference on Multimedia (pp. 1864–1872). Association for Computing Machinery. https://doi.org/10.1145/3394171.3414034
[NEW] Liu, Z., Luo, D., Wang, Y., Wang, L., Tai, Y., Wang, C., Li, J., Huang, F., &amp; Lu, T. (2020). TEINet: Towards an efficient architecture for video recognition. Proceedings of the AAAI Conference on Artificial Intelligence, 34(07), 11669–11676. https://doi.org/10.1609/aaai.v34i07.6836
[NEW] Neimark, D., Bar, O., Zohar, M., &amp; Asselmann, D. (2021). Video transformer network. In Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops (pp. 3156–3165). https://doi.org/10.1109/ICCVW54120.2021.00355
[NEW] Qi, H., Guo, Q., Juefei-Xu, F., Xie, X., Ma, L., Feng, W., Liu, Y., &amp; Zhao, J. (2020). DeepRhythm: Exposing DeepFakes with attentional visual heartbeat rhythms. In Proceedings of the 28th ACM International Conference on Multimedia (pp. 4318–4327). Association for Computing Machinery. https://doi.org/10.1145/3394171.3413707
[NEW] Qian, Y., Yin, G., Sheng, L., Chen, Z., &amp; Shao, J. (2020). Thinking in frequency: Face forgery detection by mining frequency-aware clues. In A. Vedaldi, H. Bischof, T. Brox, &amp; J.-M. Frahm (Eds.), Computer vision—ECCV 2020 (pp. 86–103). Springer. https://doi.org/10.1007/978-3-030-58610-2_6
[NEW] Sabir, E., Cheng, J., Jaiswal, A., AbdAlmageed, W., Masi, I., &amp; Natarajan, P. (2019). Recurrent convolutional strategies for face manipulation detection in videos. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops. https://openaccess.thecvf.com/content_CVPRW_2019/html/Media_Forensics/Sabir_Recurrent_Convolutional_Strategies_for_Face_Manipulation_Detection_in_Videos_CVPRW_2019_paper.html
[NEW] Tran, D., Bourdev, L., Fergus, R., Torresani, L., &amp; Paluri, M. (2015). Learning spatiotemporal features with 3D convolutional networks. In Proceedings of the IEEE International Conference on Computer Vision (pp. 4489–4497). https://doi.org/10.1109/ICCV.2015.510
[NEW] Wang, J., Wu, Z., Ouyang, W., Han, X., Chen, J., Jiang, Y.-G., &amp; Li, S.-N. (2022). M2TR: Multi-modal multi-scale transformers for deepfake detection. In Proceedings of the 2022 International Conference on Multimedia Retrieval (pp. 615–623). Association for Computing Machinery. https://doi.org/10.1145/3512527.3531415
[NEW] Wang, L., Xiong, Y., Wang, Z., Qiao, Y., Lin, D., Tang, X., &amp; Van Gool, L. (2016). Temporal segment networks: Towards good practices for deep action recognition. In B. Leibe, J. Matas, N. Sebe, &amp; M. Welling (Eds.), Computer vision—ECCV 2016 (pp. 20–36). Springer. https://doi.org/10.1007/978-3-319-46484-8_2
[NEW] Wang, P., Liu, K., Zhou, W., Zhou, H., Liu, H., Zhang, W., &amp; Yu, N. (2022). ADT: Anti-deepfake transformer. In ICASSP 2022 – 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (pp. 2899–2903). IEEE. https://doi.org/10.1109/ICASSP43922.2022.9746888
[NEW] Zhang, Y., Li, X., Liu, C., Shuai, B., Zhu, Y., Brattoli, B., Chen, H., Marsic, I., &amp; Tighe, J. (2021). VidTr: Video transformer without convolutions. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 13557–13567). https://doi.org/10.1109/ICCV48922.2021.01332
[NEW] Zhao, H., Zhou, W., Chen, D., Wei, T., Zhang, W., &amp; Yu, N. (2021). Multi-attentional deepfake detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 2185–2194). https://doi.org/10.1109/CVPR46437.2021.00222
[NEW] Zi, B., Chang, M., Chen, J., Ma, X., &amp; Jiang, Y.-G. (2020). WildDeepfake: A challenging real-world dataset for deepfake detection. In Proceedings of the 28th ACM International Conference on Multimedia (pp. 2382–2390). Association for Computing Machinery. https://doi.org/10.1145/3394171.3413769
[NEW] #### Figure B1. Hero Banner
[NEW] #### Figure B2. Deepfake 101
[NEW] #### Figure B3. SwinFusion++ Model
[NEW] #### Figure B4. Uploading Interface
[NEW] #### Figure B5. Video Resolution Standards
[NEW] #### Figure B6. Quick Start Guide
[NEW] #### Figure B7. Processing Interface
