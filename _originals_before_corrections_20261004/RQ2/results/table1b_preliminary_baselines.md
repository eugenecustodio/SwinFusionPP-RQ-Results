### Video-level, seed 1701, values as fractions

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison. I3D and SFormer have no verified local numbers in the preliminary study (blocked); they appear only as published values.

| model | train_condition | test_condition | roc_auc | f1 | accuracy | location |
|---|---|---|---|---|---|---|
| Xception (reproduced) | Celeb-DF v2 | Celeb-DF v2 | 0.6480 | 0.9140 | 0.8417 | Table 7 |
| Xception (reproduced) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9978 | 0.5821 | 0.4600 | Table 7 |
| Xception (reproduced) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.7725 | 0.6886 | 0.6964 | Table 7 |
| Xception (reproduced) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.8109 | 0.7429 | 0.7429 | Table 7 |
