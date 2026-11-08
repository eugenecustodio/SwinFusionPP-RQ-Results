# RQ2 REVIEW DRAFT (accepted view)
[NEW] ## Research Question 2: SwinFusion++ Compared With Established Baselines
[NEW] RQ2 asked: What is the performance of SwinFusion++ relative to established baselines when evaluated on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0? Three kinds of evidence are kept separate. The first is the held-out performance of SwinFusion++; following the analysis plan, the BO-selected configuration is reported with the fixed-recipe result alongside. The second is the Xception baseline that the authors trained in their preliminary study (Custodio et al., 2026), the only established baseline that this group has run on these datasets; it used an earlier pipeline, a single seed, and partly different test populations. The third is the results reported in the original publications of Xception (Chollet, 2017), I3D (Carreira &amp; Zisserman, 2017), STIL (Gu et al., 2021), FTCN (Zheng et al., 2021), TALL-Swin (Xu et al., 2023), and SFormer (Kingra et al., 2024). No baseline was retrained in the present study, so none of these comparisons is paired and none is tested; they are descriptive.
[NEW] Two features of this study’s test sets further limit comparison with published values. The Celeb-DF v2 test set contains 978 videos split by target identity rather than the official 518-video test list, and the DeeperForensics-1.0 test set is this study’s binary construction of unperturbed manipulated videos and their FaceForensics++ source originals, which differs from the published benchmark settings. Published results also come from their own splits, frame sampling, face crops, and operating points.
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
[NEW] SwinFusion++ therefore ranked videos far better than the preliminary-study Xception on FaceForensics++ C23 and C40 and much better on Celeb-DF v2, although on a different test population; on DeeperForensics-1.0 the two were similar. The two models differ in pipeline, training budget, pretraining, capacity, and number of seeds, so the comparison shows that SwinFusion++ exceeds this particular baseline, not that the architecture alone accounts for the gap.
[NEW] Comparison With Previously Reported Results
[NEW] Table 10 lists the within-dataset results reported in the original publications, with a comparability tier for each value. The full list of values considered, including those excluded from Table 10 and the reason for each exclusion, is given in Appendix J, Table J9.
[NEW] #### Table 10. Previously Reported Within-Dataset Results on the Benchmarks of This Study
[NEW] | Model | FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics-1.0 |
| --- | --- | --- | --- | --- |
[NEW] | This study: three-seed ensembles, thresholds frozen on source validation |
[NEW] | SwinFusion++ (BO-selected) | Acc 98.21; AUC 0.9964 | Acc 96.07; AUC 0.9941 | Acc 98.36; AUC 0.9983 | Acc 98.51; AUC 0.9954 |
[NEW] | SwinFusion++ (fixed recipe) | Acc 97.86; AUC 0.9942 | Acc 94.64; AUC 0.9878 | Acc 97.75; AUC 0.9951 | Acc 98.76; AUC 0.9974 |
[NEW] | Previously reported (each paper’s own split, frame sampling, and operating point) |
[NEW] | Xception | Acc 98.93–100.00 (A)ᵃᵇ | Acc 96.78–97.14 (A)ᵃᵇ | Acc 99.44 (A)ᵇ | Acc 100.00 (B)ᶜ |
[NEW] | I3D | Acc 92.86 (A)ᵇ | Acc 91.07 (A)ᵇ | Acc 99.23 (A)ᵇ | Acc 100.00 (B)ᶜ |
[NEW] | STIL | Acc 99.64 (A)ᵃ | Acc 98.21; AUC 0.9712 (A)ᵃ | Acc 99.78 (A)ᵃ | — |
[NEW] | FTCN with Temporal Transformer | Acc 99.1; AUC 0.998 (B)ᵉ | AUC 0.983 (B)ᵉ | — | AUC 1.000 (B)ᵉ |
[NEW] | TALL-Swin | Acc 98.65; AUC 0.9987 (B)ᵈ | Acc 92.82; AUC 0.9457 (B)ᵈ | — | — |
[NEW] | SFormer | Acc 98.50–99.90 (A)ᶠ | Acc 94.82–98.15 (A)ᶠ | Acc 95.04–99.10 (A)ᶠ | Acc 99.67–100.00 (A)ᶠ |
[NEW] Note. Values as printed in each paper, under its own protocol; none was tested. A: same dataset, compression, DeepFakes subset, and video level; B: otherwise or unstated. Xception values from ᵃ and ᵇ use frame-score averaging, and its FF++ ranges span two papers printing different values. Celeb-DF v2 test sets differ in size and fake share (here 978 videos, 86.20% fake); DeeperForensics-1.0 constructions differ. SFormer values were not re-verified. ᵃGu et al. (2021); ᵇX. Li et al. (2020); ᶜJiang et al. (2020); ᵈXu et al. (2023); ᵉZheng et al. (2021), supplement; ᶠKingra et al. (2024).
[NEW] In ROC-AUC, the BO-selected SwinFusion++ (0.9964; fixed recipe 0.9942) was close to the values reported for FTCN (0.998) and TALL-Swin (0.999) on FF++ C23. On C40, its ROC-AUC (0.9941; fixed recipe 0.9878) was higher than the values reported for FTCN (0.983), STIL (0.971), and TALL-Swin (0.946); the FTCN and TALL-Swin values are Tier B because their manipulation subsets are pooled or unstated, so the comparison is not like-for-like.
[NEW] Accuracy is compared only on the two FaceForensics++ test sets, where this study’s and the published test sets are balanced. There, the highest Tier A accuracies were 100.00% on C23 (Xception with frame-score averaging, as reported by X. Li et al., 2020) and 98.21% on C40 (STIL), against 98.21% and 96.07% for the BO-selected SwinFusion++, which is 1.79 and 2.14 percentage points lower; the fixed recipe was 2.14 and 3.57 points lower. Several reported values were lower than those of SwinFusion++, such as I3D at 92.86% and 91.07%. Celeb-DF v2 accuracies are not compared: this study’s test set is 86.20% fake, so calling every video fake would already score 86.20%, and the published test sets have other or unstated class balances. On DeeperForensics-1.0, every listed method was near the ceiling (reported accuracy 99.67% to 100.00% and FTCN ROC-AUC 1.000), as was SwinFusion++ (0.9954 and 98.51%; fixed recipe 0.9974 and 98.76%), on different constructions of the dataset.
[NEW] Under their own protocols, the published within-dataset results and those of SwinFusion++ therefore lie in the same high range on every benchmark. Because no test videos, splits, or operating points are shared, the data support neither a claim that SwinFusion++ outperforms these established models nor the reverse.
[NEW] Answer to Research Question 2
[NEW] On the FaceForensics++ DeepFakes C23 and C40 subsets, Celeb-DF v2, and the DeeperForensics-1.0 construction, the BO-selected SwinFusion++ reached ROC-AUC of 0.9941 to 0.9983 and accuracy of 96.07% to 98.51% (fixed recipe 0.9878 to 0.9974 and 94.64% to 98.76%). It ranked videos far better than the Xception baseline of the preliminary study on FaceForensics++ and Celeb-DF v2 and similarly on DeeperForensics-1.0, a comparison limited by the different pipeline and, for the last two datasets, by different test populations. Against results reported in the original publications, its ROC-AUC was close to or above the listed values on FaceForensics++, and its accuracy on the balanced FaceForensics++ test sets was 1.79 to 2.14 percentage points below the highest reported values (fixed recipe 2.14 to 3.57). Because those results come from other splits and protocols, they place SwinFusion++ within the range of established methods but cannot rank it against them.
[NEW] 

## New references
[NEW] Custodio, E. T., Degamo, M. K., Escueta, K. R. C., San Diego, D. A. E., &amp; Sarmiento, M. J. F. (2026). SwinFusion++: Face-aligned spatio-temporal Swin Transformer for deepfake detection [Unpublished manuscript]. College of Computer Studies and Systems, University of the East–Manila.
[NEW] Li, X., Lang, Y., Chen, Y., Mao, X., He, Y., Wang, S., Xue, H., &amp; Lu, Q. (2020). Sharp multiple instance learning for DeepFake video detection. In Proceedings of the 28th ACM International Conference on Multimedia (pp. 1864–1872). Association for Computing Machinery. https://doi.org/10.1145/3394171.3414034

## Appendix J heading and J9
[NEW] Supplementary Results for Research Questions 1 and 2
[NEW] This appendix reports the per-seed results, the supplementary analyses listed in Chapter 3 under Amendments after Test Scoring, and the predeclared horizontal-flip variant for RQ1 (Tables J1 to J8), and the full list of previously reported values considered for RQ2 (Table J9). None of these analyses was used to decide a hypothesis.
[NEW] #### Table J9. Previously Reported Values Considered for Research Question 2
[NEW] | Test set | Model | Metric | Value (as printed) | Unit | Subset | Source (paper, location) | Tier | In Table 10? | Reason if not | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | FF++ C23 | FTCN (+TT) | Accuracy | 99.1% | unstated | unstated or other | Zheng et al. (2021), Supplement Table 2 (supp. PDF p.2) | B | Yes |  | verified |
[NEW] | FF++ C23 | FTCN (+TT) | ROC-AUC | 0.998 | video | unstated or other | Zheng et al. (2021), Supplement Table 2 (supp. PDF p.2) | B | Yes |  | verified |
[NEW] | FF++ C23 | I3D | Accuracy | 92.86% | video | deepfakes | X. Li et al. (2020), Table 2 (PDF p.7) | A | Yes |  | verified |
[NEW] | FF++ C23 | SFormer | Accuracy | 98.5% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | Yes |  | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Accuracy | 99.9% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | Yes |  | as extracted (original not accessible) |
[NEW] | FF++ C23 | STIL | Accuracy | 99.64% | video | deepfakes | Gu et al. (2021), Table 1 (PDF p.5) | A | Yes |  | verified |
[NEW] | FF++ C23 | TALL-Swin | Accuracy | 98.65% | video | all four | Xu et al. (2023), Table 2 (PDF p.5) | B | Yes |  | verified |
[NEW] | FF++ C23 | TALL-Swin | ROC-AUC | 0.9987 | video | unstated or other | Xu et al. (2023), Table 2 (PDF p.5) | B | Yes |  | verified |
[NEW] | FF++ C23 | Xception (XN-avg) | Accuracy | 100% | video | deepfakes | X. Li et al. (2020), Table 2 (PDF p.7) | A | Yes |  | verified |
[NEW] | FF++ C23 | Xception (XN-avg) | Accuracy | 98.93% | video | deepfakes | Gu et al. (2021), Table 1 (PDF p.5) | A | Yes |  | verified |
[NEW] | FF++ C23 | FTCN | Accuracy | 97.9% | unstated | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | B | No | Secondary report; original value not located in Zheng et al. (2021) | as extracted (original not accessible) |
[NEW] | FF++ C23 | FTCN (+TT) | ROC-AUC | 0.999 | video | deepfakes | Zheng et al. (2021), Table 2 (PDF p.6) | A | No | Not a within-dataset result: unseen-manipulation test (trained on other FF++ manipulations) | verified |
[NEW] | FF++ C23 | FTCN (+TT, L x1) | ROC-AUC | 0.981 | video | deepfakes | Zheng et al. (2021), Table 8 (PDF p.8) | A | No | Not a within-dataset result: unseen-manipulation test (trained on other FF++ manipulations) | verified |
[NEW] | FF++ C23 | I3D | Accuracy | 92.86% | video | deepfakes | Gu et al. (2021), Table 1 (PDF p.5) | A | No | Duplicate of X. Li et al. (2020) (identical value) | verified |
[NEW] | FF++ C23 | I3D | Accuracy | 92.9% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C23 | I3D | Accuracy | 96.7% | clip | deepfakes | Zi et al. (2020), Table 4 (PDF p.8) | B | No | Clip-level unit | as extracted (not re-verified) |
[NEW] | FF++ C23 | SFormer | Accuracy | 84.16% | video | deepfakes | Kingra et al. (2024), Table 4 (PDF p.11) | A | No | Not a within-dataset result: cross-compression cell | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Accuracy | 99.33% | video | deepfakes | Kingra et al. (2024), Table 4 (PDF p.11) | A | No | Not a within-dataset result: cross-compression cell | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Accuracy | 99.9% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Precision | 99.32% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Precision | 100% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Recall | 97.67% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C23 | SFormer | Recall | 99.1% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C23 | STIL | Accuracy | 99.6% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C23 | Xception | Accuracy | 98.85% | frame | deepfakes | Rössler et al. (2019), Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C23 | Xception | Accuracy | 97.49% | frame | all four | Rössler et al. (2019), Appendix B, Table 5 (PDF p.13) | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C23 | Xception | Accuracy | 95.73% | frame | all four | Rössler et al. (2019), Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C23 | Xception | Accuracy | 99.62% | frame | deepfakes | Zi et al. (2020), Table 3 (PDF p.8) | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C23 | Xception | Accuracy | 95.73% | video | all four | Xu et al. (2023), Table 2 (PDF p.5) | B | No | Copied from earlier work; the C23 accuracy equals Rössler et al.’s frame-level value | verified |
[NEW] | FF++ C23 | Xception | ROC-AUC | 0.939 | video | deepfakes | Zheng et al. (2021), Table 2 (PDF p.6) | A | No | Not a within-dataset result: unseen-manipulation test (trained on other FF++ manipulations) | verified |
[NEW] | FF++ C23 | Xception | ROC-AUC | 0.997 | frame | deepfakes | Y. Li et al. (2020), Table 4 (PDF p.8) | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C23 | Xception | ROC-AUC | 0.963 | video | unstated or other | Xu et al. (2023), Table 2 (PDF p.5) | B | No | Copied from earlier work; the C23 accuracy equals Rössler et al.’s frame-level value | verified |
[NEW] | FF++ C23 | Xception (XN-avg) | Accuracy | 98.9% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C23 | XceptionNet (Rossler et al. 2019) | Accuracy | 96.4% | unstated | unstated or other | Zhang et al. (2024), Table 3 (PDF p.11), row "XceptionNet [4]" | B | No | Secondary report; setting or unit not stated | as extracted (not re-verified) |
[NEW] | FF++ C23 | XceptionNet (Rossler et al. 2019) | Accuracy | 86.9% | unstated | unstated or other | Zhang et al. (2024), Table 3 (PDF p.11), row "XceptionNet [4]" | B | No | Secondary report; setting or unit not stated | as extracted (not re-verified) |
[NEW] | FF++ C23 | XceptionNet (Rossler et al. 2019) | Accuracy | 90.3% | unstated | unstated or other | Zhang et al. (2024), Table 3 (PDF p.11), row "XceptionNet [4]" | B | No | Secondary report; setting or unit not stated | as extracted (not re-verified) |
[NEW] | FF++ C23 | XceptionNet (Rossler et al. 2019) | Accuracy | 80.7% | unstated | unstated or other | Zhang et al. (2024), Table 3 (PDF p.11), row "XceptionNet [4]" | B | No | Secondary report; setting or unit not stated | as extracted (not re-verified) |
[NEW] | FF++ C40 | FTCN (+TT) | ROC-AUC | 0.983 | video | unstated or other | Zheng et al. (2021), Supplement Table 2 (supp. PDF p.2) | B | Yes |  | verified |
[NEW] | FF++ C40 | I3D | Accuracy | 91.07% | video | deepfakes | X. Li et al. (2020), Table 2 (PDF p.7) | A | Yes |  | verified |
[NEW] | FF++ C40 | SFormer | Accuracy | 94.82% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | Yes |  | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Accuracy | 98.15% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | Yes |  | as extracted (original not accessible) |
[NEW] | FF++ C40 | STIL | Accuracy | 98.21% | video | deepfakes | Gu et al. (2021), Table 1 (PDF p.5) | A | Yes |  | verified |
[NEW] | FF++ C40 | STIL | ROC-AUC | 0.9712 | video | deepfakes | Gu et al. (2021), Table 3 (PDF p.6) | A | Yes |  | verified |
[NEW] | FF++ C40 | TALL-Swin | Accuracy | 92.82% | video | unstated or other | Xu et al. (2023), Table 2 (PDF p.5) | B | Yes |  | verified |
[NEW] | FF++ C40 | TALL-Swin | ROC-AUC | 0.9457 | video | unstated or other | Xu et al. (2023), Table 2 (PDF p.5) | B | Yes |  | verified |
[NEW] | FF++ C40 | Xception (XN-avg) | Accuracy | 97.14% | video | deepfakes | X. Li et al. (2020), Table 2 (PDF p.7) | A | Yes |  | verified |
[NEW] | FF++ C40 | Xception (XN-avg) | Accuracy | 96.78% | video | deepfakes | Gu et al. (2021), Table 1 (PDF p.5) | A | Yes |  | verified |
[NEW] | FF++ C40 | I3D | Accuracy | 91.07% | video | deepfakes | Gu et al. (2021), Table 1 (PDF p.5) | A | No | Duplicate of X. Li et al. (2020) (identical value) | verified |
[NEW] | FF++ C40 | I3D | Accuracy | 91.1% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C40 | I3D | Accuracy | 93.18% | clip | deepfakes | Zi et al. (2020), Table 4 (PDF p.8) | B | No | Clip-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | SFormer | Accuracy | 86.28% | video | deepfakes | Kingra et al. (2024), Table 4 (PDF p.11) | A | No | Not a within-dataset result: cross-compression cell | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Accuracy | 96.5% | video | deepfakes | Kingra et al. (2024), Table 4 (PDF p.11) | A | No | Not a within-dataset result: cross-compression cell | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Accuracy | 58.68% | video | deepfakes | Kingra et al. (2024), Table 4 (PDF p.11) | A | No | Not a within-dataset result: cross-compression cell | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Accuracy | 97.67% | video | deepfakes | Kingra et al. (2024), Table 4 (PDF p.11) | A | No | Not a within-dataset result: cross-compression cell | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Accuracy | 98.15% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Precision | 95.84% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Precision | 99.5% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Recall | 92.34% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C40 | SFormer | Recall | 94.3% | video | deepfakes | Kingra et al. (2024), Table 3 (PDF p.9) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | FF++ C40 | STIL | Accuracy | 98.2% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C40 | Xception | Accuracy | 94.28% | frame | deepfakes | Rössler et al. (2019), Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | Accuracy | 93.36% | frame | all four | Rössler et al. (2019), Appendix B, Table 5 (PDF p.13) | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | Accuracy | 81% | frame | all four | Rössler et al. (2019), Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | Accuracy | 90.25% | frame | deepfakes | Zi et al. (2020), Table 3 (PDF p.8) | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | Accuracy | 86.86% | video | all four | Xu et al. (2023), Table 2 (PDF p.5) | B | No | Copied from earlier work; the C23 accuracy equals Rössler et al.’s frame-level value | verified |
[NEW] | FF++ C40 | Xception | Accuracy | 93.46% | frame | deepfakes | Rössler et al. (2019), Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | Accuracy | 89.8% | frame | unstated or other | Rössler et al. (2019), Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | Accuracy | 92.72% | frame | unstated or other | Rössler et al. (2019), Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | ROC-AUC | 0.955 | frame | deepfakes | Y. Li et al. (2020), Table 4 (PDF p.8) | B | No | Frame-level unit | as extracted (not re-verified) |
[NEW] | FF++ C40 | Xception | ROC-AUC | 0.893 | video | unstated or other | Xu et al. (2023), Table 2 (PDF p.5) | B | No | Copied from earlier work; the C23 accuracy equals Rössler et al.’s frame-level value | verified |
[NEW] | FF++ C40 | Xception (XN-avg) | Accuracy | 96.8% | video | deepfakes | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | FF++ C40 | Xception-c40 | ROC-AUC | 0.955 | unstated | deepfakes | Gu et al. (2021), Table 3 (PDF p.6) | B | No | Frame-level value copied from Y. Li et al. (2020) | verified |
[NEW] | Celeb-DF v2 | I3D | Accuracy | 99.23% | video | unstated or other | X. Li et al. (2020), Table 1 (PDF p.7) | A | Yes |  | verified |
[NEW] | Celeb-DF v2 | SFormer | Accuracy | 95.04% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | Yes |  | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | SFormer | Accuracy | 99.1% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | Yes |  | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | STIL | Accuracy | 99.78% | video | unstated or other | Gu et al. (2021), Table 2 (PDF p.5) | A | Yes |  | verified |
[NEW] | Celeb-DF v2 | Xception (XN-avg) | Accuracy | 99.44% | video | unstated or other | Gu et al. (2021), Table 2 (PDF p.5) | A | No | Same value as X. Li et al. (2020), the earlier source | verified |
[NEW] | Celeb-DF v2 | Xception (XN-avg) | Accuracy | 99.44% | video | unstated or other | X. Li et al. (2020), Table 1 | A | Yes |  | verified (added; same value as Gu et al., 2021) |
[NEW] | Celeb-DF v2 | I3D | Accuracy | 99.23% | video | unstated or other | Gu et al. (2021), Table 2 (PDF p.5) | A | No | Duplicate of X. Li et al. (2020) (identical value) | verified |
[NEW] | Celeb-DF v2 | I3D | Accuracy | 99.2% | video | unstated or other | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | I3D | Accuracy | 92.28% | unstated | unstated or other | de Lima et al. (2020), via Saikia et al. (2022), Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | B | No | Secondary report; setting or unit not stated | as extracted (not re-verified) |
[NEW] | Celeb-DF v2 | I3D | ROC-AUC | 0.9759 | unstated | unstated or other | de Lima et al. (2020), via Saikia et al. (2022), Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | B | No | Secondary report; setting or unit not stated | as extracted (not re-verified) |
[NEW] | Celeb-DF v2 | SFormer | Accuracy | 99.1% | video | unstated or other | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | SFormer | Precision | 94.35% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | SFormer | Precision | 99.7% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | SFormer | Recall | 95.9% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | SFormer | Recall | 99% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | STIL | Accuracy | 99.8% | video | unstated or other | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | Celeb-DF v2 | Xception (XN-avg) | Accuracy | 99.4% | video | unstated or other | Kingra et al. (2024), Table 5 (PDF p.11) | A | No | Copy in a comparison table; listed under its original source | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | FTCN (+TT) | ROC-AUC | 1.000 | video | unstated or other | Zheng et al. (2021), Supplement Table 1 (supp. PDF p.2) | B | Yes |  | verified |
[NEW] | DeeperForensics-1.0 | I3D | Accuracy | 100% | video | unstated or other | Jiang et al. (2020), Table 5 (PDF p.9) | B | Yes |  | verified |
[NEW] | DeeperForensics-1.0 | SFormer | Accuracy | 99.67% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | Yes |  | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | SFormer | Accuracy | 100% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | Yes |  | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | Xception | Accuracy | 100% | video | unstated or other | Jiang et al. (2020), Table 5 (PDF p.9) | B | Yes |  | verified |
[NEW] | DeeperForensics-1.0 | I3D | Accuracy | 79.25% | video | unstated or other | Jiang et al. (2020), Table 4 / Table 6 col. 2 (PDF p.9-10) | A | No | Not a within-dataset result: DeeperForensics-1.0 hidden test set | verified |
[NEW] | DeeperForensics-1.0 | I3D | Accuracy | 90.75% | video | unstated or other | Jiang et al. (2020), Table 5 (PDF p.9) | A | No | Distortion (perturbed) test setting, not the standard test set | verified |
[NEW] | DeeperForensics-1.0 | I3D | Accuracy | 96.88% | video | unstated or other | Jiang et al. (2020), Table 5 (PDF p.9) | A | No | Distortion (perturbed) test setting, not the standard test set | verified |
[NEW] | DeeperForensics-1.0 | SFormer | Precision | 99.67% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | SFormer | Precision | 100% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | SFormer | Recall | 99.67% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | SFormer | Recall | 100% | video | unstated or other | Kingra et al. (2024), Table 2(a)/(b) (PDF p.8) | A | No | Precision and recall are not compared across studies | as extracted (original not accessible) |
[NEW] | DeeperForensics-1.0 | Xception | Accuracy | 77% | video | unstated or other | Jiang et al. (2020), Table 4 (PDF p.9) | A | No | Not a within-dataset result: DeeperForensics-1.0 hidden test set | verified |
[NEW] Note. Supplementary. All previously reported within-dataset values considered for RQ2, with the reason for each exclusion from Table 10; no value was dropped silently. Verified = checked against the original paper for this chapter; as extracted = taken from the study’s literature record without re-checking. Tiers as in Table 10. Values are not comparable with this study’s results except as described in the text.
[NEW] [IMAGE] 
[NEW] #### Figure J1. Within-Dataset ROC Curves of the Fixed-Recipe Models
[NEW] Note. Axes are truncated to false positive rates of 0–0.2 and true positive rates of 0.8–1.0, because every curve lies near the upper-left corner. Markers show operating points at the frozen source-validation threshold. Numbers are ROC-AUC (top to bottom: SwinFusion++, Swin-B, Video Swin-B). Abbreviations as in Figure 11.