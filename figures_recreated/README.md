# Recreated figures

Regenerate with `python make_figures.py` (needs `matplotlib` and `numpy`). The script reads only the
CSVs in this package. File names match the originals, so each PNG can replace the one in `RQx/results/`.
The originals are untouched.

All figures share one style. Each model keeps the same colour and marker everywhere: SwinFusion++ is a
blue circle, Swin-B an orange square, Video Swin-B a green triangle. Baselines reproduced in the
preliminary study are violet diamonds. Published values are gray, filled for Tier A and hollow for Tier B.
Set `SHOW_TITLES = False` in the script if the thesis captions carry the titles.

| Figure | Data source | Checked against source | Changed from the original |
|---|---|---|---|
| RQ1/fig1_within_ci | three_seed_mean_logit_ensemble.csv (within, plain) | all 12 points and CIs match | n per test set added; fixed model colours and markers |
| RQ1/fig2_transfer_{swinfusionpp,swin_b,video_swin_b} | same CSV (all directions) | all 39 cells match | single-hue blue scale instead of viridis; empty C40 cells labelled "not run"; diagonal in bold |
| RQ1/fig2_transfer_all_models (new) | same | — | the three heatmaps side by side on one shared scale |
| RQ2/fig1_vs_published | RQ2 table1_ours, table1b, table2_published_AB | AUC points match | accuracy row added (70 of the 101 published rows are accuracy only and were never plotted); x-axis zoomed, off-scale values shown as ◄ with their value; CNN–LSTM removed (it belongs to RQ3) |
| RQ3/fig1_vs_published | RQ3 table1_ours, table1b, table2_published_AB | — | the original plotted all 18 Sabir AUCs as DeepFakes; 12 of them are Sabir's other-manipulation curves. Only the 6 DeepFakes values are kept. Single-frame (non-recurrent) Sabir variants get their own row; accuracy row added; Xception removed (it belongs to RQ2) |
| RQ4/fig1_controls_forest | paired_cluster_effects.csv (RQ4_controls) | values match | the original's title was cut off and its labels were raw IDs. Readable labels, direction arrows, a ΔAUC [CI] / p column, and a control definitions footnote |
| RQ4/fig1b_controls_transfer_forest | paired_cluster_effects.csv (RQ4_controls_transfer) | values match | the original's rows did not say which target dataset they were; now grouped by target with n |
| RQ4/fig2_tier_b_forest | tier_b_paired_effects.csv | values match | readable labels; footnote warns that the sign is variant − full, the opposite of the control plots |
| RQ6/fig1_matrix_swinfusionpp | ensemble CSV | identical to RQ1 fig2 SwinFusion++ | same restyle (still a duplicate of RQ1's figure) |
| RQ6/fig1b_delta_vs_baselines (new) | paired_cluster_effects.csv (RQ1 + RQ6) | — | paired ΔAUC vs each baseline, with * where p_Holm < 0.05 |

Significance marks: the RQ1/RQ4/RQ6 stars and p-columns use the corrected rank-based cluster permutation
test (`paper/rank_permutation_results.csv`, Holm within each family). The original test swapped raw logits
across models with different logit scales. The Tier B forest still shows the original test, because Tier B
was not re-run.

## Paper figure and corrected significance tests

- `paper_figure.py` → `paper/fig_paired_delta_auc.{pdf,png}`: a single-column (3.5 in) forest plot of SwinFusion++ minus each baseline (ΔAUC), within-dataset and transfer. It uses vector graphics with embedded fonts. Its markers now use the corrected p-values: `python paper_figure.py paper/rank_permutation_p.csv`. The interim bootstrap version flagged the same 9 comparisons.
- `rerun_paired_tests.py <raw_predictions_v020 folder>` re-runs every paired test. It uses a rank-based cluster permutation test because the original swapped raw logits across models with different logit scales. It also recomputes the original test as a self-check: the new p-values are valid only if that check reports `original p reproduced: True`. It writes `paper/rank_permutation_results.csv` and `paper/rank_permutation_p.csv`. A full run takes about 20–30 minutes.
