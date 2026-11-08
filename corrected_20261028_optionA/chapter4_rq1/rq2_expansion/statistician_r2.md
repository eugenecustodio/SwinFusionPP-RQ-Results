# Statistician, Round 2 (RQ2 expansion): replies and production

## Replies to the plan

**Rule 1: AGREE, with one category application added (please confirm).**
- **TALL Table 2's two-branch AUCs.** TALL's 98.70 (C23) and 86.59 (C40) are **identical to Masi et al.'s frame-level AUCs**. Masi's Table 2 prints 98.70/86.59 at frame level and 99.12/91.10 at video level, yet TALL labels them video level.
  - I treat them as 1(c), a misquoted unit, and list them in J9 only.
  - TALL's two-branch accuracies (96.43/86.34) stay in Table 11.
- **TALL's Xception C23 accuracy (95.73)** equals Rössler et al.'s frame-level, all-manipulation accuracy. It is kept in Table 11 but marked ‡, because TALL's other Xception values match no known frame-level value.

Neither decision depends on a value's size, only on its provenance.

**Rule 2: AGREE.**

**Rule 3: AGREE.** It is my proposal; the methodologist still needs to confirm it.

**Rule 4: AGREE.** Face X-ray, Two-branch, MesoNet and Xception each have one row per source in Table 11.

**Rule 5: AGREE.**

**Model set: AGREE.**
- **Table 10:** I placed D-FWA with Xception in the frame-level group. FWA is a frame-level warping-artifact detector.
- **Table 11:** DSP-FWA, Masi's Xception and LipForensics' Xception are included as their own rows.

**Chapters 1 and 3: AGREE.** The methodologist drafts them.

## Files (`team/rq2x/tables/`)

**Built by `team/scripts/statistician_rq2x_tables.py`.**
- It merges `rq2/tables/J9.csv`, `statistician_values.csv`, `methodologist_values.csv` and `methodologist_values_extra.csv`.
- Duplicates were removed on test set, model, metric, value and producing source: 246 records became 234.
- Every chapter-table cell is asserted to exist in the merged verified records.
- The SwinFusion++ cells are asserted against the RQ2 T9 values.

| File | Contents |
|---|---|
| `T10.csv` + `T10_note.txt` (93 words) | Tier A, 12 published model rows grouped by family, with SwinFusion++ BO and fixed first. Sources: ᵃ Gu et al., ᵇ X. Li et al., ᶜ Jiang et al., ᵈ Kingra et al. |
| `T11.csv` + `T11_note.txt` (100 words) | Tier B, 28 rows from 5 sources (ᵃ Xu, ᵇ Haliassos, ᶜ Masi, ᵈ Rössler, ᵉ Zheng supplement). The SwinFusion++ rows are marked "DeepFakes subset only; not like-for-like". FTCN's DeeperForensics AUC 1.000 (own split) is in its Setting cell. |
| `J9.csv` + `J9_note.txt` | 234 values: 40 in Table 10, 86 in Table 11, and 108 not in a chapter table, each with its category reason, (a)–(f) or Rule 5. |
| `KEY_NUMBERS_RQ2X.md` | Computed from the CSVs |

**Data rows excluded from the chapter tables (108):**
- 33 copies;
- 16 non-detectors;
- 16 precision/recall values;
- 13 non-within-dataset results;
- 10 variants;
- 13 values from source tables not adopted (Zi et al., Y. Li et al., the Rössler Table 5 and Table 1 entries, Sabir's copies);
- 4 not peer-reviewed;
- 3 misquoted, including the TALL two-branch AUCs.

## Changes the lead must make in the RQ2 prose (from KEY_NUMBERS_RQ2X)

- **Unchanged.** The highest Tier A FF++ accuracies are still 100.00 (C23, Xception XN-avg) and 98.21 (C40, STIL). The gaps stay 1.79 / 2.14 (BO) and 2.14 / 3.57 (fixed).
- **New Tier A ranges:**
  - C23: 92.14 (ADDNet-3D) to 100.00;
  - C40: 89.29 (C3D) to 98.21.
  - The "lower values" example (I3D 92.86 / 91.07) still holds. Fixed C23 97.86 **equals** TEI's 97.86, so do not say "above TEI" for the fixed recipe.
- **DeeperForensics-1.0, now Tier A.** The reported range is 98.50 (C3D) to 100.00. SwinFusion++ 98.51 (BO) and 98.76 (fixed) lie within it: "near the ceiling, within the reported range".
  - The old "99.67% to 100.00% … on different constructions" must change.
- **C40 ROC-AUC sentence, in range form (Tier B).** Reported values span 0.6160 (Face X-ray, via Xu et al.) to 0.983 (FTCN). SwinFusion++ reached 0.9941 / 0.9878 on the DeepFakes subset alone, so the comparison is not like-for-like. No count of models.
- **C23 ROC-AUC (Tier B)** spans 0.5749 (DSP-FWA) to 0.9987 (TALL-Swin). SwinFusion++'s 0.9964 / 0.9942 lie within the range.
