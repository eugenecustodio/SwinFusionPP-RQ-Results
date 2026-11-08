### Source thresholds unchanged; full target tests with v020 lineage-overlap disclosure

| training | test | model | regimen | roc_auc | ci_low | ci_high | accuracy | precision | recall | f1 | pr_auc | seed_auc_mean | seed_auc_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.9739 | 0.9572 | 0.9885 | 0.9179 | 0.9606 | 0.8714 | 0.9139 | 0.9793 | 0.9713 | 0.0059 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.9862 | 0.9739 | 0.9959 | 0.9357 | 0.9766 | 0.8929 | 0.9328 | 0.9882 | 0.9850 | 0.0012 |
| FF++ C23 (HQ) | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.9746 | 0.9570 | 0.9893 | 0.9179 | 0.9756 | 0.8571 | 0.9125 | 0.9786 | 0.9741 | 0.0025 |
| FF++ C23 (HQ) | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.8680 | 0.8086 | 0.9184 | 0.6748 | 0.9781 | 0.6370 | 0.7716 | 0.9762 | 0.8618 | 0.0131 |
| FF++ C23 (HQ) | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.8785 | 0.8253 | 0.9256 | 0.6738 | 0.9695 | 0.6418 | 0.7723 | 0.9783 | 0.8702 | 0.0039 |
| FF++ C23 (HQ) | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.8676 | 0.8251 | 0.9108 | 0.6646 | 0.9831 | 0.6216 | 0.7616 | 0.9763 | 0.8660 | 0.0026 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.5678 | 0.5250 | 0.6105 | 0.5274 | 0.9231 | 0.0597 | 0.1121 | 0.6282 | 0.5686 | 0.0182 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.7316 | 0.7015 | 0.7638 | 0.5199 | 0.9000 | 0.0448 | 0.0853 | 0.7458 | 0.6968 | 0.0534 |
| FF++ C23 (HQ) | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.8421 | 0.8092 | 0.8740 | 0.5796 | 0.9706 | 0.1642 | 0.2809 | 0.8542 | 0.8379 | 0.0245 |
| Celeb-DF v2 | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.8468 | 0.8129 | 0.8814 | 0.6036 | 1.0000 | 0.2071 | 0.3432 | 0.8684 | 0.8444 | 0.0108 |
| Celeb-DF v2 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.8657 | 0.8283 | 0.9038 | 0.6357 | 1.0000 | 0.2714 | 0.4270 | 0.8950 | 0.8663 | 0.0108 |
| Celeb-DF v2 | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.9047 | 0.8739 | 0.9340 | 0.7071 | 0.9833 | 0.4214 | 0.5900 | 0.9194 | 0.8996 | 0.0178 |
| Celeb-DF v2 | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.7770 | 0.7430 | 0.8102 | 0.5214 | 1.0000 | 0.0429 | 0.0822 | 0.7879 | 0.7747 | 0.0054 |
| Celeb-DF v2 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7345 | 0.6961 | 0.7741 | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.7836 | 0.7282 | 0.0227 |
| Celeb-DF v2 | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.7630 | 0.7201 | 0.8035 | 0.5286 | 1.0000 | 0.0571 | 0.1081 | 0.8024 | 0.7515 | 0.0526 |
| Celeb-DF v2 | DeeperForensics-1.0 | Swin-B | fixed_no_bo | 0.6012 | 0.5624 | 0.6408 | 0.5100 | 1.0000 | 0.0199 | 0.0390 | 0.6671 | 0.5971 | 0.0176 |
| Celeb-DF v2 | DeeperForensics-1.0 | SwinFusion++ | dataset_specific_bo | 0.6824 | 0.6488 | 0.7178 | 0.5199 | 1.0000 | 0.0398 | 0.0766 | 0.7257 | 0.6727 | 0.0146 |
| Celeb-DF v2 | DeeperForensics-1.0 | Video Swin-B | fixed_no_bo | 0.6603 | 0.6130 | 0.7048 | 0.5348 | 1.0000 | 0.0697 | 0.1302 | 0.7051 | 0.6503 | 0.0142 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | Swin-B | fixed_no_bo | 0.6115 | 0.5774 | 0.6466 | 0.5000 | — | 0.0000 | — | 0.6287 | 0.5970 | 0.0437 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | SwinFusion++ | dataset_specific_bo | 0.7236 | 0.6918 | 0.7579 | 0.5036 | 1.0000 | 0.0071 | 0.0142 | 0.7138 | 0.6681 | 0.0503 |
| DeeperForensics-1.0 | FF++ C23 (HQ) | Video Swin-B | fixed_no_bo | 0.7676 | 0.7358 | 0.8021 | 0.5107 | 0.8000 | 0.0286 | 0.0552 | 0.7756 | 0.7560 | 0.0244 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | Swin-B | fixed_no_bo | 0.5964 | 0.5592 | 0.6330 | 0.5000 | — | 0.0000 | — | 0.6191 | 0.5840 | 0.0389 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | SwinFusion++ | dataset_specific_bo | 0.7067 | 0.6758 | 0.7410 | 0.5000 | — | 0.0000 | — | 0.6937 | 0.6599 | 0.0337 |
| DeeperForensics-1.0 | FF++ C40 (LQ) | Video Swin-B | fixed_no_bo | 0.6829 | 0.6430 | 0.7265 | 0.5071 | 1.0000 | 0.0143 | 0.0282 | 0.6995 | 0.6751 | 0.0235 |
| DeeperForensics-1.0 | Celeb-DF v2 | Swin-B | fixed_no_bo | 0.4593 | 0.3970 | 0.5259 | 0.1380 | — | 0.0000 | — | 0.8414 | 0.4545 | 0.0305 |
| DeeperForensics-1.0 | Celeb-DF v2 | SwinFusion++ | dataset_specific_bo | 0.5519 | 0.4954 | 0.6128 | 0.1380 | — | 0.0000 | — | 0.8749 | 0.5533 | 0.0104 |
| DeeperForensics-1.0 | Celeb-DF v2 | Video Swin-B | fixed_no_bo | 0.6001 | 0.5354 | 0.6750 | 0.1524 | 0.9375 | 0.0178 | 0.0349 | 0.9018 | 0.5948 | 0.0158 |
