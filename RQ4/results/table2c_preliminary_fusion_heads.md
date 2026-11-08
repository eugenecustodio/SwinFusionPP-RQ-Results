### Earlier pipeline; fixed encoders, 4-epoch heads

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison.

| model | train_condition | test_condition | roc_auc | f1 | accuracy | location |
|---|---|---|---|---|---|---|
| Full TLBG-HCA head (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9964 | 0.9857 | 0.9857 | Table 8 |
| Late concatenation head (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9952 | 0.9892 | 0.9893 | Table 8 |
| No-exchange head (capacity-matched) (preliminary) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.9964 | 0.9857 | 0.9857 | Table 8 |
