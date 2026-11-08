### Transfer metrics, C23-trained models

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C40 (LQ) | Capacity control | fixed_no_bo | 0.9763 | 0.9575 | 0.9906 | 0.9036 | 0.9593 | 0.8429 | 0.8973 | 0.9797 | 0.9739 | 0.0020 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | SwinFusion++ | fixed_no_bo | 0.9760 | 0.9575 | 0.9910 | 0.8857 | 0.9737 | 0.7929 | 0.8740 | 0.9796 | 0.9733 | 0.0017 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | Topology control | fixed_no_bo | 0.9780 | 0.9607 | 0.9916 | 0.9071 | 0.9597 | 0.8500 | 0.9015 | 0.9811 | 0.9755 | 0.0016 |
| FF++ C23 (HQ) | Celeb-DF v2 | Capacity control | fixed_no_bo | 0.8627 | 0.8012 | 0.9149 | 0.5920 | 0.9805 | 0.5374 | 0.6943 | 0.9748 | 0.8569 | 0.0154 |
| FF++ C23 (HQ) | Celeb-DF v2 | SwinFusion++ | fixed_no_bo | 0.8624 | 0.8052 | 0.9149 | 0.5941 | 0.9869 | 0.5362 | 0.6949 | 0.9752 | 0.8553 | 0.0076 |
| FF++ C23 (HQ) | Celeb-DF v2 | Topology control | fixed_no_bo | 0.8577 | 0.7977 | 0.9116 | 0.6370 | 0.9784 | 0.5919 | 0.7376 | 0.9738 | 0.8489 | 0.0139 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Capacity control | fixed_no_bo | 0.7846 | 0.7468 | 0.8212 | 0.5174 | 0.8889 | 0.0398 | 0.0762 | 0.8042 | 0.7529 | 0.0603 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | SwinFusion++ | fixed_no_bo | 0.8261 | 0.7926 | 0.8603 | 0.5149 | 0.8750 | 0.0348 | 0.0670 | 0.8255 | 0.7973 | 0.0539 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Topology control | fixed_no_bo | 0.8481 | 0.8138 | 0.8813 | 0.5398 | 0.9444 | 0.0846 | 0.1553 | 0.8528 | 0.8200 | 0.0467 |
