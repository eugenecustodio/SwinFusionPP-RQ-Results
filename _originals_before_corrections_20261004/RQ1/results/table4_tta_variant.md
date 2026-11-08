### Labelled variant (A-13); the main results and tests use the plain variant

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.9965 | 0.9889 | 1.0000 | 0.9821 | 0.9787 | 0.9857 | 0.9822 | 0.9975 | 0.9965 | 7.22e-04 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9855 | 0.9722 | 0.9957 | 0.9321 | 0.9690 | 0.8929 | 0.9294 | 0.9874 | 0.9844 | 0.0018 |
| FF++ C23 (HQ) | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.8847 | 0.8275 | 0.9356 | 0.6677 | 0.9796 | 0.6275 | 0.7650 | 0.9792 | 0.8779 | 0.0058 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.7338 | 0.7040 | 0.7672 | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.7425 | 0.7007 | 0.0566 |
| FF++ C40 (LQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9937 | 0.9865 | 0.9988 | 0.9607 | 0.9388 | 0.9857 | 0.9617 | 0.9942 | 0.9915 | 0.0020 |
| Celeb-DF v2 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.8665 | 0.8287 | 0.9039 | 0.6250 | 1.0000 | 0.2500 | 0.4000 | 0.8947 | 0.8670 | 0.0116 |
| Celeb-DF v2 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7360 | 0.6980 | 0.7754 | 0.5250 | 1.0000 | 0.0500 | 0.0952 | 0.7862 | 0.7321 | 0.0237 |
| Celeb-DF v2 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.9983 | 0.9966 | 0.9999 | 0.9796 | 0.9976 | 0.9786 | 0.9880 | 0.9997 | 0.9977 | 8.41e-04 |
| Celeb-DF v2 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.6827 | 0.6487 | 0.7188 | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.7270 | 0.6736 | 0.0136 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.7268 | 0.6963 | 0.7607 | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.7160 | 0.6712 | 0.0513 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7085 | 0.6776 | 0.7431 | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.6977 | 0.6618 | 0.0349 |
| DeeperForensics-1.0 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.5537 | 0.4951 | 0.6180 | 0.1380 | — | 0.0000 | — | 0.8750 | 0.5520 | 0.0171 |
| DeeperForensics-1.0 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.9956 | 0.9881 | 1.0000 | 0.9876 | 1.0000 | 0.9751 | 0.9874 | 0.9969 | 0.9954 | 0.0016 |
