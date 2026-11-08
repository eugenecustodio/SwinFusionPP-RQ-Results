### Video-level, seed 1701, values as fractions

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison. Preliminary paired result (Table 6): C40 seed-1701 SwinFusion++ − CNN-LSTM ΔAUC +0.1846 [0.1503, 0.2165], ΔF1 +0.1867 [0.1503, 0.2201], Holm p = 0.0004 (preliminary pipeline, single models).

| model | train_condition | test_condition | roc_auc | f1 | accuracy | location |
|---|---|---|---|---|---|---|
| CNN-LSTM (ResNet-18 + LSTM, reproduced) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.7876 | 0.7452 | 0.7143 | Table 7 |
| CNN-LSTM (ResNet-18 + LSTM, reproduced) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.7984 | 0.7515 | 0.7071 | Table 7 |
