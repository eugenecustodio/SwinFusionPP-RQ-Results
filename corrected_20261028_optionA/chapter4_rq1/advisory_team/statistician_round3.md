# Statistician, Round 3: review of REVIEW_DRAFT.md

## How I checked

**Tables.** I parsed every table in the draft and compared it cell by cell with the verified CSVs in `team/tables/`. All 14 tables match: T4–T9 and J1–J8 have 0 differences.

**Prose numbers.** I checked every number in the prose against the CSVs, the package, `bo_summary.csv` and the operating-points file. Examples:
- 956/933/961 and 397/393/390 correct classifications;
- 0.9977–0.9994 best validation AUC;
- 279/280 source-validation coverage;
- −0.092;
- 7 of 8;
- 6 of 18 and 2.

**Figures.** I checked all four against the values:
- Fig 11: the cell values round correctly, including VSB DFo 0.994517 → 0.995.
- Fig 12: 10 filled markers, with the DFo → C23 vs VSB marker open.
- Figs 13 and J1: the operating points sit at the T4/T7 recall and 1 − specificity.

All numbers are correct. The must-fixes concern wording that claims more than the tests show, one rule violation in printing p-values, and two notes.

## MUST-FIX

**1. Line 92, "for any of the three models".**
- **Problem:** Swin-B and Video Swin-B were never compared with each other.
- **Replace** "These intervals rule out a large advantage or disadvantage for any of the three models, but they do not establish equivalence:"
- **With** "These intervals are incompatible with a large difference between SwinFusion++ and either encoder, but they do not establish equivalence:"

**2. Line 92: treating absence of evidence as evidence of absence.**
- **Replace** "Because the corresponding ROC-AUC differences were not significant, these gains reflect where the frozen thresholds fell rather than a better separation of real and fake videos."
- **With** "Because the corresponding ROC-AUC differences were not detectable, these gains are best read as differences in where the frozen thresholds fell, not as evidence of better separation of real and fake videos."

**3. Line 92, last sentence.**
- **Problem:** "among the three architectures" again implies that the two encoders were compared.
- **Replace** "Within each benchmark, therefore, no difference among the three architectures was detectable, and all three operated near the ceiling of the metric."
- **With** "Within each benchmark, therefore, no difference between SwinFusion++ and either encoder was detectable, and all three models operated near the ceiling of the metric."

**4. Line 172, "it made the fewest positive calls".**
- **Problem:** this is true only from FF++ C23. From Celeb-DF v2 → C23 and → DFo, and from all three DFo-source directions, Swin-B made fewer positive calls (Table 7 TP + FP, e.g. 29 vs 40 on CDF → C23, and 0 vs 2 on DFo → C23).
- **Replace** "Its high precision and specificity reflect that it made the fewest positive calls."
- **With** "From FF++ C23, its high precision and specificity reflect that it made the fewest positive calls of the three models."

**5. Line 173, "low-recall part of the curve".**
- **Problem:** this is false for FF++ C23 → C40, where recall was 79.29–87.14% and AUC was about 0.975.
- **Replace** "Where ROC-AUC stayed near or above 0.8, the curves show that the ranking of fake above real videos was largely retained, but the frozen operating point sat in the low-recall part of the curve."
- **With** "Outside FF++ C23 → C40, where ROC-AUC stayed near or above 0.8, the curves show that the ranking of fake above real videos was largely retained, but the frozen operating point sat in the low-recall part of the curve."

**6. Line 226: the same inference problem as item 2.**
- **Replace** "reflect threshold placement rather than ranking."
- **With** "are best read as threshold placement, since the corresponding ranking differences were not detectable."

**7. Line 228: "not within datasets" breaks the no-detectable-difference rule.**
- **Problem:** the transfer half of the sentence also ignores the 2 higher-accuracy results.
- **Replace** "The improvement that RQ1 asks about is therefore present in ranking performance under transfer, mainly against Swin-B, but not within datasets and not in threshold-dependent performance at the source operating points."
- **With** "The improvement that RQ1 asks about is therefore present in ranking performance under transfer, mainly against Swin-B; it was not detectable within datasets, and under transfer it did not carry over to threshold-dependent performance at the frozen source operating points."

**8. Line 228, "traded transfer for in-distribution fit".**
- **Problem:** this is inaccurate, because BO also *gained* transfer on C23 → C40 and had no detectable in-distribution gain on C23 or DFo. M-D6 also requires "consistent with".
- **Replace** "The BO-selected configuration traded transfer for in-distribution fit."
- **With** "Relative to the fixed recipe, the BO-selected configuration gained ROC-AUC within FF++ C40 and Celeb-DF v2 and from FF++ C23 to C40 but lost it in five other transfer directions, consistent with tighter fitting to each training source."

**9. One Holm value breaks the lead's own "< 0.005" rule.**
- **Problem:** the optimization effect CDF → DFo has p_Holm = 0.004799, printed as "0.005".
- **Fix:**
  - Table 9, row CDF → DFo: Holm p "0.005" → "< 0.005".
  - Table J5, row "Optimization effect, transfer (m = 9) | SwinFusion++ (BO) vs SwinFusion++, CDF → DFo": Holm (rank) "0.005" → "< 0.005".
- **Leave unchanged:** the configured-system CDF → C23 vs VSB value (0.0052) correctly stays "0.005" in T8 and J5. I scanned every Holm value in all families and partitions; this is the only one between 0.0045 and 0.005.

**10. The Table J7 note was not updated to the new rule.**
- **Problem:** its "< 0.005" cells now include a non-floor value (CDF → DFo vs VSB, 0.0040).
- **Replace** '"< 0.005" marks the family floor; floors at m = 26/27 round to 0.005.'
- **With** '"< 0.005" = Holm-adjusted p below 0.005; with m = 26 and 27 the smallest attainable values (0.0052 and 0.0054) are printed as 0.005.'

**11. The Table 2 note defines "pooled grouping" only for the architecture rows.**
- **Problem:** the optimization-effect transfer row also claims "same decisions under the pre-scoring and pooled groupings". There, the pooled grouping is a different one: each optimization-effect family pooled with the matching configured-system family, which is the package's sensitivity column.
- **Replace** "The pooled grouping combines all 26 architecture comparisons in one family."
- **With** "The pooled grouping combines all 26 architecture comparisons in one family; for the configured-system and optimization-effect rows, it pools each optimization-effect family with the matching configured-system family (12 within, 27 transfer)."

## SUGGEST

**S1. Dates.** Use the American date format consistently, as in D-2:
- the T2 note: "2 October 2026" → "October 2, 2026";
- the T3 note: "30 September 2026" → "September 30, 2026".

**S2. Section name.** Lines 12 and 52 and the Appendix J intro cite "Amendments after Test Scoring", but the run-in heading reads "Amendments after test scoring." Pick one capitalization.

**S3. Line 22.** "its effective sample size for the fake class is nine" → "its fake class rests on nine independent clusters". "Effective sample size" is a technical term with a specific formula.

**S4. Line 124.** "shares no source lineage with the training data" → "shares no source lineage with the FF++ C23 training or validation data", to match the J3 definition.

**S5. Table J5 note.** Add: "Raw p below 0.001 is written < 0.001 and Holm p below 0.005 as < 0.005."

**S6. Table J6 note.** After "(z + 0.84) × SE", add "with z = 1.96 (α = 0.05) or 2.73 (α = 0.05/8)".

**S7. Table 1 note.** Name each source-validation count: "Source-validation coverage: 279/280 (FF++ C23 and C40), 977/977 (Celeb-DF v2), 192/192 (DeeperForensics-1.0)." I verified these in the operating-points file.

**S8. D-2, last sentence.** The sentence is accurate as written (350 of 395 clusters hold several videos). If the lead wants it exact: "because the clusters held up to 207 videos (four in FaceForensics++, two in DeeperForensics-1.0), so one independent decision per cluster could not be assumed."

## Checked and correct

- **D-2 as inserted:** it matches `D2_final.txt` word for word (297 words), and every count states its basis.
- **The Option A sentence:** verbatim.
- **The rank-correction sentence:** correct.
- **Appendix J tables J1–J8:** they render sensibly. The span rows, the "n.e."/"—"/"†" conventions and the signed CIs are all correct.
- **Wording discipline:** no "equivalent", "robust", "generalizes" or "tied" appears in RQ1. "Never significantly worse" carries −0.092.

**APPROVE WITH THE MUST-FIXES ABOVE**
