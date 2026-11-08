### Earlier pipeline; DeeperForensics = full view

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison.

| model | train_condition | test_condition | roc_auc | roc_auc_ci_low | roc_auc_ci_high | f1 | accuracy | location |
|---|---|---|---|---|---|---|---|---|
| Swin-B (preliminary) | FF++ C23 (HQ) | Celeb-DF v2 | 0.9052 | 0.8958 | 0.9118 | 0.9315 | 0.8824 | Table 9 |
| Swin-B (preliminary) | FF++ C23 (HQ) | DeeperForensics-1.0 | 0.8002 | 0.7663 | 0.8350 | 0.3555 | 0.2809 | Table 9 |
| Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C40 (LQ) | 0.9719 | 0.9532 | 0.9878 | 0.8664 | 0.8821 | Table 9 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | Celeb-DF v2 | 0.8730 | 0.8549 | 0.8864 | 0.8821 | 0.8149 | Table 9 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | DeeperForensics-1.0 | 0.8021 | 0.7764 | 0.8317 | 0.2362 | 0.2055 | Table 9 |
| SwinFusion++ (preliminary) | FF++ C23 (HQ) | FF++ C40 (LQ) | 0.9686 | 0.9522 | 0.9829 | 0.7686 | 0.8107 | Table 9 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | Celeb-DF v2 | 0.9045 | 0.8901 | 0.9138 | 0.9289 | 0.8824 | Table 9 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | DeeperForensics-1.0 | 0.7508 | 0.7175 | 0.7898 | 0.2110 | 0.1912 | Table 9 |
| Video Swin-B (preliminary) | FF++ C23 (HQ) | FF++ C40 (LQ) | 0.9440 | 0.9190 | 0.9677 | 0.7182 | 0.7786 | Table 9 |
