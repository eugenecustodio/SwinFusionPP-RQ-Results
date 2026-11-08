# SwinFusion++ — Results and Discussion package (per RQ)

> **Use `corrected_20261028_optionA/` for Chapter 4 (added 2026-10-28).** It reports the results per the manuscript's Chapter 3 plan: the fixed-recipe comparison is principal and the BO-selected SwinFusion++ is a separately labeled configured system. It supersedes `corrected_20261004/` and the "presented model" convention below. Everything else in this package is unchanged.

Generated 2026-10-04 (v020 protocol). Open each `RQX/RQX_RESULTS_AND_DISCUSSION.md` first:
it contains the RQ wording, the results tables with the final test numbers, an interpretation,
the answer to the RQ, and the limitations to state. The `RQX/results/` folder holds every
table (.md readable, .csv for Word/Excel) and figure (.png) for that RQ, plus
`00_all_tables_inline.md` (all tables of that RQ in one file).

| Folder | Content |
|---|---|
| `RQ1/` | SwinFusion++ vs Swin-B / Video Swin-B, within-dataset and cross-dataset (main results) |
| `RQ2/` | SwinFusion++ vs established baselines (Xception reproduced; I3D, STIL, FTCN, TALL-Swin, SFormer published) |
| `RQ3/` | SwinFusion++ vs CNN-LSTM (reproduced + published) on FF++ HQ/LQ |
| `RQ4/` | Cross-attention: matched controls, Tier B ablations, CAST / TSFF-Net published |
| `RQ6/` | Synthesis within and across datasets vs CNN- and transformer-based models |
| `00_Shared/` | raw statistics (CSV), Bayesian-optimisation trials and selected settings, literature tables + your preliminary paper, evaluation protocol and decision log, the two official summary reports |

RQ5 (usability study) is outside this computational package.

Conventions used in every table: "SwinFusion++" = Bayesian-optimised configuration (presented model);
Swin-B and Video Swin-B = shared fixed recipe; video-level held-out test sets; three-seed mean-logit
ensembles; thresholds frozen on source validation before any test scoring; ROC-AUC 95% intervals from
5,000 class-preserving cluster-bootstrap draws; paired tests = cluster permutation with Holm correction
within each pre-declared family. Published values are context under their own protocols (tiers A/B/C).
