# Statistician, Round 2 (RQ2): replies to the plan, and the check of T10 and J9

## Replies to the plan items

1. AGREE.
2. AGREE. T9 is produced in this layout.
   - The Xception CI cell is printed "[—]" so the column stays parseable.
   - The analyzed DeeperForensics-1.0 fake count is confirmed as 2,185 of 2,385 (preliminary Table 2: 200/2,185).
3. AGREE.
   - The XN-avg range citing both sources is fine: my de-duplication rule applies only to identical copied values.
   - Celeb-DF stays "A". Tier A describes dataset, subset and unit, not identical test videos, and the note says the test sets differ.
4. **AGREE with one condition (rule A7).** "Within about two points" holds for the **BO-selected** configuration only:
   - C23: 100.00 vs 98.21, a gap of 1.79;
   - C40: 98.21 vs 96.07, a gap of 2.14.

   For the fixed recipe the gaps are 2.14 (C23, 97.86) and **3.57** (C40, 94.64). The prose must say "BO-selected" or give both gaps. M's draft RQ2 answer ("Its accuracy was within about two percentage points of the highest previously reported values") must become: "On FF++, the BO-selected configuration's accuracy was within about two percentage points of the highest previously reported values (fixed recipe: 2.1 and 3.6 points)".
5. AGREE.
6. AGREE. C-4 holds for both configurations: C40 ROC-AUC BO 0.9941 and fixed 0.9878 are both above FTCN 0.983, STIL 0.971 and TALL-Swin 0.946. C-5 needs the fixed values added (98.76% / 0.9974).
7. AGREE.
8. AGREE.
9. AGREE. `refs_rq2.txt` matches M's Crossref-verified entry.
10. AGREE.

## Check of T10.csv against the package and M's verification

All cell values match `table2_published_AB.csv`, M's §D verification and J9. This includes:
- the SwinFusion++ rows, which equal T9;
- XN-avg 98.93–100.00 / 96.78–97.14 / 99.44;
- I3D 92.86 / 91.07 / 99.23 / 100.00;
- STIL 99.64 / 98.21 with 0.9712 / 99.78;
- FTCN 99.1 with 0.998 / 0.983 / 1.000;
- TALL-Swin 98.65 with 0.9987 / 92.82 with 0.9457;
- SFormer's four ranges.

The cross-manipulation, hidden-set and frame-level values are correctly excluded.

### MUST-FIX

**T10-1. The T10 note is 101 words (the limit is 90), and it lacks the agreed XN-avg sentence (plan item 3).** Replace it with this 88-word version:

> Note. Values as printed under each paper's own protocol; none was tested. A: same dataset, compression, DeepFakes subset, and video level; B: subset, unit, or protocol differs or is unstated. Xception ranges span two papers printing different values. Celeb-DF v2 test sets differ in size and fake share (here 978 videos, 86.20% fake), and DeeperForensics-1.0 constructions differ. SFormer values were not re-verified. ᵃGu et al. (2021); ᵇX. Li et al. (2020); ᶜJiang et al. (2020); ᵈXu et al. (2023); ᵉZheng et al. (2021), supplement; ᶠKingra et al. (2024).

**T10-2 (J9). Two "Yes" rows have fields that contradict their Tier A label.**
- **The problem:**
  - Row "FF++ C23, STIL, 99.64%" has subset "unstated or other".
  - Row "FF++ C40, STIL, ROC-AUC 0.9712" has unit "unstated".
  - Tier A requires the DeepFakes subset and video level.
- **The fix:** M verified both as DeepFakes and video level, so set Subset = "deepfakes" on the first and Unit = "video" on the second. If either cannot be confirmed, the value becomes (B) in T10 as well.

### SUGGEST

**T10-3. Row label "Xception (frame-score average)".** That label describes the XN-avg values (ᵃᵇ). The DeeperForensics-1.0 cell is Jiang et al.'s Xception (J9 lists it as "Xception"). Either rename the row "Xception" and add "XN-avg in ᵃ, ᵇ", or move the DeeperForensics-1.0 value into the note.

**T10-4. De-duplication is inconsistent.**
- For I3D, the identical Gu et al. copies are marked "No (duplicate)".
- For XN-avg on Celeb-DF v2 (99.44 in both papers), both rows are "Yes" and the cell cites ᵃᵇ.

For consistency, cite ᵇ only there and mark the Gu row as a duplicate. This changes nothing numerically.

## Files produced

All in `team/rq2/tables/`:
- `T9.csv`, `T9_note.txt` (70 words);
- `KEY_NUMBERS_RQ2.md`;
- `_t9_values.json` (unrounded values, internal).

Script: `team/scripts/statistician_rq2_T9.py`. It asserts every SwinFusion++ value against the package and derives Xception's confusion counts as unique integer solutions, which match the preliminary manuscript's text. The superseded drafts were moved to `rq2/work/superseded/`.
