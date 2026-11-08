# Option A version (2026-10-28) — use this folder for Chapter 4

This folder **supersedes `../corrected_20261004/`** for every write-up, table and figure it contains. The originals in `../RQ1/`–`../RQ6/`, the backup in `../_originals_before_corrections_20261004/` and the 2026-10-04 corrected copies are untouched.

## What Option A means

The manuscript (Chapter 3, *Statistical Treatment of Data*) and decision D-25 (2026-09-30) declared the analysis this way. This folder reports the results that way.

| Question | Model used | Holm family (size) |
|---|---|---|
| RQ1 / RQ6 internal architecture comparison (**principal**) | SwinFusion++, Swin-B and Video Swin-B, **all fixed recipe** | `RQ1_architecture` (8), `RQ6_architecture` (18) |
| Configured-system comparison (unequal tuning) | **BO-selected** SwinFusion++ vs fixed-recipe Swin-B / Video Swin-B | `RQ1_configured_system` (8), `RQ6_configured_system` (18) |
| Effect of the Bayesian optimization | BO-selected minus fixed-recipe SwinFusion++ | `RQ1_optimization_effect` (4), `RQ6_optimization_effect` (9) |
| RQ2, RQ3, published context in RQ4 and RQ6 (external models) | **BO-selected** SwinFusion++, with the fixed-recipe value alongside | no paired tests (published values) |
| RQ4 matched controls | fixed-recipe SwinFusion++ vs topology / capacity controls | `RQ4_controls` (2), `RQ4_controls_transfer` (6), unchanged |
| RQ4 Tier B ablations | one-change variants of the BO-selected model, single seed | unchanged; still the original test, not re-run |

The interim decision of 2026-10-02 (`../00_Shared/protocol_and_decisions/presented_model_decision_v020.json`) had made the BO-selected model the primary comparison. That decision was made before any test scoring. On 2026-10-28 the user chose to report according to the manuscript's declared plan instead. **Both regimens are reported in full and no comparison was dropped; only the labels "principal" and "configured system" changed.** Because this choice was made after the test results were known, state it in the thesis. For example: *"Results are reported according to the analysis plan in Chapter 3. An interim decision to present the BO-selected configuration as primary was reverted to the approved plan; all comparisons under both regimens are reported."*

## What changed in the conclusions

- **RQ1 within-dataset.** Under the fixed recipe, SwinFusion++ is statistically indistinguishable from both encoders (all 8 p_Holm = 1.00). Its point estimates are slightly lower on C23, C40 and Celeb-DF and highest on DeeperForensics. The BO-selected configuration (configured system) has the highest AUC on C40 and Celeb-DF; that difference is also not significant.
- **RQ1 / RQ6 transfer.** Under the fixed recipe, SwinFusion++ is significantly better than Swin-B in 7 of 9 directions and than Video Swin-B in 3. It is never significantly worse than either encoder, and its mean transfer AUC is the highest (0.810 vs 0.785 / 0.700). From FF++ C23 to C40 and to Celeb-DF, the three models are tied.
- **Optimization effect.** BO significantly improves within-C40 (+0.0063), within-Celeb-DF (+0.0031) and C23 → C40 (+0.0102). It significantly lowers five transfer directions (−0.04 to −0.10).
- **RQ6 against published models, FF++ → Celeb-DF.** The fixed recipe gives 0.862 (above all listed except FTCN 0.869 and TALL-Swin 0.908). The BO-selected model gives 0.878 (above all but TALL-Swin). The intervals overlap the top published values.
- **Chapter 3 criterion and hypothesis.** RQ6 now evaluates the "strong only if" criterion and gives an explicit H0 decision.
- **Sensitivity to the family grouping.** Re-grouping changed exactly one conclusion compared with the 2026-10-04 grouping. BO vs fixed within Celeb-DF is significant in its own 4-test family (p_Holm = 0.021) but was not when pooled with 12 tests (0.077). Column `holm_sensitivity_pooled` in `paired_tests_optionA.csv` gives the pooled values for every test.

## Other corrections included here

- **RQ2: SFormer within-dataset accuracy ranges.** These are now C23 98.5–99.9% and C40 94.8–98.2%. Six cells from SFormer's cross-compression Table 4 had been labelled train = test. They are flagged in `RQ2/results/table2_published_AB.csv` (`optionA_20261028_note`) and excluded from the RQ2 figure.
- **RQ3:**
  - Chen et al. 2022 is now Tier C, because only secondary survey quotes are available.
  - Saikia et al.'s FF++ AUC is 0.75–0.91; the 0.73 is a Celeb-DF value.
  - The "early designs" claim is narrowed to Saikia et al., since Güera & Delp report on different data.
  - Sabir's ablation is added: alignment, not recurrence, gives most of the gain.
  - The causal claim that C40 is "where temporal transformers help most" is removed. Under the matched recipe, SwinFusion++ does not exceed the encoders on C40.
- **RQ4.** The conclusion now says the advantages "cannot be attributed to cross-attention". It no longer says they are "a property of the optimized system", which is not supported once the fixed recipe also transfers better.
- **RQ6.** The preliminary-study comparison is now a change in pattern, not a "reversal".
- **Spelling and terminology.** American spelling and the manuscript's terms are used throughout: "fixed-recipe", "BO-selected", "configured system".

## Files

| Path | Content |
|---|---|
| `RQ1/`, `RQ6/` | Rewritten write-ups and regenerated tables (`.md` + `.csv`) |
| `RQ2/`, `RQ3/`, `RQ4/` | Write-ups edited from the 2026-10-04 corrected copies; RQ2 flagged published table; RQ4 control tables |
| `paired_tests_optionA.csv` | All 73 paired tests with the Option A family, Holm p, the previous family's Holm p and the pooled-sensitivity Holm p |
| `figures/` | All figures regenerated with `figures/make_figures_optionA.py`, a patched copy of `../figures_recreated/make_figures.py`. Principal figures use the fixed recipe. Configured-system figures have `configured_system` or `_bo` in their names. |
| `calibration/` | **Added 2026-10-30.** Brier score, ECE (15 bins) and reliability diagrams for all 60 ensemble cells, using the frozen source-validation temperatures. Includes `CALIBRATION.md`, two CSVs and the figure. |
| `compute/` | **Added 2026-10-30.** Parameters, FLOPs per clip and per video, training throughput, peak memory and checkpoint size (`COMPUTE_COST.md`, `compute_cost.csv`) |
| `CHAPTER4_NOTES.md` | **Read before writing Chapter 4.** Holds the Fix 1 verdict text, the Option A disclosure and the open items |
| `scripts/optionA_tables.py` | Rebuilds every table and `paired_tests_optionA.csv` from `../00_Shared/statistics_raw/` |
| `scripts/calibration.py`, `scripts/reliability_fig.py` | Calibration from the held-out video predictions in the project backup (`results/raw_predictions_v020/`, plain variant) |
| `scripts/flops.py` | Parameter and FLOP counts using the project's model code from the backup (`src/swinfusionpp/models/`, `configs/models/`), with random weights |

**Reproduce:** `python scripts/optionA_tables.py .. .` then `python figures/make_figures_optionA.py`. Run both from this folder; the second needs `matplotlib`.

**Check performed:** the Holm implementation in `optionA_tables.py` reproduces all 73 stored adjusted p-values for the previous families exactly before computing the new ones.

## Still open

- **The LaTeX paper (`../../DA.zip`, `paper/main.tex`) still uses the old framing**, with the BO-selected model as primary, and has not been updated.
- **Manuscript deviations not covered by Option A:**
  - BO used 8 trials for Celeb-DF and DeeperForensics; the manuscript declares 12/16/20.
  - The gamma and RandAugment ablations were skipped.
  - Calibration and compute cost are now computed (`calibration/`, `compute/`). The metadata-shortcut audit was run before training (backup: `reports/audit/metadata_shortcut_audit_v001.md`, decision D-43) and needs reporting in Chapter 4.
  - Latency was never properly measured (only cold single-clip timings).
  - Gamma correction was disabled in the final pipeline (decision D-08), but the manuscript describes it as applied.
