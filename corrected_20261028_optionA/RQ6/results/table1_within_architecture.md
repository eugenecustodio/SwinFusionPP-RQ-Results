| Condition | Model | ROC-AUC [95% CI] | Accuracy | Precision | Recall | Specificity | F1 | Seed AUC mean ± SD |
|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | SwinFusion++ (fixed recipe) | 0.9942 [0.9834, 0.9999] | 97.86% | 98.55% | 97.14% | 98.57% | 0.9784 | 0.9939 ± 0.0009 |
| FF++ C23 (HQ) | Swin-B | 0.9965 [0.9906, 0.9999] | 97.86% | 97.18% | 98.57% | 97.14% | 0.9787 | 0.9965 ± 0.0007 |
| FF++ C23 (HQ) | Video Swin-B | 0.9951 [0.9856, 1.0000] | 98.93% | 99.28% | 98.57% | 99.29% | 0.9892 | 0.9952 ± 0.0009 |
| FF++ C40 (LQ) | SwinFusion++ (fixed recipe) | 0.9878 [0.9772, 0.9965] | 94.64% | 93.71% | 95.71% | 93.57% | 0.9470 | 0.9860 ± 0.0017 |
| FF++ C40 (LQ) | Swin-B | 0.9883 [0.9777, 0.9960] | 94.64% | 95.62% | 93.57% | 95.71% | 0.9458 | 0.9875 ± 0.0013 |
| FF++ C40 (LQ) | Video Swin-B | 0.9915 [0.9818, 0.9983] | 95.71% | 95.71% | 95.71% | 95.71% | 0.9571 | 0.9910 ± 0.0022 |
| Celeb-DF v2 | SwinFusion++ (fixed recipe) | 0.9951 [0.9905, 0.9995] | 97.75% | 99.28% | 98.10% | 95.56% | 0.9869 | 0.9939 ± 0.0022 |
| Celeb-DF v2 | Swin-B | 0.9958 [0.9925, 0.9990] | 95.40% | 99.63% | 95.02% | 97.78% | 0.9727 | 0.9956 ± 0.0002 |
| Celeb-DF v2 | Video Swin-B | 0.9958 [0.9915, 0.9994] | 98.26% | 99.28% | 98.70% | 95.56% | 0.9899 | 0.9954 ± 0.0003 |
| DeeperForensics-1.0 | SwinFusion++ (fixed recipe) | 0.9974 [0.9921, 1.0000] | 98.76% | 100.00% | 97.51% | 100.00% | 0.9874 | 0.9971 ± 0.0011 |
| DeeperForensics-1.0 | Swin-B | 0.9966 [0.9892, 1.0000] | 97.76% | 100.00% | 95.52% | 100.00% | 0.9771 | 0.9968 ± 0.0009 |
| DeeperForensics-1.0 | Video Swin-B | 0.9945 [0.9842, 0.9999] | 97.01% | 99.48% | 94.53% | 99.50% | 0.9694 | 0.9944 ± 0.0006 |

Principal architecture comparison: all three models trained with the identical fixed (non-BO) recipe. Three-seed mean-logit ensembles; thresholds frozen on source validation.
