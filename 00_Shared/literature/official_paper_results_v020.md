
#### Xception

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Rössler 2019 | Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | FF++ DeepFakes only (manipulation-specific detector) + pristine -> FF++ test split (DeepFakes vs pristine frames) | DeepFakes only | raw (c0) | frame | Accuracy (%) = 99.59 | primary |
| Rössler 2019 | Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | FF++ DeepFakes only (manipulation-specific detector) + pristine -> FF++ test split (DeepFakes vs pristine frames) | DeepFakes only | c23 (HQ) | frame | Accuracy (%) = 98.85 | primary |
| Rössler 2019 | Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | FF++ DeepFakes only (manipulation-specific detector) + pristine -> FF++ test split (DeepFakes vs pristine frames) | DeepFakes only | c40 (LQ) | frame | Accuracy (%) = 94.28 | primary |
| Rössler 2019 | Appendix B, Table 5 (PDF p.13) | FF++ all four manipulations + pristine (trained jointly) -> FF++ test split, DeepFakes fake frames only (per-method accuracy) | Trained on all 4; evaluated on DeepFakes subset | raw (c0) | frame | Accuracy (%) on DF fake images = 99.29 | primary |
| Rössler 2019 | Appendix B, Table 5 (PDF p.13) | FF++ all four manipulations + pristine (trained jointly) -> FF++ test split, DeepFakes fake frames only (per-method accuracy) | Trained on all 4; evaluated on DeepFakes subset | c23 (HQ) | frame | Accuracy (%) on DF fake images = 97.49 | primary |
| Rössler 2019 | Appendix B, Table 5 (PDF p.13) | FF++ all four manipulations + pristine (trained jointly) -> FF++ test split, DeepFakes fake frames only (per-method accuracy) | Trained on all 4; evaluated on DeepFakes subset | c40 (LQ) | frame | Accuracy (%) on DF fake images = 93.36 | primary |
| Rössler 2019 | Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | FF++ all four manipulations + pristine -> FF++ test split (all manipulations + pristine) | All four manipulations | raw (c0) | frame | Binary detection accuracy (%) = 99.26 | primary |
| Rössler 2019 | Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | FF++ all four manipulations + pristine -> FF++ test split (all manipulations + pristine) | All four manipulations | c23 (HQ) | frame | Binary detection accuracy (%) = 95.73 | primary |
| Rössler 2019 | Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | FF++ all four manipulations + pristine -> FF++ test split (all manipulations + pristine) | All four manipulations | c40 (LQ) | frame | Binary detection accuracy (%) = 81.00 | primary |
| Rössler 2019 | Section 5, Table 2 (PDF p.8) | FF++ all four manipulations, LQ (c40)-trained model -> FaceForensics benchmark hidden set (1000 images, randomly processed) | DeepFakes column | unknown/randomized (benchmark) | frame (single image) | Precision (%) per caption (column header reads "Accuracies") = 96.36 | primary |
| Li 2020 | Table 4 (PDF p.8) | FF++ (Xception-c23 released model; subset not stated beyond "trained on FaceForensics++") -> FF-DF (FF++ DeepFakes) | DeepFakes | c23 (training) | frame | AUC (%) = 99.7 | secondary (Celeb-DF paper, Li et al. 2020) |
| Li 2020 | Table 4 (PDF p.8) | FF++ (Xception-c23) -> Celeb-DF (v2, CVPR 2020 version) | n/a (cross-dataset) | c23 (training) | frame | AUC (%) = 65.3 | secondary (Celeb-DF paper, Li et al. 2020) |
| Li 2020 | Table 4 (PDF p.8) | FF++ (Xception-c40) -> FF-DF (FF++ DeepFakes) | DeepFakes | c40 (training) | frame | AUC (%) = 95.5 | secondary (Celeb-DF paper, Li et al. 2020) |
| Li 2020 | Table 4 (PDF p.8) | FF++ (Xception-c40) -> Celeb-DF (v2) | n/a (cross-dataset) | c40 (training) | frame | AUC (%) = 65.5 | secondary (Celeb-DF paper, Li et al. 2020) |
| Jiang 2020 | Table 4 (PDF p.9) | FF++ DeepFakes (same split as DFo) -> DeeperForensics-1.0 hidden test set (400 videos) | DeepFakes (training) | not stated | video | Accuracy (%) = 57.38 | secondary (benchmark run in DeeperForensics-1.0 paper) |
| Jiang 2020 | Table 4 (PDF p.9) | DeeperForensics-1.0 standard training set (std, no distortion) -> DeeperForensics-1.0 hidden test set | DeeperForensics manipulated (DF-VAE) | raw DFo std set | video | Accuracy (%) = 77.00 | secondary (benchmark run in DeeperForensics-1.0 paper) |
| Jiang 2020 | Table 5 (PDF p.9) | DeeperForensics-1.0 std -> DeeperForensics-1.0 std test | DeeperForensics manipulated | raw DFo std set | video | Accuracy (%) = 100.00 | secondary (benchmark run in DeeperForensics-1.0 paper) |
| Zi 2020 | Table 3 (PDF p.8) | FF++ (Deepfake) HQ -> FF++ (Deepfake) HQ test | DeepFakes only | HQ (c23 per FF++ naming) | image/frame | Accuracy (%) = 99.62% | secondary (WildDeepfake paper, Zi et al. 2020) |
| Zi 2020 | Table 3 (PDF p.8) | FF++ (Deepfake) LQ -> FF++ (Deepfake) LQ test | DeepFakes only | LQ (c40 per FF++ naming) | image/frame | Accuracy (%) = 90.25% | secondary (WildDeepfake paper, Zi et al. 2020) |
| Zheng 2021 | Table 2 (PDF p.6) | FF++ HQ: F2F+FS+NT (leave-one-out) -> FF++ HQ DeepFakes | DeepFakes (unseen manipulation) | c23 (HQ) | video | AUC (%) = 93.9 | secondary (FTCN paper, from LipForensics) |
| Zheng 2021 | Table 4 (PDF p.6) | FF++ HQ, all four manipulations -> Celeb-DF-v2 | n/a | c23 (HQ) training | video | AUC (%) = 73.7 | secondary (FTCN paper, from LipForensics) |
| Zheng 2021 | Table 4 (PDF p.6) | FF++ HQ, all four manipulations -> DeeperForensics (DFo) | n/a | c23 (HQ) training | video | AUC (%) = 84.5 | secondary (FTCN paper, from LipForensics) |
| Xu 2023 | Table 2 (PDF p.5) | FF++ (HQ) -> FF++ (HQ) | FF++ (manipulation subset not stated; appears all four) | c23 (HQ) | video (per TALL caption) | Accuracy (%) = 95.73 | secondary (TALL paper) |
| Xu 2023 | Table 2 (PDF p.5) | FF++ (HQ) -> FF++ (HQ) | FF++ (subset not stated) | c23 (HQ) | video (per TALL caption) | AUC (%) = 96.30 | secondary (TALL paper) |
| Xu 2023 | Table 2 (PDF p.5) | FF++ (LQ) -> FF++ (LQ) | FF++ (manipulation subset not stated; appears all four) | c40 (LQ) | video (per TALL caption) | Accuracy (%) = 86.86 | secondary (TALL paper) |
| Xu 2023 | Table 2 (PDF p.5) | FF++ (LQ) -> FF++ (LQ) | FF++ (subset not stated) | c40 (LQ) | video (per TALL caption) | AUC (%) = 89.30 | secondary (TALL paper) |
| Kingra 2024 | Fig. 8 bar label (PDF p.11) | FF++ (subset/compression not stated) -> Celeb-DF | n/a | not stated | not stated | Accuracy (%) per y-axis label = 65.3 | secondary (SFormer paper, from Lin et al. 2023 / Liang et al. 2023a) |
| Saikia 2022 | Table I (base-model comparison, batch size 128), PDF p.4 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy (test) = 63.20%; F1 = 64.19%; ROC-AUC = 0.64 | secondary (reported in Saikia et al. 2022, own re-run; not from Xception/FF++ benchmark papers) |
| Saikia 2022 | Table I (base-model comparison, batch size 128), PDF p.4 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy (test) = 59.22%; F1 = 63.49%; ROC-AUC = 0.63 | secondary (reported in Saikia et al. 2022, own re-run; not from Xception/FF++ benchmark papers) |
| Saikia 2022 | Table I (base-model comparison, batch size 128), PDF p.4 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy (test) = 73.86%; F1 = 73.04%; ROC-AUC = 0.73 | secondary (reported in Saikia et al. 2022, own re-run; not from Xception/FF++ benchmark papers) |
| Roessler 2019 | Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | frame (single-frame baseline) | Accuracy = 93.46 | secondary (Sabir et al. 2019 Table 1, copied from Roessler et al. FF++ paper) |
| Roessler 2019 | Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | frame (single-frame baseline) | Accuracy = 89.8 | secondary (Sabir et al. 2019 Table 1, copied from Roessler et al. FF++ paper) |
| Roessler 2019 | Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | frame (single-frame baseline) | Accuracy = 92.72 | secondary (Sabir et al. 2019 Table 1, copied from Roessler et al. FF++ paper) |

#### Xception (XN-avg)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Li 2020 | Table 2 (PDF p.7) | FF++ -> FF++ DeepFakes | DeepFakes column | c23 | video | Accuracy (fraction) = 1.0000 | secondary (S-MIL paper, Li et al. 2020) |
| Li 2020 | Table 2 (PDF p.7) | FF++ -> FF++ DeepFakes | DeepFakes column | c40 | video | Accuracy (fraction) = 0.9714 | secondary (S-MIL paper, Li et al. 2020) |
| Gu 2021 | Table 1 (PDF p.5) | FF++ -> FF++ DeepFakes | DeepFakes column | c23 | video | Accuracy (fraction) = 0.9893 | secondary (STIL paper) |
| Gu 2021 | Table 1 (PDF p.5) | FF++ -> FF++ DeepFakes | DeepFakes column | c40 | video | Accuracy (fraction) = 0.9678 | secondary (STIL paper) |
| Gu 2021 | Table 2 (PDF p.5) | Celeb-DF -> Celeb-DF | n/a | n/a | video | Accuracy (fraction) = 0.9944 | secondary (STIL paper; same as S-MIL Table 1) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | HQ (c23) | video (per source) | Accuracy (%) = 98.9 | secondary (SFormer paper; copied from STIL/S-MIL literature) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | LQ (c40) | video (per source) | Accuracy (%) = 96.8 | secondary (SFormer paper; copied from STIL/S-MIL literature) |
| Kingra 2024 | Table 5 (PDF p.11) | Celeb-DF -> Celeb-DF | n/a | n/a | video (per source) | Accuracy (%) = 99.4 | secondary (SFormer paper) |

#### Xception-c40

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Gu 2021 | Table 3 (PDF p.6) | FF++ c40 -> FF++ DF | DeepFakes (test column) | c40 | not stated (frame-level in original source) | AUC (fraction) = 0.9550 | secondary (STIL paper, copied) |
| Gu 2021 | Table 3 (PDF p.6) | FF++ c40 -> Celeb-DF | n/a | c40 (training) | not stated (frame-level in original source) | AUC (fraction) = 0.6550 | secondary (STIL paper, copied) |

#### XceptionNet (Rossler et al. 2019)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Zhang 2024 | Table 3 (PDF p.11), row "XceptionNet [4]" | as labelled by TSFF-Net: FF++ (HQ) (see notes - likely mislabelled) -> as labelled: FF++ (HQ) Deepfakes | per-manipulation column: Deepfakes | labelled 'FF++ (HQ)' (c23) by TSFF-Net - see notes | not stated | Accuracy (as labelled) = 96.4 | secondary (reported in TSFF-Net, PLOS ONE 2024) |
| Zhang 2024 | Table 3 (PDF p.11), row "XceptionNet [4]" | as labelled by TSFF-Net: FF++ (HQ) (see notes - likely mislabelled) -> as labelled: FF++ (HQ) Face2Face | per-manipulation column: Face2Face | labelled 'FF++ (HQ)' (c23) by TSFF-Net - see notes | not stated | Accuracy (as labelled) = 86.9 | secondary (reported in TSFF-Net, PLOS ONE 2024) |
| Zhang 2024 | Table 3 (PDF p.11), row "XceptionNet [4]" | as labelled by TSFF-Net: FF++ (HQ) (see notes - likely mislabelled) -> as labelled: FF++ (HQ) FaceSwap | per-manipulation column: FaceSwap | labelled 'FF++ (HQ)' (c23) by TSFF-Net - see notes | not stated | Accuracy (as labelled) = 90.3 | secondary (reported in TSFF-Net, PLOS ONE 2024) |
| Zhang 2024 | Table 3 (PDF p.11), row "XceptionNet [4]" | as labelled by TSFF-Net: FF++ (HQ) (see notes - likely mislabelled) -> as labelled: FF++ (HQ) NeuralTextures | per-manipulation column: NeuralTextures | labelled 'FF++ (HQ)' (c23) by TSFF-Net - see notes | not stated | Accuracy (as labelled) = 80.7 | secondary (reported in TSFF-Net, PLOS ONE 2024) |

#### I3D

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Jiang 2020 | Table 4 (PDF p.9) | FF++ DeepFakes (same split as DFo) -> DeeperForensics-1.0 hidden test set (400 videos) | DeepFakes (training) | not stated | video | Accuracy (%) = 56.63 | original third-party run (DeeperForensics paper); I3D primary paper has no deepfake results |
| Jiang 2020 | Table 4 / Table 6 col. 2 (PDF p.9-10) | DeeperForensics-1.0 std training set (no distortion) -> DeeperForensics-1.0 hidden test set | DeeperForensics manipulated (DF-VAE) | raw DFo std set | video | Accuracy (%) = 79.25 | original third-party run (DeeperForensics paper) |
| Jiang 2020 | Table 5 (PDF p.9) | DeeperForensics-1.0 std -> DeeperForensics-1.0 std test | DeeperForensics manipulated | raw std | video | Accuracy (%) = 100.00 | original third-party run (DeeperForensics paper) |
| Jiang 2020 | Table 5 (PDF p.9) | DeeperForensics-1.0 std -> DeeperForensics-1.0 std/sing test | DeeperForensics manipulated | std/sing distortions at test | video | Accuracy (%) = 90.75 | original third-party run (DeeperForensics paper) |
| Jiang 2020 | Table 5 (PDF p.9) | DeeperForensics-1.0 std -> DeeperForensics-1.0 std/rand test | DeeperForensics manipulated | std/rand distortions at test | video | Accuracy (%) = 96.88 | original third-party run (DeeperForensics paper) |
| Li 2020 | Table 2 (PDF p.7) | FF++ (training per manipulation not explicitly stated) -> FF++ DeepFakes | DeepFakes column | c23 | video | Accuracy (fraction) = 0.9286 | original third-party run (S-MIL paper; baselines retrained with official code) |
| Li 2020 | Table 2 (PDF p.7) | FF++ -> FF++ DeepFakes | DeepFakes column | c40 | video | Accuracy (fraction) = 0.9107 | original third-party run (S-MIL paper) |
| Li 2020 | Table 1 (PDF p.7) | Celeb-DF -> Celeb-DF (5,639 fake videos = v2) | n/a | n/a | video | Accuracy (fraction) = 0.9923 | original third-party run (S-MIL paper) |
| Zi 2020 | Table 4 (PDF p.8) | FF++ (Deepfake) HQ -> FF++ (Deepfake) HQ test | DeepFakes only | HQ (c23 per FF++ naming) | clip/sequence | Accuracy (%) = 96.70% | original third-party run (WildDeepfake paper) |
| Zi 2020 | Table 4 (PDF p.8) | FF++ (Deepfake) LQ -> FF++ (Deepfake) LQ test | DeepFakes only | LQ (c40 per FF++ naming) | clip/sequence | Accuracy (%) = 93.18% | original third-party run (WildDeepfake paper) |
| Gu 2021 | Table 1 (PDF p.5) | FF++ -> FF++ DeepFakes | DeepFakes column | c23 | video | Accuracy (fraction) = 0.9286 | secondary (STIL paper; identical to S-MIL Table 2) |
| Gu 2021 | Table 1 (PDF p.5) | FF++ -> FF++ DeepFakes | DeepFakes column | c40 | video | Accuracy (fraction) = 0.9107 | secondary (STIL paper; identical to S-MIL Table 2) |
| Gu 2021 | Table 2 (PDF p.5) | Celeb-DF -> Celeb-DF | n/a | n/a | video | Accuracy (fraction) = 0.9923 | secondary (STIL paper; identical to S-MIL Table 1) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | HQ (c23) | video (per source) | Accuracy (%) = 92.9 | secondary (SFormer paper; copied) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | LQ (c40) | video (per source) | Accuracy (%) = 91.1 | secondary (SFormer paper; copied) |
| Kingra 2024 | Table 5 (PDF p.11) | Celeb-DF -> Celeb-DF | n/a | n/a | video (per source) | Accuracy (%) = 99.2 | secondary (SFormer paper; copied) |
| de Lima 2020 | Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | Celeb-DF (as reported) -> Celeb-DF (as reported) | n/a | not stated | not stated | Accuracy = 92.28%; ROC-AUC = 97.59 | secondary (Saikia et al. 2022 Table IV, copied from de Lima et al. 2020) |

#### I3D (I3D-RGB*)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Xu 2023 | Table 1 (PDF p.5) | FF++ (HQ) -> Celeb-DF | n/a (cross-dataset) | c23 (HQ) training | video | AUC (%) = 78.24 | original third-party run (TALL paper, own implementation) |

#### STIL

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Gu 2021 | Table 1 (PDF p.5) | FF++ c23 -> FF++ c23 DeepFakes | DeepFakes column (per-manipulation columns) | c23 (HQ) | video | Accuracy (fraction) = 0.9964 | primary |
| Gu 2021 | Table 1 (PDF p.5) | FF++ c40 -> FF++ c40 DeepFakes | DeepFakes column | c40 (LQ) | video | Accuracy (fraction) = 0.9821 | primary |
| Gu 2021 | Table 2 (PDF p.5) | Celeb-DF -> Celeb-DF (described with 5,639 fakes = v2) | n/a | n/a | video | Accuracy (fraction) = 0.9978 | primary |
| Gu 2021 | Table 3 (PDF p.6) | FF++ c40 (following DoubleRNN [18] convention; training manipulation subset not stated) -> FF++ DF | DeepFakes (test column) | c40 | not stated (video-level setting overall) | AUC (fraction) = 0.9712 | primary |
| Gu 2021 | Table 3 (PDF p.6) | FF++ c40 -> Celeb-DF | n/a (cross-dataset) | c40 (training) | not stated (video-level setting overall) | AUC (fraction) = 0.7558 | primary |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | HQ (c23) | video (per source) | Accuracy (%) = 99.6 | secondary (SFormer paper; copied) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | LQ (c40) | video (per source) | Accuracy (%) = 98.2 | secondary (SFormer paper; copied) |
| Kingra 2024 | Table 5 (PDF p.11) | Celeb-DF -> Celeb-DF | n/a | n/a | video (per source) | Accuracy (%) = 99.8 | secondary (SFormer paper; copied) |

#### FTCN (+TT)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Zheng 2021 | Table 2 (PDF p.6) | FF++ HQ: F2F+FS+NT (leave-one-out) -> FF++ HQ DeepFakes | DeepFakes (unseen manipulation) | c23 (HQ) | video | AUC (%) = 99.9 | primary |
| Zheng 2021 | Table 4 (PDF p.6) | FF++ HQ, all four manipulations -> Celeb-DF-v2 | n/a (cross-dataset) | c23 (HQ) training | video | AUC (%) = 86.9 | primary |
| Zheng 2021 | Table 4 (PDF p.6) | FF++ HQ, all four manipulations -> DeeperForensics (DFo) | n/a (cross-dataset) | c23 (HQ) training | video | AUC (%) = 98.8 | primary |
| Zheng 2021 suppl. | Supplement Table 2 (supp. PDF p.2) | FF++ (HQ) -> FF++ (HQ) | FF++ (subset not stated; follows PE-LSTM / Two-branch setups) | c23 (HQ) | not stated | Accuracy (%) = 99.1 | primary (supplementary) |
| Zheng 2021 suppl. | Supplement Table 2 (supp. PDF p.2) | FF++ (HQ) -> FF++ (HQ) | FF++ (subset not stated) | c23 (HQ) | video | AUC (%) = 99.8 | primary (supplementary) |
| Zheng 2021 suppl. | Supplement Table 2 (supp. PDF p.2) | FF++ (LQ) -> FF++ (LQ) | FF++ (subset not stated; follows Two-branch/LipForensics setup) | c40 (LQ) | video | AUC (%) = 98.3 | primary (supplementary) |
| Zheng 2021 suppl. | Supplement Table 1 (supp. PDF p.2) | DeeperForensics (DFo) -> DeeperForensics (DFo) | n/a | not stated | video | AUC (%) = 100 | primary (supplementary) |
| Zheng 2021 suppl. | Supplement Table 1 (supp. PDF p.2) | DeeperForensics (DFo) -> FF++ DeepFakes | DeepFakes (test) | not stated | video | AUC (%) = 99.1 | primary (supplementary) |

#### FTCN (+TT, L x1)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Zheng 2021 | Table 8 (PDF p.8) | FF++ F2F only -> FF++ DeepFakes | DeepFakes (unseen manipulation) | not stated (paper trains on HQ) | video | AUC (%) = 98.1 | primary |

#### FTCN

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Xu 2023 | Table 3 (PDF p.6) | FF++ (HQ) -> Celeb-DF | n/a | c23 (HQ) training | video | AUC (%) = 86.90 | secondary (TALL paper; matches FTCN Table 4) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | HQ (c23) | not stated | Accuracy (%) = 97.9 | secondary (SFormer paper) |

#### TALL-Swin

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Xu 2023 | Table 2 (PDF p.5) | FF++ (HQ) -> FF++ (HQ) | FF++ (manipulation subset not stated; appears all four) | c23 (HQ) | video | Accuracy (%) = 98.65 | primary |
| Xu 2023 | Table 2 (PDF p.5) | FF++ (HQ) -> FF++ (HQ) | FF++ (subset not stated) | c23 (HQ) | video | AUC (%) = 99.87 | primary |
| Xu 2023 | Table 2 (PDF p.5) | FF++ (LQ) -> FF++ (LQ) | FF++ (subset not stated) | c40 (LQ) | video | Accuracy (%) = 92.82; AUC (%) = 94.57 | primary |
| Xu 2023 | Table 1 and Table 3 (PDF p.5-6) | FF++ (HQ) -> Celeb-DF | n/a (cross-dataset) | c23 (HQ) training | video | AUC (%) = 90.79 | primary |
| Xu 2023 | Table 3 (PDF p.6) | FF++ (HQ) -> DeeperForensics (DFo) | n/a (cross-dataset) | c23 (HQ) training | video | AUC (%) = 99.62 | primary |

#### Swin-B (baseline, context only)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Xu 2023 | Table 1 (PDF p.5) | FF++ (HQ) -> Celeb-DF | n/a (cross-dataset) | c23 (HQ) training | video | AUC (%) = 83.13 | original third-party run (TALL paper) |

#### SFormer

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Kingra 2024 | Table 3 (PDF p.9) | FF++ DF Raw (trained per category) -> FF++ DF Raw test (300 real + 300 fake per Table 1) | DeepFakes only | raw (c0) | video (SS: one 20-frame subsequence per video; MS: aggregated subsequences) | Accuracy (%) = 99.67; Precision (%) = 100; Recall (%) = 99.33; FPR (%) = 0; FNR (%) = 0.67; Accuracy (%) = 100; Precision (%) = 100; Recall (%) = 100; FPR (%) = 0; FNR (%) = 0 | primary |
| Kingra 2024 | Table 3 (PDF p.9) | FF++ DF HQ (trained per category) -> FF++ DF HQ test (300 real + 300 fake per Table 1) | DeepFakes only | HQ (c23) | video (SS: one 20-frame subsequence per video; MS: aggregated subsequences) | Accuracy (%) = 98.5; Precision (%) = 99.32; Recall (%) = 97.67; FPR (%) = 0.67; FNR (%) = 2.33; Accuracy (%) = 99.9; Precision (%) = 100; Recall (%) = 99.1; FPR (%) = 0; FNR (%) = 0.8 | primary |
| Kingra 2024 | Table 3 (PDF p.9) | FF++ DF LQ (trained per category) -> FF++ DF LQ test (300 real + 300 fake per Table 1) | DeepFakes only | LQ (c40) | video (SS: one 20-frame subsequence per video; MS: aggregated subsequences) | Accuracy (%) = 94.82; Precision (%) = 95.84; Recall (%) = 92.34; FPR (%) = 4.33; FNR (%) = 7.99; Accuracy (%) = 98.15; Precision (%) = 99.5; Recall (%) = 94.3; FPR (%) = 1; FNR (%) = 5.41 | primary |
| Kingra 2024 | Table 2(a)/(b) (PDF p.8) | Celeb-DF -> Celeb-DF (subject-disjoint split) | n/a | n/a | video | Accuracy (%) = 95.04; Precision (%) = 94.35; Recall (%) = 95.9; FPR (%) = 5.83; FNR (%) = 4.09; Accuracy (%) = 99.1; Precision (%) = 99.7; Recall (%) = 99; FPR (%) = 0.2; FNR (%) = 0.8 | primary |
| Kingra 2024 | Table 2(a)/(b) (PDF p.8) | DeeperForensics -> DeeperForensics (subject-disjoint split) | n/a | n/a (DFo: no perturbation subset) | video | Accuracy (%) = 99.67; Precision (%) = 99.67; Recall (%) = 99.67; FPR (%) = 0.33; FNR (%) = 0.33; Accuracy (%) = 100; Precision (%) = 100; Recall (%) = 100; FPR (%) = 0; FNR (%) = 0 | primary |
| Kingra 2024 | Table 4 (PDF p.11) | FF++ DF C23 -> FF++ DF C40 | DeepFakes only | train C23 -> test C40 | video | Accuracy (%) (metric not named in caption; text refers to accuracy) = 86.28 | primary |
| Kingra 2024 | Table 4 (PDF p.11) | FF++ DF C40 -> FF++ DF C23 | DeepFakes only | train C40 -> test C23 | video | Accuracy (%) (metric not named in caption; text refers to accuracy) = 96.5 | primary |
| Kingra 2024 | Table 4 (PDF p.11) | FF++ DF C0 -> FF++ DF C23 | DeepFakes only | train C0 -> test C23 | video | Accuracy (%) (metric not named in caption; text refers to accuracy) = 84.16 | primary |
| Kingra 2024 | Table 4 (PDF p.11) | FF++ DF C0 -> FF++ DF C40 | DeepFakes only | train C0 -> test C40 | video | Accuracy (%) (metric not named in caption; text refers to accuracy) = 58.68 | primary |
| Kingra 2024 | Table 4 (PDF p.11) | FF++ DF C23 -> FF++ DF C0 | DeepFakes only | train C23 -> test C0 | video | Accuracy (%) (metric not named in caption; text refers to accuracy) = 99.33 | primary |
| Kingra 2024 | Table 4 (PDF p.11) | FF++ DF C40 -> FF++ DF C0 | DeepFakes only | train C40 -> test C0 | video | Accuracy (%) (metric not named in caption; text refers to accuracy) = 97.67 | primary |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) HQ -> FF++ (DF) HQ | DeepFakes | HQ (c23) | video | Accuracy (%) = 99.9 | primary |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) LQ -> FF++ (DF) LQ | DeepFakes | LQ (c40) | video | Accuracy (%) = 98.15 | primary |
| Kingra 2024 | Table 5 (PDF p.11) | Celeb-DF -> Celeb-DF | n/a | n/a | video | Accuracy (%) = 99.1 | primary |
| Kingra 2024 | Fig. 7 heatmap, bottom-right panel (PDF p.10) | FF++ (subset/compression not stated) -> Celeb-DF | n/a (cross-dataset) | not stated | not stated | not stated (accuracy implied; Fig. 8 shows the same 77.8 as accuracy) = 77.80 | primary (figure) |
| Kingra 2024 | Fig. 7 heatmap, bottom-right panel (PDF p.10) | FF++ (subset/compression not stated) -> DeeperForensics | n/a (cross-dataset) | not stated | not stated | not stated (accuracy implied; Fig. 8 shows the same 77.8 as accuracy) = 61.83 | primary (figure) |
| Kingra 2024 | Fig. 8 bar label (PDF p.11) | FF++ (subset/compression not stated) -> Celeb-DF | n/a (cross-dataset) | not stated | not stated | Accuracy (%) per y-axis label = 77.8 | primary (figure) |

#### SFormer ablation: Swin spatial only

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Kingra 2024 | Table 7 / Table 8 (PDF p.12) | FF++ DF-HQ -> FF++ DF-HQ | DeepFakes only | HQ (c23) | not stated | Accuracy (%) = 86.31 | primary (ablation) |

#### Chen et al. 2022 Xception + spatiotemporal attention + ConvLSTM (Xception-ConvLSTM/'Xception-LSTM')

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Chen 2022 | Abstract + introduction preview (ScienceDirect article preview) | not accessible -> 'three widely used datasets' (names not given in abstract) | not accessible | not accessible | n/a | none = no numeric results in abstract | primary (abstract only; full text paywalled/not accessible) |
| Kingra 2024 | SFormer Table 6 (row 'Xception-LSTM Chen et al. (2022)'), PDF p.11 | Celeb-DF (as reported; intra-dataset implied) -> Celeb-DF (as reported) | n/a | not stated | not stated | Accuracy = 99.93 | secondary (SFormer, Kingra et al. 2024, Table 6) |
| Kingra 2024 | SFormer Table 6 (row 'Xception-LSTM Chen et al. (2022)'), PDF p.11 | DFDC-P (as reported; intra-dataset implied) -> DFDC-P (as reported) | n/a | not stated | not stated | Accuracy = 92.43 | secondary (SFormer, Kingra et al. 2024, Table 6) |
| Hriez 2025 | Hriez 2025 Table 6 (top-10 AUC, Celeb-DF; ref [157]), journal p.143972 (PDF p.16) | Celeb-DF (as reported) -> Celeb-DF (as reported) | n/a | not stated | not stated | ROC-AUC = 99.91 | secondary (Hriez 2025 IEEE Access review) |
| Hriez 2025 | Hriez 2025 Table 7 (top-10 accuracy, Celeb-DF; ref [157]), journal p.143972; text p.143971 | Celeb-DF (as reported) -> Celeb-DF (as reported) | n/a | not stated | not stated | Accuracy = 99.93 | secondary (Hriez 2025 IEEE Access review) |
| Hriez 2025 | Hriez 2025 Table 9 (top-10 accuracy, DFDC; ref [157]), journal p.143972 | DFDC (as reported) -> DFDC (as reported) | n/a | not stated | not stated | Accuracy = 99.91 | secondary (Hriez 2025 IEEE Access review) |
| Waseem 2023 | Table 10 ('Summary of Spatiotemporal Approach for Deepfake'), row [195], PDF p.30 (early-access pagination) | listed: FF++(DF), FF++(FS), FF++(NT), FF++(F2F), Celeb-DF, DFDC -> not specified which of the listed datasets | FF++ evaluated per manipulation (DF, FS, NT, F2F) per this listing | not stated | not stated | Accuracy = ACC = 1.0 | secondary (Waseem et al. 2023 IEEE Access review) |
| Tipper 2024 | Sec. text (ref [36]), PDF p.13 | FaceForensics++ (as reported) -> FaceForensics++ (as reported) | not stated | not stated | not stated | Accuracy = 99% detection accuracy | secondary (Tipper et al. 2024 review) |
| Song 2026 | Related-work text, PDF p.3 (journal p.36038) | Celeb-DF (as reported) -> Celeb-DF (as reported) | n/a | not stated | not stated | Accuracy = 99.93% | secondary (Song et al. 2026) |

#### Saikia et al. 2022 hybrid OF+CNN+LSTM (OF+RNN+CNN, proposed)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Saikia 2022 | Table II, PDF p.4 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 79.49%; Precision = 82.49%; Recall = 79.08%; ROC-AUC = 0.79 | primary |
| Saikia 2022 | Table II, PDF p.4 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 66.26%; Precision = 67.11%; Recall = 65.73%; ROC-AUC = 0.66 | primary |
| Saikia 2022 | Table II, PDF p.4 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 91.21%; Precision = 91.20%; Recall = 91.21%; ROC-AUC = 0.91 | primary |
| Saikia 2022 | Table III, PDF p.5 (also plotted in Fig. 4, p.6) | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 64.58%; Precision = 64.39%; ROC-AUC = 0.63; Accuracy = 64.27%; Precision = 65.99%; ROC-AUC = 0.64; Accuracy = 66.26%; Precision = 67.11%; ROC-AUC = 0.66; Accuracy = 64.12%; Precision = 69.04%; ROC-AUC = 0.63 | primary |
| Saikia 2022 | Table III, PDF p.5 (also plotted in Fig. 4, p.6) | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 74.87%; Precision = 75.71%; ROC-AUC = 0.75; Accuracy = 78.39%; Precision = 78.80%; ROC-AUC = 0.78; Accuracy = 83.17%; Precision = 83.26%; ROC-AUC = 0.83; Accuracy = 77.89%; Precision = 82.31%; ROC-AUC = 0.79; Accuracy = 86.68%; Precision = 86.95%; ROC-AUC = 0.87; Accuracy = 83.17%; Precision = 86.32%; ROC-AUC = 0.84; Accuracy = 91.21%; Precision = 91.20%; ROC-AUC = 0.91 | primary |
| Saikia 2022 | Table III, PDF p.5 (also plotted in Fig. 4, p.6) | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 63.25%; Precision = 66.67%; ROC-AUC = 0.65; Accuracy = 67.09%; Precision = 68.64%; ROC-AUC = 0.68; Accuracy = 73.07%; Precision = 72.94%; ROC-AUC = 0.73; Accuracy = 73.08%; Precision = 72.84%; ROC-AUC = 0.73; Accuracy = 78.21%; Precision = 78.19%; ROC-AUC = 0.78; Accuracy = 72.65%; Precision = 76.33%; ROC-AUC = 0.73; Accuracy = 74.36%; Precision = 76.34%; ROC-AUC = 0.74; Accuracy = 76.07%; Precision = 81.83%; ROC-AUC = 0.76; Accuracy = 79.49%; Precision = 82.69%; ROC-AUC = 0.79; Accuracy = 76.07%; Precision = 79.92%; ROC-AUC = 0.76 | primary |
| Saikia 2022 | Table IV ('Our Work'), PDF p.6 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 91.21%; ROC-AUC = 0.91 | primary |
| Saikia 2022 | Table IV ('Our Work'), PDF p.6 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 79.49%; ROC-AUC = 0.79 | primary |
| Saikia 2022 | Table IV ('Our Work'), PDF p.6 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 66.26%; ROC-AUC = 0.66 | primary |
| Saikia 2022 | Sec. V text (paragraph after Table IV), PDF p.6 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 79.80%; F1 = 78.80%; Precision = 82.49%; Recall = 79.08%; ROC-AUC = 0.79 | primary |
| Saikia 2022 | Sec. V text (paragraph after Table IV), PDF p.6 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 91.21%; F1 = 91.20%; Precision = 91.20%; Recall = 91.21%; ROC-AUC = 0.91 | primary |
| Saikia 2022 | Sec. V text (paragraph after Table IV), PDF p.6 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 66.26%; F1 = 65.35%; Precision = 67.11%; Recall = 65.73%; ROC-AUC = 0.66 | primary |
| Saikia 2022 | Abstract, PDF p.1 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 66.26% | primary |
| Saikia 2022 | Abstract, PDF p.1 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 91.21% | primary |
| Saikia 2022 | Abstract, PDF p.1 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 79.49% | primary |
| Kingra 2024 | SFormer Table 6 (row 'CNN-LSTM Saikia et al. (2022)'), PDF p.11 | Celeb-DF (as reported) -> Celeb-DF (as reported) | n/a | not stated | not stated | Accuracy = 79.49 | secondary (SFormer, Kingra et al. 2024, Table 6) |
| Kingra 2024 | SFormer Table 6 (row 'CNN-LSTM Saikia et al. (2022)'), PDF p.11 | DFDC-P (as reported) -> DFDC-P (as reported) | n/a | not stated | not stated | Accuracy = 66.26 | secondary (SFormer, Kingra et al. 2024, Table 6) |

#### Saikia et al. 2022 ablation variant OF+RNN (not the proposed model)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Saikia 2022 | Table II, PDF p.4 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 52.13%; Precision = 26.06%; Recall = 34.21%; ROC-AUC = 0.5 | primary |
| Saikia 2022 | Table II, PDF p.4 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 54.08%; Precision = 24.96%; Recall = 35.08%; ROC-AUC = 0.5 | primary |
| Saikia 2022 | Table II, PDF p.4 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 47.73%; Precision = 23.68%; Recall = 50%; ROC-AUC = 0.5 | primary |

#### Saikia et al. 2022 ablation variant OF+CNN (not the proposed model)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Saikia 2022 | Table II, PDF p.4 | Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) -> Celeb-DF (version not stated; described as 408 real/795 fake = Celeb-DF v1 counts) | n/a (Celeb-DF face swaps) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 83.33%; Precision = 83.78%; Recall = 83.71%; ROC-AUC = 0.83 | primary |
| Saikia 2022 | Table II, PDF p.4 | DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) -> DFDC (described as 5214 videos, 78.125% fake = DFDC-Preview counts; 3293 videos used per Sec. V) | n/a (DFDC) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 69.77%; Precision = 69.36%; Recall = 68.64%; ROC-AUC = 0.68 | primary |
| Saikia 2022 | Table II, PDF p.4 | FaceForensics++ (FF++) -> FaceForensics++ (FF++) | not stated (paper lists all four FF++ methods Face2Face/Deepfakes/FaceSwap/NeuralTextures; subset actually used not specified) | not stated | video (one N-frame optical-flow sequence per video; level not explicitly named) | Accuracy = 89.19%; Precision = 89.51%; Recall = 88.92%; ROC-AUC = 0.88 | primary |

#### Guera & Delp 2018 Conv-LSTM (InceptionV3 + LSTM), 20 frames

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Guera 2018 | Table 1, PDF p.5 (author copy) | Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) -> Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) | n/a (deepfake face swaps, FakeApp-style, collected from web) | not stated (web-sourced videos) | clip (continuous sub-sequence of N frames; paper says 'video sub-sequences') | Accuracy (test split) = 96.7; Accuracy (validation split) = 96.9; Accuracy (training split) = 99.5 | primary |

#### Guera & Delp 2018 Conv-LSTM (InceptionV3 + LSTM), 40 frames

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Guera 2018 | Table 1, PDF p.5 (author copy) | Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) -> Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) | n/a (deepfake face swaps, FakeApp-style, collected from web) | not stated (web-sourced videos) | clip (continuous sub-sequence of N frames; paper says 'video sub-sequences') | Accuracy (test split) = 97.1; Accuracy (validation split) = 97.1; Accuracy (training split) = 99.3 | primary |
| Guera 2018 | Sec. 5.3 text after Table 1, PDF p.5 | Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) -> Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) | n/a | not stated | clip (sub-sequence) | Accuracy (text claim) = greater than 97% | primary |

#### Guera & Delp 2018 Conv-LSTM (InceptionV3 + LSTM), 80 frames

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Guera 2018 | Table 1, PDF p.5 (author copy) | Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) -> Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) | n/a (deepfake face swaps, FakeApp-style, collected from web) | not stated (web-sourced videos) | clip (continuous sub-sequence of N frames; paper says 'video sub-sequences') | Accuracy (test split) = 97.1; Accuracy (validation split) = 97.2; Accuracy (training split) = 99.7 | primary |

#### Guera & Delp 2018 Conv-LSTM (InceptionV3 + LSTM)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Guera 2018 | Sec. 1 contributions paragraph, PDF p.2 | Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) -> Own dataset: 300 deepfake videos collected from multiple video-hosting websites + 300 pristine videos from HOHA (Hollywood Human Actions) = 600 videos (NOT FF++) | n/a | not stated | not stated | Relative accuracy gain over random detector (text claim) = 94% more accuracy than a random detector baseline in a balanced setting | primary |

#### Sabir et al. 2019 RCN variant: ResNet50, 1 frame(s) [no recurrence (single frame)]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.8 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 90.25 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 91.34 | primary |

#### Sabir et al. 2019 RCN variant: DenseNet, 1 frame(s) [no recurrence (single frame)]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.5 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 90.65 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 91.04 | primary |

#### Sabir et al. 2019 RCN variant: ResNet50 + Alignment, 1 frame(s) [no recurrence (single frame)]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.1 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 89.31 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 93.85 | primary |

#### Sabir et al. 2019 RCN variant: DenseNet + Alignment, 1 frame(s) [no recurrence (single frame)]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.4 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 87.18 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.1 | primary |

#### Sabir et al. 2019 RCN variant: ResNet50, 5 frame(s) [unidirectional GRU]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.6 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 90.25 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 90.95 | primary |

#### Sabir et al. 2019 RCN variant: DenseNet, 5 frame(s) [unidirectional GRU]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.7 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 89.8 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 93.11 | primary |

#### Sabir et al. 2019 RCN variant: ResNet50 + Alignment, 5 frame(s) [unidirectional GRU]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.0 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 92.4 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 95.07 | primary |

#### Sabir et al. 2019 RCN variant: DenseNet + Alignment, 5 frame(s) [unidirectional GRU]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.7 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 93.21 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 95.8 | primary |

#### Sabir et al. 2019 RCN variant: ResNet50 + Alignment + BiDir, 5 frame(s) [bidirectional GRU]

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.9 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 93.05 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 95.4 | primary |

#### Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.9 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.35 | primary |
| Sabir 2019 | Table 1, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.3 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.9 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.35 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 96.3 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9959 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9843 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9941 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9964 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9864 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9944 | primary |

#### Sabir et al. 2019 RCN variant: Spatial Transformer (STN alignment instead of landmarks)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 91.7 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 87.46 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 93.2 | primary |

#### Sabir et al. 2019 RCN variant: Multi Recurrence (4 recurrent nets on DenseNet blocks)

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.4 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 89.9 | primary |
| Sabir 2019 | Table 2, PDF p.4 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Accuracy = 94.8 | primary |

#### Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9923 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9609 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9857 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9936 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9675 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9866 | primary |

#### Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9889 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9824 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9891 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9891 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9863 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9896 | primary |

#### Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9916 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9762 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9896 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9930 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9815 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9901 | primary |

#### Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9949 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9593 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9930 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9953 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9676 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9934 | primary |

#### Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9950 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9808 | primary |
| Sabir 2019 | Fig. 2 legend (ROC plots), PDF p.5 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | ROC-AUC = AUC = 0.9930 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | DeepFakes only (real vs Deepfakes; per-manipulation experiment, separate training per type implied) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9957 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | Face2Face only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9842 | primary |
| Sabir 2019 | Fig. 3 legend (PR plots), PDF p.6 | FaceForensics++ -> FaceForensics++ | FaceSwap only (per-manipulation experiment) | c40 / LQ ('all results are on the heavily compressed version of dataset from [34]'; raw/HQ not evaluated) | not stated (per input sequence of 1 or 5 frames; no video-level aggregation described) | Average precision (AP, PR curve) = AP = 0.9935 | primary |

#### CAST-B5

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: Deepfakes only; test: Deepfakes only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 99.95 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: Deepfakes only; test: Face2Face only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 82.43 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: Deepfakes only; test: FaceSwap only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 59.88 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: Deepfakes only; test: NeuralTextures only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 86.41 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: Deepfakes only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 82.16 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: Face2Face only; test: Deepfakes only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 88.64 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: Face2Face only; test: Face2Face only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 98.61 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: Face2Face only; test: FaceSwap only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 65.69 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: Face2Face only; test: NeuralTextures only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 70.19 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: Face2Face only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 80.78 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: FaceSwap only; test: Deepfakes only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 58.13 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: FaceSwap only; test: Face2Face only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 74.71 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: FaceSwap only; test: FaceSwap only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 99.99 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: FaceSwap only; test: NeuralTextures only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 53.61 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: FaceSwap only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 71.61 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: NeuralTextures only; test: Deepfakes only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 95.6 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: NeuralTextures only; test: Face2Face only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 77.73 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: NeuralTextures only; test: FaceSwap only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 62.17 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: NeuralTextures only; test: NeuralTextures only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 97.97 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: NeuralTextures only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 83.36 | primary |
| Thakre 2026 | arXiv v2 Table 3 (PDF p.31) | FF++ (HQ) -> FF++ (HQ) test split | not explicitly stated for Table 3 ('intra-dataset setting using the HQ subset of FF++'); Sec. 4.1 says FF++ with four manipulations (DF, F2F, FS, NT) and that 'We trained separate models for each manipulation type'. Compared baselines (F3-Net, MAT, RECCE...) are conventionally all-four-manipulation numbers | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | Accuracy = 97.57; AUC = 99.49 | primary |
| Thakre 2026 | arXiv v2 Table 4 (PDF p.32) | FF++ (HQ) -> DeepFakeDetection (DFD, Google) - "curated subset of pristine and fake videos" | train: FF++ (HQ), manipulation subset not stated for cross-dataset experiment; test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed (not stated) | video | AUC = 92.07 | primary |
| Thakre 2026 | arXiv v2 Table 4 (PDF p.32) | FF++ (HQ) -> Celeb-DF (v2) | train: FF++ (HQ), manipulation subset not stated for cross-dataset experiment; test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed (not stated) | video | AUC = 74.92 | primary |
| Thakre 2026 | arXiv v2 Table 4 (PDF p.32) | FF++ (HQ) -> DFDC (Deepfake Detection Challenge) | train: FF++ (HQ), manipulation subset not stated for cross-dataset experiment; test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed (not stated) | video | AUC = 78.39 | primary |

#### CAST-B0

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: Deepfakes only; test: Deepfakes only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 100.00 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: Deepfakes only; test: Face2Face only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 86.29 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: Deepfakes only; test: FaceSwap only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 60.15 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: Deepfakes only; test: NeuralTextures only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 92.02 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Deepfakes subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: Deepfakes only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 84.65 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: Face2Face only; test: Deepfakes only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 94.33 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: Face2Face only; test: Face2Face only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 99.68 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: Face2Face only; test: FaceSwap only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 58.42 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: Face2Face only; test: NeuralTextures only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 82.74 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - Face2Face subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: Face2Face only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 83.79 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: FaceSwap only; test: Deepfakes only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 59.97 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: FaceSwap only; test: Face2Face only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 83.39 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: FaceSwap only; test: FaceSwap only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 99.29 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: FaceSwap only; test: NeuralTextures only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 51.11 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - FaceSwap subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: FaceSwap only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 73.44 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) Deepfakes test subset (+ pristine test videos) | train: NeuralTextures only; test: Deepfakes only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 95.27 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) Face2Face test subset (+ pristine test videos) | train: NeuralTextures only; test: Face2Face only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 74.42 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) FaceSwap test subset (+ pristine test videos) | train: NeuralTextures only; test: FaceSwap only (cross-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 51.33 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) NeuralTextures test subset (+ pristine test videos) | train: NeuralTextures only; test: NeuralTextures only (intra-manipulation) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 97.82 | primary |
| Thakre 2026 | arXiv v2 Table 2 (PDF p.29) | FF++ (HQ) - NeuralTextures subset only -> FF++ (HQ) mean over DF, F2F, FS, NT test subsets | train: NeuralTextures only; test: average of all four manipulation subsets (DF, F2F, FS, NT) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 79.71 | primary |
| Thakre 2026 | arXiv v2 Table 3 (PDF p.31) | FF++ (HQ) -> FF++ (HQ) test split | not explicitly stated for Table 3 ('intra-dataset setting using the HQ subset of FF++'); Sec. 4.1 says FF++ with four manipulations (DF, F2F, FS, NT) and that 'We trained separate models for each manipulation type'. Compared baselines (F3-Net, MAT, RECCE...) are conventionally all-four-manipulation numbers | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | Accuracy = 96.89; AUC = 98.98 | primary |
| Thakre 2026 | arXiv v2 Table 4 (PDF p.32) | FF++ (HQ) -> DeepFakeDetection (DFD, Google) - "curated subset of pristine and fake videos" | train: FF++ (HQ), manipulation subset not stated for cross-dataset experiment; test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed (not stated) | video | AUC = 93.31 | primary |
| Thakre 2026 | arXiv v2 Table 4 (PDF p.32) | FF++ (HQ) -> Celeb-DF (v2) | train: FF++ (HQ), manipulation subset not stated for cross-dataset experiment; test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed (not stated) | video | AUC = 76.98 | primary |
| Thakre 2026 | arXiv v2 Table 4 (PDF p.32) | FF++ (HQ) -> DFDC (Deepfake Detection Challenge) | train: FF++ (HQ), manipulation subset not stated for cross-dataset experiment; test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed (not stated) | video | AUC = 81.25 | primary |
| Thakre 2026 | arXiv v2 Table 5 (PDF p.35) | FF++ (HQ) - Face2Face, FaceSwap, NeuralTextures (three manipulations) -> FF++ (HQ) Deepfakes (unseen manipulation) | multi-source leave-one-out: train on the other three manipulations, test on Deepfakes only | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 97.04 | primary |
| Thakre 2026 | arXiv v2 Table 5 (PDF p.35) | FF++ (HQ) - Deepfakes, FaceSwap, NeuralTextures (three manipulations) -> FF++ (HQ) Face2Face (unseen manipulation) | multi-source leave-one-out: train on the other three manipulations, test on Face2Face only | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 87.50 | primary |
| Thakre 2026 | arXiv v2 Table 5 (PDF p.35) | FF++ (HQ) - Deepfakes, Face2Face, FaceSwap (three manipulations) -> FF++ (HQ) NeuralTextures (unseen manipulation) | multi-source leave-one-out: train on the other three manipulations, test on NeuralTextures only | c23 (paper: 'FF++ (HQ)'; Sec. 4.1: 'high-quality (c23) compressed version of FF++') | video | AUC = 84.50 | primary |

#### TSFF-Net

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Zhang 2024 | Table 3 (PDF p.11) | FF++ (HQ) -> FF++ (HQ) Deepfakes test split | per-manipulation column: Deepfakes (training subset composition not stated) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1 defines c23 = high quality (HQ)) | not stated | Accuracy = 97.7 | primary |
| Zhang 2024 | Table 3 (PDF p.11) | FF++ (HQ) -> FF++ (HQ) Face2Face test split | per-manipulation column: Face2Face (training subset composition not stated) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1 defines c23 = high quality (HQ)) | not stated | Accuracy = 91.0 | primary |
| Zhang 2024 | Table 3 (PDF p.11) | FF++ (HQ) -> FF++ (HQ) FaceSwap test split | per-manipulation column: FaceSwap (training subset composition not stated) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1 defines c23 = high quality (HQ)) | not stated | Accuracy = 98.9 | primary |
| Zhang 2024 | Table 3 (PDF p.11) | FF++ (HQ) -> FF++ (HQ) NeuralTextures test split | per-manipulation column: NeuralTextures (training subset composition not stated) | c23 (paper: 'FF++ (HQ)'; Sec. 4.1 defines c23 = high quality (HQ)) | not stated | Accuracy = 90.0 | primary |
| Zhang 2024 | Table 4 (PDF p.12) | FF++ (LQ) -> FF++ (LQ) Deepfakes test split | per-manipulation column: Deepfakes (training subset composition not stated) | c40 (paper: 'FF++ (LQ)'; Sec. 4.1 defines c40 = low quality (LQ)) | not stated | Accuracy = 85.1 | primary |
| Zhang 2024 | Table 4 (PDF p.12) | FF++ (LQ) -> FF++ (LQ) Face2Face test split | per-manipulation column: Face2Face (training subset composition not stated) | c40 (paper: 'FF++ (LQ)'; Sec. 4.1 defines c40 = low quality (LQ)) | not stated | Accuracy = 83.1 | primary |
| Zhang 2024 | Table 4 (PDF p.12) | FF++ (LQ) -> FF++ (LQ) FaceSwap test split | per-manipulation column: FaceSwap (training subset composition not stated) | c40 (paper: 'FF++ (LQ)'; Sec. 4.1 defines c40 = low quality (LQ)) | not stated | Accuracy = 78.5 | primary |
| Zhang 2024 | Table 4 (PDF p.12) | FF++ (LQ) -> FF++ (LQ) NeuralTextures test split | per-manipulation column: NeuralTextures (training subset composition not stated) | c40 (paper: 'FF++ (LQ)'; Sec. 4.1 defines c40 = low quality (LQ)) | not stated | Accuracy = 66.0 | primary |
| Zhang 2024 | Table 5 (PDF p.12) | FF++ (HQ) -> Celeb-DF (version not named; 590 real / 5,639 fake videos = v2 counts) | train: FF++ (HQ), manipulation subset not stated; test: whole Celeb-DF | train c23 (FF++ HQ); test: Celeb-DF as distributed | not stated | AUC = 77.10 | primary |

#### ISTVT

| Source | Location | Train -> Test | Subset | Comp. | Unit | Metric = value (as printed) | P/S |
|---|---|---|---|---|---|---|---|
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | HQ (c23) | not stated | Accuracy (%) = 99.8 | secondary (SFormer paper) |
| Kingra 2024 | Table 5 (PDF p.11) | FF++ (DF) -> FF++ (DF) | DeepFakes | LQ (c40) | not stated | Accuracy (%) = 99.6 | secondary (SFormer paper) |
| Zhao 2023 | full text not accessed (paywalled) |  ->  |  |  |  | not_accessible = not accessible | primary (not accessed) |
| Xu 2023 | TALL Table 2 (arXiv v3 PDF p.5) | FF++ (HQ) -> FF++ (HQ) | not stated in TALL (FF++ overall; all four manipulations implied) | c23 (TALL: "FF++ (HQ)"; DIP Table I labels same value "FF++ (C23)") | video | Accuracy = 99.00 | secondary (reported in TALL, ICCV 2023) |
| Xu 2023 | TALL Table 2 (arXiv v3 PDF p.5) | FF++ (LQ) -> FF++ (LQ) | not stated in TALL (FF++ overall; all four manipulations implied) | c40 (TALL: "FF++ (LQ)"; DIP Table I labels same value "FF++ (C40)") | video | Accuracy = 96.15 | secondary (reported in TALL, ICCV 2023) |
| Xu 2023 | TALL Table 3 (arXiv v3 PDF p.6) | FF++ (HQ) -> Celeb-DF (v2) (TALL: "Celeb-DF (CDF)") | train: FF++ (HQ); ISTVT training subset not stated in TALL (TALL itself follows the LipForensics protocol [18], which trains on all four manipulations); test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed | video | AUC = 84.10 | secondary (reported in TALL, ICCV 2023) |
| Xu 2023 | TALL Table 3 (arXiv v3 PDF p.6) | FF++ (HQ) -> DFDC | train: FF++ (HQ); ISTVT training subset not stated in TALL (TALL itself follows the LipForensics protocol [18], which trains on all four manipulations); test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed | video | AUC = 74.20 | secondary (reported in TALL, ICCV 2023) |
| Xu 2023 | TALL Table 3 (arXiv v3 PDF p.6) | FF++ (HQ) -> FaceShifter (FSh) | train: FF++ (HQ); ISTVT training subset not stated in TALL (TALL itself follows the LipForensics protocol [18], which trains on all four manipulations); test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed | video | AUC = 99.30 | secondary (reported in TALL, ICCV 2023) |
| Xu 2023 | TALL Table 3 (arXiv v3 PDF p.6) | FF++ (HQ) -> DeeperForensics-1.0 (DFo) | train: FF++ (HQ); ISTVT training subset not stated in TALL (TALL itself follows the LipForensics protocol [18], which trains on all four manipulations); test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed | video | AUC = 98.60 | secondary (reported in TALL, ICCV 2023) |
| Xu 2023 | TALL Table 3 (arXiv v3 PDF p.6) | FF++ (HQ) -> mean over CDF, DFDC, FSh, DFo | train: FF++ (HQ); ISTVT training subset not stated in TALL (TALL itself follows the LipForensics protocol [18], which trains on all four manipulations); test: whole target dataset | train c23 (FF++ HQ); test: target dataset as distributed | video | AUC = 89.10 | secondary (reported in TALL, ICCV 2023) |
| He 2024 | GazeForensics Table 1 (arXiv v2 PDF p.17) | FF++ c23 (HQ) (training composition not stated) -> FF++ c23 (HQ) Deepfakes test subset | Deepfakes only (per-manipulation column) | c23 (HQ) | not stated | Accuracy = 0.9964 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 1 (arXiv v2 PDF p.17) | FF++ c23 (HQ) (training composition not stated) -> FF++ c23 (HQ) Face2Face test subset | Face2Face only (per-manipulation column) | c23 (HQ) | not stated | Accuracy = 0.9964 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 1 (arXiv v2 PDF p.17) | FF++ c23 (HQ) (training composition not stated) -> FF++ c23 (HQ) FaceSwap test subset | FaceSwap only (per-manipulation column) | c23 (HQ) | not stated | Accuracy = 1.0 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 1 (arXiv v2 PDF p.17) | FF++ c23 (HQ) (training composition not stated) -> FF++ c23 (HQ) NeuralTextures test subset | NeuralTextures only (per-manipulation column) | c23 (HQ) | not stated | Accuracy = 0.9676 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 1 (arXiv v2 PDF p.17) | FF++ c23 (HQ) -> FF++ c23 (HQ) average over DF/F2F/FS/NT | average of four per-manipulation accuracies | c23 (HQ) | not stated | Accuracy = 0.9901 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 2 (arXiv v2 PDF p.18) | FF++ c40 (LQ) (training composition not stated) -> FF++ c40 (LQ) Deepfakes test subset | Deepfakes only (per-manipulation column) | c40 (LQ) | not stated | Accuracy = 0.9893 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 2 (arXiv v2 PDF p.18) | FF++ c40 (LQ) (training composition not stated) -> FF++ c40 (LQ) Face2Face test subset | Face2Face only (per-manipulation column) | c40 (LQ) | not stated | Accuracy = 0.9607 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 2 (arXiv v2 PDF p.18) | FF++ c40 (LQ) (training composition not stated) -> FF++ c40 (LQ) FaceSwap test subset | FaceSwap only (per-manipulation column) | c40 (LQ) | not stated | Accuracy = 0.9750 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 2 (arXiv v2 PDF p.18) | FF++ c40 (LQ) (training composition not stated) -> FF++ c40 (LQ) NeuralTextures test subset | NeuralTextures only (per-manipulation column) | c40 (LQ) | not stated | Accuracy = 0.9214 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 2 (arXiv v2 PDF p.18) | FF++ c40 (LQ) -> FF++ c40 (LQ) average over DF/F2F/FS/NT | average of four per-manipulation accuracies | c40 (LQ) | not stated | Accuracy = 0.9616 | secondary (reported in GazeForensics, Neural Networks 2024) |
| He 2024 | GazeForensics Table 3 (arXiv v2 PDF p.19) | Celeb-DF -> Celeb-DF (intra-dataset) | n/a (Celeb-DF) | n/a (Celeb-DF as distributed) | not stated | Accuracy = 0.9981 | secondary (reported in GazeForensics, Neural Networks 2024) |
| Hussain 2026 | Table 1 (HTML, PMC12827133) | FaceForensics++ (not specified) -> FaceForensics++ DeepFakes | DeepFakes column | not stated | not stated | Accuracy = 98.74 ± 0.31 | secondary (reported in Hussain et al., Frontiers in Big Data 2026) |