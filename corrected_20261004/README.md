# Corrected copies (2026-10-04)

This folder holds corrected versions of the files that needed changes. The originals in `RQ1/` to `RQ6/` are untouched; an extra backup is in `_originals_before_corrections_20261004/`. To adopt a correction, replace the original file with the copy here (same relative path).

## What was corrected

1. **Paired-test p-values (RQ1, RQ4, RQ6, and the RQ1 supplementary tables).** The original cluster permutation test swapped raw ensemble logits between models whose logit scales differ, so its p-values were unreliable. All 73 paired comparisons were re-run with a rank-based version, which converts each model's logits to within-model ranks before the swap (Bandos et al., 2005). The re-run used the same seeds, the same 5,000 permutations and the same videos, and it reproduced every original p-value exactly before computing the corrected ones. ΔAUC values, bootstrap intervals and all metrics are unchanged. Full results: `00_Shared/statistics_raw/paired_cluster_effects_rank_corrected.csv`.
2. **Published values in RQ2 and RQ6.**
   - TALL-Swin's row showed Xception's numbers as reported in the TALL paper. The correct values are C23 98.7% / AUC 0.999 and C40 92.8% / AUC 0.946.
   - STIL's accuracies were misquoted. The correct values are C23 99.6% and C40 98.2%; 0.971 is its C40 AUC.
   - The C40 values for I3D, SFormer and FTCN were missing and have been added.
   - Xception's accuracies are now given as the published ranges.
3. **RQ3:** Sabir et al.'s DeepFakes ROC-AUC (best 0.996, above SwinFusion++'s 0.994 on C40) was missing, as was the note that Sabir's models are GRU-based. The conclusion is now "comparable to, not better than" the best aligned recurrent models.
4. **Rounding:** SwinFusion++'s FF++ C23 → Celeb-DF AUC is 0.878 (exact 0.87850), not 0.879.

## Conclusions that changed

- **RQ1 (within-dataset):** unchanged. There are still no significant differences.
- **RQ1 / RQ6 (transfer):**
  - SwinFusion++'s C23 → C40 advantage is now significant against both baselines.
  - SwinFusion++ beats Swin-B in six directions, up from four.
  - Video Swin-B is also significantly better on Celeb-DF → C23.
- **RQ4:**
  - The within-C23 topology difference is no longer significant.
  - On C23 → DeeperForensics, the topology control (no exchange block) is now significantly better than SwinFusion++. The +0.042 advantage over the capacity control still holds.
- **RQ2:** SwinFusion++ has the highest C40 ROC-AUC among published values, but its accuracy is one to two points below the best published values on C23, C40 and Celeb-DF.

Tier B ablation p-values were not re-run and still come from the original test.

## Files

- `RQ1/`, `RQ2/`, `RQ3/`, `RQ4/`, `RQ6/`: `*_RESULTS_AND_DISCUSSION.md`, each starting with a correction note.
- `RQ*/results/`: the paired-test tables (.csv and .md, including `00_all_tables_inline.md`). They carry corrected `permutation_p` / `holm_p` values and, in the CSVs, a `p_method` column.
- Recreated figures with the corrected significance marks are in `../figures_recreated/`.
