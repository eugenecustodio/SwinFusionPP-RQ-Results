# RQ2 — writing package (v020)

> What is the performance of SwinFusion++ relative to established baselines when evaluated on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0?

**Status:** Results complete.

## Table 1 — SwinFusion++ (ours, BO-selected, 3-seed ensemble)

### Video-level, held-out test

| dataset | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 |
|---|---|---|---|---|---|---|---|
| Celeb-DF v2 | 0.9983 | 0.9963 | 1.0000 | 0.9836 | 0.9976 | 0.9834 | 0.9904 |
| DeeperForensics-1.0 | 0.9954 | 0.9874 | 1.0000 | 0.9851 | 1.0000 | 0.9701 | 0.9848 |
| FF++ C23 (HQ) | 0.9964 | 0.9886 | 1.0000 | 0.9821 | 0.9787 | 0.9857 | 0.9822 |
| FF++ C40 (LQ) | 0.9941 | 0.9875 | 0.9989 | 0.9607 | 0.9388 | 0.9857 | 0.9617 |

## Table 1b — Xception reproduced in the preliminary study

### Video-level, seed 1701, values as fractions

Preliminary study by the same authors (references/preliminary/SwinFusionPP_UERJ_Revised.pdf): earlier pipeline (MTCNN face cache, three test anchors, fixed recipe, no hyperparameter search). FF++ C23/C40 test size matches (280 videos); Celeb-DF/DeeperForensics test populations differ (859 / 2,385 analysed vs 978 / 402 here). Context, not a paired comparison. I3D and SFormer have no verified local numbers in the preliminary study (blocked); they appear only as published values.

| model | train_condition | test_condition | roc_auc | f1 | accuracy | location |
|---|---|---|---|---|---|---|
| Xception (reproduced) | Celeb-DF v2 | Celeb-DF v2 | 0.6480 | 0.9140 | 0.8417 | Table 7 |
| Xception (reproduced) | DeeperForensics-1.0 | DeeperForensics-1.0 | 0.9978 | 0.5821 | 0.4600 | Table 7 |
| Xception (reproduced) | FF++ C23 (HQ) | FF++ C23 (HQ) | 0.7725 | 0.6886 | 0.6964 | Table 7 |
| Xception (reproduced) | FF++ C40 (LQ) | FF++ C40 (LQ) | 0.8109 | 0.7429 | 0.7429 | Table 7 |

## Table 2 — Published results, comparable rows (Tier A/B)

### Values as fractions

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.

| tier | family | model | train_condition | test_condition | metric_std | value | level | subset | location | primary_or_secondary | source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | I3D | I3D | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9923 | video | unstated_or_other | Table 1 (PDF p.7) | original third-party run (S-MIL paper) | Li et al. 2020 |
| A | I3D | I3D | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9923 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (STIL paper; identical to S-MIL Table 1) | Gu et al. 2021 |
| A | I3D | I3D | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9920 | video | unstated_or_other | Table 5 (PDF p.11) | secondary (SFormer paper; copied) | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9504 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9910 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9910 | video | unstated_or_other | Table 5 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | precision | 0.9435 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | precision | 0.9970 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | recall | 0.9590 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | celeb_df_v2 | celeb_df_v2 | recall | 0.9900 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | STIL | STIL | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9978 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Gu et al. 2021 |
| A | STIL | STIL | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9980 | video | unstated_or_other | Table 5 (PDF p.11) | secondary (SFormer paper; copied) | Kingra et al. 2024 |
| A | Xception | Xception (XN-avg) | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9944 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (STIL paper; same as S-MIL Table 1) | Gu et al. 2021 |
| A | Xception | Xception (XN-avg) | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9940 | video | unstated_or_other | Table 5 (PDF p.11) | secondary (SFormer paper) | Kingra et al. 2024 |
| A | FTCN | FTCN (+TT) | deeperforensics_1_0 | deeperforensics_1_0 | roc_auc | 1.0000 | video | unstated_or_other | Supplement Table 1 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| A | I3D | I3D | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 0.7925 | video | unstated_or_other | Table 4 / Table 6 col. 2 (PDF p.9-10) | original third-party run (DeeperForensics paper) | Jiang et al. 2020 |
| A | I3D | I3D | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 1.0000 | video | unstated_or_other | Table 5 (PDF p.9) | original third-party run (DeeperForensics paper) | Jiang et al. 2020 |
| A | I3D | I3D | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 0.9075 | video | unstated_or_other | Table 5 (PDF p.9) | original third-party run (DeeperForensics paper) | Jiang et al. 2020 |
| A | I3D | I3D | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 0.9688 | video | unstated_or_other | Table 5 (PDF p.9) | original third-party run (DeeperForensics paper) | Jiang et al. 2020 |
| A | SFormer | SFormer | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 0.9967 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 1.0000 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | deeperforensics_1_0 | deeperforensics_1_0 | precision | 0.9967 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | deeperforensics_1_0 | deeperforensics_1_0 | precision | 1.0000 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | deeperforensics_1_0 | deeperforensics_1_0 | recall | 0.9967 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | deeperforensics_1_0 | deeperforensics_1_0 | recall | 1.0000 | video | unstated_or_other | Table 2(a)/(b) (PDF p.8) | primary | Kingra et al. 2024 |
| A | Xception | Xception | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 0.7700 | video | unstated_or_other | Table 4 (PDF p.9) | secondary (benchmark run in DeeperForensics-1.0 paper) | Jiang et al. 2020 |
| A | Xception | Xception | deeperforensics_1_0 | deeperforensics_1_0 | accuracy | 1.0000 | video | unstated_or_other | Table 5 (PDF p.9) | secondary (benchmark run in DeeperForensics-1.0 paper) | Jiang et al. 2020 |
| A | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9990 | video | deepfakes | Table 2 (PDF p.6) | primary | Zheng et al. 2021 |
| A | FTCN | FTCN (+TT, L x1) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9810 | video | deepfakes | Table 8 (PDF p.8) | primary | Zheng et al. 2021 |
| A | I3D | I3D | ffpp_c23 | ffpp_c23 | accuracy | 0.9286 | video | deepfakes | Table 2 (PDF p.7) | original third-party run (S-MIL paper; baselines retrained with official code) | Li et al. 2020 |
| A | I3D | I3D | ffpp_c23 | ffpp_c23 | accuracy | 0.9286 | video | deepfakes | Table 1 (PDF p.5) | secondary (STIL paper; identical to S-MIL Table 2) | Gu et al. 2021 |
| A | I3D | I3D | ffpp_c23 | ffpp_c23 | accuracy | 0.9290 | video | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper; copied) | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | accuracy | 0.9850 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | accuracy | 0.9990 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | accuracy | 0.8416 | video | deepfakes | Table 4 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | accuracy | 0.9933 | video | deepfakes | Table 4 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | accuracy | 0.9990 | video | deepfakes | Table 5 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | precision | 0.9932 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | precision | 1.0000 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | recall | 0.9767 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c23 | ffpp_c23 | recall | 0.9910 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | STIL | STIL | ffpp_c23 | ffpp_c23 | accuracy | 0.9960 | video | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper; copied) | Kingra et al. 2024 |
| A | Xception | Xception (XN-avg) | ffpp_c23 | ffpp_c23 | accuracy | 1.0000 | video | deepfakes | Table 2 (PDF p.7) | secondary (S-MIL paper, Li et al. 2020) | Li et al. 2020 |
| A | Xception | Xception (XN-avg) | ffpp_c23 | ffpp_c23 | accuracy | 0.9893 | video | deepfakes | Table 1 (PDF p.5) | secondary (STIL paper) | Gu et al. 2021 |
| A | Xception | Xception (XN-avg) | ffpp_c23 | ffpp_c23 | accuracy | 0.9890 | video | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper; copied from STIL/S-MIL literature) | Kingra et al. 2024 |
| A | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9390 | video | deepfakes | Table 2 (PDF p.6) | secondary (FTCN paper, from LipForensics) | Zheng et al. 2021 |
| A | I3D | I3D | ffpp_c40 | ffpp_c40 | accuracy | 0.9107 | video | deepfakes | Table 2 (PDF p.7) | original third-party run (S-MIL paper) | Li et al. 2020 |
| A | I3D | I3D | ffpp_c40 | ffpp_c40 | accuracy | 0.9107 | video | deepfakes | Table 1 (PDF p.5) | secondary (STIL paper; identical to S-MIL Table 2) | Gu et al. 2021 |
| A | I3D | I3D | ffpp_c40 | ffpp_c40 | accuracy | 0.9110 | video | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper; copied) | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.9482 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.9815 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.8628 | video | deepfakes | Table 4 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.9650 | video | deepfakes | Table 4 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.5868 | video | deepfakes | Table 4 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.9767 | video | deepfakes | Table 4 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | accuracy | 0.9815 | video | deepfakes | Table 5 (PDF p.11) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | precision | 0.9584 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | precision | 0.9950 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | recall | 0.9234 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | SFormer | SFormer | ffpp_c40 | ffpp_c40 | recall | 0.9430 | video | deepfakes | Table 3 (PDF p.9) | primary | Kingra et al. 2024 |
| A | STIL | STIL | ffpp_c40 | ffpp_c40 | accuracy | 0.9821 | video | deepfakes | Table 1 (PDF p.5) | primary | Gu et al. 2021 |
| A | STIL | STIL | ffpp_c40 | ffpp_c40 | accuracy | 0.9820 | video | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper; copied) | Kingra et al. 2024 |
| A | Xception | Xception (XN-avg) | ffpp_c40 | ffpp_c40 | accuracy | 0.9714 | video | deepfakes | Table 2 (PDF p.7) | secondary (S-MIL paper, Li et al. 2020) | Li et al. 2020 |
| A | Xception | Xception (XN-avg) | ffpp_c40 | ffpp_c40 | accuracy | 0.9678 | video | deepfakes | Table 1 (PDF p.5) | secondary (STIL paper) | Gu et al. 2021 |
| A | Xception | Xception (XN-avg) | ffpp_c40 | ffpp_c40 | accuracy | 0.9680 | video | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper; copied from STIL/S-MIL literature) | Kingra et al. 2024 |
| B | I3D | I3D | celeb_df_v2 | celeb_df_v2 | accuracy | 0.9228 | unstated | unstated_or_other | Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | secondary (Saikia et al. 2022 Table IV, copied from de Lima et al. 2020) | de Lima et al. 2020 |
| B | I3D | I3D | celeb_df_v2 | celeb_df_v2 | roc_auc | 0.9759 | unstated | unstated_or_other | Saikia et al. 2022 Table IV (row 'De Lima et al. [39]', model I3D), PDF p.6 | secondary (Saikia et al. 2022 Table IV, copied from de Lima et al. 2020) | de Lima et al. 2020 |
| B | FTCN | FTCN | ffpp_c23 | ffpp_c23 | accuracy | 0.9790 | unstated | deepfakes | Table 5 (PDF p.11) | secondary (SFormer paper) | Kingra et al. 2024 |
| B | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | accuracy | 0.9910 | unstated | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | FTCN | FTCN (+TT) | ffpp_c23 | ffpp_c23 | roc_auc | 0.9980 | video | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | I3D | I3D | ffpp_c23 | ffpp_c23 | accuracy | 0.9670 | clip | deepfakes | Table 4 (PDF p.8) | original third-party run (WildDeepfake paper) | Zi et al. 2020 |
| B | STIL | STIL | ffpp_c23 | ffpp_c23 | accuracy | 0.9964 | video | unstated_or_other | Table 1 (PDF p.5) | primary | Gu et al. 2021 |
| B | TALL-Swin | TALL-Swin | ffpp_c23 | ffpp_c23 | accuracy | 0.9865 | video | all_four | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | TALL-Swin | TALL-Swin | ffpp_c23 | ffpp_c23 | roc_auc | 0.9987 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | accuracy | 0.9885 | frame | deepfakes | Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | primary | Rössler et al. 2019 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | accuracy | 0.9749 | frame | all_four | Appendix B, Table 5 (PDF p.13) | primary | Rössler et al. 2019 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | accuracy | 0.9573 | frame | all_four | Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | primary | Rössler et al. 2019 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | accuracy | 0.9962 | frame | deepfakes | Table 3 (PDF p.8) | secondary (WildDeepfake paper, Zi et al. 2020) | Zi et al. 2020 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | accuracy | 0.9573 | video | all_four | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | Xception | XceptionNet (Rossler et al. 2019) | ffpp_c23 | ffpp_c23 | accuracy | 0.9640 | unstated | unstated_or_other | Table 3 (PDF p.11), row "XceptionNet [4]" | secondary (reported in TSFF-Net, PLOS ONE 2024) | Zhang et al. 2024 |
| B | Xception | XceptionNet (Rossler et al. 2019) | ffpp_c23 | ffpp_c23 | accuracy | 0.8690 | unstated | unstated_or_other | Table 3 (PDF p.11), row "XceptionNet [4]" | secondary (reported in TSFF-Net, PLOS ONE 2024) | Zhang et al. 2024 |
| B | Xception | XceptionNet (Rossler et al. 2019) | ffpp_c23 | ffpp_c23 | accuracy | 0.9030 | unstated | unstated_or_other | Table 3 (PDF p.11), row "XceptionNet [4]" | secondary (reported in TSFF-Net, PLOS ONE 2024) | Zhang et al. 2024 |
| B | Xception | XceptionNet (Rossler et al. 2019) | ffpp_c23 | ffpp_c23 | accuracy | 0.8070 | unstated | unstated_or_other | Table 3 (PDF p.11), row "XceptionNet [4]" | secondary (reported in TSFF-Net, PLOS ONE 2024) | Zhang et al. 2024 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9970 | frame | deepfakes | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c23 | ffpp_c23 | roc_auc | 0.9630 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | FTCN | FTCN (+TT) | ffpp_c40 | ffpp_c40 | roc_auc | 0.9830 | video | unstated_or_other | Supplement Table 2 (supp. PDF p.2) | primary (supplementary) | Zheng et al. 2021 |
| B | I3D | I3D | ffpp_c40 | ffpp_c40 | accuracy | 0.9318 | clip | deepfakes | Table 4 (PDF p.8) | original third-party run (WildDeepfake paper) | Zi et al. 2020 |
| B | STIL | STIL | ffpp_c40 | ffpp_c40 | roc_auc | 0.9712 | unstated | deepfakes | Table 3 (PDF p.6) | primary | Gu et al. 2021 |
| B | TALL-Swin | TALL-Swin | ffpp_c40 | ffpp_c40 | accuracy | 0.9282 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | TALL-Swin | TALL-Swin | ffpp_c40 | ffpp_c40 | roc_auc | 0.9457 | video | unstated_or_other | Table 2 (PDF p.5) | primary | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.9428 | frame | deepfakes | Appendix B, Table 4 (PDF p.13); numbers behind Fig. 6 | primary | Rössler et al. 2019 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.9336 | frame | all_four | Appendix B, Table 5 (PDF p.13) | primary | Rössler et al. 2019 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.8100 | frame | all_four | Section 4.2.2, Table 1 (PDF p.7); also Fig. 7 | primary | Rössler et al. 2019 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.9025 | frame | deepfakes | Table 3 (PDF p.8) | secondary (WildDeepfake paper, Zi et al. 2020) | Zi et al. 2020 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.8686 | video | all_four | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.9346 | frame | deepfakes | Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | secondary (Sabir et al. 2019 Table 1, copied from Roessler et al. FF++ paper) | Roessler et al. 2019 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.8980 | frame | unstated_or_other | Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | secondary (Sabir et al. 2019 Table 1, copied from Roessler et al. FF++ paper) | Roessler et al. 2019 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | accuracy | 0.9272 | frame | unstated_or_other | Sabir et al. Table 1, column 'FF++ [34]', PDF p.4 | secondary (Sabir et al. 2019 Table 1, copied from Roessler et al. FF++ paper) | Roessler et al. 2019 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | roc_auc | 0.9550 | frame | deepfakes | Table 4 (PDF p.8) | secondary (Celeb-DF paper, Li et al. 2020) | Li et al. 2020 |
| B | Xception | Xception | ffpp_c40 | ffpp_c40 | roc_auc | 0.8930 | video | unstated_or_other | Table 2 (PDF p.5) | secondary (TALL paper) | Xu et al. 2023 |
| B | Xception | Xception-c40 | ffpp_c40 | ffpp_c40 | roc_auc | 0.9550 | unstated | deepfakes | Table 3 (PDF p.6) | secondary (STIL paper, copied) | Gu et al. 2021 |

## Table 3 — Published results on other data (Tier C, context only)

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

## Caveats

Published values come from each paper's own protocol (splits, frame sampling, face crops, manipulation subsets, unit of evaluation). They are context, not a matched comparison; no statistical test is run against them. Tier A = closest protocol match, Tier B = same dataset with a different/unstated unit or subset.
- Native inputs and optimisation budgets differ across papers and must be disclosed.
