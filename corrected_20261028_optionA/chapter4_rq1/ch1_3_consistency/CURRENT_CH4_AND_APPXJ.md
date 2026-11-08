# CURRENT Chapter 4 (accepted view, after the user removed the deviations table)
[NEW] # Chapter 4 – PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA
[NEW] This chapter presents, analyzes, and interprets the results of the experiments described in Chapter 3. It begins with the evaluation setting shared by all model comparisons and then addresses the research questions in turn. Each table and figure is introduced, its main values are stated, and their meaning for the research question is then interpreted.
[NEW] ## Evaluation Setting
[NEW] All model results in this chapter come from held-out test videos that were not used for training, model selection, threshold selection, or calibration. Swin-B, Video Swin-B, and SwinFusion++ were each trained with the same predefined non-BO recipe on each of the four within-dataset conditions (FaceForensics++ [FF++] DeepFakes at compression C23 and C40, Celeb-DF v2, and DeeperForensics-1.0), using three recorded seeds (260901, 260902, and 260903). SwinFusion++ was also trained with the training parameters selected by its condition-specific Bayesian optimization (BO) study. Each test video produced one prediction: the logits of its seven locked 16-frame clips of aligned 224 × 224 face crops, sampled at 2 frames per second, were averaged into one video logit. The three seeds of each model were combined into a three-seed ensemble by averaging their video logits.
[NEW] The operating threshold, chosen to maximize Youden’s J, and the calibration temperature were fitted on source-validation videos only and frozen before any test video was scored. Under cross-dataset transfer, the source-trained ensemble, threshold, and temperature were applied unchanged to the target dataset, and no target label was used for any decision. All results use the plain inference variant; the predeclared horizontal-flip variant is reported in Appendix J.
[NEW] Results are reported according to the analysis plan in Chapter 3. An interim decision to present the BO-selected configuration as primary was reverted to the approved plan; all comparisons under both regimens are reported. The statistical amendments made after test scoring, including the rank-based form of the permutation test and the regrouping of the comparison families, are described in Chapter 3 under Amendments after Test Scoring. The rank correction removed one significant difference favoring SwinFusion++ (within DeeperForensics-1.0, against Video Swin-B) and added two (Celeb-DF v2 → FF++ C23 and DeeperForensics-1.0 → Celeb-DF v2, both against Swin-B).
[NEW] Table 1 summarizes the four test sets, their dependence structure, and their coverage.
[NEW] #### Table 1. Test Sets, Dependence Structure, and Coverage
[NEW] | Test set | Videos (fake / real) | Clusters | Coverage | Preprocessing failures | Test videos sharing lineage with another condition | Strict lineage-free subset, by transfer source |
| --- | --- | --- | --- | --- | --- | --- |
[NEW] | FF++ C23 (HQ) | 280 (140 / 140) | 70 | 100.0% | 0 | 260 (92.9%) | from Celeb-DF v2: 280; from DeeperForensics-1.0: 20 |
[NEW] | FF++ C40 (LQ) | 280 (140 / 140) | 70 | 100.0% | 0 | 260 (92.9%) | from FF++ C23: 280; from Celeb-DF v2: 280; from DeeperForensics-1.0: 20 |
[NEW] | Celeb-DF v2 | 978 (843 / 135) | 54 (all fakes in 9) | 100.0% | 0 | 0 (0.0%) | from FF++ C23: 978; from DeeperForensics-1.0: 978 |
[NEW] | DeeperForensics-1.0 | 402 (201 / 201) | 201 | 100.0% | 0 | 382 (95.0%) | from FF++ C23: 60; from Celeb-DF v2: 402 |
[NEW] Note. Videos are the frozen test manifests; coverage and preprocessing failures were identical for every model, seed, and direction. Clusters are the resampling units. Celeb-DF v2 was split by target identity; all 843 fake videos lie in 9 identity clusters, so its intervals are approximate, and whether the swapped-in source identity was also held out could not be verified. Lineage counts follow the evaluation protocol. Strict subsets exclude target videos whose lineage appears in the source's training or validation data. Source-validation coverage: 279/280 (FF++ C23 and C40), 977/977 (Celeb-DF v2), 192/192 (DeeperForensics-1.0).
[NEW] All test videos were analyzed. Coverage was 100%, and no video ended in a preprocessing failure or an insufficient-evidence state, so no result in this chapter depends on how failed videos would have been counted. The test sets differ in their dependence structure. The FaceForensics++ test sets each contain 70 source clusters of four videos, and DeeperForensics-1.0 contains 201 real–fake source pairs. Celeb-DF v2 contains 978 videos, but all 843 of its fake videos lie in nine target-identity clusters, so its fake class rests on nine independent clusters and its intervals are approximate. Because the clusters are keyed by target identity, whether the identity of the swapped-in source face was also held out could not be verified from the archived records.
[NEW] Three features limit how cleanly the test sets are separated from model development. First, most FaceForensics++ and DeeperForensics-1.0 test videos share source lineage with another condition's training or validation videos: 260 of 280 in each FaceForensics++ set and 382 of 402 in DeeperForensics-1.0. The Celeb-DF v2 test set has no recorded cross-condition overlap. Table 1 gives these counts. Second, the preprocessing recovery rules were developed on 247 pooled training videos, 67 of which share lineage with held-out videos (15 physically identical). In addition, frames from 157 held-out videos were shown, without labels or scores, during face-quality review. No claim of untouched preprocessing selection is therefore made. Third, a metadata-only audit before training found that raw file metadata separated real from fake videos in Celeb-DF v2 (validation AUC 0.67) and DeeperForensics-1.0 (0.68). The models were then restricted to the rebuilt face-clip cache, and the repeated audit gave 0.50 on every dataset.
[NEW] Table 2 maps each analysis to its comparison family and to the section in which it is reported. Holm adjustment was applied within each family.
[NEW] #### Table 2. Analyses, Comparison Families, and Where They Are Reported
[NEW] | Analysis | Models (regimen) | Family (m) | Grouping status | Section |
| --- | --- | --- | --- | --- |
[NEW] | Within-dataset architecture comparison | SwinFusion++, Swin-B, Video Swin-B (all fixed recipe) | Within-dataset architecture family (8) | Regrouped after scoring; same decisions under the pre-scoring and pooled groupings | RQ1, in-distribution |
[NEW] | Frozen-transfer architecture comparison | SwinFusion++, Swin-B, Video Swin-B (all fixed recipe) | Frozen-transfer architecture family (18) | Regrouped after scoring; same decisions under the pre-scoring and pooled groupings | RQ1, frozen transfer; cited in RQ6 |
[NEW] | Threshold-dependent transfer metrics | SwinFusion++, Swin-B, Video Swin-B (all fixed recipe) | None (descriptive; supplementary paired intervals in Appendix J) | Not applicable | RQ1, threshold-dependent metrics |
[NEW] | Configured system, within datasets | BO-selected SwinFusion++ vs fixed-recipe Swin-B and Video Swin-B | Configured-system family, within (8) | Primary family before scoring (A-16); relabeled after scoring; same decisions | RQ1, configured system and optimization effect |
[NEW] | Configured system, frozen transfer | BO-selected SwinFusion++ vs fixed-recipe Swin-B and Video Swin-B | Configured-system family, transfer (18) | Primary family before scoring (A-16); relabeled after scoring; same decisions | RQ1, configured system and optimization effect |
[NEW] | Optimization effect, within datasets | BO-selected minus fixed-recipe SwinFusion++ | Optimization-effect family, within (4) | Separated after scoring; one decision depends on grouping (Celeb-DF v2: Holm p 0.021 vs 0.077) | RQ1, configured system and optimization effect |
[NEW] | Optimization effect, frozen transfer | BO-selected minus fixed-recipe SwinFusion++ | Optimization-effect family, transfer (9) | Regrouped after scoring; same decisions under the pre-scoring and pooled groupings | RQ1, configured system and optimization effect |
[NEW] | Matched controls | Fixed-recipe SwinFusion++ vs topology and capacity controls (FF++ C23 training) | Controls families (2 within; 6 transfer) | Unchanged since before scoring (A-16, A-18) | RQ4 |
[NEW] | Component ablations (Tier B) | One-change variants of BO-selected SwinFusion++, one seed, FF++ C23 | None (descriptive) | Not applicable | RQ4 |
[NEW] | Calibration and computational cost | All internal models | None (descriptive) | Not applicable | Section after RQ6 |
[NEW] Note. Every family applies Holm correction to rank-based cluster permutation p-values. The pre-scoring grouping is the one recorded on October 2, 2026 (A-16): the BO-selected comparisons formed the primary families, and the fixed-recipe comparisons were pooled with the optimization effect (12 within, 27 transfer). The pooled grouping combines all 26 architecture comparisons in one family; for the configured-system and optimization-effect rows, it pools each optimization-effect family with the matching configured-system family (12 within, 27 transfer).
[NEW] Two rules apply to every comparison in this chapter. First, ROC-AUC differences are paired: both models are evaluated on the same videos, and each bootstrap draw or permutation is applied to both. Intervals are 95% percentile intervals from 5,000 stratified cluster-bootstrap draws and are not adjusted for multiplicity, so the decision for each comparison is the Holm-adjusted p-value of the rank-based cluster permutation test; Holm-adjusted p-values below 0.005, which include the smallest attainable values, are written as &lt; 0.005. Second, the inference is conditional on the trained ensembles: it describes how the evaluated models perform on new test videos, not how a retrained model would perform. Threshold-independent results (ROC-AUC and PR-AUC) and threshold-dependent results (accuracy, precision, recall, specificity, and F1-score) are reported separately, and differences in threshold-dependent metrics are given only as supplementary paired intervals, without tests.
[NEW] ## Research Question 1: SwinFusion++ Compared With the Standalone Encoders
[NEW] RQ1 asked: To what extent does SwinFusion++ improve video-level deepfake detection performance compared with standalone Swin Transformer and standalone Video Swin Transformer under in-distribution and cross-dataset evaluation, in terms of Accuracy, Precision, Recall, F1-Score, and ROC-AUC? The principal evidence is the fixed-recipe comparison, in which all three models were trained with the identical recipe. The BO-selected SwinFusion++ is reported afterward as a configured system with unequal optimization effort.
[NEW] In-Distribution Performance Under the Fixed Recipe
[NEW] Table 3 presents the within-dataset results of the three fixed-recipe models.
[NEW] #### Table 3. Within-Dataset Performance of the Fixed-Recipe Models
[NEW] | Model | ROC-AUC [95% CI] | PR-AUC | Acc (%) | Prec (%) | Rec (%) | Spec (%) | F1 | FP | FN | Seed AUC mean ± SD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | FF++ C23 — 280 videos (140 fake), 70 clusters |
[NEW] | SwinFusion++ | 0.9942 [0.9834, 0.9999] | 0.9963 | 97.86 | 98.55 | 97.14 | 98.57 | 0.9784 | 2 | 4 | 0.9939 ± 0.0009 |
[NEW] | Swin-B | 0.9965 [0.9906, 0.9999] | 0.9973 | 97.86 | 97.18 | 98.57 | 97.14 | 0.9787 | 4 | 2 | 0.9965 ± 0.0007 |
[NEW] | Video Swin-B | 0.9951 [0.9856, 1.0000] | 0.9967 | 98.93 | 99.28 | 98.57 | 99.29 | 0.9892 | 1 | 2 | 0.9952 ± 0.0009 |
[NEW] | FF++ C40 — 280 videos (140 fake), 70 clusters |
[NEW] | SwinFusion++ | 0.9878 [0.9772, 0.9965] | 0.9896 | 94.64 | 93.71 | 95.71 | 93.57 | 0.9470 | 9 | 6 | 0.9860 ± 0.0017 |
[NEW] | Swin-B | 0.9883 [0.9777, 0.9960] | 0.9895 | 94.64 | 95.62 | 93.57 | 95.71 | 0.9458 | 6 | 9 | 0.9875 ± 0.0013 |
[NEW] | Video Swin-B | 0.9915 [0.9818, 0.9983] | 0.9933 | 95.71 | 95.71 | 95.71 | 95.71 | 0.9571 | 6 | 6 | 0.9910 ± 0.0022 |
[NEW] | Celeb-DF v2 — 978 videos (843 fake), 54 clusters; all fakes in 9 identity clusters |
[NEW] | SwinFusion++ | 0.9951 [0.9905, 0.9995] | 0.9992 | 97.75 | 99.28 | 98.10 | 95.56 | 0.9869 | 6 | 16 | 0.9939 ± 0.0022 |
[NEW] | Swin-B | 0.9958 [0.9925, 0.9990] | 0.9993 | 95.40 | 99.63 | 95.02 | 97.78 | 0.9727 | 3 | 42 | 0.9956 ± 0.0002 |
[NEW] | Video Swin-B | 0.9958 [0.9915, 0.9994] | 0.9993 | 98.26 | 99.28 | 98.70 | 95.56 | 0.9899 | 6 | 11 | 0.9954 ± 0.0003 |
[NEW] | DeeperForensics-1.0 — 402 videos (201 fake), 201 clusters |
[NEW] | SwinFusion++ | 0.9974 [0.9921, 1.0000] | 0.9980 | 98.76 | 100.00 | 97.51 | 100.00 | 0.9874 | 0 | 5 | 0.9971 ± 0.0011 |
[NEW] | Swin-B | 0.9966 [0.9892, 1.0000] | 0.9978 | 97.76 | 100.00 | 95.52 | 100.00 | 0.9771 | 0 | 9 | 0.9968 ± 0.0009 |
[NEW] | Video Swin-B | 0.9945 [0.9842, 0.9999] | 0.9966 | 97.01 | 99.48 | 94.53 | 99.50 | 0.9694 | 1 | 11 | 0.9944 ± 0.0006 |
[NEW] Note. Three-seed mean-logit ensembles, fixed recipe; thresholds frozen on source validation. ROC-AUC intervals: 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity. PR-AUC prevalence baselines: 0.500 (FF++, DFo), 0.862 (CDF). FPR = 1 − specificity; FNR = 1 − recall. Seed SD from three seeds is descriptive. Celeb-DF v2 intervals are approximate: all 843 fake videos lie in 9 identity clusters.
[NEW] All three models reached ROC-AUC between 0.9878 and 0.9974 on every test set. SwinFusion++ had the highest point estimate on DeeperForensics-1.0 (0.9974) and the lowest on FF++ C23 (0.9942) and C40 (0.9878), and on Celeb-DF v2 it was 0.0007 below both encoders. Accuracy on the FaceForensics++ test sets differed by at most three of 280 videos: SwinFusion++ matched Swin-B on C23 (97.86%) and C40 (94.64%), and Video Swin-B classified three more videos correctly on each. The differences were larger on the other two test sets. On Celeb-DF v2, SwinFusion++ classified 956 of 978 videos correctly, compared with 933 for Swin-B and 961 for Video Swin-B; on DeeperForensics-1.0, it classified 397 of 402 correctly, compared with 393 and 390. All three models therefore operated near the ceiling of the metric on every test set.
[NEW] Table 4 presents the paired ROC-AUC differences between SwinFusion++ and each encoder.
[NEW] #### Table 4. Paired ROC-AUC Differences Within Datasets, Fixed Recipe
[NEW] | Test set | Comparator | ΔAUC | 95% CI | Raw p | Holm p |
| --- | --- | --- | --- | --- | --- |
[NEW] | FF++ C23 | Swin-B | −0.0023 | [−0.0079, +0.0009] | 0.461 | 1.000 |
[NEW] |  | Video Swin-B | −0.0008 | [−0.0031, +0.0002] | 0.254 | 1.000 |
[NEW] | FF++ C40 | Swin-B | −0.0005 | [−0.0076, +0.0061] | 0.907 | 1.000 |
[NEW] |  | Video Swin-B | −0.0037 | [−0.0101, +0.0013] | 0.198 | 1.000 |
[NEW] | Celeb-DF v2 | Swin-B | −0.0007 | [−0.0048, +0.0026] | 0.925 | 1.000 |
[NEW] |  | Video Swin-B | −0.0007 | [−0.0033, +0.0012] | 0.774 | 1.000 |
[NEW] | DeeperForensics-1.0 | Swin-B | +0.0009 | [−0.0007, +0.0036] | 0.652 | 1.000 |
[NEW] |  | Video Swin-B | +0.0029 | [−0.0005, +0.0085] | 0.299 | 1.000 |
[NEW] Note. ΔAUC = fixed-recipe SwinFusion++ minus comparator (three-seed ensembles). Intervals: 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity. Raw p: two-sided rank-based cluster permutation test (5,000 permutations). Holm p: within-dataset architecture family (m = 8; file label RQ1_architecture). Celeb-DF v2 intervals are approximate: all 843 fake videos lie in 9 identity clusters.
[NEW] None of the eight differences was significant (all Holm-adjusted p = 1.000; raw p from 0.198 to 0.925). SwinFusion++ had the lower point estimate in six of the eight comparisons, and each paired 95% interval lay between −0.011 and +0.009 AUC. These intervals are incompatible with a large difference between SwinFusion++ and either encoder, but they do not establish equivalence: at this ceiling, the tests had less than 80% power to detect even the largest gain the ceiling allowed in seven of the eight comparisons (Appendix J, Table J6). In the supplementary paired intervals for threshold-dependent metrics (Table J2), SwinFusion++ had higher accuracy than Swin-B on Celeb-DF v2 (+2.35 percentage points [+0.08, +5.10]) and than Video Swin-B on DeeperForensics-1.0 (+1.74 percentage points [+0.50, +3.23]); the Celeb-DF v2 interval rests on nine fake-class clusters and is approximate. Because the corresponding ROC-AUC differences were not detectable, these gains are best read as differences in where the frozen thresholds fell, not as evidence of better separation of real and fake videos. Within each benchmark, therefore, no ROC-AUC difference between SwinFusion++ and either encoder was detectable, and all three models operated near the ceiling of the metric.
[NEW] Frozen Cross-Dataset Transfer Under the Fixed Recipe
[NEW] Figure 11 shows the ROC-AUC of each fixed-recipe model for every combination of training and test dataset, Table 5 gives the paired differences for the nine transfer directions, and Figure 12 shows all 26 paired differences of the fixed-recipe comparison together.
[NEW] [IMAGE] 
[NEW] #### Figure 11. Transfer ROC-AUC of the Fixed-Recipe Models by Training and Test Dataset
[NEW] Note. Three-seed mean-logit ensembles, plain variant. Rows are training datasets and columns are test datasets; the bold diagonal is in-distribution. C23 and C40 = FaceForensics++ DeepFakes HQ and LQ; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. — = not evaluated (C40 was not a transfer source). Colors do not distinguish values below 0.5.
[NEW] #### Table 5. Paired ROC-AUC Differences Under Frozen Transfer, Fixed Recipe
[NEW] | Direction | Comparator | SwinFusion++ AUC | Comparator AUC | ΔAUC | 95% CI | Raw p | Holm p |
| --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C40 | Swin-B | 0.9760 | 0.9739 | +0.0021 | [−0.0068, +0.0103] | 0.631 | 1.000 |
[NEW] |  | Video Swin-B | 0.9760 | 0.9746 | +0.0014 | [−0.0089, +0.0102] | 0.801 | 1.000 |
[NEW] | C23 → CDF | Swin-B | 0.8624 | 0.8680 | −0.0056 | [−0.0282, +0.0201] | 0.693 | 1.000 |
[NEW] |  | Video Swin-B | 0.8624 | 0.8676 | −0.0052 | [−0.0304, +0.0175] | 0.687 | 1.000 |
[NEW] | C23 → DFo | Swin-B | 0.8261 | 0.5678 | +0.2584 | [+0.2133, +0.3046] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.8261 | 0.8421 | −0.0159 | [−0.0407, +0.0090] | 0.214 | 1.000 |
[NEW] | CDF → C23 | Swin-B | 0.8958 | 0.8468 | +0.0490 | [+0.0200, +0.0770] | 0.002 | 0.018 |
[NEW] |  | Video Swin-B | 0.8958 | 0.9047 | −0.0089 | [−0.0320, +0.0154] | 0.466 | 1.000 |
[NEW] | CDF → C40 | Swin-B | 0.8384 | 0.7770 | +0.0614 | [+0.0339, +0.0918] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.8384 | 0.7630 | +0.0754 | [+0.0354, +0.1164] | &lt; 0.001 | &lt; 0.005 |
[NEW] | CDF → DFo | Swin-B | 0.7233 | 0.6012 | +0.1220 | [+0.0933, +0.1544] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.7233 | 0.6603 | +0.0630 | [+0.0302, +0.0991] | &lt; 0.001 | &lt; 0.005 |
[NEW] | DFo → C23 | Swin-B | 0.8127 | 0.6115 | +0.2012 | [+0.1569, +0.2492] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.8127 | 0.7676 | +0.0451 | [+0.0077, +0.0816] | 0.019 | 0.152 |
[NEW] | DFo → C40 | Swin-B | 0.7668 | 0.5964 | +0.1705 | [+0.1290, +0.2164] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.7668 | 0.6829 | +0.0840 | [+0.0439, +0.1229] | &lt; 0.001 | &lt; 0.005 |
[NEW] | DFo → CDF | Swin-B | 0.5879 | 0.4593 | +0.1286 | [+0.0626, +0.1864] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.5879 | 0.6001 | −0.0122 | [−0.0917, +0.0487] | 0.793 | 1.000 |
[NEW] Note. X → Y: trained on X, tested on Y with frozen source weights, thresholds and temperatures. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. ΔAUC = fixed-recipe SwinFusion++ minus comparator. Intervals: 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity. Raw p: two-sided rank-based cluster permutation test (5,000 permutations); Holm p: Holm-adjusted within the family; "&lt; 0.005" = Holm-adjusted p below 0.005, including the smallest attainable values. Family: frozen-transfer architecture (m = 18; file label RQ6_architecture). CDF-target intervals are approximate (9 fake-bearing clusters).
[NEW] [IMAGE] 
[NEW] #### Figure 12. Paired Differences in ROC-AUC Between Fixed-Recipe SwinFusion++ and Each Encoder
[NEW] Note. Points are ensemble ΔROC-AUC (SwinFusion++ minus comparator). Bars are unadjusted 95% percentile intervals from 5,000 stratified cluster-bootstrap draws. Filled markers denote Holm-adjusted p &lt; 0.05 (rank-based cluster permutation test). Because the intervals are unadjusted, one interval excludes 0 without significance (DFo → C23 vs Video Swin-B). Panels use different x-scales. Abbreviations as in Figure 11.
[NEW] Transfer lowered ROC-AUC for every model, to between 0.459 and 0.976. Against Swin-B, SwinFusion++ had a significantly higher ROC-AUC in seven of the nine directions, by +0.049 to +0.258 (Holm-adjusted p from &lt; 0.005 to 0.018). Against Video Swin-B, it was significantly higher in three directions, Celeb-DF v2 → FF++ C40 (+0.0754), Celeb-DF v2 → DeeperForensics-1.0 (+0.0630), and DeeperForensics-1.0 → FF++ C40 (+0.0840), all with Holm-adjusted p &lt; 0.005, and showed no detectable difference in the other six. SwinFusion++ was significantly lower than an encoder in none of the 18 comparisons. This is not evidence of non-inferiority: the five negative point estimates were not significant, but the widest interval reached −0.092 (DeeperForensics-1.0 → Celeb-DF v2, against Video Swin-B). One comparison, DeeperForensics-1.0 → FF++ C23 against Video Swin-B, had an interval that excluded zero (+0.0451 [+0.0077, +0.0816]) but was not significant after Holm adjustment (p = 0.152), so Figure 12 shows it with an open marker.
[NEW] The advantage depended on the training source. Trained on Celeb-DF v2 or DeeperForensics-1.0, SwinFusion++ was significantly better than Swin-B in all six directions and better than Video Swin-B in three. Trained on FF++ C23, it showed no detectable difference from either encoder on FF++ C40 or Celeb-DF v2, and its only significant difference from that source was against Swin-B on DeeperForensics-1.0. In that direction, Swin-B’s ROC-AUC fell to 0.5678 [0.5250, 0.6105], while the two models with a temporal stream kept 0.8261 (SwinFusion++) and 0.8421 (Video Swin-B). The same ordering appeared on the 60-video subset that shares no source lineage with the FF++ C23 training or validation data (seed means: Swin-B 0.5322, SwinFusion++ 0.7356, Video Swin-B 0.7874; no interval; Appendix J, Table J3). This pattern is consistent with temporal evidence transferring better than frame appearance in this direction. Swin-B and Video Swin-B also differ in pretraining and input handling, however, so the comparison does not isolate the cause.
[NEW] Three further points qualify the transfer results. First, ROC-AUC was modest in several directions, and from DeeperForensics-1.0 to Celeb-DF v2 all three models were near chance (0.4593 to 0.6001). Second, the two significant differences against Swin-B from DeeperForensics-1.0 to FF++ C23 and C40, and the one against Video Swin-B from DeeperForensics-1.0 to FF++ C40, could not be checked meaningfully on a lineage-free subset, because only 20 such test videos exist (Table 1; per-seed values in Table J3). Third, the individual seeds agreed with the ensembles: nine of the ten significant differences had the same sign in all nine pairings of individual seeds, and the tenth (Celeb-DF v2 → FF++ C40 against Video Swin-B) in eight of nine (Appendix J, Table J7). Under matched training, SwinFusion++ was therefore less degraded by transfer than Swin-B in most directions and than Video Swin-B in a minority of directions. Whether these differences can be attributed to TLBG-HCA, rather than to the combination of two encoders, is examined under RQ4 with the topology and capacity-matched controls.
[NEW] Threshold-Dependent Metrics Under Transfer
[NEW] RQ1 also concerns accuracy, precision, recall, and F1-score. Table 6 gives these metrics at the frozen source thresholds, and Figure 13 shows where each frozen threshold fell on the target ROC curve.
[NEW] #### Table 6. Threshold-Dependent Metrics Under Frozen Transfer, Fixed Recipe
[NEW] | Model | PR-AUC | Acc (%) | Prec (%) | Rec (%) | Spec (%) | F1 | TP | FP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C40 — 280 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.9796 | 88.57 | 97.37 | 79.29 | 97.86 | 0.8740 | 111 | 3 |
[NEW] | Swin-B | 0.9793 | 91.79 | 96.06 | 87.14 | 96.43 | 0.9139 | 122 | 5 |
[NEW] | Video Swin-B | 0.9786 | 91.79 | 97.56 | 85.71 | 97.86 | 0.9125 | 120 | 3 |
[NEW] | C23 → CDF — 978 videos, fake prevalence 86.20% |
[NEW] | SwinFusion++ | 0.9752 | 59.41 | 98.69 | 53.62 | 95.56 | 0.6949 | 452 | 6 |
[NEW] | Swin-B | 0.9762 | 67.48 | 97.81 | 63.70 | 91.11 | 0.7716 | 537 | 12 |
[NEW] | Video Swin-B | 0.9763 | 66.46 | 98.31 | 62.16 | 93.33 | 0.7616 | 524 | 9 |
[NEW] | C23 → DFo — 402 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.8255 | 51.49 | 87.50† | 3.48 | 99.50 | 0.0670 | 7 | 1 |
[NEW] | Swin-B | 0.6282 | 52.74 | 92.31 | 5.97 | 99.50 | 0.1121 | 12 | 1 |
[NEW] | Video Swin-B | 0.8542 | 57.96 | 97.06 | 16.42 | 99.50 | 0.2809 | 33 | 1 |
[NEW] | CDF → C23 — 280 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.9019 | 63.57 | 97.50 | 27.86 | 99.29 | 0.4333 | 39 | 1 |
[NEW] | Swin-B | 0.8684 | 60.36 | 100.00 | 20.71 | 100.00 | 0.3432 | 29 | 0 |
[NEW] | Video Swin-B | 0.9194 | 70.71 | 98.33 | 42.14 | 99.29 | 0.5900 | 59 | 1 |
[NEW] | CDF → C40 — 280 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.8461 | 52.14 | 100.00† | 4.29 | 100.00 | 0.0822 | 6 | 0 |
[NEW] | Swin-B | 0.7879 | 52.14 | 100.00† | 4.29 | 100.00 | 0.0822 | 6 | 0 |
[NEW] | Video Swin-B | 0.8024 | 52.86 | 100.00† | 5.71 | 100.00 | 0.1081 | 8 | 0 |
[NEW] | CDF → DFo — 402 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.7409 | 52.74 | 100.00 | 5.47 | 100.00 | 0.1038 | 11 | 0 |
[NEW] | Swin-B | 0.6671 | 51.00 | 100.00† | 1.99 | 100.00 | 0.0390 | 4 | 0 |
[NEW] | Video Swin-B | 0.7051 | 53.48 | 100.00 | 6.97 | 100.00 | 0.1302 | 14 | 0 |
[NEW] | DFo → C23 — 280 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.8060 | 50.71 | 100.00† | 1.43 | 100.00 | 0.0282 | 2 | 0 |
[NEW] | Swin-B | 0.6287 | 50.00 | — | 0.00 | 100.00 | — | 0 | 0 |
[NEW] | Video Swin-B | 0.7756 | 51.07 | 80.00† | 2.86 | 99.29 | 0.0552 | 4 | 1 |
[NEW] | DFo → C40 — 280 videos, fake prevalence 50.00% |
[NEW] | SwinFusion++ | 0.7671 | 50.36 | 100.00† | 0.71 | 100.00 | 0.0142 | 1 | 0 |
[NEW] | Swin-B | 0.6191 | 50.00 | — | 0.00 | 100.00 | — | 0 | 0 |
[NEW] | Video Swin-B | 0.6995 | 50.71 | 100.00† | 1.43 | 100.00 | 0.0282 | 2 | 0 |
[NEW] | DFo → CDF — 978 videos, fake prevalence 86.20% |
[NEW] | SwinFusion++ | 0.8877 | 14.21 | 100.00† | 0.47 | 100.00 | 0.0094 | 4 | 0 |
[NEW] | Swin-B | 0.8414 | 13.80 | — | 0.00 | 100.00 | — | 0 | 0 |
[NEW] | Video Swin-B | 0.9018 | 15.24 | 93.75 | 1.78 | 99.26 | 0.0349 | 15 | 1 |
[NEW] Note. Fixed-recipe three-seed ensembles at frozen source-validation thresholds; no target labels were used. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. Precision and F1: "—" = no positive calls (undefined); † = fewer than 10 positive calls. PR-AUC baseline equals the fake prevalence. Descriptive; no tests. Paired differences: Table J2.
[NEW] [IMAGE] 
[NEW] #### Figure 13. ROC Curves Under Frozen Cross-Dataset Transfer With the Frozen Operating Points
[NEW] Note. Fixed-recipe three-seed ensembles. Markers show each model's operating point at its frozen source-validation threshold. Numbers are ROC-AUC (top to bottom: SwinFusion++, Swin-B, Video Swin-B). The dashed diagonal marks chance. Markers near the origin overlap because almost no target videos were flagged as fake. Abbreviations as in Figure 11.
[NEW] At the frozen source thresholds, every model became conservative on the target data. Specificity stayed between 91.11% and 100.00%, while recall was below 64% in every direction except FF++ C23 → C40 (79.29% to 87.14%). From the Celeb-DF v2 and DeeperForensics-1.0 sources, no model flagged more than 60 test videos as fake, so accuracy in those directions mainly reflects the share of real videos. From DeeperForensics-1.0 to Celeb-DF v2, where 86.20% of the test videos are fake, accuracy was only 13.80% to 15.24%, close to the 13.80% obtained by calling every video real.
[NEW] SwinFusion++ did not have the highest accuracy, recall, or F1-score in any of the nine directions (point estimates; several margins were one or two videos). From FF++ C23, its high precision and specificity reflect that it made the fewest positive calls of the three models (114, 458, and 8 on C40, Celeb-DF v2, and DeeperForensics-1.0); from the other two sources, Swin-B made the fewest or tied for the fewest. From FF++ C23 to Celeb-DF v2, for example, it raised only six false alarms among 135 real videos (specificity 95.56%) but detected 53.62% of the fake videos, and its accuracy (59.41%) was lower than that of Swin-B (67.48%) and Video Swin-B (66.46%), although the three ROC-AUC values did not differ detectably. In the supplementary paired intervals (Table J2), its transfer accuracy was lower than an encoder’s in 6 of 18 comparisons (both encoders from FF++ C23 to C40 and to Celeb-DF v2; Video Swin-B from FF++ C23 to DeeperForensics-1.0 and from Celeb-DF v2 to C23) and higher in 2 (Swin-B from Celeb-DF v2 to C23 and to DeeperForensics-1.0).
[NEW] Figure 13 illustrates the split between ROC-AUC and accuracy. Outside FF++ C23 → C40, where ROC-AUC stayed near or above 0.8, the curves show that the ranking of fake above real videos was largely retained, but the frozen operating point sat in the low-recall part of the curve. Moving it would require target labels, which the frozen-transfer design excludes. Where ROC-AUC was near 0.5, as from DeeperForensics-1.0 to Celeb-DF v2, the ranking itself was close to chance, so the problem was not only the threshold. For an unseen dataset, the frozen screening label is therefore much less informative than the ranking results suggest, for all three models.
[NEW] Configured System and Optimization Effect
[NEW] Table 7 compares the BO-selected SwinFusion++ with the fixed-recipe encoders, and Table 8 compares it with the fixed-recipe SwinFusion++. Because only SwinFusion++ received a hyperparameter search, Table 7 measures configured-system performance with unequal optimization effort and is not evidence about the architecture itself.
[NEW] #### Table 7. BO-Selected SwinFusion++ Compared With the Fixed-Recipe Encoders
[NEW] | Condition | Comparator | SwinFusion++ (BO) AUC | Comparator AUC | ΔAUC | 95% CI | Raw p | Holm p |
| --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C23 | Swin-B | 0.9964 | 0.9965 | −0.0001 | [−0.0027, +0.0017] | 0.945 | 1.000 |
[NEW] |  | Video Swin-B | 0.9964 | 0.9951 | +0.0014 | [0.0000, +0.0037] | 0.189 | 1.000 |
[NEW] | C40 → C40 | Swin-B | 0.9941 | 0.9883 | +0.0058 | [+0.0010, +0.0124] | 0.022 | 0.178 |
[NEW] |  | Video Swin-B | 0.9941 | 0.9915 | +0.0026 | [−0.0026, +0.0090] | 0.485 | 1.000 |
[NEW] | CDF → CDF | Swin-B | 0.9983 | 0.9958 | +0.0024 | [+0.0002, +0.0057] | 0.071 | 0.500 |
[NEW] |  | Video Swin-B | 0.9983 | 0.9958 | +0.0024 | [+0.0001, +0.0058] | 0.204 | 1.000 |
[NEW] | DFo → DFo | Swin-B | 0.9954 | 0.9966 | −0.0012 | [−0.0041, +0.0007] | 0.531 | 1.000 |
[NEW] |  | Video Swin-B | 0.9954 | 0.9945 | +0.0008 | [−0.0030, +0.0050] | 0.774 | 1.000 |
[NEW] | C23 → C40 | Swin-B | 0.9862 | 0.9739 | +0.0123 | [+0.0048, +0.0211] | &lt; 0.001 | 0.010 |
[NEW] |  | Video Swin-B | 0.9862 | 0.9746 | +0.0116 | [+0.0040, +0.0214] | 0.001 | 0.015 |
[NEW] | C23 → CDF | Swin-B | 0.8785 | 0.8680 | +0.0105 | [−0.0090, +0.0315] | 0.268 | 1.000 |
[NEW] |  | Video Swin-B | 0.8785 | 0.8676 | +0.0109 | [−0.0086, +0.0298] | 0.366 | 1.000 |
[NEW] | C23 → DFo | Swin-B | 0.7316 | 0.5678 | +0.1638 | [+0.1220, +0.2096] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.7316 | 0.8421 | −0.1105 | [−0.1374, −0.0820] | &lt; 0.001 | &lt; 0.005 |
[NEW] | CDF → C23 | Swin-B | 0.8657 | 0.8468 | +0.0189 | [−0.0140, +0.0499] | 0.228 | 1.000 |
[NEW] |  | Video Swin-B | 0.8657 | 0.9047 | −0.0390 | [−0.0617, −0.0179] | &lt; 0.001 | 0.005 |
[NEW] | CDF → C40 | Swin-B | 0.7345 | 0.7770 | −0.0425 | [−0.0806, −0.0026] | 0.025 | 0.197 |
[NEW] |  | Video Swin-B | 0.7345 | 0.7630 | −0.0285 | [−0.0606, +0.0070] | 0.107 | 0.747 |
[NEW] | CDF → DFo | Swin-B | 0.6824 | 0.6012 | +0.0811 | [+0.0511, +0.1130] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.6824 | 0.6603 | +0.0221 | [−0.0104, +0.0573] | 0.189 | 1.000 |
[NEW] | DFo → C23 | Swin-B | 0.7236 | 0.6115 | +0.1121 | [+0.0724, +0.1563] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.7236 | 0.7676 | −0.0439 | [−0.0770, −0.0106] | 0.016 | 0.144 |
[NEW] | DFo → C40 | Swin-B | 0.7067 | 0.5964 | +0.1103 | [+0.0750, +0.1501] | &lt; 0.001 | &lt; 0.005 |
[NEW] |  | Video Swin-B | 0.7067 | 0.6829 | +0.0239 | [−0.0127, +0.0609] | 0.193 | 1.000 |
[NEW] | DFo → CDF | Swin-B | 0.5519 | 0.4593 | +0.0926 | [+0.0263, +0.1477] | 0.002 | 0.022 |
[NEW] |  | Video Swin-B | 0.5519 | 0.6001 | −0.0482 | [−0.1277, +0.0138] | 0.168 | 1.000 |
[NEW] Note. Configured system: BO-selected SwinFusion++ minus fixed-recipe comparator; optimization effort is unequal. X → X = within-dataset. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. Intervals: 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity. Raw p: two-sided rank-based cluster permutation test (5,000 permutations); Holm p: Holm-adjusted within the family; "&lt; 0.005" = Holm-adjusted p below 0.005, including the smallest attainable values. Families: configured system within (m = 8) and transfer (m = 18). CDF-target intervals are approximate.
[NEW] Within datasets, the BO-selected configuration did not differ significantly from either encoder in any of the eight comparisons, and its higher point estimates on FF++ C40 (0.9941) and Celeb-DF v2 (0.9983) are descriptive only. Under transfer, it was significantly better than Swin-B in six of the nine directions. Against Video Swin-B, it was significantly better only from FF++ C23 to C40 (+0.0116) and significantly worse from FF++ C23 to DeeperForensics-1.0 (−0.1105) and from Celeb-DF v2 to FF++ C23 (−0.0390).
[NEW] #### Table 8. Optimization Effect: BO-Selected Minus Fixed-Recipe SwinFusion++
[NEW] | Condition | BO AUC | Fixed AUC | ΔAUC | 95% CI | Raw p | Holm p |
| --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C23 | 0.9964 | 0.9942 | +0.0022 | [+0.0001, +0.0058] | 0.074 | 0.148 |
[NEW] | C40 → C40 | 0.9941 | 0.9878 | +0.0063 | [+0.0018, +0.0118] | &lt; 0.001 | &lt; 0.005 |
[NEW] | CDF → CDF | 0.9983 | 0.9951 | +0.0031 | [+0.0005, +0.0060] | 0.007 | 0.021 |
[NEW] | DFo → DFo | 0.9954 | 0.9974 | −0.0021 | [−0.0051, 0.0000] | 0.115 | 0.148 |
[NEW] | C23 → C40 | 0.9862 | 0.9760 | +0.0102 | [+0.0043, +0.0182] | &lt; 0.001 | &lt; 0.005 |
[NEW] | C23 → CDF | 0.8785 | 0.8624 | +0.0161 | [+0.0018, +0.0301] | 0.054 | 0.109 |
[NEW] | C23 → DFo | 0.7316 | 0.8261 | −0.0946 | [−0.1218, −0.0662] | &lt; 0.001 | &lt; 0.005 |
[NEW] | CDF → C23 | 0.8657 | 0.8958 | −0.0302 | [−0.0589, −0.0042] | 0.022 | 0.066 |
[NEW] | CDF → C40 | 0.7345 | 0.8384 | −0.1039 | [−0.1416, −0.0662] | &lt; 0.001 | &lt; 0.005 |
[NEW] | CDF → DFo | 0.6824 | 0.7233 | −0.0409 | [−0.0649, −0.0170] | 0.001 | &lt; 0.005 |
[NEW] | DFo → C23 | 0.7236 | 0.8127 | −0.0891 | [−0.1239, −0.0526] | &lt; 0.001 | &lt; 0.005 |
[NEW] | DFo → C40 | 0.7067 | 0.7668 | −0.0601 | [−0.0868, −0.0313] | &lt; 0.001 | &lt; 0.005 |
[NEW] | DFo → CDF | 0.5519 | 0.5879 | −0.0360 | [−0.0780, +0.0025] | 0.093 | 0.109 |
[NEW] Note. Optimization effect: BO-selected minus fixed-recipe SwinFusion++. X → X = within-dataset. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. Intervals: 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity. Raw p: two-sided rank-based cluster permutation test (5,000 permutations); Holm p: Holm-adjusted within the family; "&lt; 0.005" = Holm-adjusted p below 0.005, including the smallest attainable values. Families: within (m = 4) and transfer (m = 9). CDF → CDF is grouping-dependent: Holm p = 0.077 when pooled with the 8 architecture tests.
[NEW] Table 8 shows the source of this pattern. The BO-selected parameters significantly raised ROC-AUC within FF++ C40 (+0.0063) and Celeb-DF v2 (+0.0031) and from FF++ C23 to C40 (+0.0102), but they significantly lowered it in five transfer directions, by 0.041 to 0.104. The Celeb-DF v2 gain was significant in its own family (Holm-adjusted p = 0.021) but not when the families were pooled as recorded before scoring (p = 0.077). The pattern is consistent with the BO objective, source-validation ROC-AUC, fitting each training source more tightly at the expense of transfer. Two limitations apply: the searches used 12, 12, 8, and 8 trials, which limits how fully each search space was explored, and the objective was close to saturation, with best validation ROC-AUC between 0.9977 and 0.9994. The BO-selected configurations also differed from the fixed recipe in several training parameters at once, so the effect cannot be attributed to any single parameter.
[NEW] Answer to Research Question 1
[NEW] In distribution, under the principal fixed-recipe comparison, SwinFusion++ did not measurably improve on standalone Swin-B or Video Swin-B. All three models reached ROC-AUC of 0.988 to 0.997, no paired ROC-AUC difference was detectable, and each paired interval lay between −0.011 and +0.009 AUC. The threshold-dependent metrics were similarly close: accuracy differed by at most three videos on FaceForensics++, and precision and recall differed from those of either encoder by at most 2.0 and 3.1 percentage points. The supplementary accuracy and F1-score intervals excluded zero only on Celeb-DF v2 (against Swin-B) and DeeperForensics-1.0 (against Video Swin-B), both favoring SwinFusion++; because the ROC-AUC differences there were not detectable, these gains are best read as threshold placement rather than better ranking.
[NEW] Under frozen cross-dataset evaluation, SwinFusion++ had significantly higher ROC-AUC than Swin-B in seven of nine directions (by +0.049 to +0.258) and than Video Swin-B in three (by +0.063 to +0.084). It showed no detectable difference in the remaining directions and was significantly lower in none, although the widest interval reached −0.092. The differences came mainly from the Celeb-DF v2 and DeeperForensics-1.0 sources; from FF++ C23, only the difference from Swin-B on DeeperForensics-1.0 was detectable. At the frozen source thresholds, however, SwinFusion++ never had the highest transfer accuracy, recall, or F1-score (point estimates; several margins were one or two videos), and precision was 80% or higher for every model where it was defined, often on very few positive calls. In supplementary paired intervals, its transfer accuracy was lower than an encoder’s in 6 of 18 comparisons (both encoders from FF++ C23 to C40 and to Celeb-DF v2; Video Swin-B from FF++ C23 to DeeperForensics-1.0 and from Celeb-DF v2 to C23) and higher in 2 (Swin-B from Celeb-DF v2 to C23 and to DeeperForensics-1.0).
[NEW] The improvement that RQ1 asks about is therefore present in ranking performance under frozen transfer, in most directions against Swin-B and in three of nine against Video Swin-B. It was not detectable within datasets, and under transfer it did not carry over to threshold-dependent performance at the frozen source operating points. Relative to the fixed recipe, the BO-selected configuration significantly raised ROC-AUC within FF++ C40 and Celeb-DF v2 (the latter depending on the family grouping) and from FF++ C23 to C40, but significantly lowered it in five other transfer directions, consistent with tighter fitting to each training source. Whether the transfer differences are due to TLBG-HCA is examined under RQ4, and the verdict against the Chapter 3 criterion for a strong model is given under RQ6.

# CURRENT Appendix J
[NEW] #### APPENDIX J
[NEW] Supplementary Results for Research Question 1
[NEW] This appendix reports the per-seed results, the supplementary analyses listed in Chapter 3 under Amendments after Test Scoring, and the predeclared horizontal-flip variant. None of these analyses was used to decide a hypothesis.
[NEW] #### Table J1. Per-Seed ROC-AUC for Every Model, Regimen, and Test Condition
[NEW] | Training → test | Model | Seed 1 | Seed 2 | Seed 3 | Mean ± SD | Ensemble |
| --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C23 | SwinFusion++ | 0.9946 | 0.9941 | 0.9929 | 0.9939 ± 0.0009 | 0.9942 |
[NEW] |  | SwinFusion++ (BO) | 0.9970 | 0.9969 | 0.9959 | 0.9966 ± 0.0006 | 0.9964 |
[NEW] |  | Swin-B | 0.9957 | 0.9969 | 0.9968 | 0.9965 ± 0.0007 | 0.9965 |
[NEW] |  | Video Swin-B | 0.9954 | 0.9942 | 0.9959 | 0.9952 ± 0.0009 | 0.9951 |
[NEW] | C40 → C40 | SwinFusion++ | 0.9874 | 0.9841 | 0.9865 | 0.9860 ± 0.0017 | 0.9878 |
[NEW] |  | SwinFusion++ (BO) | 0.9928 | 0.9937 | 0.9904 | 0.9923 ± 0.0017 | 0.9941 |
[NEW] |  | Swin-B | 0.9879 | 0.9886 | 0.9861 | 0.9875 ± 0.0013 | 0.9883 |
[NEW] |  | Video Swin-B | 0.9931 | 0.9913 | 0.9886 | 0.9910 ± 0.0022 | 0.9915 |
[NEW] | CDF → CDF | SwinFusion++ | 0.9948 | 0.9913 | 0.9955 | 0.9939 ± 0.0022 | 0.9951 |
[NEW] |  | SwinFusion++ (BO) | 0.9982 | 0.9965 | 0.9976 | 0.9974 ± 0.0008 | 0.9983 |
[NEW] |  | Swin-B | 0.9958 | 0.9954 | 0.9958 | 0.9956 ± 0.0002 | 0.9958 |
[NEW] |  | Video Swin-B | 0.9956 | 0.9956 | 0.9951 | 0.9954 ± 0.0003 | 0.9958 |
[NEW] | DFo → DFo | SwinFusion++ | 0.9977 | 0.9959 | 0.9977 | 0.9971 ± 0.0011 | 0.9974 |
[NEW] |  | SwinFusion++ (BO) | 0.9969 | 0.9949 | 0.9938 | 0.9952 ± 0.0016 | 0.9954 |
[NEW] |  | Swin-B | 0.9960 | 0.9965 | 0.9977 | 0.9968 ± 0.0009 | 0.9966 |
[NEW] |  | Video Swin-B | 0.9936 | 0.9948 | 0.9947 | 0.9944 ± 0.0006 | 0.9945 |
[NEW] | C23 → C40 | SwinFusion++ | 0.9742 | 0.9743 | 0.9713 | 0.9733 ± 0.0017 | 0.9760 |
[NEW] |  | SwinFusion++ (BO) | 0.9853 | 0.9861 | 0.9836 | 0.9850 ± 0.0012 | 0.9862 |
[NEW] |  | Swin-B | 0.9646 | 0.9739 | 0.9755 | 0.9713 ± 0.0059 | 0.9739 |
[NEW] |  | Video Swin-B | 0.9769 | 0.9722 | 0.9733 | 0.9741 ± 0.0025 | 0.9746 |
[NEW] | C23 → CDF | SwinFusion++ | 0.8515 | 0.8641 | 0.8504 | 0.8553 ± 0.0076 | 0.8624 |
[NEW] |  | SwinFusion++ (BO) | 0.8698 | 0.8665 | 0.8743 | 0.8702 ± 0.0039 | 0.8785 |
[NEW] |  | Swin-B | 0.8557 | 0.8530 | 0.8768 | 0.8618 ± 0.0131 | 0.8680 |
[NEW] |  | Video Swin-B | 0.8671 | 0.8631 | 0.8678 | 0.8660 ± 0.0026 | 0.8676 |
[NEW] | C23 → DFo | SwinFusion++ | 0.8343 | 0.8221 | 0.7354 | 0.7973 ± 0.0539 | 0.8261 |
[NEW] |  | SwinFusion++ (BO) | 0.6856 | 0.6499 | 0.7550 | 0.6968 ± 0.0534 | 0.7316 |
[NEW] |  | Swin-B | 0.5893 | 0.5613 | 0.5552 | 0.5686 ± 0.0182 | 0.5678 |
[NEW] |  | Video Swin-B | 0.8628 | 0.8139 | 0.8371 | 0.8379 ± 0.0245 | 0.8421 |
[NEW] | CDF → C23 | SwinFusion++ | 0.8855 | 0.8944 | 0.8843 | 0.8881 ± 0.0055 | 0.8958 |
[NEW] |  | SwinFusion++ (BO) | 0.8708 | 0.8540 | 0.8741 | 0.8663 ± 0.0108 | 0.8657 |
[NEW] |  | Swin-B | 0.8556 | 0.8341 | 0.8435 | 0.8444 ± 0.0108 | 0.8468 |
[NEW] |  | Video Swin-B | 0.9178 | 0.8987 | 0.8823 | 0.8996 ± 0.0178 | 0.9047 |
[NEW] | CDF → C40 | SwinFusion++ | 0.8261 | 0.8386 | 0.8013 | 0.8220 ± 0.0190 | 0.8384 |
[NEW] |  | SwinFusion++ (BO) | 0.7145 | 0.7158 | 0.7545 | 0.7282 ± 0.0227 | 0.7345 |
[NEW] |  | Swin-B | 0.7809 | 0.7723 | 0.7708 | 0.7747 ± 0.0054 | 0.7770 |
[NEW] |  | Video Swin-B | 0.8080 | 0.7424 | 0.7040 | 0.7515 ± 0.0526 | 0.7630 |
[NEW] | CDF → DFo | SwinFusion++ | 0.7583 | 0.6999 | 0.6875 | 0.7153 ± 0.0378 | 0.7233 |
[NEW] |  | SwinFusion++ (BO) | 0.6571 | 0.6749 | 0.6861 | 0.6727 ± 0.0146 | 0.6824 |
[NEW] |  | Swin-B | 0.5844 | 0.5896 | 0.6172 | 0.5971 ± 0.0176 | 0.6012 |
[NEW] |  | Video Swin-B | 0.6646 | 0.6502 | 0.6361 | 0.6503 ± 0.0142 | 0.6603 |
[NEW] | DFo → C23 | SwinFusion++ | 0.8030 | 0.7633 | 0.7959 | 0.7874 ± 0.0212 | 0.8127 |
[NEW] |  | SwinFusion++ (BO) | 0.6289 | 0.6506 | 0.7248 | 0.6681 ± 0.0503 | 0.7236 |
[NEW] |  | Swin-B | 0.5679 | 0.6473 | 0.5759 | 0.5970 ± 0.0437 | 0.6115 |
[NEW] |  | Video Swin-B | 0.7761 | 0.7288 | 0.7629 | 0.7560 ± 0.0244 | 0.7676 |
[NEW] | DFo → C40 | SwinFusion++ | 0.7539 | 0.7319 | 0.7569 | 0.7476 ± 0.0137 | 0.7668 |
[NEW] |  | SwinFusion++ (BO) | 0.6409 | 0.6400 | 0.6988 | 0.6599 ± 0.0337 | 0.7067 |
[NEW] |  | Swin-B | 0.5579 | 0.6287 | 0.5653 | 0.5840 ± 0.0389 | 0.5964 |
[NEW] |  | Video Swin-B | 0.6985 | 0.6516 | 0.6751 | 0.6751 ± 0.0235 | 0.6829 |
[NEW] | DFo → CDF | SwinFusion++ | 0.5919 | 0.5672 | 0.5841 | 0.5811 ± 0.0126 | 0.5879 |
[NEW] |  | SwinFusion++ (BO) | 0.5652 | 0.5461 | 0.5485 | 0.5533 ± 0.0104 | 0.5519 |
[NEW] |  | Swin-B | 0.4398 | 0.4896 | 0.4341 | 0.4545 ± 0.0305 | 0.4593 |
[NEW] |  | Video Swin-B | 0.6043 | 0.5766 | 0.6036 | 0.5948 ± 0.0158 | 0.6001 |
[NEW] Note. Video-level ROC-AUC of each training seed (260901, 260902, 260903) and of the three-seed mean-logit ensemble. X → X = within-dataset. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. SD from three seeds is descriptive and imprecise. Seeds are not resampled or tested. Per-seed accuracy, precision, recall, specificity, and F1-score were also computed for every cell but are not tabulated; Chapter 4 reports the three-seed ensembles.
[NEW] #### Table J2. Supplementary Paired Differences in Threshold-Dependent Metrics, Fixed Recipe
[NEW] | Condition | Comparator | ΔAcc [95% CI] | ΔPrec [95% CI] | ΔRec [95% CI] | ΔF1 [95% CI] |
| --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C23 | Swin-B | 0.00 [−2.14, +1.79] | +1.37 [−1.45, +4.14] | −1.43 [−3.57, 0.00] | −0.0003 [−0.0217, +0.0174] |
[NEW] |  | Video Swin-B | −1.07 [−2.50, 0.00] | −0.73 [−2.19, 0.00] | −1.43 [−3.57, 0.00] | −0.0108 [−0.0250, 0.0000] |
[NEW] | C40 → C40 | Swin-B | 0.00 [−2.14, +2.14] | −1.91 [−5.39, +1.41] | +2.14 [−1.43, +5.71] | +0.0011 [−0.0188, +0.0219] |
[NEW] |  | Video Swin-B | −1.07 [−3.21, +1.07] | −2.01 [−4.99, +0.73] | 0.00 [−2.86, +2.86] | −0.0101 [−0.0312, +0.0109] |
[NEW] | CDF → CDF | Swin-B | +2.35 [+0.08, +5.10] | −0.35 [−0.78, +0.25] | +3.08 [+0.59, +5.99] | +0.0142 [+0.0005, +0.0318] |
[NEW] |  | Video Swin-B | −0.51 [−1.78, +0.25] | 0.00 [−0.33, +0.40] | −0.59 [−2.07, +0.41] | −0.0030 [−0.0106, +0.0014] |
[NEW] | DFo → DFo | Swin-B | +1.00 [0.00, +2.24] | 0.00 [0.00, 0.00] | +1.99 [0.00, +4.48] | +0.0103 [0.0000, +0.0235] |
[NEW] |  | Video Swin-B | +1.74 [+0.50, +3.23] | +0.52 [0.00, +1.58] | +2.99 [+0.50, +5.97] | +0.0180 [+0.0050, +0.0338] |
[NEW] | C23 → C40 | Swin-B | −3.21 [−6.07, −0.36] | +1.31 [−2.60, +5.11] | −7.86 [−13.57, −2.14] | −0.0398 [−0.0751, −0.0053] |
[NEW] |  | Video Swin-B | −3.21 [−5.36, −1.07] | −0.19 [−2.64, +2.25] | −6.43 [−10.71, −2.86] | −0.0385 [−0.0656, −0.0137] |
[NEW] | C23 → CDF | Swin-B | −8.08 [−13.53, −1.78] | +0.88 [−0.09, +2.68] | −10.08 [−16.44, −2.90] | −0.0767 [−0.1340, −0.0198] |
[NEW] |  | Video Swin-B | −7.06 [−13.22, −1.17] | +0.38 [−0.57, +1.48] | −8.54 [−15.96, −1.67] | −0.0668 [−0.1446, −0.0110] |
[NEW] | C23 → DFo | Swin-B | −1.24 [−2.74, +0.25] | n.e. | −2.49 [−5.47, +0.50] | −0.0452 [−0.0978, +0.0083] |
[NEW] |  | Video Swin-B | −6.47 [−8.71, −4.23] | n.e. | −12.94 [−17.41, −8.46] | −0.2139 [−0.2826, −0.1441] |
[NEW] | CDF → C23 | Swin-B | +3.21 [+1.07, +5.71] | −2.50 [−7.89, 0.00] | +7.14 [+2.86, +12.14] | +0.0901 [+0.0352, +0.1535] |
[NEW] |  | Video Swin-B | −7.14 [−10.36, −4.29] | −0.83 [−6.91, +4.48] | −14.29 [−20.00, −9.29] | −0.1567 [−0.2208, −0.0972] |
[NEW] | CDF → C40 | Swin-B | 0.00 [−1.79, +1.79] | n.e. | 0.00 [−3.57, +3.57] | 0.0000 [−0.0635, +0.0652] |
[NEW] |  | Video Swin-B | −0.71 [−2.14, +0.71] | n.e. | −1.43 [−4.29, +1.43] | −0.0259 [−0.0778, +0.0252] |
[NEW] | CDF → DFo | Swin-B | +1.74 [+0.50, +3.23] | n.e. | +3.48 [+1.00, +6.47] | +0.0647 [+0.0195, +0.1126] |
[NEW] |  | Video Swin-B | −0.75 [−1.74, 0.00] | 0.00 [0.00, 0.00] | −1.49 [−3.48, 0.00] | −0.0265 [−0.0606, 0.0000] |
[NEW] | DFo → C23 | Swin-B | +0.71 [0.00, +1.79] | n.e. | +1.43 [0.00, +3.57] | n.e. |
[NEW] |  | Video Swin-B | −0.36 [−1.43, +0.71] | n.e. | −1.43 [−3.57, 0.00] | −0.0270 [−0.0674, +0.0004] |
[NEW] | DFo → C40 | Swin-B | +0.36 [0.00, +1.07] | n.e. | +0.71 [0.00, +2.14] | n.e. |
[NEW] |  | Video Swin-B | −0.36 [−1.07, 0.00] | n.e. | −0.71 [−2.14, 0.00] | −0.0140 [−0.0420, 0.0000] |
[NEW] | DFo → CDF | Swin-B | +0.41 [0.00, +0.90] | n.e. | +0.47 [0.00, +1.08] | n.e. |
[NEW] |  | Video Swin-B | −1.02 [−2.61, +0.35] | n.e. | −1.30 [−3.11, +0.33] | −0.0255 [−0.0602, +0.0066] |
[NEW] Note. Supplementary, post hoc. Fixed-recipe SwinFusion++ minus comparator at frozen thresholds; accuracy, precision and recall in percentage points. Paired 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity; no p-values. n.e. = not estimable (precision: a model made fewer than 10 positive calls; F1: a model made no positive calls). X → X = within-dataset. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. CDF intervals are approximate (9 fake-bearing clusters).
[NEW] #### Table J3. ROC-AUC on the Strict Lineage-Free Subsets, by Seed
[NEW] | Direction (n) | Model | Seed 1 | Seed 2 | Seed 3 | Mean |
| --- | --- | --- | --- | --- | --- |
[NEW] | C23 → DFo (n = 60) | SwinFusion++ | 0.7494 | 0.8000 | 0.6572 | 0.7356 |
[NEW] |  | SwinFusion++ (BO) | 0.6000 | 0.5939 | 0.6772 | 0.6237 |
[NEW] |  | Swin-B | 0.5733 | 0.5072 | 0.5161 | 0.5322 |
[NEW] |  | Video Swin-B | 0.8089 | 0.7750 | 0.7783 | 0.7874 |
[NEW] | DFo → C23 (n = 20) | SwinFusion++ | 0.7250 | 0.6350 | 0.7100 | 0.6900 |
[NEW] |  | SwinFusion++ (BO) | 0.5550 | 0.6650 | 0.7300 | 0.6500 |
[NEW] |  | Swin-B | 0.4600 | 0.6250 | 0.4150 | 0.5000 |
[NEW] |  | Video Swin-B | 0.7900 | 0.6500 | 0.7100 | 0.7167 |
[NEW] | DFo → C40 (n = 20) | SwinFusion++ | 0.6500 | 0.6300 | 0.7000 | 0.6600 |
[NEW] |  | SwinFusion++ (BO) | 0.6950 | 0.6650 | 0.7500 | 0.7033 |
[NEW] |  | Swin-B | 0.4900 | 0.6900 | 0.4900 | 0.5567 |
[NEW] |  | Video Swin-B | 0.6300 | 0.5850 | 0.5500 | 0.5883 |
[NEW] Note. Strict lineage-free subsets: target test videos whose lineage never appears in the source training or validation split. Per-seed ROC-AUC only; no ensemble, interval or test. Other directions are lineage-free on the full test set. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0.
[NEW] #### Table J4. Plain and Horizontal-Flip ROC-AUC for All Models
[NEW] | Condition | SwinFusion++ plain | SwinFusion++ TTA | Swin-B plain | Swin-B TTA | Video Swin-B plain | Video Swin-B TTA | SwinFusion++ (BO) plain | SwinFusion++ (BO) TTA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → C23 | 0.9942 | 0.9946 | 0.9965 | 0.9974 | 0.9951 | 0.9960 | 0.9964 | 0.9965 |
[NEW] | C40 → C40 | 0.9878 | 0.9881 | 0.9883 | 0.9884 | 0.9915 | 0.9916 | 0.9941 | 0.9937 |
[NEW] | CDF → CDF | 0.9951 | 0.9957 | 0.9958 | 0.9962 | 0.9958 | 0.9965 | 0.9983 | 0.9983 |
[NEW] | DFo → DFo | 0.9974 | 0.9976 | 0.9966 | 0.9966 | 0.9945 | 0.9944 | 0.9954 | 0.9956 |
[NEW] | C23 → C40 | 0.9760 | 0.9762 | 0.9739 | 0.9747 | 0.9746 | 0.9749 | 0.9862 | 0.9855 |
[NEW] | C23 → CDF | 0.8624 | 0.8660 | 0.8680 | 0.8693 | 0.8676 | 0.8755 | 0.8785 | 0.8847 |
[NEW] | C23 → DFo | 0.8261 | 0.8279 | 0.5678 | 0.5708 | 0.8421 | 0.8490 | 0.7316 | 0.7338 |
[NEW] | CDF → C23 | 0.8958 | 0.8946 | 0.8468 | 0.8456 | 0.9047 | 0.9012 | 0.8657 | 0.8665 |
[NEW] | CDF → C40 | 0.8384 | 0.8402 | 0.7770 | 0.7804 | 0.7630 | 0.7685 | 0.7345 | 0.7360 |
[NEW] | CDF → DFo | 0.7233 | 0.7227 | 0.6012 | 0.5971 | 0.6603 | 0.6610 | 0.6824 | 0.6827 |
[NEW] | DFo → C23 | 0.8127 | 0.8133 | 0.6115 | 0.6108 | 0.7676 | 0.7682 | 0.7236 | 0.7268 |
[NEW] | DFo → C40 | 0.7668 | 0.7698 | 0.5964 | 0.5997 | 0.6829 | 0.6863 | 0.7067 | 0.7085 |
[NEW] | DFo → CDF | 0.5879 | 0.5872 | 0.4593 | 0.4609 | 0.6001 | 0.5968 | 0.5519 | 0.5537 |
[NEW] Note. Ensemble ROC-AUC without (plain) and with the predeclared horizontal-flip test-time augmentation (TTA), for all models. Plain values are used throughout Chapter 4. TTA values are from the package ensemble file (raw TTA predictions were not available for re-computation). X → X = within-dataset. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0.
[NEW] #### Table J5. Original Raw-Logit and Corrected Rank-Based Permutation Tests
[NEW] | Family | Comparison | ΔAUC | Raw-logit p | Holm (original) | Rank p | Holm (rank) | Decision changed? |
| --- | --- | --- | --- | --- | --- | --- | --- |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Swin-B, C23 → C23 | −0.0023 | 0.400 | 1.000 | 0.461 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Video Swin-B, C23 → C23 | −0.0008 | 1.000 | 1.000 | 0.254 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Swin-B, C40 → C40 | −0.0005 | 0.944 | 1.000 | 0.907 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Video Swin-B, C40 → C40 | −0.0037 | 0.189 | 1.000 | 0.198 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Swin-B, CDF → CDF | −0.0007 | 0.874 | 1.000 | 0.925 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Video Swin-B, CDF → CDF | −0.0007 | 0.850 | 1.000 | 0.774 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Swin-B, DFo → DFo | +0.0009 | 1.000 | 1.000 | 0.652 | 1.000 | No |
[NEW] | Architecture, within (m = 8) | SwinFusion++ vs Video Swin-B, DFo → DFo | +0.0029 | &lt; 0.001 | &lt; 0.005 | 0.299 | 1.000 | Yes |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, C23 → C40 | +0.0021 | 0.829 | 1.000 | 0.631 | 1.000 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, C23 → C40 | +0.0014 | 0.948 | 1.000 | 0.801 | 1.000 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, C23 → CDF | −0.0056 | 0.863 | 1.000 | 0.693 | 1.000 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, C23 → CDF | −0.0052 | 0.877 | 1.000 | 0.687 | 1.000 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, C23 → DFo | +0.2584 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, C23 → DFo | −0.0159 | 0.345 | 1.000 | 0.214 | 1.000 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, CDF → C23 | +0.0490 | 0.034 | 0.342 | 0.002 | 0.018 | Yes |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, CDF → C23 | −0.0089 | 0.450 | 1.000 | 0.466 | 1.000 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, CDF → C40 | +0.0614 | 0.002 | 0.020 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, CDF → C40 | +0.0754 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, CDF → DFo | +0.1220 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, CDF → DFo | +0.0630 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, DFo → C23 | +0.2012 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, DFo → C23 | +0.0451 | 0.056 | 0.502 | 0.019 | 0.152 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, DFo → C40 | +0.1705 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, DFo → C40 | +0.0840 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Swin-B, DFo → CDF | +0.1286 | 0.316 | 1.000 | &lt; 0.001 | &lt; 0.005 | Yes |
[NEW] | Architecture, transfer (m = 18) | SwinFusion++ vs Video Swin-B, DFo → CDF | −0.0122 | 0.896 | 1.000 | 0.793 | 1.000 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Swin-B, C23 → C23 | −0.0001 | 1.000 | 1.000 | 0.945 | 1.000 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Video Swin-B, C23 → C23 | +0.0014 | 1.000 | 1.000 | 0.189 | 1.000 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Swin-B, C40 → C40 | +0.0058 | 0.150 | 1.000 | 0.022 | 0.178 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Video Swin-B, C40 → C40 | +0.0026 | 0.337 | 1.000 | 0.485 | 1.000 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Swin-B, CDF → CDF | +0.0024 | 0.632 | 1.000 | 0.071 | 0.500 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Video Swin-B, CDF → CDF | +0.0024 | 0.903 | 1.000 | 0.204 | 1.000 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Swin-B, DFo → DFo | −0.0012 | 0.998 | 1.000 | 0.531 | 1.000 | No |
[NEW] | Configured system, within (m = 8) | SwinFusion++ (BO) vs Video Swin-B, DFo → DFo | +0.0008 | 0.762 | 1.000 | 0.774 | 1.000 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, C23 → C40 | +0.0123 | 0.332 | 1.000 | &lt; 0.001 | 0.010 | Yes |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, C23 → C40 | +0.0116 | 0.059 | 0.586 | 0.001 | 0.015 | Yes |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, C23 → CDF | +0.0105 | 0.766 | 1.000 | 0.268 | 1.000 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, C23 → CDF | +0.0109 | 0.370 | 1.000 | 0.366 | 1.000 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, C23 → DFo | +0.1638 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, C23 → DFo | −0.1105 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, CDF → C23 | +0.0189 | 0.359 | 1.000 | 0.228 | 1.000 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, CDF → C23 | −0.0390 | 0.013 | 0.161 | &lt; 0.001 | 0.005 | Yes |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, CDF → C40 | −0.0425 | 0.012 | 0.153 | 0.025 | 0.197 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, CDF → C40 | −0.0285 | 0.247 | 1.000 | 0.107 | 0.747 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, CDF → DFo | +0.0811 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, CDF → DFo | +0.0221 | 0.261 | 1.000 | 0.189 | 1.000 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, DFo → C23 | +0.1121 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, DFo → C23 | −0.0439 | 0.048 | 0.523 | 0.016 | 0.144 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, DFo → C40 | +0.1103 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, DFo → C40 | +0.0239 | 0.281 | 1.000 | 0.193 | 1.000 | No |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Swin-B, DFo → CDF | +0.0926 | 0.499 | 1.000 | 0.002 | 0.022 | Yes |
[NEW] | Configured system, transfer (m = 18) | SwinFusion++ (BO) vs Video Swin-B, DFo → CDF | −0.0482 | 0.302 | 1.000 | 0.168 | 1.000 | No |
[NEW] | Optimization effect, within (m = 4) | SwinFusion++ (BO) vs SwinFusion++, C23 → C23 | +0.0022 | 0.999 | 1.000 | 0.074 | 0.148 | No |
[NEW] | Optimization effect, within (m = 4) | SwinFusion++ (BO) vs SwinFusion++, C40 → C40 | +0.0063 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Optimization effect, within (m = 4) | SwinFusion++ (BO) vs SwinFusion++, CDF → CDF | +0.0031 | 0.992 | 1.000 | 0.007 | 0.021 | Yes |
[NEW] | Optimization effect, within (m = 4) | SwinFusion++ (BO) vs SwinFusion++, DFo → DFo | −0.0021 | 0.498 | 1.000 | 0.115 | 0.148 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, C23 → C40 | +0.0102 | 0.283 | 0.850 | &lt; 0.001 | &lt; 0.005 | Yes |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, C23 → CDF | +0.0161 | 0.314 | 0.850 | 0.054 | 0.109 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, C23 → DFo | −0.0946 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, CDF → C23 | −0.0302 | 0.068 | 0.271 | 0.022 | 0.066 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, CDF → C40 | −0.1039 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, CDF → DFo | −0.0409 | 0.022 | 0.110 | 0.001 | &lt; 0.005 | Yes |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, DFo → C23 | −0.0891 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, DFo → C40 | −0.0601 | &lt; 0.001 | &lt; 0.005 | &lt; 0.001 | &lt; 0.005 | No |
[NEW] | Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, DFo → CDF | −0.0360 | 0.712 | 0.850 | 0.093 | 0.109 | No |
[NEW] Note. Original predeclared test: cluster permutation exchanging raw ensemble logits. Corrected test: cluster-level rank-based adaptation of Bandos et al. (2005). Both use 5,000 permutations and Holm adjustment within the six final families; ΔAUC is identical. Decision changed = significance at 0.05 after Holm adjustment differs. X → X = within-dataset. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. Raw p below 0.001 is written &lt; 0.001 and Holm p below 0.005 as &lt; 0.005.
[NEW] #### Table J6. Within-Dataset Sensitivity: Detectable Difference and Available Headroom
[NEW] | Test set | Comparator | SE(ΔAUC) | MDD (α = 0.05) | MDD (α = 0.05/8) | Headroom |
| --- | --- | --- | --- | --- | --- |
[NEW] | FF++ C23 | Swin-B | 0.0024 | 0.0066 | 0.0084 | 0.0035 |
[NEW] |  | Video Swin-B | 0.0008 | 0.0024 | 0.0030 | 0.0049 |
[NEW] | FF++ C40 | Swin-B | 0.0034 | 0.0096 | 0.0123 | 0.0117 |
[NEW] |  | Video Swin-B | 0.0029 | 0.0081 | 0.0104 | 0.0085 |
[NEW] | Celeb-DF v2 | Swin-B | 0.0020 | 0.0056 | 0.0072 | 0.0042 |
[NEW] |  | Video Swin-B | 0.0012 | 0.0034 | 0.0044 | 0.0042 |
[NEW] | DeeperForensics-1.0 | Swin-B | 0.0011 | 0.0032 | 0.0040 | 0.0034 |
[NEW] |  | Video Swin-B | 0.0024 | 0.0067 | 0.0085 | 0.0055 |
[NEW] Note. Supplementary, post hoc. SE: standard deviation of the 5,000 paired cluster-bootstrap ΔAUC draws. MDD: smallest ΔAUC detectable with 80% power by a two-sided normal-approximation test, (z + 0.84) × SE, with z = 1.96 (α = 0.05) or 2.73 (α = 0.05/8). Headroom: 1 − comparator ROC-AUC, the largest possible gain for SwinFusion++. MDD exceeds headroom in 7 of 8 comparisons at α = 0.05/8. Celeb-DF v2 intervals are approximate: all 843 fake videos lie in 9 identity clusters.
[NEW] #### Table J7. Robustness of the Ten Significant Architecture Differences
[NEW] | Comparison | Holm p (final, m = 18) | Holm p (pre-scoring, m = 27) | Holm p (pooled, m = 26) | Seed sign agreement | Holm p (DFo global clusters) | CDF leave-one-identity-out ΔAUC |
| --- | --- | --- | --- | --- | --- | --- |
[NEW] | C23 → DFo vs Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | &lt; 0.005 | — |
[NEW] | CDF → C23 vs Swin-B | 0.018 | 0.024 | 0.034 | 9/9 | — | — |
[NEW] | CDF → C40 vs Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | — | — |
[NEW] | CDF → C40 vs Video Swin-B | &lt; 0.005 | 0.005 | 0.005 | 8/9 | — | — |
[NEW] | CDF → DFo vs Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | &lt; 0.005 | — |
[NEW] | CDF → DFo vs Video Swin-B | &lt; 0.005 | 0.006 | 0.007 | 9/9 | &lt; 0.005 | — |
[NEW] | DFo → C23 vs Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | — | — |
[NEW] | DFo → C40 vs Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | — | — |
[NEW] | DFo → C40 vs Video Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | — | — |
[NEW] | DFo → CDF vs Swin-B | &lt; 0.005 | 0.005 | 0.005 | 9/9 | — | +0.1122 to +0.1477 |
[NEW] Note. Supplementary. The ten fixed-recipe SwinFusion++ differences significant after Holm adjustment. Pre-scoring partition: grouping recorded before test scoring. Seed sign agreement: cross-seed pairings with the ensemble ΔAUC sign. DFo global clusters: 175 lineage clusters instead of 201. "&lt; 0.005" = Holm-adjusted p below 0.005; with m = 26 and 27 the smallest attainable values (0.0052 and 0.0054) are printed as 0.005. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. Delete-one-cluster jackknife standard errors of ΔAUC were 0.99 to 1.32 times the bootstrap standard errors for Celeb-DF v2 targets (mean 1.15; 15 comparisons) and 0.84 to 1.05 times for the other test sets (mean 1.00; 50 comparisons), so Celeb-DF v2 intervals may be narrower than nominal. Across all 15 DeeperForensics-1.0-target comparisons, the 175-cluster re-analysis changed no Holm decision.
[NEW] #### Table J8. Transfer ROC-AUC With 95% Intervals for All Models
[NEW] | Direction | SwinFusion++ | Swin-B | Video Swin-B | SwinFusion++ (BO) |
| --- | --- | --- | --- | --- |
[NEW] | C23 → C40 | 0.9760 [0.9575, 0.9910] | 0.9739 [0.9572, 0.9885] | 0.9746 [0.9570, 0.9893] | 0.9862 [0.9739, 0.9959] |
[NEW] | C23 → CDF | 0.8624 [0.8052, 0.9149] | 0.8680 [0.8086, 0.9184] | 0.8676 [0.8251, 0.9108] | 0.8785 [0.8253, 0.9256] |
[NEW] | C23 → DFo | 0.8261 [0.7926, 0.8603] | 0.5678 [0.5250, 0.6105] | 0.8421 [0.8092, 0.8740] | 0.7316 [0.7015, 0.7638] |
[NEW] | CDF → C23 | 0.8958 [0.8663, 0.9253] | 0.8468 [0.8129, 0.8814] | 0.9047 [0.8739, 0.9340] | 0.8657 [0.8283, 0.9038] |
[NEW] | CDF → C40 | 0.8384 [0.8056, 0.8725] | 0.7770 [0.7430, 0.8102] | 0.7630 [0.7201, 0.8035] | 0.7345 [0.6961, 0.7741] |
[NEW] | CDF → DFo | 0.7233 [0.6869, 0.7604] | 0.6012 [0.5624, 0.6408] | 0.6603 [0.6130, 0.7048] | 0.6824 [0.6488, 0.7178] |
[NEW] | DFo → C23 | 0.8127 [0.7802, 0.8475] | 0.6115 [0.5774, 0.6466] | 0.7676 [0.7358, 0.8021] | 0.7236 [0.6918, 0.7579] |
[NEW] | DFo → C40 | 0.7668 [0.7322, 0.8032] | 0.5964 [0.5592, 0.6330] | 0.6829 [0.6430, 0.7265] | 0.7067 [0.6758, 0.7410] |
[NEW] | DFo → CDF | 0.5879 [0.5210, 0.6592] | 0.4593 [0.3970, 0.5259] | 0.6001 [0.5354, 0.6750] | 0.5519 [0.4954, 0.6128] |
[NEW] | Unweighted mean (descriptive) | 0.8099 | 0.7002 | 0.7848 | 0.7623 |
[NEW] Note. Ensemble ROC-AUC [95% CI] under frozen transfer; intervals: 95% percentile intervals from 5,000 stratified cluster-bootstrap draws, not adjusted for multiplicity. C23/C40 = FaceForensics++ DeepFakes at compression C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. The unweighted mean summarizes this grid only: directions share sources and test sets, the mean was not predeclared, and the study’s analysis registry rules out a collapsed generalization score; it supports no claim.
[NEW] [IMAGE] 
[NEW] #### Figure J1. Within-Dataset ROC Curves of the Fixed-Recipe Models
[NEW] Note. Axes are truncated to false positive rates of 0–0.2 and true positive rates of 0.8–1.0, because every curve lies near the upper-left corner. Markers show operating points at the frozen source-validation threshold. Numbers are ROC-AUC (top to bottom: SwinFusion++, Swin-B, Video Swin-B). Abbreviations as in Figure 11.