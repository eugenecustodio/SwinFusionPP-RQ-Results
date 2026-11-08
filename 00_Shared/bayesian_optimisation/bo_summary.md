### Bayesian optimisation (Optuna TPE + median pruning), selected configurations

Selection on source-validation video-level ROC-AUC only; the selected checkpoint was replayed exactly in a clean process.

| condition | trials | completed | pruned | best_validation_auc | selected_trial | new_lr | backbone_lr | weight_decay | effective_batch | schedule |
|---|---|---|---|---|---|---|---|---|---|---|
| FF++ C23 (HQ) | 12 | 8 | 4 | 0.9994 | 11 | 3.15e-05 | 2.78e-05 | 1.22e-04 | 8 | A |
| FF++ C40 (LQ) | 12 | 8 | 4 | 0.9978 | 4 | 2.86e-04 | 2.73e-05 | 0.0826 | 8 | C |
| Celeb-DF v2 | 8 | 5 | 3 | 0.9993 | 2 | 3.40e-05 | 2.18e-05 | 0.0063 | 8 | A |
| DeeperForensics-1.0 | 8 | 8 | 0 | 0.9977 | 4 | 3.01e-05 | 2.18e-05 | 1.22e-04 | 8 | A |
