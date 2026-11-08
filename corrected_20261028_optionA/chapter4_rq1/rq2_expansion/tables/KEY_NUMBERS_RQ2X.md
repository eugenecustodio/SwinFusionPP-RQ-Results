# KEY_NUMBERS_RQ2X: numbers the revised RQ2 prose may cite (computed from T10.csv and T11.csv)

Rows are 1-based CSV data rows (header excluded, `__SPAN__` counted). SwinFusion++: BO-selected / fixed recipe. No tests; no vote counts.

## Tier A (Table 10)

- **FF++ C23** accuracy, published Tier A: 92.14 (ADDNet-3D) to 100.00 (Xception); 11 values from 9 models.
  - Highest Tier A 100.00 vs SwinFusion++ 98.21 / 97.86: gaps 1.79 (BO) and 2.14 (fixed).
  - Reported values below BO (98.21): ADDNet-3D 92.14; C3D 92.86; I3D 92.86; TEI 97.86. Below fixed (97.86): ADDNet-3D 92.14; C3D 92.86; I3D 92.86. (Descriptive only; never as a count.)
- **FF++ C40** accuracy, published Tier A: 89.29 (C3D) to 98.21 (STIL); 11 values from 9 models.
  - Highest Tier A 98.21 vs SwinFusion++ 96.07 / 94.64: gaps 2.14 (BO) and 3.57 (fixed).
  - Reported values below BO (96.07): ADDNet-3D 90.36; C3D 89.29; I3D 91.07; SFormer 94.82; TEI 95.00. Below fixed (94.64): ADDNet-3D 90.36; C3D 89.29; I3D 91.07. (Descriptive only; never as a count.)
- **Celeb-DF v2** accuracy, published Tier A: 95.04 (SFormer) to 99.78 (STIL); 10 values from 9 models.
  - Not compared (fake shares differ; this study 86.20% fake).
- **DeeperForensics-1.0** accuracy, published Tier A: 98.50 (C3D) to 100.00 (I3D, ResNet+LSTM, SFormer, Xception); 7 values from 6 models.
  - SwinFusion++ 98.51 (BO) and 98.76 (fixed) lie within this range (standard set, balanced test sets): "near the ceiling, within the reported range".
- **Tier A ROC-AUC:** only STIL C40 0.9712 (T10, STIL row). SwinFusion++ C40 0.9941 / 0.9878.

## Tier B (Table 11), ranges per column (SwinFusion++ rows excluded)

- **FF++ C23 Acc (%):** 78.4 (Face X-ray ᵇ, T11 r25) to 99.1 (FTCN with Temporal Transformer ᵉ, T11 r32); 23 values.
- **FF++ C23 AUC:** 0.5749 (DSP-FWA ᶜ, T11 r29) to 0.9987 (TALL-Swin ᵃ, T11 r22); 20 values.
- **FF++ C40 Acc (%):** 34.2 (Face X-ray ᵇ, T11 r25) to 96.15 (ISTVT (not re-verified) ᵃ, T11 r21); 22 values.
- **FF++ C40 AUC:** 0.6160 (Face X-ray ᵃ, T11 r7) to 0.983 (FTCN with Temporal Transformer ᵉ, T11 r32); 20 values.
- SwinFusion++ (DeepFakes subset only, not like for like): C23 98.21 / 0.9964 and 97.86 / 0.9942; C40 96.07 / 0.9941 and 94.64 / 0.9878.
- Allowed C40 sentence (range form): "On all four FF++ manipulations or unstated subsets, reported C40 ROC-AUC values ranged from 0.6160 (Face X-ray, as reported by Xu et al., 2023) to 0.983 (FTCN); SwinFusion++ reached 0.9941 (fixed recipe 0.9878) on the DeepFakes subset alone, so the values are not like-for-like." Check the endpoints against the line above.

## Counts

- Table 10: 12 previously reported model rows (Tier A). Table 11: 28 rows from 5 sources (one row per model and source).
- J9: 234 values; in Table 10: 40, in Table 11: 86, not in a chapter table: 108 (each with its category reason).
