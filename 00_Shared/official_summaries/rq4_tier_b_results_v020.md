# RQ4 Tier B ablations: held-out FF++ C23 (v020)

Exploratory single seed (260901); BO-selected C23 parameters; one declared change per variant;
thresholds from each variant's own source validation; ΔAUC = variant − full (same seed), cluster-bootstrap 95% CI.

| Variant | ROC-AUC | Acc | Prec | Rec | F1 | ΔAUC vs full [95% CI] | perm p | Holm p |
|---|---|---|---|---|---|---|---|---|
| full | 0.9970 | 0.9857 | 0.9857 | 0.9857 | 0.9857 | — | — | — |
| one_directional | 0.9965 | 0.9857 | 0.9789 | 0.9929 | 0.9858 | -0.0006 [-0.0020, +0.0001] | 1.0000 | 1.0000 |
| no_gate | 0.9977 | 0.9786 | 0.9718 | 0.9857 | 0.9787 | +0.0007 [-0.0005, +0.0031] | 0.5159 | 1.0000 |
| no_agreement | 0.9970 | 0.9893 | 0.9928 | 0.9857 | 0.9892 | -0.0001 [-0.0012, +0.0015] | 1.0000 | 1.0000 |
| stages_34_only | 0.9964 | 0.9714 | 0.9521 | 0.9929 | 0.9720 | -0.0007 [-0.0022, +0.0001] | 1.0000 | 1.0000 |
