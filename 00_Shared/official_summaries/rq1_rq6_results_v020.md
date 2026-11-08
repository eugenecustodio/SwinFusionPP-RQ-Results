# RQ1 / RQ6 held-out results (v020, staged track A-04)

Three-seed mean-logit ensembles; ROC-AUC with 5000-draw class-preserving cluster-bootstrap 95% CI;
thresholds/temperatures from source validation only; full test sets with the v020 exposure disclosure.

Presented model: SwinFusion++ with BO-selected training parameters (dataset_specific_bo); baselines use the shared fixed recipe.
Paired tests use the plain variant; tta_flip is the pre-declared flip-TTA variant (A-13), reported descriptively.
Families: RQ1/RQ6 = presented SwinFusion++ vs baselines; *_secondary = recipe-matched; RQ4_controls(_transfer) = matched controls (C23-trained).

| Training | Test | Model | Regimen | Variant | ROC-AUC [95% CI] | Acc | Prec | Rec | F1 | seed AUC mean±SD |
|---|---|---|---|---|---|---|---|---|---|---|
| celeb_df_v2 | celeb_df_v2 | swin_b | fixed_no_bo | plain | 0.9958 [0.9925, 0.9990] | 0.9540 | 0.9963 | 0.9502 | 0.9727 | 0.9956±0.0002 |
| celeb_df_v2 | celeb_df_v2 | swin_b | fixed_no_bo | tta_flip | 0.9962 [0.9926, 0.9992] | 0.9622 | 0.9951 | 0.9609 | 0.9777 | 0.9960±0.0002 |
| celeb_df_v2 | celeb_df_v2 | swinfusionpp | dataset_specific_bo | plain | 0.9983 [0.9963, 1.0000] | 0.9836 | 0.9976 | 0.9834 | 0.9904 | 0.9974±0.0008 |
| celeb_df_v2 | celeb_df_v2 | swinfusionpp | dataset_specific_bo | tta_flip | 0.9983 [0.9966, 0.9999] | 0.9796 | 0.9976 | 0.9786 | 0.9880 | 0.9977±0.0008 |
| celeb_df_v2 | celeb_df_v2 | swinfusionpp | fixed_no_bo | plain | 0.9951 [0.9905, 0.9995] | 0.9775 | 0.9928 | 0.9810 | 0.9869 | 0.9939±0.0022 |
| celeb_df_v2 | celeb_df_v2 | swinfusionpp | fixed_no_bo | tta_flip | 0.9957 [0.9917, 0.9997] | 0.9601 | 0.9975 | 0.9561 | 0.9764 | 0.9944±0.0022 |
| celeb_df_v2 | celeb_df_v2 | video_swin_b | fixed_no_bo | plain | 0.9958 [0.9915, 0.9994] | 0.9826 | 0.9928 | 0.9870 | 0.9899 | 0.9954±0.0003 |
| celeb_df_v2 | celeb_df_v2 | video_swin_b | fixed_no_bo | tta_flip | 0.9965 [0.9932, 0.9995] | 0.9826 | 0.9893 | 0.9905 | 0.9899 | 0.9963±0.0004 |
| deeperforensics_1_0 | deeperforensics_1_0 | swin_b | fixed_no_bo | plain | 0.9966 [0.9892, 1.0000] | 0.9776 | 1.0000 | 0.9552 | 0.9771 | 0.9968±0.0009 |
| deeperforensics_1_0 | deeperforensics_1_0 | swin_b | fixed_no_bo | tta_flip | 0.9966 [0.9894, 1.0000] | 0.9801 | 1.0000 | 0.9602 | 0.9797 | 0.9968±0.0008 |
| deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp | dataset_specific_bo | plain | 0.9954 [0.9874, 1.0000] | 0.9851 | 1.0000 | 0.9701 | 0.9848 | 0.9952±0.0016 |
| deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp | dataset_specific_bo | tta_flip | 0.9956 [0.9881, 1.0000] | 0.9876 | 1.0000 | 0.9751 | 0.9874 | 0.9954±0.0016 |
| deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp | fixed_no_bo | plain | 0.9974 [0.9921, 1.0000] | 0.9876 | 1.0000 | 0.9751 | 0.9874 | 0.9971±0.0011 |
| deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp | fixed_no_bo | tta_flip | 0.9976 [0.9926, 1.0000] | 0.9900 | 1.0000 | 0.9801 | 0.9899 | 0.9972±0.0011 |
| deeperforensics_1_0 | deeperforensics_1_0 | video_swin_b | fixed_no_bo | plain | 0.9945 [0.9842, 0.9999] | 0.9701 | 0.9948 | 0.9453 | 0.9694 | 0.9944±0.0006 |
| deeperforensics_1_0 | deeperforensics_1_0 | video_swin_b | fixed_no_bo | tta_flip | 0.9944 [0.9840, 0.9999] | 0.9751 | 0.9948 | 0.9552 | 0.9746 | 0.9943±0.0005 |
| ffpp_c23 | ffpp_c23 | capacity_control | fixed_no_bo | plain | 0.9945 [0.9848, 0.9999] | 0.9857 | 0.9928 | 0.9786 | 0.9856 | 0.9944±0.0011 |
| ffpp_c23 | ffpp_c23 | capacity_control | fixed_no_bo | tta_flip | 0.9945 [0.9847, 0.9999] | 0.9857 | 0.9928 | 0.9786 | 0.9856 | 0.9943±0.0011 |
| ffpp_c23 | ffpp_c23 | swin_b | fixed_no_bo | plain | 0.9965 [0.9906, 0.9999] | 0.9786 | 0.9718 | 0.9857 | 0.9787 | 0.9965±0.0007 |
| ffpp_c23 | ffpp_c23 | swin_b | fixed_no_bo | tta_flip | 0.9974 [0.9934, 0.9999] | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9970±0.0009 |
| ffpp_c23 | ffpp_c23 | swinfusionpp | dataset_specific_bo | plain | 0.9964 [0.9886, 1.0000] | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9966±0.0006 |
| ffpp_c23 | ffpp_c23 | swinfusionpp | dataset_specific_bo | tta_flip | 0.9965 [0.9889, 1.0000] | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9965±0.0007 |
| ffpp_c23 | ffpp_c23 | swinfusionpp | fixed_no_bo | plain | 0.9942 [0.9834, 0.9999] | 0.9786 | 0.9855 | 0.9714 | 0.9784 | 0.9939±0.0009 |
| ffpp_c23 | ffpp_c23 | swinfusionpp | fixed_no_bo | tta_flip | 0.9946 [0.9845, 0.9999] | 0.9786 | 0.9855 | 0.9714 | 0.9784 | 0.9939±0.0010 |
| ffpp_c23 | ffpp_c23 | topology_control | fixed_no_bo | plain | 0.9962 [0.9888, 1.0000] | 0.9821 | 0.9856 | 0.9786 | 0.9821 | 0.9960±0.0002 |
| ffpp_c23 | ffpp_c23 | topology_control | fixed_no_bo | tta_flip | 0.9962 [0.9890, 1.0000] | 0.9821 | 0.9856 | 0.9786 | 0.9821 | 0.9960±0.0004 |
| ffpp_c23 | ffpp_c23 | video_swin_b | fixed_no_bo | plain | 0.9951 [0.9856, 1.0000] | 0.9893 | 0.9928 | 0.9857 | 0.9892 | 0.9952±0.0009 |
| ffpp_c23 | ffpp_c23 | video_swin_b | fixed_no_bo | tta_flip | 0.9960 [0.9886, 1.0000] | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9959±0.0009 |
| ffpp_c40 | ffpp_c40 | swin_b | fixed_no_bo | plain | 0.9883 [0.9777, 0.9960] | 0.9464 | 0.9562 | 0.9357 | 0.9458 | 0.9875±0.0013 |
| ffpp_c40 | ffpp_c40 | swin_b | fixed_no_bo | tta_flip | 0.9884 [0.9772, 0.9963] | 0.9429 | 0.9493 | 0.9357 | 0.9424 | 0.9874±0.0011 |
| ffpp_c40 | ffpp_c40 | swinfusionpp | dataset_specific_bo | plain | 0.9941 [0.9875, 0.9989] | 0.9607 | 0.9388 | 0.9857 | 0.9617 | 0.9923±0.0017 |
| ffpp_c40 | ffpp_c40 | swinfusionpp | dataset_specific_bo | tta_flip | 0.9937 [0.9865, 0.9988] | 0.9607 | 0.9388 | 0.9857 | 0.9617 | 0.9915±0.0020 |
| ffpp_c40 | ffpp_c40 | swinfusionpp | fixed_no_bo | plain | 0.9878 [0.9772, 0.9965] | 0.9464 | 0.9371 | 0.9571 | 0.9470 | 0.9860±0.0017 |
| ffpp_c40 | ffpp_c40 | swinfusionpp | fixed_no_bo | tta_flip | 0.9881 [0.9772, 0.9965] | 0.9464 | 0.9371 | 0.9571 | 0.9470 | 0.9865±0.0014 |
| ffpp_c40 | ffpp_c40 | video_swin_b | fixed_no_bo | plain | 0.9915 [0.9818, 0.9983] | 0.9571 | 0.9571 | 0.9571 | 0.9571 | 0.9910±0.0022 |
| ffpp_c40 | ffpp_c40 | video_swin_b | fixed_no_bo | tta_flip | 0.9916 [0.9822, 0.9982] | 0.9536 | 0.9704 | 0.9357 | 0.9527 | 0.9913±0.0019 |
| celeb_df_v2 | deeperforensics_1_0 | swin_b | fixed_no_bo | plain | 0.6012 [0.5624, 0.6408] | 0.5100 | 1.0000 | 0.0199 | 0.0390 | 0.5971±0.0176 |
| celeb_df_v2 | deeperforensics_1_0 | swin_b | fixed_no_bo | tta_flip | 0.5971 [0.5583, 0.6363] | 0.5174 | 1.0000 | 0.0348 | 0.0673 | 0.5933±0.0180 |
| celeb_df_v2 | deeperforensics_1_0 | swinfusionpp | dataset_specific_bo | plain | 0.6824 [0.6488, 0.7178] | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.6727±0.0146 |
| celeb_df_v2 | deeperforensics_1_0 | swinfusionpp | dataset_specific_bo | tta_flip | 0.6827 [0.6487, 0.7188] | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.6736±0.0136 |
| celeb_df_v2 | deeperforensics_1_0 | swinfusionpp | fixed_no_bo | plain | 0.7233 [0.6869, 0.7604] | 0.5274 | 1.0000 | 0.0547 | 0.1038 | 0.7153±0.0378 |
| celeb_df_v2 | deeperforensics_1_0 | swinfusionpp | fixed_no_bo | tta_flip | 0.7227 [0.6868, 0.7591] | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.7151±0.0375 |
| celeb_df_v2 | deeperforensics_1_0 | video_swin_b | fixed_no_bo | plain | 0.6603 [0.6130, 0.7048] | 0.5348 | 1.0000 | 0.0697 | 0.1302 | 0.6503±0.0142 |
| celeb_df_v2 | deeperforensics_1_0 | video_swin_b | fixed_no_bo | tta_flip | 0.6610 [0.6138, 0.7050] | 0.5398 | 1.0000 | 0.0796 | 0.1475 | 0.6526±0.0130 |
| celeb_df_v2 | ffpp_c23 | swin_b | fixed_no_bo | plain | 0.8468 [0.8129, 0.8814] | 0.6036 | 1.0000 | 0.2071 | 0.3432 | 0.8444±0.0108 |
| celeb_df_v2 | ffpp_c23 | swin_b | fixed_no_bo | tta_flip | 0.8456 [0.8116, 0.8803] | 0.6071 | 0.9688 | 0.2214 | 0.3605 | 0.8441±0.0108 |
| celeb_df_v2 | ffpp_c23 | swinfusionpp | dataset_specific_bo | plain | 0.8657 [0.8283, 0.9038] | 0.6357 | 1.0000 | 0.2714 | 0.4270 | 0.8663±0.0108 |
| celeb_df_v2 | ffpp_c23 | swinfusionpp | dataset_specific_bo | tta_flip | 0.8665 [0.8287, 0.9039] | 0.6250 | 1.0000 | 0.2500 | 0.4000 | 0.8670±0.0116 |
| celeb_df_v2 | ffpp_c23 | swinfusionpp | fixed_no_bo | plain | 0.8958 [0.8663, 0.9253] | 0.6357 | 0.9750 | 0.2786 | 0.4333 | 0.8881±0.0055 |
| celeb_df_v2 | ffpp_c23 | swinfusionpp | fixed_no_bo | tta_flip | 0.8946 [0.8649, 0.9245] | 0.5929 | 1.0000 | 0.1857 | 0.3133 | 0.8874±0.0049 |
| celeb_df_v2 | ffpp_c23 | video_swin_b | fixed_no_bo | plain | 0.9047 [0.8739, 0.9340] | 0.7071 | 0.9833 | 0.4214 | 0.5900 | 0.8996±0.0178 |
| celeb_df_v2 | ffpp_c23 | video_swin_b | fixed_no_bo | tta_flip | 0.9012 [0.8702, 0.9317] | 0.7036 | 0.9831 | 0.4143 | 0.5829 | 0.8976±0.0177 |
| celeb_df_v2 | ffpp_c40 | swin_b | fixed_no_bo | plain | 0.7770 [0.7430, 0.8102] | 0.5214 | 1.0000 | 0.0429 | 0.0822 | 0.7747±0.0054 |
| celeb_df_v2 | ffpp_c40 | swin_b | fixed_no_bo | tta_flip | 0.7804 [0.7470, 0.8130] | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.7783±0.0048 |
| celeb_df_v2 | ffpp_c40 | swinfusionpp | dataset_specific_bo | plain | 0.7345 [0.6961, 0.7741] | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.7282±0.0227 |
| celeb_df_v2 | ffpp_c40 | swinfusionpp | dataset_specific_bo | tta_flip | 0.7360 [0.6980, 0.7754] | 0.5250 | 1.0000 | 0.0500 | 0.0952 | 0.7321±0.0237 |
| celeb_df_v2 | ffpp_c40 | swinfusionpp | fixed_no_bo | plain | 0.8384 [0.8056, 0.8725] | 0.5214 | 1.0000 | 0.0429 | 0.0822 | 0.8220±0.0190 |
| celeb_df_v2 | ffpp_c40 | swinfusionpp | fixed_no_bo | tta_flip | 0.8402 [0.8080, 0.8740] | 0.5107 | 1.0000 | 0.0214 | 0.0420 | 0.8244±0.0167 |
| celeb_df_v2 | ffpp_c40 | video_swin_b | fixed_no_bo | plain | 0.7630 [0.7201, 0.8035] | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.7515±0.0526 |
| celeb_df_v2 | ffpp_c40 | video_swin_b | fixed_no_bo | tta_flip | 0.7685 [0.7262, 0.8102] | 0.5357 | 1.0000 | 0.0714 | 0.1333 | 0.7581±0.0539 |
| deeperforensics_1_0 | celeb_df_v2 | swin_b | fixed_no_bo | plain | 0.4593 [0.3970, 0.5259] | 0.1380 | nan | 0.0000 | nan | 0.4545±0.0305 |
| deeperforensics_1_0 | celeb_df_v2 | swin_b | fixed_no_bo | tta_flip | 0.4609 [0.3966, 0.5290] | 0.1380 | nan | 0.0000 | nan | 0.4558±0.0287 |
| deeperforensics_1_0 | celeb_df_v2 | swinfusionpp | dataset_specific_bo | plain | 0.5519 [0.4954, 0.6128] | 0.1380 | nan | 0.0000 | nan | 0.5533±0.0104 |
| deeperforensics_1_0 | celeb_df_v2 | swinfusionpp | dataset_specific_bo | tta_flip | 0.5537 [0.4951, 0.6180] | 0.1380 | nan | 0.0000 | nan | 0.5520±0.0171 |
| deeperforensics_1_0 | celeb_df_v2 | swinfusionpp | fixed_no_bo | plain | 0.5879 [0.5210, 0.6592] | 0.1421 | 1.0000 | 0.0047 | 0.0094 | 0.5811±0.0126 |
| deeperforensics_1_0 | celeb_df_v2 | swinfusionpp | fixed_no_bo | tta_flip | 0.5872 [0.5212, 0.6574] | 0.1411 | 1.0000 | 0.0036 | 0.0071 | 0.5809±0.0144 |
| deeperforensics_1_0 | celeb_df_v2 | video_swin_b | fixed_no_bo | plain | 0.6001 [0.5354, 0.6750] | 0.1524 | 0.9375 | 0.0178 | 0.0349 | 0.5948±0.0158 |
| deeperforensics_1_0 | celeb_df_v2 | video_swin_b | fixed_no_bo | tta_flip | 0.5968 [0.5346, 0.6674] | 0.1595 | 0.9565 | 0.0261 | 0.0508 | 0.5909±0.0149 |
| deeperforensics_1_0 | ffpp_c23 | swin_b | fixed_no_bo | plain | 0.6115 [0.5774, 0.6466] | 0.5000 | nan | 0.0000 | nan | 0.5970±0.0437 |
| deeperforensics_1_0 | ffpp_c23 | swin_b | fixed_no_bo | tta_flip | 0.6108 [0.5764, 0.6472] | 0.5000 | nan | 0.0000 | nan | 0.5994±0.0426 |
| deeperforensics_1_0 | ffpp_c23 | swinfusionpp | dataset_specific_bo | plain | 0.7236 [0.6918, 0.7579] | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.6681±0.0503 |
| deeperforensics_1_0 | ffpp_c23 | swinfusionpp | dataset_specific_bo | tta_flip | 0.7268 [0.6963, 0.7607] | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.6712±0.0513 |
| deeperforensics_1_0 | ffpp_c23 | swinfusionpp | fixed_no_bo | plain | 0.8127 [0.7802, 0.8475] | 0.5071 | 1.0000 | 0.0143 | 0.0282 | 0.7874±0.0212 |
| deeperforensics_1_0 | ffpp_c23 | swinfusionpp | fixed_no_bo | tta_flip | 0.8133 [0.7816, 0.8477] | 0.5036 | 0.6667 | 0.0143 | 0.0280 | 0.7887±0.0190 |
| deeperforensics_1_0 | ffpp_c23 | video_swin_b | fixed_no_bo | plain | 0.7676 [0.7358, 0.8021] | 0.5107 | 0.8000 | 0.0286 | 0.0552 | 0.7560±0.0244 |
| deeperforensics_1_0 | ffpp_c23 | video_swin_b | fixed_no_bo | tta_flip | 0.7682 [0.7365, 0.8025] | 0.5143 | 0.8333 | 0.0357 | 0.0685 | 0.7574±0.0243 |
| deeperforensics_1_0 | ffpp_c40 | swin_b | fixed_no_bo | plain | 0.5964 [0.5592, 0.6330] | 0.5000 | nan | 0.0000 | nan | 0.5840±0.0389 |
| deeperforensics_1_0 | ffpp_c40 | swin_b | fixed_no_bo | tta_flip | 0.5997 [0.5632, 0.6371] | 0.5000 | nan | 0.0000 | nan | 0.5865±0.0334 |
| deeperforensics_1_0 | ffpp_c40 | swinfusionpp | dataset_specific_bo | plain | 0.7067 [0.6758, 0.7410] | 0.5000 | nan | 0.0000 | nan | 0.6599±0.0337 |
| deeperforensics_1_0 | ffpp_c40 | swinfusionpp | dataset_specific_bo | tta_flip | 0.7085 [0.6776, 0.7431] | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.6618±0.0349 |
| deeperforensics_1_0 | ffpp_c40 | swinfusionpp | fixed_no_bo | plain | 0.7668 [0.7322, 0.8032] | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.7476±0.0137 |
| deeperforensics_1_0 | ffpp_c40 | swinfusionpp | fixed_no_bo | tta_flip | 0.7698 [0.7352, 0.8063] | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.7509±0.0132 |
| deeperforensics_1_0 | ffpp_c40 | video_swin_b | fixed_no_bo | plain | 0.6829 [0.6430, 0.7265] | 0.5071 | 1.0000 | 0.0143 | 0.0282 | 0.6751±0.0235 |
| deeperforensics_1_0 | ffpp_c40 | video_swin_b | fixed_no_bo | tta_flip | 0.6863 [0.6462, 0.7304] | 0.5071 | 1.0000 | 0.0143 | 0.0282 | 0.6797±0.0220 |
| ffpp_c23 | celeb_df_v2 | capacity_control | fixed_no_bo | plain | 0.8627 [0.8012, 0.9149] | 0.5920 | 0.9805 | 0.5374 | 0.6943 | 0.8569±0.0154 |
| ffpp_c23 | celeb_df_v2 | capacity_control | fixed_no_bo | tta_flip | 0.8632 [0.7976, 0.9181] | 0.5910 | 0.9784 | 0.5374 | 0.6937 | 0.8571±0.0147 |
| ffpp_c23 | celeb_df_v2 | swin_b | fixed_no_bo | plain | 0.8680 [0.8086, 0.9184] | 0.6748 | 0.9781 | 0.6370 | 0.7716 | 0.8618±0.0131 |
| ffpp_c23 | celeb_df_v2 | swin_b | fixed_no_bo | tta_flip | 0.8693 [0.8054, 0.9236] | 0.6636 | 0.9831 | 0.6204 | 0.7607 | 0.8635±0.0111 |
| ffpp_c23 | celeb_df_v2 | swinfusionpp | dataset_specific_bo | plain | 0.8785 [0.8253, 0.9256] | 0.6738 | 0.9695 | 0.6418 | 0.7723 | 0.8702±0.0039 |
| ffpp_c23 | celeb_df_v2 | swinfusionpp | dataset_specific_bo | tta_flip | 0.8847 [0.8275, 0.9356] | 0.6677 | 0.9796 | 0.6275 | 0.7650 | 0.8779±0.0058 |
| ffpp_c23 | celeb_df_v2 | swinfusionpp | fixed_no_bo | plain | 0.8624 [0.8052, 0.9149] | 0.5941 | 0.9869 | 0.5362 | 0.6949 | 0.8553±0.0076 |
| ffpp_c23 | celeb_df_v2 | swinfusionpp | fixed_no_bo | tta_flip | 0.8660 [0.8068, 0.9207] | 0.6053 | 0.9872 | 0.5492 | 0.7058 | 0.8588±0.0058 |
| ffpp_c23 | celeb_df_v2 | topology_control | fixed_no_bo | plain | 0.8577 [0.7977, 0.9116] | 0.6370 | 0.9784 | 0.5919 | 0.7376 | 0.8489±0.0139 |
| ffpp_c23 | celeb_df_v2 | topology_control | fixed_no_bo | tta_flip | 0.8602 [0.7963, 0.9164] | 0.6309 | 0.9763 | 0.5860 | 0.7324 | 0.8520±0.0138 |
| ffpp_c23 | celeb_df_v2 | video_swin_b | fixed_no_bo | plain | 0.8676 [0.8251, 0.9108] | 0.6646 | 0.9831 | 0.6216 | 0.7616 | 0.8660±0.0026 |
| ffpp_c23 | celeb_df_v2 | video_swin_b | fixed_no_bo | tta_flip | 0.8755 [0.8309, 0.9216] | 0.7055 | 0.9727 | 0.6773 | 0.7986 | 0.8735±0.0036 |
| ffpp_c23 | deeperforensics_1_0 | capacity_control | fixed_no_bo | plain | 0.7846 [0.7468, 0.8212] | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.7529±0.0603 |
| ffpp_c23 | deeperforensics_1_0 | capacity_control | fixed_no_bo | tta_flip | 0.7882 [0.7510, 0.8245] | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.7564±0.0600 |
| ffpp_c23 | deeperforensics_1_0 | swin_b | fixed_no_bo | plain | 0.5678 [0.5250, 0.6105] | 0.5274 | 0.9231 | 0.0597 | 0.1121 | 0.5686±0.0182 |
| ffpp_c23 | deeperforensics_1_0 | swin_b | fixed_no_bo | tta_flip | 0.5708 [0.5280, 0.6119] | 0.5249 | 0.9167 | 0.0547 | 0.1033 | 0.5709±0.0181 |
| ffpp_c23 | deeperforensics_1_0 | swinfusionpp | dataset_specific_bo | plain | 0.7316 [0.7015, 0.7638] | 0.5199 | 0.9000 | 0.0448 | 0.0853 | 0.6968±0.0534 |
| ffpp_c23 | deeperforensics_1_0 | swinfusionpp | dataset_specific_bo | tta_flip | 0.7338 [0.7040, 0.7672] | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.7007±0.0566 |
| ffpp_c23 | deeperforensics_1_0 | swinfusionpp | fixed_no_bo | plain | 0.8261 [0.7926, 0.8603] | 0.5149 | 0.8750 | 0.0348 | 0.0670 | 0.7973±0.0539 |
| ffpp_c23 | deeperforensics_1_0 | swinfusionpp | fixed_no_bo | tta_flip | 0.8279 [0.7939, 0.8623] | 0.5149 | 0.8750 | 0.0348 | 0.0670 | 0.8016±0.0498 |
| ffpp_c23 | deeperforensics_1_0 | topology_control | fixed_no_bo | plain | 0.8481 [0.8138, 0.8813] | 0.5398 | 0.9444 | 0.0846 | 0.1553 | 0.8200±0.0467 |
| ffpp_c23 | deeperforensics_1_0 | topology_control | fixed_no_bo | tta_flip | 0.8483 [0.8144, 0.8813] | 0.5398 | 0.9444 | 0.0846 | 0.1553 | 0.8214±0.0473 |
| ffpp_c23 | deeperforensics_1_0 | video_swin_b | fixed_no_bo | plain | 0.8421 [0.8092, 0.8740] | 0.5796 | 0.9706 | 0.1642 | 0.2809 | 0.8379±0.0245 |
| ffpp_c23 | deeperforensics_1_0 | video_swin_b | fixed_no_bo | tta_flip | 0.8490 [0.8185, 0.8801] | 0.5995 | 0.9762 | 0.2040 | 0.3374 | 0.8437±0.0225 |
| ffpp_c23 | ffpp_c40 | capacity_control | fixed_no_bo | plain | 0.9763 [0.9575, 0.9906] | 0.9036 | 0.9593 | 0.8429 | 0.8973 | 0.9739±0.0020 |
| ffpp_c23 | ffpp_c40 | capacity_control | fixed_no_bo | tta_flip | 0.9763 [0.9571, 0.9905] | 0.8929 | 0.9583 | 0.8214 | 0.8846 | 0.9744±0.0020 |
| ffpp_c23 | ffpp_c40 | swin_b | fixed_no_bo | plain | 0.9739 [0.9572, 0.9885] | 0.9179 | 0.9606 | 0.8714 | 0.9139 | 0.9713±0.0059 |
| ffpp_c23 | ffpp_c40 | swin_b | fixed_no_bo | tta_flip | 0.9747 [0.9584, 0.9889] | 0.9179 | 0.9606 | 0.8714 | 0.9139 | 0.9725±0.0058 |
| ffpp_c23 | ffpp_c40 | swinfusionpp | dataset_specific_bo | plain | 0.9862 [0.9739, 0.9959] | 0.9357 | 0.9766 | 0.8929 | 0.9328 | 0.9850±0.0012 |
| ffpp_c23 | ffpp_c40 | swinfusionpp | dataset_specific_bo | tta_flip | 0.9855 [0.9722, 0.9957] | 0.9321 | 0.9690 | 0.8929 | 0.9294 | 0.9844±0.0018 |
| ffpp_c23 | ffpp_c40 | swinfusionpp | fixed_no_bo | plain | 0.9760 [0.9575, 0.9910] | 0.8857 | 0.9737 | 0.7929 | 0.8740 | 0.9733±0.0017 |
| ffpp_c23 | ffpp_c40 | swinfusionpp | fixed_no_bo | tta_flip | 0.9762 [0.9569, 0.9913] | 0.8893 | 0.9739 | 0.8000 | 0.8784 | 0.9738±0.0020 |
| ffpp_c23 | ffpp_c40 | topology_control | fixed_no_bo | plain | 0.9780 [0.9607, 0.9916] | 0.9071 | 0.9597 | 0.8500 | 0.9015 | 0.9755±0.0016 |
| ffpp_c23 | ffpp_c40 | topology_control | fixed_no_bo | tta_flip | 0.9777 [0.9605, 0.9911] | 0.9071 | 0.9597 | 0.8500 | 0.9015 | 0.9753±0.0011 |
| ffpp_c23 | ffpp_c40 | video_swin_b | fixed_no_bo | plain | 0.9746 [0.9570, 0.9893] | 0.9179 | 0.9756 | 0.8571 | 0.9125 | 0.9741±0.0025 |
| ffpp_c23 | ffpp_c40 | video_swin_b | fixed_no_bo | tta_flip | 0.9749 [0.9579, 0.9891] | 0.9179 | 0.9535 | 0.8786 | 0.9145 | 0.9747±0.0029 |

| Family | Training | Test | A vs B | ΔAUC [95% CI] | perm p | Holm p |
|---|---|---|---|---|---|---|
| RQ1 | celeb_df_v2 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0024 [+0.0002, +0.0057] | 0.6325 | 1.0000 |
| RQ6 | celeb_df_v2 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0811 [+0.0511, +0.1130] | 0.0002 | 0.0036 |
| RQ6 | celeb_df_v2 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0189 [-0.0140, +0.0499] | 0.3591 | 1.0000 |
| RQ6 | celeb_df_v2 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -0.0425 [-0.0806, -0.0026] | 0.0118 | 0.1534 |
| RQ6 | deeperforensics_1_0 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0926 [+0.0263, +0.1477] | 0.4989 | 1.0000 |
| RQ1 | deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -0.0012 [-0.0041, +0.0007] | 0.9982 | 1.0000 |
| RQ6 | deeperforensics_1_0 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.1121 [+0.0724, +0.1563] | 0.0002 | 0.0036 |
| RQ6 | deeperforensics_1_0 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.1103 [+0.0750, +0.1501] | 0.0002 | 0.0036 |
| RQ6 | ffpp_c23 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0105 [-0.0090, +0.0315] | 0.7656 | 1.0000 |
| RQ6 | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.1638 [+0.1220, +0.2096] | 0.0002 | 0.0036 |
| RQ1 | ffpp_c23 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | -0.0001 [-0.0027, +0.0017] | 1.0000 | 1.0000 |
| RQ6 | ffpp_c23 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0123 [+0.0048, +0.0211] | 0.3321 | 1.0000 |
| RQ1 | ffpp_c40 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swin_b__fixed_no_bo | +0.0058 [+0.0010, +0.0124] | 0.1504 | 1.0000 |
| RQ1 | celeb_df_v2 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0024 [+0.0001, +0.0058] | 0.9032 | 1.0000 |
| RQ6 | celeb_df_v2 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0221 [-0.0104, +0.0573] | 0.2607 | 1.0000 |
| RQ6 | celeb_df_v2 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0390 [-0.0617, -0.0179] | 0.0134 | 0.1608 |
| RQ6 | celeb_df_v2 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0285 [-0.0606, +0.0070] | 0.2474 | 1.0000 |
| RQ6 | deeperforensics_1_0 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0482 [-0.1277, +0.0138] | 0.3015 | 1.0000 |
| RQ1 | deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0008 [-0.0030, +0.0050] | 0.7616 | 1.0000 |
| RQ6 | deeperforensics_1_0 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.0439 [-0.0770, -0.0106] | 0.0476 | 0.5235 |
| RQ6 | deeperforensics_1_0 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0239 [-0.0127, +0.0609] | 0.2807 | 1.0000 |
| RQ6 | ffpp_c23 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0109 [-0.0086, +0.0298] | 0.3703 | 1.0000 |
| RQ6 | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | -0.1105 [-0.1374, -0.0820] | 0.0002 | 0.0036 |
| RQ1 | ffpp_c23 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0014 [+0.0000, +0.0037] | 1.0000 | 1.0000 |
| RQ6 | ffpp_c23 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0116 [+0.0040, +0.0214] | 0.0586 | 0.5859 |
| RQ1 | ffpp_c40 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs video_swin_b__fixed_no_bo | +0.0026 [-0.0026, +0.0090] | 0.3365 | 1.0000 |
| RQ1_secondary | celeb_df_v2 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0007 [-0.0048, +0.0026] | 0.8740 | 1.0000 |
| RQ6_secondary | celeb_df_v2 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.1220 [+0.0933, +0.1544] | 0.0002 | 0.0054 |
| RQ6_secondary | celeb_df_v2 | ffpp_c23 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.0490 [+0.0200, +0.0770] | 0.0342 | 0.4787 |
| RQ6_secondary | celeb_df_v2 | ffpp_c40 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.0614 [+0.0339, +0.0918] | 0.0018 | 0.0288 |
| RQ6_secondary | deeperforensics_1_0 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.1286 [+0.0626, +0.1864] | 0.3157 | 1.0000 |
| RQ1_secondary | deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.0009 [-0.0007, +0.0036] | 1.0000 | 1.0000 |
| RQ6_secondary | deeperforensics_1_0 | ffpp_c23 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.2012 [+0.1569, +0.2492] | 0.0002 | 0.0054 |
| RQ6_secondary | deeperforensics_1_0 | ffpp_c40 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.1705 [+0.1290, +0.2164] | 0.0002 | 0.0054 |
| RQ6_secondary | ffpp_c23 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0056 [-0.0282, +0.0201] | 0.8628 | 1.0000 |
| RQ6_secondary | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.2584 [+0.2133, +0.3046] | 0.0002 | 0.0054 |
| RQ1_secondary | ffpp_c23 | ffpp_c23 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0023 [-0.0079, +0.0009] | 0.3997 | 1.0000 |
| RQ6_secondary | ffpp_c23 | ffpp_c40 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | +0.0021 [-0.0068, +0.0103] | 0.8286 | 1.0000 |
| RQ1_secondary | ffpp_c40 | ffpp_c40 | swinfusionpp__fixed_no_bo vs swin_b__fixed_no_bo | -0.0005 [-0.0076, +0.0061] | 0.9442 | 1.0000 |
| RQ1_secondary | celeb_df_v2 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0007 [-0.0033, +0.0012] | 0.8500 | 1.0000 |
| RQ6_secondary | celeb_df_v2 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | +0.0630 [+0.0302, +0.0991] | 0.0002 | 0.0054 |
| RQ6_secondary | celeb_df_v2 | ffpp_c23 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0089 [-0.0320, +0.0154] | 0.4503 | 1.0000 |
| RQ6_secondary | celeb_df_v2 | ffpp_c40 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | +0.0754 [+0.0354, +0.1164] | 0.0002 | 0.0054 |
| RQ6_secondary | deeperforensics_1_0 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0122 [-0.0917, +0.0487] | 0.8956 | 1.0000 |
| RQ1_secondary | deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | +0.0029 [-0.0005, +0.0085] | 0.0002 | 0.0024 |
| RQ6_secondary | deeperforensics_1_0 | ffpp_c23 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | +0.0451 [+0.0077, +0.0816] | 0.0558 | 0.7253 |
| RQ6_secondary | deeperforensics_1_0 | ffpp_c40 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | +0.0840 [+0.0439, +0.1229] | 0.0002 | 0.0054 |
| RQ6_secondary | ffpp_c23 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0052 [-0.0304, +0.0175] | 0.8768 | 1.0000 |
| RQ6_secondary | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0159 [-0.0407, +0.0090] | 0.3451 | 1.0000 |
| RQ1_secondary | ffpp_c23 | ffpp_c23 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0008 [-0.0031, +0.0002] | 1.0000 | 1.0000 |
| RQ6_secondary | ffpp_c23 | ffpp_c40 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | +0.0014 [-0.0089, +0.0102] | 0.9476 | 1.0000 |
| RQ1_secondary | ffpp_c40 | ffpp_c40 | swinfusionpp__fixed_no_bo vs video_swin_b__fixed_no_bo | -0.0037 [-0.0101, +0.0013] | 0.1890 | 1.0000 |
| RQ1_secondary | celeb_df_v2 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | +0.0031 [+0.0005, +0.0060] | 0.9922 | 1.0000 |
| RQ6_secondary | celeb_df_v2 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0409 [-0.0649, -0.0170] | 0.0220 | 0.3299 |
| RQ6_secondary | celeb_df_v2 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0302 [-0.0589, -0.0042] | 0.0678 | 0.8134 |
| RQ6_secondary | celeb_df_v2 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.1039 [-0.1416, -0.0662] | 0.0002 | 0.0054 |
| RQ6_secondary | deeperforensics_1_0 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0360 [-0.0780, +0.0025] | 0.7117 | 1.0000 |
| RQ1_secondary | deeperforensics_1_0 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0021 [-0.0051, +0.0000] | 0.4983 | 1.0000 |
| RQ6_secondary | deeperforensics_1_0 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0891 [-0.1239, -0.0526] | 0.0002 | 0.0054 |
| RQ6_secondary | deeperforensics_1_0 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0601 [-0.0868, -0.0313] | 0.0006 | 0.0102 |
| RQ6_secondary | ffpp_c23 | celeb_df_v2 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | +0.0161 [+0.0018, +0.0301] | 0.3135 | 1.0000 |
| RQ6_secondary | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | -0.0946 [-0.1218, -0.0662] | 0.0002 | 0.0054 |
| RQ1_secondary | ffpp_c23 | ffpp_c23 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | +0.0022 [+0.0001, +0.0058] | 0.9992 | 1.0000 |
| RQ6_secondary | ffpp_c23 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | +0.0102 [+0.0043, +0.0182] | 0.2833 | 1.0000 |
| RQ1_secondary | ffpp_c40 | ffpp_c40 | swinfusionpp__dataset_specific_bo vs swinfusionpp__fixed_no_bo | +0.0063 [+0.0018, +0.0118] | 0.0002 | 0.0024 |
| RQ4_controls_transfer | ffpp_c23 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | +0.0046 [-0.0072, +0.0159] | 0.4691 | 1.0000 |
| RQ4_controls_transfer | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0219 [-0.0380, -0.0064] | 0.0148 | 0.0740 |
| RQ4_controls | ffpp_c23 | ffpp_c23 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0019 [-0.0060, +0.0001] | 0.0150 | 0.0300 |
| RQ4_controls_transfer | ffpp_c23 | ffpp_c40 | swinfusionpp__fixed_no_bo vs topology_control__fixed_no_bo | -0.0020 [-0.0062, +0.0016] | 0.2667 | 1.0000 |
| RQ4_controls_transfer | ffpp_c23 | celeb_df_v2 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -0.0003 [-0.0113, +0.0131] | 0.9804 | 1.0000 |
| RQ4_controls_transfer | ffpp_c23 | deeperforensics_1_0 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | +0.0416 [+0.0227, +0.0612] | 0.0006 | 0.0036 |
| RQ4_controls | ffpp_c23 | ffpp_c23 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -0.0003 [-0.0019, +0.0009] | 0.7109 | 0.7109 |
| RQ4_controls_transfer | ffpp_c23 | ffpp_c40 | swinfusionpp__fixed_no_bo vs capacity_control__fixed_no_bo | -0.0003 [-0.0047, +0.0036] | 0.8868 | 1.0000 |
