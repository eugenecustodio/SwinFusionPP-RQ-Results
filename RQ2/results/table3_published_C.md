### Not comparable to our protocol

| family | model | train_dataset | test_dataset | metric | value | location | source |
|---|---|---|---|---|---|---|---|
| Xception | Xception | FF++ DeepFakes only (manipulation-specific detector) + pristine | FF++ test split (DeepFakes vs pristine frames) | Accuracy (%) | 0.9959 | Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | Rössler et al. 2019 |
| Xception | Xception | FF++ all four manipulations + pristine (trained jointly) | FF++ test split, DeepFakes fake frames only (per-method accuracy) | Accuracy (%) on DF fake images | 0.9929 | Appendix B, Table 5 (PDF p.13) | Rössler et al. 2019 |
| Xception | Xception | FF++ all four manipulations + pristine | FF++ test split (all manipulations + pristine) | Binary detection accuracy (%) | 0.9926 | Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | Rössler et al. 2019 |
| Xception | Xception | FF++ all four manipulations, LQ (c40)-trained model | FaceForensics benchmark hidden set (1000 images, randomly processed) | Precision (%) per caption (column header reads "Accuracies") | 0.9636 | Section 5, Table 2 (PDF p.8) | Rössler et al. 2019 |
| Xception | Xception | FF++ DeepFakes (same split as DFo) | DeeperForensics-1.0 hidden test set (400 videos) | Accuracy (%) | 0.5738 | Table 4 (PDF p.9) | Jiang et al. 2020 |
| Xception | Xception | FF++ (subset/compression not stated) | Celeb-DF | Accuracy (%) per y-axis label | 0.6530 | Fig. 8 bar label (PDF p.11) | Kingra et al. 2024 |
| Xception | Xception | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | Accuracy (test) | 0.6320 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | F1 | 0.6419 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | ROC-AUC | 0.6400 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | Accuracy (test) | 0.5922 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | F1 | 0.6349 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | ROC-AUC | 0.6300 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | FaceForensics++ (FF++) | FaceForensics++ (FF++) | Accuracy (test) | 0.7386 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | FaceForensics++ (FF++) | FaceForensics++ (FF++) | F1 | 0.7304 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| Xception | Xception | FaceForensics++ (FF++) | FaceForensics++ (FF++) | ROC-AUC | 0.7300 | Table I (base-model comparison, batch size 128), PDF p.4 | Saikia et al. 2022 |
| I3D | I3D | FF++ DeepFakes (same split as DFo) | DeeperForensics-1.0 hidden test set (400 videos) | Accuracy (%) | 0.5663 | Table 4 (PDF p.9) | Jiang et al. 2020 |
| FTCN | FTCN (+TT) | DeeperForensics (DFo) | FF++ DeepFakes | AUC (%) | 0.9910 | Supplement Table 1 (supp. PDF p.2) | Zheng et al. 2021 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | Accuracy (%) | 0.9967 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | Precision (%) | 1.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | Recall (%) | 0.9933 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | FPR (%) | 0.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | FNR (%) | 0.0067 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | Accuracy (%) | 1.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | Precision (%) | 1.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | Recall (%) | 1.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | FPR (%) | 0.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ DF Raw (trained per category) | FF++ DF Raw test (300 real + 300 fake per Table 1) | FNR (%) | 0.0000 | Table 3 (PDF p.9) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ (subset/compression not stated) | Celeb-DF | not stated (accuracy implied; Fig. 8 shows the same 77.8 as accuracy) | 0.7780 | Fig. 7 heatmap, bottom-right panel (PDF p.10) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ (subset/compression not stated) | DeeperForensics | not stated (accuracy implied; Fig. 8 shows the same 77.8 as accuracy) | 0.6183 | Fig. 7 heatmap, bottom-right panel (PDF p.10) | Kingra et al. 2024 |
| SFormer | SFormer | FF++ (subset/compression not stated) | Celeb-DF | Accuracy (%) per y-axis label | 0.7780 | Fig. 8 bar label (PDF p.11) | Kingra et al. 2024 |
