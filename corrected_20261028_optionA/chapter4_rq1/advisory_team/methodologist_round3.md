# Methodologist (examiner), Round 3 review of REVIEW_DRAFT.md

The new checks are in `team/scripts/m_r3_checks.py`. Quoted "old" text is copied from REVIEW_DRAFT.md.

Overall, the draft is faithful to Option A and the agreed plan, and the numbers I spot-checked are correct:
- T1, T4, T6, T7 PR-AUC, J1, J3, J4 and J8;
- the 10/65 change count, verified from J5.

The items below concern accuracy, plan fidelity and panel risk.

## MUST-FIX

**M1. Holm p printed against the stated rule (Table 9 and Table J5).**
- The Holm p for CDF → DFo in the optimization effect is 0.0048. The text says that values below 0.005 are written as "< 0.005".
- Table 9, row "CDF → DFo": "0.001 | 0.005" → "0.001 | &lt; 0.005".
- Table J5, row "Optimization effect, transfer (m = 9) | … CDF → DFo": "Holm (rank)" "0.005" → "&lt; 0.005".
- Table 8's CDF → C23 vs Video Swin-B value (0.0052) correctly stays "0.005".

**M2. Table 3 cites a section that does not exist.** Chapter 2 has no "Synthesis" heading; the source paragraph (block 238) is under "Review of Related Studies".
- In both T3 rows (component ablations; metadata-shortcut audit), replace "Ch. 2, Synthesis" with "Ch. 2, Review of Related Studies".

**M3. The within-dataset interpretation overreaches (the paragraph after Table 5).** The tests compare SwinFusion++ with each encoder only (Swin-B vs Video Swin-B was never tested), and non-significance does not establish what caused a threshold gain.
- (a) Old: "These intervals rule out a large advantage or disadvantage for any of the three models, but they do not establish equivalence:"
  → New: "These intervals rule out an advantage or disadvantage of SwinFusion++ larger than about 0.01 AUC relative to either encoder, but they do not establish equivalence:"
- (b) Old: "Because the corresponding ROC-AUC differences were not significant, these gains reflect where the frozen thresholds fell rather than a better separation of real and fake videos."
  → New: "Because the corresponding ROC-AUC differences were not detectable, these gains are more consistent with where the frozen thresholds fell than with better separation of real and fake videos."
- (c) Old: "Within each benchmark, therefore, no difference among the three architectures was detectable, and all three operated near the ceiling of the metric."
  → New: "Within each benchmark, therefore, no ROC-AUC difference between SwinFusion++ and either encoder was detectable, and all three models operated near the ceiling of the metric."

**M4. A false general claim about positive calls (the second paragraph after Figure 13).**
- SwinFusion++ made the fewest positive calls only from FF++ C23: 114 / 458 / 8 vs Swin-B 127 / 549 / 13 and Video Swin-B 123 / 533 / 34.
- From Celeb-DF v2 and DeeperForensics-1.0, Swin-B made the fewest: 4, 29, 6 (tied with SwinFusion++), 0, 0 and 0.
- Old: "Its high precision and specificity reflect that it made the fewest positive calls."
  → New: "From FF++ C23, its high precision and specificity reflect that it made the fewest positive calls of the three models (114, 458, and 8 on C40, Celeb-DF v2, and DeeperForensics-1.0); from the other two sources, Swin-B made the fewest."

**M5. The Answer to Research Question 1 needs fidelity fixes.** As drafted:
- it does not address precision, recall or F1 in distribution, although RQ1 names all five metrics;
- it gives no magnitudes, although RQ1 asks "to what extent";
- it omits the agreed widest-lower-bound rule (AGREED_PLAN 11);
- it repeats the non-significance → cause inference;
- "traded" is causal.

Replace the three paragraphs with the following (every number has been checked against T4, T6, T9, J2 and the ensemble CSV):

> In distribution, under the principal fixed-recipe comparison, SwinFusion++ did not measurably improve on standalone Swin-B or Video Swin-B. All three models reached ROC-AUC of 0.988 to 0.997, no paired difference was detectable, and each paired interval lay between −0.011 and +0.009 AUC. The threshold-dependent metrics were similarly close: accuracy differed by at most three videos on FaceForensics++, and precision and recall differed by at most 2.0 and 3.1 percentage points. The supplementary accuracy and F1-score intervals excluded zero only on Celeb-DF v2 (against Swin-B) and DeeperForensics-1.0 (against Video Swin-B), both favoring SwinFusion++; because the ROC-AUC differences there were not detectable, these gains are more consistent with threshold placement than with better ranking.
>
> Under frozen cross-dataset evaluation, SwinFusion++ had significantly higher ROC-AUC than Swin-B in seven of nine directions (by +0.049 to +0.258) and than Video Swin-B in three (by +0.063 to +0.084). It showed no detectable difference in the remaining directions and was significantly lower in none, although the widest interval reached −0.092. The differences came mainly from the Celeb-DF v2 and DeeperForensics-1.0 sources; from FF++ C23, only the difference from Swin-B on DeeperForensics-1.0 was detectable. At the frozen source thresholds, however, SwinFusion++ never had the highest transfer accuracy, recall, or F1-score (point estimates; several margins were one or two videos), and precision was 80% or higher for every model where it was defined, often on very few positive calls. In supplementary paired intervals, its transfer accuracy was lower than an encoder’s in 6 of 18 comparisons (both encoders from FF++ C23 to C40 and to Celeb-DF v2; Video Swin-B from FF++ C23 to DeeperForensics-1.0 and from Celeb-DF v2 to C23) and higher in 2 (Swin-B from Celeb-DF v2 to C23 and to DeeperForensics-1.0).
>
> The improvement that RQ1 asks about is therefore present in ranking performance under frozen transfer, in most directions against Swin-B and in three of nine against Video Swin-B, but not within datasets and not in threshold-dependent performance at the source operating points. The BO-selected configuration raised ROC-AUC within FF++ C40 and Celeb-DF v2 (the latter depending on the family grouping) and from FF++ C23 to C40, but lowered it in five other transfer directions. Whether the transfer differences are due to TLBG-HCA is examined under RQ4, and the verdict against the Chapter 3 criterion for a strong model is given under RQ6.

**M6. The Chapter 3 amendment promises an analysis that appears nowhere.** "Jackknife-to-bootstrap standard-error ratios" is listed, but no Appendix J table reports them. Append this to the Table J7 note (source: `stats_out/statistician_jackknife_vs_bootstrap.csv`, 65 comparisons):

> "Delete-one-cluster jackknife standard errors of ΔAUC were 0.99 to 1.32 times the bootstrap standard errors for Celeb-DF v2 targets (mean 1.15; 15 comparisons) and 0.84 to 1.05 times for the other test sets (mean 1.00; 50 comparisons), so Celeb-DF v2 intervals may be narrower than nominal."

**M7. "FF++" is never defined.** It does not occur in Chapters 1–3, and its first Chapter 4 use is in the Option A paragraph.
- In the first Evaluation Setting paragraph, old: "on each of the four within-dataset conditions, using three recorded seeds"
- → New: "on each of the four within-dataset conditions (FaceForensics++ [FF++] DeepFakes at compression C23 and C40, Celeb-DF v2, and DeeperForensics-1.0), using three recorded seeds"

**M8. Plan fidelity: per-seed metrics.**
- Chapter 3 (Statistical Treatment) promises "per-seed metrics plus mean and standard deviation", but J1 gives per-seed ROC-AUC only.
- Append to the Table J1 note: "Per-seed accuracy, precision, recall, specificity, and F1-score were also computed for every cell but are not tabulated; Chapter 4 reports the three-seed ensembles."

## SUGGEST

- **S1. The lead's question on R14: I ACCEPT leaving the preliminary-study sentences out.** The manuscript never cites that study, and no Chapter 4 claim depends on it. Ask the user whether to add it, with its reference, under RQ6 or in Chapter 5.
- **S2. Decision IDs (A-xx, D-xx) cite a log the panel cannot see.** Extend the T3 note: "…refer to dated entries in the project's decision log, which is kept with the project records and can be made available to the panel."
- **S3. Chapter 3 amendment, McNemar sentence.** 45 of the 54 Celeb-DF clusters are single videos.
  - Old: "because most clusters contained several videos, so one independent decision per cluster could not be assumed"
  - New: "because every test set contained clusters of several related videos, so one independent decision per cluster could not be assumed"
- **S4. "its effective sample size for the fake class is nine"** (the paragraph after Table 1) → "only nine independent clusters carry its fake class". The effective sample size itself was not estimated.
- **S5. Title Case.** APA 7 capitalizes words of four or more letters: "Compared With" (Table 8 and the RQ1 heading), "Deviations From the Approved Plan" (Table 3). Figure 13 already uses "With". The alternative is lowercase everywhere; pick one and apply it throughout.
- **S6. "Figure 13 explains the split…"** → "Figure 13 illustrates the split…".
- **S7.** "could not be checked on a lineage-free subset, because only 20 such test videos exist (Table 1)" → "could not be checked meaningfully on a lineage-free subset, because only 20 such test videos exist (Table 1; per-seed values in Table J3)".
- **S8. After the Table 9 limitations, add:** "The BO-selected configurations also differed from the fixed recipe in several training parameters at once, so the effect cannot be attributed to any single parameter."
- **S9. Bootstrap tie convention (the statistician's call).** The "all 73" agreement holds for the stored bootstrap p-values. Under a mid-p tie convention, one optimization-effect decision (within FF++ C23) would differ (S Round 2). Consider adding "as stored" to that sentence.
- **S10. Table J7 note:** "Across all 15 DeeperForensics-1.0-target comparisons, the 175-cluster re-analysis changed no Holm decision." This supports the Chapter 3 claim beyond the three rows shown.
- **S11. Readability.** The Evaluation Setting carries three tables and seven paragraphs before RQ1 begins. To lighten Table 2, drop the bracketed file labels and decision IDs from its cells; the note already maps the labels.
- **S12.** Table J2 note: "F1: none" → "F1: a model made no positive calls".
- **S13.** Table J8 note: "the registry" → "the study's analysis registry".
- **S14. Philippine format.** Add one interpretive sentence after Table 4, before Table 5 is introduced, e.g. "All three models therefore operated near the ceiling, where differences amounted to a few videos on most test sets."

APPROVE WITH THE MUST-FIXES ABOVE
