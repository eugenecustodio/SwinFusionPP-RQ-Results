### Values as fractions; shows the change from the earlier pipeline

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison.

| model | train_condition | test_condition | roc_auc | roc_auc_ci_low | roc_auc_ci_high | f1 | accuracy | location |
|---|---|---|---|---|---|---|---|---|
| Swin-B (preliminary) | Celeb-DF v2 | Celeb-DF v2 | 0.9824 | 0.9785 | 0.9835 | 0.9433 | 0.9092 | Table 4 |
| Swin-B (preliminary) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9989 | 0.9974 | 0.9999 | 0.9940 | 0.9891 | Table 4 |
| Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9930 | 0.9824 | 1.0000 | 0.9856 | 0.9857 | Table 4 |
| Swin-B (preliminary) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.9917 | 0.9817 | 0.9987 | 0.9712 | 0.9714 | Table 4 |
| SwinFusion++ (preliminary) | Celeb-DF v2 | Celeb-DF v2 | 0.9724 | 0.9680 | 0.9746 | 0.9561 | 0.9278 | Table 4 |
| SwinFusion++ (preliminary) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9990 | 0.9970 | 1.0000 | 0.9844 | 0.9719 | Table 4 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9965 | 0.9921 | 0.9994 | 0.9712 | 0.9714 | Table 4 |
| SwinFusion++ (preliminary) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.9854 | 0.9727 | 0.9952 | 0.9420 | 0.9429 | Table 4 |
| Video Swin-B (preliminary) | Celeb-DF v2 | Celeb-DF v2 | 0.9749 | 0.9710 | 0.9770 | 0.9414 | 0.9057 | Table 4 |
| Video Swin-B (preliminary) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9989 | 0.9970 | 0.9999 | 0.9861 | 0.9748 | Table 4 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9972 | 0.9923 | 0.9999 | 0.9784 | 0.9786 | Table 4 |
| Video Swin-B (preliminary) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.9930 | 0.9864 | 0.9979 | 0.9577 | 0.9571 | Table 4 |
