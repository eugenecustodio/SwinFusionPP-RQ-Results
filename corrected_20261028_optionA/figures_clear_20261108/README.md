# Clear figures (2026-11-08)

These 21 charts replace the figures in `../figures/`, `../chapter4_rq1/figures/` and the reliability chart in `../calibration/`. Nothing older was changed or deleted.

Regenerate them with `python make_figures_clear.py` (needs matplotlib, numpy and pandas). Every chart is at most 6.0 in wide at 300 dpi and all text is at least 8 pt, so the text stays readable at full thesis-page width.

## How they were checked

- All 39 distinct older images were viewed one by one.
- 112 values read from the older images matched the source CSVs with no mismatches (52 AUC heatmap cells, 52 difference cells with their significance stars, 8 RQ4 rows). All 73 paired differences equal the difference between the two ensemble AUCs.
- The script stops with an error if the data disagrees: ROC curves are recomputed against the ensemble CSV (39 model-cells), and Figure 12 and RQ2 values are checked against their source tables.
- Each new chart was rendered and inspected for clipped or overlapping text.

## What changed

| Chart | Problem in the old version | New version |
|---|---|---|
| Figure 11 and all train/test heatmaps | White text on mid-blue cells was hard to read (11 cells); "frozen", "directional" and similar jargon | Color-coded number table, always the more readable text color, "Trained on / Tested on" labels |
| Figure 12 | Forest plot with hollow/filled markers, no direction cue, "m = 8" | **Simple bars.** Right of 0 means SwinFusion++ higher; blue means significant, gray means not |
| Figure 13 and J1 | AUC numbers had no label and were in hard-to-read colored text; the zoom in J1 was not stated; missing 0 ticks | "AUC" key in dark text, plain axis names, zoom stated |
| RQ6 difference heatmaps | Color scale stopped at ±0.17 without saying so (+0.201 and +0.258 looked the same); internal names such as `RQ1_architecture` in the note; 6 low-contrast cells | Full-range scale, plain note |
| RQ1 within-dataset | Long title left about 25% of the image empty; text shrank when placed on a page | Short title, states that the y-axis starts at 0.975 |
| **RQ2** | **Wrong data:** FTCN 0.981 and 0.999 and Xception 0.939 (cross-manipulation or ablation results) were plotted as within-dataset; hidden-set DeeperForensics values were included; 3.9 pt text at page width | Rebuilt from the verified Tier A table (`T10.csv`); both SwinFusion++ versions shown |
| RQ3 | BO model only; Sabir variants overplotted; a p value from different model runs sat next to these points | **Simple bars from 0**, both SwinFusion++ versions, note explains the earlier test |
| RQ4 (3 charts) | Internal names in notes; significance not marked; opposite sign convention on the ablation chart was easy to miss | Same simple bars as Figure 12; ablation chart reads "variant minus full model" |
| Calibration | Three overplotted scatter sets; only 4 of the 9 transfer directions shown, without saying so | Two line charts covering all 4 within-dataset and all 9 transfer cells, with ECE printed |

RQ2 was deliberately left out of Chapter 4 (notes, section 9). This corrected version is here if you decide to use it. The RQ2 chart shows accuracy only because Tier A has just one ROC-AUC value (STIL C40, 0.9712); the Tier B ROC-AUC values are in the chapter's Tier B table.

## Thesis captions

Figures 11, 13 and J1 can be swapped in with their existing captions. **Figure 12 needs this new note**, because the chart type changed:

> *Note.* Bars are ensemble ΔROC-AUC (SwinFusion++ minus comparator). Whiskers are unadjusted 95% percentile intervals from 5,000 stratified cluster-bootstrap draws. Blue bars denote Holm-adjusted p < 0.05 (rank-based cluster permutation test); gray bars are not significant. Because the intervals are unadjusted, one interval excludes 0 without significance (DFo → C23 vs Video Swin-B). Panels use different x-scales. Abbreviations as in Figure 11.

The thesis files themselves were not edited. The new images still need to be inserted into the Word and Google Docs versions.

## Older figure folders

| Folder | Status |
|---|---|
| `../../RQ*/results/`, `../../_originals_before_corrections_20261004/` | Original raw output. Do not use: raw internal names, cut-off titles on the RQ4 charts, and the RQ3 chart plots 12 non-DeepFakes Sabir values as DeepFakes. |
| `../../figures_recreated/` | The October 4 version, where "SwinFusion++" means the BO-selected model. Superseded by the fixed-recipe framing. The same file names exist in other folders with different data, so check the folder before using one. |
| `../figures/`, `../chapter4_rq1/figures/` | The October 28–30 versions. The numbers are correct except RQ2; these clear versions replace them. |
