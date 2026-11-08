# Figure captions (Heading4, below the image: “Figure N.” followed by the title; the note goes in a 10-pt paragraph under the caption)

## Figure 11. Transfer ROC-AUC of the Fixed-Recipe Models by Training and Test Dataset
File: fig11_transfer_heatmap.png (script: scripts/m_fig11.py; source: 00_Shared/statistics_raw/three_seed_mean_logit_ensemble.csv)

Note. Three-seed mean-logit ensembles, plain variant. Rows are training datasets and columns are test datasets; the bold diagonal is in-distribution. C23 and C40 = FaceForensics++ DeepFakes HQ and LQ; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. — = not evaluated (C40 was not a transfer source). Colors do not distinguish values below 0.5.

## Figure 12. Paired Differences in ROC-AUC Between Fixed-Recipe SwinFusion++ and Each Encoder
File: fig12_forest.png (script: scripts/m_fig12.py; source: tables/fig12_forest.csv, cross-checked against paired_tests_optionA.csv)

Note. Points are ensemble ΔROC-AUC (SwinFusion++ minus comparator). Bars are unadjusted 95% percentile intervals from 5,000 stratified cluster-bootstrap draws. Filled markers denote Holm-adjusted p < 0.05 (rank-based cluster permutation test). Because the intervals are unadjusted, one interval excludes 0 without significance (DFo → C23 vs Video Swin-B). Panels use different x-scales. Abbreviations as in Figure 11.

## Figure 13. ROC Curves Under Frozen Cross-Dataset Transfer With the Frozen Operating Points
File: fig13_transfer_roc.png (script: scripts/m_fig13.py; source: tables/roc_points.csv, checked against the ensemble CSV)

Note. Fixed-recipe three-seed ensembles. Markers show each model’s operating point at its frozen source-validation threshold. Numbers are ROC-AUC (top to bottom: SwinFusion++, Swin-B, Video Swin-B). The dashed diagonal marks chance. Markers near the origin overlap because almost no target videos were flagged as fake. Abbreviations as in Figure 11.

## Figure J1. Within-Dataset ROC Curves of the Fixed-Recipe Models
File: figJ1_within_roc.png (script: scripts/m_fig13.py; source: tables/roc_points.csv)

Note. Axes are truncated to false positive rates of 0–0.2 and true positive rates of 0.8–1.0, because every curve lies near the upper-left corner. Markers show operating points at the frozen source-validation threshold. Numbers are ROC-AUC (top to bottom: SwinFusion++, Swin-B, Video Swin-B). Abbreviations as in Figure 11.
