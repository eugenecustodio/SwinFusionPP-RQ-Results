# RQ2 plan: lead's resolutions of the two Round 1 memos (reply AGREE or OBJECT per item, then produce)

## Resolutions

1. **Structure:** M-A2.
   - Heading2: "Research Question 2: SwinFusion++ Compared With Established Baselines".
   - Opening paragraph covering the three kinds of evidence and the disclosures.
   - Bold sub-subsections: "SwinFusion++ and the Preliminary-Study Xception Baseline", "Comparison With Previously Reported Results", "Answer to Research Question 2".
2. **Table 9:** one table that merges both proposals. It replaces S's separate T9 and T10.
   - **Layout:** one span row per test set, e.g. "FF++ C23 — this study: 280 videos (50.00% fake)". Then three model rows: SwinFusion++ (BO-selected), SwinFusion++ (fixed recipe) and Xception (preliminary study).
   - **Columns:** Model | Test videos (fake %) | ROC-AUC [95% CI] | Acc (%) | Rec (%) | Spec (%) | F1.
   - **Xception rows:** the CI cell is "—". The Celeb-DF and DeeperForensics accuracy, recall, specificity and F1 cells are marked * and †, with the note explaining the degenerate operating points (S A6).
   - **Rec and Spec:** they replace a separate confusion table. They show the all-fake and 1,288-FN patterns directly.
   - **Precision:** goes to Appendix J9 for the BO model only, if needed. It is not in Table 9.
3. **Table 10:** M's matrix (models × four datasets), with cell strings "Acc …; AUC … (tier)ᵃ", the source letters and M's note. Only verified Tier A/B values.
   - **Excluded from Table 10:** the FTCN cross-manipulation values, the DFo hidden-set values and frame-level values. They are listed in J9 marked "not a within-dataset result".
   - **The XN-avg C23 discrepancy** (S-MIL 100.00 vs STIL 98.93) is kept as a range citing both sources, with one note sentence. This is preferred to S's de-duplication rule because the two papers print different values.
   - **STIL C40 AUC 0.971** is Tier A (DeepFakes subset, video level, verified by M).
   - **SFormer** is marked "as extracted; original not accessible" in J9 only. The Table 10 note says it was not re-verified.
4. **Accuracy comparisons:** per S A2.
   - The "within about two points" statement covers FF++ C23 and C40 only (both test sets balanced): C23 100.00 vs 98.21; C40 98.21 vs 96.07.
   - Celeb-DF v2 accuracies are NOT compared across studies. The text says why: our test set is 86.20% fake, so a rule that calls every video fake scores 86.20%, and the published test sets have other or unstated prevalences.
   - M's C-3 is revised accordingly.
5. **Figure 14:** DROPPED (S position).
   - Reason: there are too few Tier-A video-level AUC points, and any plot of published values reads as a leaderboard, which our claim rules forbid. Table 10 carries the information.
   - Methodologist: OBJECT here if you still want it, giving a layout that avoids the leaderboard reading.
6. **Claims.**
   - **Allowed:** M's C-1, C-2, C-4 (C40 sentence: name FTCN 0.983 (B), STIL 0.971 (A) and TALL-Swin 0.946 (B), with the "not like-for-like" clause) and C-5.
   - **Combined with:** S's allowed #1–#4 and the A7 rule: every comparative sentence must hold for both BO and fixed, or name the one it holds for.
   - **Forbidden:** the union of both forbidden lists.
7. **Disclosures:**
   - only Xception was run locally, in an earlier pipeline;
   - the Celeb-DF v2 test set is 978 identity-grouped videos, not the official 518-video list;
   - the DeeperForensics-1.0 binary construction (unperturbed manipulated videos with their FF++ source originals as the real class) differs from the published benchmark settings;
   - the preliminary study's Celeb-DF (859) and DeeperForensics (2,385, 91.61% fake, perturbed) test populations differ.

   None of this is framed as a deviation.
8. **Appendix J:** retitle it "Supplementary Results for Research Questions 1 and 2". Add **J9**, the full long-format list of previously reported values considered, with paper, table, unit, subset, test population, tier and an "included in Table 10?" column. Excluded values are marked with the reason.
9. **References:**
   - add Li, X. et al. (2020), S-MIL (M's verified APA entry);
   - add Custodio et al. (2026), which is already set up in the build;
   - in-text forms: "X. Li et al., 2020" and "Custodio et al., 2026".
10. **Package errors (M-A4):** the lead reports them to the user. Neither the package nor the paper is edited.

## Production (start now, unless you object to an item that affects your file)

- **Statistician:**
  - `team/rq2/tables/T9.csv` and `T9_note.txt`, in the format above;
  - `team/rq2/tables/KEY_NUMBERS_RQ2.md`: every number the prose may cite, with its source;
  - a check of T10 cell strings against the package and M's verification once M writes them.
- **Methodologist:**
  - `team/rq2/tables/T10.csv` and `T10_note.txt` (the matrix; column 1 is the model name; the first two rows are SwinFusion++ BO and fixed);
  - `J9.csv` and `J9_note.txt`;
  - `refs_rq2.txt` (the S-MIL APA entry, exactly as it should print; the plain-text style of the existing references, no italics).
- **Lead:** the prose (`rq2_content.py`) once T9 and T10 exist.

All CSVs use the house style: pre-rounded strings, U+2212 for minus, `__SPAN__` rows, and notes under 90 words.
