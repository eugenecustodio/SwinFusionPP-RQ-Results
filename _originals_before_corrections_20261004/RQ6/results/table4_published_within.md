### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | family | model | train_condition | test_condition | metric_std | value | level | subset | location | primary_or_secondary | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | FTCN | FTCN (+TT) | deeperforensics_1_0 | deeperforensics_1_0 | roc_auc | 1.0000 | video | unstated_or_other | Supplement Table 1 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 1.0000 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8629 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.6015 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9202 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8465 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9433 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5997 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9527 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9704 | video | deepfakes | arXiv v2 Table 5 (PDF p.35) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9995 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8243 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5988 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8641 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8216 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8864 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5813 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9560 | video | deepfakes | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| A | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9990 | video | deepfakes | Table 2 (PDF p.6) | primary | Zheng et al. 2021 |
| A | FTCN | FTCN (+TT, L x1) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9810 | video | deepfakes | Table 8 (PDF p.8) | primary | Zheng et al. 2021 |
| A | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9390 | video | deepfakes | Table 2 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| B | Chen et al. 2022 | Chen et al. 2022 Xception + spatiotemporal attention + ConvLSTM (Xception-ConvLSTM/'Xception-LSTM') | celeb_df_v2 | celeb_df_v2 | roc_auc | 0.9991 | unstated | unstated_or_other | Hriez 2025 Table 6 (top-10 AUC, Celeb-DF; ref [157]), journal p.143972 (PDF p.16) | secondary (Hriez 2025 IEEE Access review) | Hriez et al. 2025 |
| B | I3D | I3D | celeb_df_v2 | celeb_df_v2 | roc_auc | 0.9759 | unstated | unstated_or_other | Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | secondary (Saikia et al. 2022 Table IV, copied from de Lima et al. 2020) | de Lima et al. 2020 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9968 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5842 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8274 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8379 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8339 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9929 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5111 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7344 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7442 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5133 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9782 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7971 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9898 | video | unstated_or_other | arXiv v2 Table 3 (PDF p.31) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8750 | video | unstated_or_other | arXiv v2 Table 5 (PDF p.35) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B0 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8450 | video | unstated_or_other | arXiv v2 Table 5 (PDF p.35) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9861 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.6569 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7019 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8078 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7471 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9999 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.5361 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7161 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.7773 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.6217 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9797 | video | unstated_or_other | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.8336 | video | all_four | arXiv v2 Table 2 (PDF p.29) | primary | Thakre et al. 2026 |
| B | CAST | CAST-B5 | ffpp_c23 | ffpp_c23 | roc_auc | 0.9949 | video | unstated_or_other | arXiv v2 Table 3 (PDF p.31) | primary | Thakre et al. 2026 |
| B | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9980 | video | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | TALL-Swin | TALL-Swin | ffpp_c23 | ffpp_c23 | roc_auc | 0.9987 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9970 | frame | deepfakes | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9630 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | FTCN | FTCN (+TT) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9830 | video | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | STIL | STIL | ffpp_c40 | ffpp_c40 | roc_auc | 0.9712 | unstated | deepfakes | Table 3 (PDF p.6) | primary | Gu et al. 2021 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9949 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9593 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9930 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9950 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9808 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: densenet frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9930 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9923 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9609 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-1 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9857 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9916 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9762 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-0 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9896 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9889 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9824 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN variant: resnet50 frame-5 BiGRU-1 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9891 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9959 | unstated | deepfakes | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9843 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | Sabir et al. | Sabir et al. 2019 RCN, DenseNet + landmark alignment + BiGRU, 5 frames (proposed/best) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9941 | unstated | unstated_or_other | Fig. 2 legend (ROC plots), PDF p.5 | primary | Sabir et al. 2019 |
| B | TALL-Swin | TALL-Swin | ffpp_c40 | ffpp_c40 | roc_auc | 0.9457 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | roc_auc | 0.9550 | frame | deepfakes | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | roc_auc | 0.8930 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | Xception | Xception-c40 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9550 | unstated | deepfakes | Table 3 (PDF p.6) | secondary (STIL paper, copied) | Gu et al. 2021 |
