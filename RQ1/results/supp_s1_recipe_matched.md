### Architecture-only check: identical training recipe for every model

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.9965 | 0.9906 | 0.9999 | 0.9786 | 0.9718 | 0.9857 | 0.9787 | 0.9973 | 0.9965 | 6.71e-04 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | SwinFusion++ | fixed_no_bo | 0.9942 | 0.9834 | 0.9999 | 0.9786 | 0.9855 | 0.9714 | 0.9784 | 0.9963 | 0.9939 | 8.57e-04 |
| FF++ C23 (HQ) | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.9951 | 0.9856 | 1.0000 | 0.9893 | 0.9928 | 0.9857 | 0.9892 | 0.9967 | 0.9952 | 8.68e-04 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.9883 | 0.9777 | 0.9960 | 0.9464 | 0.9562 | 0.9357 | 0.9458 | 0.9895 | 0.9875 | 0.0013 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | SwinFusion++ | fixed_no_bo | 0.9878 | 0.9772 | 0.9965 | 0.9464 | 0.9371 | 0.9571 | 0.9470 | 0.9896 | 0.9860 | 0.0017 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.9915 | 0.9818 | 0.9983 | 0.9571 | 0.9571 | 0.9571 | 0.9571 | 0.9933 | 0.9910 | 0.0022 |
| Celeb-DF v2 | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.9958 | 0.9925 | 0.9990 | 0.9540 | 0.9963 | 0.9502 | 0.9727 | 0.9993 | 0.9956 | 2.28e-04 |
| Celeb-DF v2 | Celeb-DF v2 | SwinFusion++ | fixed_no_bo | 0.9951 | 0.9905 | 0.9995 | 0.9775 | 0.9928 | 0.9810 | 0.9869 | 0.9992 | 0.9939 | 0.0022 |
| Celeb-DF v2 | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.9958 | 0.9915 | 0.9994 | 0.9826 | 0.9928 | 0.9870 | 0.9899 | 0.9993 | 0.9954 | 2.75e-04 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.9966 | 0.9892 | 1.0000 | 0.9776 | 1.0000 | 0.9552 | 0.9771 | 0.9978 | 0.9968 | 8.53e-04 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | SwinFusion++ | fixed_no_bo | 0.9974 | 0.9921 | 1.0000 | 0.9876 | 1.0000 | 0.9751 | 0.9874 | 0.9980 | 0.9971 | 0.0011 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.9945 | 0.9842 | 0.9999 | 0.9701 | 0.9948 | 0.9453 | 0.9694 | 0.9966 | 0.9944 | 6.34e-04 |
