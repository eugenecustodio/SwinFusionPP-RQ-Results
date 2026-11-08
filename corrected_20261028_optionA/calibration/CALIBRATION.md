# Calibration (Brier score, ECE, reliability diagrams)

Promised in the manuscript (Chapter 3, *Statistical Treatment of Data*): "Calibration will use the previously frozen source-validation temperature and will be reported separately by dataset and transfer direction through Brier score, ECE with the declared binning method, and reliability diagrams."

## Method
- **Probability:** sigmoid(mean of the three seed video logits / T). T is the three-seed ensemble temperature fitted on source-validation videos only, before any test scoring (`../../00_Shared/statistics_raw/source_validation_operating_points_v020.csv`). No target-domain recalibration.
- **ECE:** 15 equal-width bins on P(fake), the binning declared in the preliminary study. **Brier:** mean squared error of P(fake).
- **Data:** the held-out video-level predictions (`results/raw_predictions_v020/*/…video_predictions.parquet`, plain variant) from the project backup.
- **Self-checks (the run stops if one fails):** every one of the 180 seed files reproduces its stored calibrated probability exactly, and all 60 ensemble ROC-AUCs equal the package values. Script: `../scripts/calibration.py`.

## Results — ECE / Brier (lower is better)

| Condition | n | SwinFusion++ (fixed) | Swin-B | Video Swin-B | SwinFusion++ (BO-selected) |
|---|---|---|---|---|---|
| Within C23 | 280 | 0.019 / 0.015 | 0.019 / 0.016 | 0.014 / 0.009 | 0.009 / 0.008 |
| Within C40 | 280 | 0.026 / 0.041 | 0.036 / 0.044 | 0.024 / 0.031 | 0.019 / 0.028 |
| Within Celeb-DF | 978 | 0.012 / 0.018 | 0.018 / 0.020 | 0.012 / 0.013 | 0.010 / 0.011 |
| Within DFo | 402 | 0.012 / 0.009 | 0.010 / 0.010 | 0.036 / 0.028 | 0.009 / 0.008 |
| C23 → C40 | 280 | 0.080 / 0.075 | 0.102 / 0.082 | 0.071 / 0.070 | 0.065 / 0.062 |
| C23 → Celeb-DF | 978 | 0.312 / 0.276 | 0.405 / 0.354 | 0.324 / 0.283 | 0.349 / 0.320 |
| C23 → DFo | 402 | 0.447 / 0.430 | 0.479 / 0.473 | 0.412 / 0.391 | 0.476 / 0.471 |
| Celeb-DF → C23 | 280 | 0.289 / 0.275 | 0.339 / 0.322 | 0.266 / 0.246 | 0.327 / 0.315 |
| Celeb-DF → C40 | 280 | 0.442 / 0.429 | 0.444 / 0.432 | 0.456 / 0.442 | 0.463 / 0.457 |
| Celeb-DF → DFo | 402 | 0.443 / 0.440 | 0.467 / 0.458 | 0.451 / 0.443 | 0.468 / 0.463 |
| DFo → C23 | 280 | 0.481 / 0.477 | 0.489 / 0.487 | 0.481 / 0.472 | 0.490 / 0.487 |
| DFo → C40 | 280 | 0.489 / 0.484 | 0.487 / 0.485 | 0.483 / 0.479 | 0.490 / 0.486 |
| DFo → Celeb-DF | 978 | 0.848 / 0.839 | 0.850 / 0.844 | 0.837 / 0.822 | 0.852 / 0.846 |

All 60 cells, including the controls and the uncalibrated values, are in `calibration_ensembles.csv`; the reliability-diagram bins are in `reliability_bins.csv`; the figure is `fig_reliability_fixed_recipe.png`.

## Interpretation
1. **Within datasets, every model is well calibrated:**
   - ECE 0.009–0.036 and Brier 0.008–0.044.
   - Temperature scaling lowered ECE in 12 of 18 within-dataset cells. In the rest the uncalibrated scores were already as good or better.
   - Differences between models are small. The BO-selected configuration is the best calibrated within datasets.
2. **Under frozen transfer, calibration breaks down for every model.**
   - Median ECE is 0.446.
   - In 35 of 42 transfer cells, the calibrated Brier score is worse than always predicting the target's fake prevalence.
   - The source temperature still helps, lowering ECE in 41 of 42 transfer cells, but it cannot fix a domain shift.
   - The reliability diagrams show the cause: on new datasets the models give many fake videos a low P(fake). This matches the recall collapse at the source threshold (RQ1/RQ6).
3. **Consequence for the platform.** The "Validation-Calibrated Estimated Probability" is trustworthy only for videos resembling the training data. It should be described as a screening score whose calibration is not guaranteed for unfamiliar sources. That is consistent with the manuscript's own *Decision support, not forensic proof* limitation.
