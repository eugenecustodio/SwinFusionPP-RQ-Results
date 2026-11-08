### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | family | model | train_condition | test_condition | metric_std | value | level | subset | location | primary_or_secondary | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | CAST | CAST-B0 | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7698 | video | unstated_or_other | arXiv v2 Table 4 (PDF p.32) | primary | Thakre et al. 2026 |
| A | CAST | CAST-B5 | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7492 | video | unstated_or_other | arXiv v2 Table 4 (PDF p.32) | primary | Thakre et al. 2026 |
| A | FTCN | FTCN | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8690 | video | unstated_or_other | Table 3 (PDF p.6) | secondary (TALL paper; matches FTCN Table 4) | Xu et al. 2023 |
| A | FTCN | FTCN (+TT) | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8690 | video | not_applicable | Table 4 (PDF p.6) | primary | Zheng et al. 2021 |
| A | I3D | I3D (I3D-RGB*) | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7824 | video | not_applicable | Table 1 (PDF p.5) | original third-party run (TALL paper, own implementation) | Xu et al. 2023 |
| A | ISTVT | ISTVT | ffpp_c23 | celeb_df_v2 | roc_auc | 0.8410 | video | all_four | TALL Table 3 (arXiv v3 PDF p.6) | secondary (reported in TALL, ICCV 2023) | Xu et al. 2023 |
| A | TALL-Swin | TALL-Swin | ffpp_c23 | celeb_df_v2 | roc_auc | 0.9079 | video | not_applicable | Table 1 and Table 3 (PDF p.5-6) | primary | Xu et al. 2023 |
| A | Xception | Xception | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7370 | video | unstated_or_other | Table 4 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| A | FTCN | FTCN (+TT) | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.9880 | video | not_applicable | Table 4 (PDF p.6) | primary | Zheng et al. 2021 |
| A | ISTVT | ISTVT | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.9860 | video | all_four | TALL Table 3 (arXiv v3 PDF p.6) | secondary (reported in TALL, ICCV 2023) | Xu et al. 2023 |
| A | TALL-Swin | TALL-Swin | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.9962 | video | not_applicable | Table 3 (PDF p.6) | primary | Xu et al. 2023 |
| A | Xception | Xception | ffpp_c23 | deeperforensics_1_0 | roc_auc | 0.8450 | video | unstated_or_other | Table 4 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| B | STIL | STIL | ffpp_c40 | celeb_df_v2 | roc_auc | 0.7558 | unstated | not_applicable | Table 3 (PDF p.6) | primary | Gu et al. 2021 |
| B | TSFF-Net | TSFF-Net | ffpp_c23 | celeb_df_v2 | roc_auc | 0.7710 | unstated | unstated_or_other | Table 5 (PDF p.12) | primary | Zhang et al. 2024 |
| B | Xception | Xception | ffpp_c23 | celeb_df_v2 | roc_auc | 0.6530 | frame | not_applicable | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c40 | celeb_df_v2 | roc_auc | 0.6550 | frame | not_applicable | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception-c40 | ffpp_c40 | celeb_df_v2 | roc_auc | 0.6550 | unstated | unstated_or_other | Table 3 (PDF p.6) | secondary (STIL paper, copied) | Gu et al. 2021 |
