# Final check, round 1: statistician

**Verdict.**
- (a) No numeric error found in Chapter 4, Tables 1–11, Tables J1–J9 or Figures 11–13/J1.
- One note inconsistency (J9) and one traceability gap (metadata audit) are listed under (a).
- (b) Fourteen framing edits are listed: one MUST because of a forbidden word, the rest SHOULD. Together they deliver the user's request without dropping any required disclosure.
- (c) Rulings on seven strength statements: four allowed as worded below, two allowed only in a narrower form, one rejected in its proposed form.

---

## A. Re-verification (a)

### Method

All checks were independent of our earlier CSVs where possible.

1. **Paired tests and ensemble intervals recomputed from the raw predictions.** I re-ran the bootstrap and permutation code against `raw_predictions_v020` and compared the results with `paired_tests_optionA.csv` and `three_seed_mean_logit_ensemble.csv`.
   - Result: all 65 RQ1/RQ6 paired tests reproduced exactly (ΔAUC, 95% CI, rank-permutation p, Holm). All 52 ensemble AUC intervals and per-seed AUCs also reproduced exactly (tolerance 1e-12).
   - Output: `work/validation_rerun.csv`.
2. **Every table rebuilt from raw data and package into `work/regen/`, then compared cell by cell with every `<TR>` row of FULL_ACCEPTED_TEXT.txt.**
   - Script: `scripts/statistician_final_compare.py`.
   - Tables 3–8, J1–J8, 10, 11 and J9: 0 mismatches, covering 595 body rows including all headers and span rows.
   - Table 9: the document equals the canonical `rq2/tables/T9.csv`. My regenerated copy differs only because my old script still printed "[—]" after the Xception AUCs, a display change the team made earlier. This is not a document issue.
3. **Prose claims recomputed from raw data.** Every number in blocks 629–720, in the J notes and in block 618 that is not a table cell was recomputed from the raw predictions, the package paired-test file, `bo_summary.csv`, `source_validation_operating_points_v020.csv` and `evaluation_protocol_v020.json`.
   - Scripts: `scripts/statistician_final_claims.py` and `scripts/statistician_final_prose.py`.
   - All verified. Selected values:

| Claim (block) | Recomputed |
|---|---|
| within AUC 0.9878–0.9974 (652, 694 "0.988 to 0.997") | 0.987806–0.997426 |
| 956/933/961 of 978; 397/393/390 of 402; ≤ 3 of 280 on FF++ (652) | exact |
| raw p 0.198–0.925; 6 of 8 negative; envelope −0.0101/+0.0085 (657) | exact |
| precision / recall within-dataset gaps ≤ 2.0 / 3.1 pp (694) | 2.008 / 3.084 |
| transfer AUC 0.459–0.976 (669) | 0.45934–0.97599 |
| +0.049 to +0.258, Holm < 0.005 to 0.018; VSB +0.0630/+0.0754/+0.0840; widest −0.0917; DFo→C23 vs VSB +0.0451 [+0.0077, +0.0816], Holm 0.152 (669) | exact |
| specificity 91.11–100.00; recall < 64% except C23→C40 (79.29–87.14); ≤ 60 positive calls from CDF/DFo; precision ≥ 80% where defined (VSB DFo→C23, 4 of 5 calls) (680, 695) | max other recall 63.70; max 60 calls |
| DFo→CDF accuracy 13.80–15.24 (680) | 13.80 / 14.21 / 15.24 |
| SF++ never highest or tied on accuracy, recall or F1 in 9 directions (681) | confirmed, ties included |
| positive calls 114 / 458 / 8 from C23, the fewest; Swin-B fewest or tied from CDF/DFo (681) | confirmed (CDF→C40 tie 6/6) |
| C23→CDF: 6 FP, spec 95.56, recall 53.62, acc 59.41 vs 67.48 / 66.46 (681) | exact |
| BO within: 0 of 8 significant; BO vs SB 6 of 9 transfer; VSB +0.0116 / −0.1105 / −0.0390 (688) | exact |
| BO−fixed +0.0063 / +0.0031 / +0.0102; five drops 0.041–0.104; Holm 0.021 vs 0.077 (692) | −0.0409 to −0.1039 |
| BO trials 12/12/8/8; best validation AUC 0.9977–0.9994 (692) | 0.99772–0.99938 |
| rank correction removed DFo→DFo vs VSB and added CDF→C23 and DFo→CDF vs SB; 10 of 65 (633, 618) | `rank_correction_impact` |
| jackknife/bootstrap ratio CDF 0.99–1.32, mean 1.15 (n = 15); others 0.84–1.05, mean 1.00 (n = 50) (J7 note) | exact |
| MDD > headroom in 7 of 8 (J6) | exact (exception C23 vs VSB) |
| source-validation coverage 279/280, 977/977, 192/192; lineage 260 and 382; clean 20; 247 / 67 / 15; 157 (637–639) | package files |
| RQ2 ranges and gaps 1.79 / 2.14 / 3.57; BO accuracy 96.07–98.51 (BO CDF accuracy 98.36); Xception 46.00% = 1097/2385 (706–720) | exact |

4. **Figures.** I extracted the four PNGs from `render/thesis_current_accepted.docx` and compared every printed value and marker with the recomputed data.
   - Figure 11: all 39 cells are correct, including the rounding-boundary cases (0.99653 → 0.997, 0.61148 → 0.611, 0.99153 → 0.992, 0.99452 → 0.995).
   - Figure 12: all 26 intervals are correct. Exactly the 10 Holm-significant comparisons are filled, and DFo→C23 vs VSB is open.
   - Figure 13: AUC labels and operating points are correct.
   - Figure J1: AUC labels are correct, and all 12 operating points match Table 3 recall and FPR.

### Findings

- **F1 (SHOULD; group iii, J9 note).** The note says that rows outside Tables 10 and 11 "give the category rule that excludes them: 1(a) … 1(f)". In fact, 29 of the 108 such rows carry other reasons:
  - "Rule 5: precision and recall are not compared across studies": 16 rows;
  - "Source table not adopted for Table 11 (frame/clip-level value from another table)": 13 rows.

  This is not a value-based exclusion, but a reader cannot match these reasons to the note. Add to the note, after "…1(f) another variant or aggregation of a listed model;":

  > «precision and recall values (not compared across studies) and frame- or clip-level values from source tables not used for Table 11 are also listed.»

  None of these 29 rows changes a chapter statement. The largest C40 ROC-AUC among them is 0.9550, and every C23 value lies inside the stated C23 range.
- **F2 (VERIFY; user).** The metadata-audit values in block 639 (0.67, 0.68, 0.50) trace only to the package's `CHAPTER4_NOTES.md` §4. The audit report itself (`reports/audit/metadata_shortcut_audit_v001.md`) is not in the package. No change to the text is needed; the user should copy the file into the package, as that note already asks.

---

## B. Rulings on the proposed strength statements (c)

**S1. "All fixed-recipe AUCs are ≥ 0.9878 within datasets." ALLOWED, but only as a shared-ceiling statement.**
- It is true for all 12 fixed-recipe values.
- The 0.9878 is SwinFusion++'s own C40 value and the lowest of the 12, so the statement must not read as an SF++-specific advantage.
- Use: "All three models reached ROC-AUC between 0.9878 and 0.9974" (current text), or "SwinFusion++ performed at the same near-ceiling level as both encoders".

**S2. Transfer: significantly higher than Swin-B in 7 of 9 directions and than Video Swin-B in 3 of 9, never significantly lower. ALLOWED; this is the chapter's main positive finding and may lead.**
- Required in the same paragraph: the non-inferiority caveat (widest −0.092).
- New and verified: in those three VSB directions (CDF→C40, CDF→DFo, DFo→C40), fixed SF++ was significantly above **both** encoders.
- This test-backed statement is stronger than S3 and should be preferred.

**S3. "Highest point AUC among the three matched models in 5 of 9 transfer directions." ALLOWED ONLY IN THIS NARROWER FORM. Not in the RQ1 answer, the abstract or Chapter 5.**
- Verified directions:

| Direction | ΔAUC | Holm p | Significant vs both encoders? |
|---|---|---|---|
| C23→C40 | +0.0014 over VSB | n.s. | no |
| CDF→C40 | — | — | yes |
| CDF→DFo | — | — | yes |
| DFo→C23 | +0.0451 over VSB | 0.152 | no |
| DFo→C40 | — | — | yes |

- For balance: VSB had the highest point estimate in 3 directions and Swin-B in 1 (C23→CDF, by 0.0004).
- Why the narrower form: it is a count of point estimates within our own paired models, not a vote count against published models. However, a bare "5 of 9" tally is a collapsed score of the kind the registry rules out (J8 note), and two of the five leads are not significant.
- The allowed form names the directions and splits them by significance (see edit E3-B). Never write "best in 5 of 9" or "won".
- The chapter's existing point-estimate count for threshold metrics (block 681) is the precedent that makes the direction-named version consistent.

**S4. C23→DFo, "temporal models held while Swin-B collapsed". ALLOWED IN NEUTRAL WORDING; reject "held" and "collapsed".**
- Both temporal models dropped from about 0.99 to 0.83–0.84.
- Swin-B's interval [0.5250, 0.6105] excludes 0.5, so "collapsed" overstates.
- Allowed: "Swin-B's ROC-AUC fell to 0.5678 while the two models with a temporal stream kept 0.8261 and 0.8421".
- True and new: this +0.258 is the largest of all 18 architecture differences.
- Must name the fixed recipe. The BO-selected SF++ had 0.7316 here and was significantly **worse** than VSB (−0.1105), so per rule A7 this strength does not hold for BO.
- The attribution caveat (pretraining and input differ) stays.

**S5. BO-selected: the highest point AUC within C40 (0.9941) and Celeb-DF (0.9983). ALLOWED, descriptive.**
- Verified against every ensemble in the package on those test sets, including the RQ4 controls (the Tier B ablations were tested on C23 only).
- Required: "none of its differences from the encoders was significant". Do not say "among all our models" without "on those test sets".

**S6. RQ2 statements.**
- (i) **Far above the preliminary Xception on FF++ and CDF: ALLOWED** with the current caveats (different pipeline; different CDF population).
- (ii) **C40 AUC above every reported value: ALLOWED, and verifiable more broadly.**
  - Both regimens, BO 0.9941 and fixed 0.9878, exceed every C40 ROC-AUC in Tables 10–11 **and in all 27 C40 ROC-AUC values in J9** (maximum 0.983, FTCN; the only Tier A value is STIL's 0.9712).
  - Keep "almost all Tier B, not like-for-like".
- (iii) **DFo within 98.50–100.00: ALLOWED** (already stated).
- (iv) **"FF++ accuracy within about 2 points of the best reported (BO)": ALLOWED ONLY WITH EXACT VALUES.**
  - "About 2" understates C40 (2.14).
  - Write "within the reported Tier A ranges, 1.79 and 2.14 points below the highest values (fixed recipe 2.14 and 3.57)".
  - New and verified: both regimens lie inside both Tier A accuracy ranges (C23 92.14–100.00; C40 89.29–98.21).
- (v) **"Thresholds frozen on source validation, unlike most published operating points, which are not stated": REJECTED as worded.**
  - "Most … not stated" is a count over the cited papers that nobody has checked.
  - Allowed neutral form: "Its accuracies were obtained at thresholds fixed on source-validation data before testing, whereas each published accuracy uses its own paper's operating point."

**S7. Considered and rejected by me.**
- Citing the unadjusted intervals that exclude zero in BO's favor within datasets (CDF vs both encoders; C40). Those decisions were Holm-non-significant, and for balance we would also have to cite four unfavorable ones. Table 7 already shows them.
- The mean transfer AUC (0.8099) stays in Appendix J only, as the registry rule requires.

---

## C. Positive-framing edit list (b)

All edits are in group **(ii), Chapter 4 prose via the content files**, unless marked otherwise.
- "OLD" is the accepted-view text, quoted from FULL_ACCEPTED_TEXT.txt.
- The content files use "<" where the accepted view shows "&lt;".
- Every number in the NEW text is from section A.

**Required disclosures kept verbatim or in substance in every edit:**
- Option A framing;
- the rank-correction sentence (block 633, untouched);
- the Celeb-DF caveat;
- the non-inferiority caveat;
- the threshold-transfer result;
- the BO caveats (blocks 692 and 696, untouched apart from E10);
- the RQ4/RQ6 deferrals.

### E1 (SHOULD). Block 652 (`ch4_content.py:171`). Replace the whole paragraph.

OLD: «All three models reached ROC-AUC between 0.9878 and 0.9974 on every test set. SwinFusion++ had the highest point estimate on DeeperForensics-1.0 (0.9974) and the lowest on FF++ C23 (0.9942) and C40 (0.9878), and on Celeb-DF v2 it was 0.0007 below both encoders. Accuracy on the FaceForensics++ test sets differed by at most three of 280 videos: SwinFusion++ matched Swin-B on C23 (97.86%) and C40 (94.64%), and Video Swin-B classified three more videos correctly on each. The differences were larger on the other two test sets. On Celeb-DF v2, SwinFusion++ classified 956 of 978 videos correctly, compared with 933 for Swin-B and 961 for Video Swin-B; on DeeperForensics-1.0, it classified 397 of 402 correctly, compared with 393 and 390. All three models therefore operated near the ceiling of the metric on every test set.»

NEW: «All three models reached ROC-AUC between 0.9878 and 0.9974 on every test set. SwinFusion++ had the highest point estimate of the three on DeeperForensics-1.0 (0.9974) and was within 0.0037 of the highest on the other three test sets (FF++ C23 0.9942, C40 0.9878, Celeb-DF v2 0.9951). In accuracy, it classified the most videos correctly of the three on DeeperForensics-1.0 (397 of 402, compared with 393 for Swin-B and 390 for Video Swin-B) and the second most on Celeb-DF v2 (956 of 978, compared with 933 and 961). On the FaceForensics++ test sets, the three models differed by at most three of 280 videos: SwinFusion++ matched Swin-B on C23 (97.86%) and C40 (94.64%), and Video Swin-B classified three more videos correctly on each. All three models therefore operated near the ceiling of the metric on every test set.»

Evidence:
- Largest gap to the top value: C40 0.991531 − 0.987806 = 0.0037; C23 0.0023; CDF 0.0007.
- Counts as in A.
- "Lower point estimate in six of eight" is kept in E2, so the ranking disclosure is stated once.

### E2 (SHOULD). Block 657 (`ch4_content.py:180`). Replace the whole paragraph.

NEW: «No ROC-AUC difference between SwinFusion++ and either encoder was detectable (all Holm-adjusted p = 1.000; raw p from 0.198 to 0.925), and every paired 95% interval lay between −0.011 and +0.009 AUC, which rules out a large difference in either direction. SwinFusion++ had the lower point estimate in six of the eight comparisons. The ceiling left little room to detect a gain: in seven of the eight comparisons, even the largest gain still possible was smaller than the difference the test could detect with 80% power (Appendix J, Table J6), so these results do not establish equivalence. In the supplementary paired intervals for threshold-dependent metrics (Table J2), SwinFusion++ had higher accuracy than Swin-B on Celeb-DF v2 (+2.35 percentage points [+0.08, +5.10]; approximate, nine fake-class clusters) and than Video Swin-B on DeeperForensics-1.0 (+1.74 percentage points [+0.50, +3.23]), and no accuracy interval excluded zero in an encoder’s favor. Because the corresponding ROC-AUC differences were not detectable, these gains reflect where the frozen thresholds fell rather than better separation of real and fake videos. Within each benchmark, the three models were therefore statistically indistinguishable in ROC-AUC, and all operated near the ceiling of the metric.»

Evidence:
- J6: MDD at α = 0.05/8 exceeds headroom in 7 of 8.
- J2 within-dataset accuracy rows: no interval lies wholly below 0. The C23 vs VSB upper bound is exactly 0.00, because accuracy differences on 280 videos are multiples of 1/280.

### E3 (SHOULD). Block 669 (`ch4_content.py:196`). Replace the whole paragraph.

The first sentence moves into E5, so the negative appears once and after the finding.

**NEW (A):** «Under frozen transfer, SwinFusion++ had a significantly higher ROC-AUC than Swin-B in seven of the nine directions, by +0.049 to +0.258 (Holm-adjusted p from &lt; 0.005 to 0.018), and than Video Swin-B in three, Celeb-DF v2 → FF++ C40 (+0.0754), Celeb-DF v2 → DeeperForensics-1.0 (+0.0630), and DeeperForensics-1.0 → FF++ C40 (+0.0840), all with Holm-adjusted p &lt; 0.005. In these three directions, it was significantly better than both encoders and had the highest ROC-AUC of the three models. SwinFusion++ was significantly lower than an encoder in none of the 18 comparisons. This is not evidence of non-inferiority: the five negative point estimates were not significant, but the widest interval reached −0.092 (DeeperForensics-1.0 → Celeb-DF v2, against Video Swin-B). One comparison, DeeperForensics-1.0 → FF++ C23 against Video Swin-B, had an interval that excluded zero (+0.0451 [+0.0077, +0.0816]) but was not significant after Holm adjustment (p = 0.152), so Figure 12 shows it with an open marker.»

**E3-B (optional, only if the team accepts the S3 ruling).** Replace the last sentence of NEW (A) with:

«SwinFusion++ also had the highest point estimate in FF++ C23 → C40 and DeeperForensics-1.0 → FF++ C23 (Figure 11), but its lead over Video Swin-B there was not significant (+0.0014; and +0.0451 [+0.0077, +0.0816], Holm-adjusted p = 0.152, shown with an open marker in Figure 12).»

### E4 (SHOULD). Block 670 (`ch4_content.py:207`). Replace the first four sentences; the rest of the paragraph is unchanged.

OLD: «The advantage depended on the training source. Trained on Celeb-DF v2 or DeeperForensics-1.0, SwinFusion++ was significantly better than Swin-B in all six directions and better than Video Swin-B in three. Trained on FF++ C23, it showed no detectable difference from either encoder on FF++ C40 or Celeb-DF v2, and its only significant difference from that source was against Swin-B on DeeperForensics-1.0. In that direction, Swin-B’s ROC-AUC fell to 0.5678 [0.5250, 0.6105], while the two models with a temporal stream kept 0.8261 (SwinFusion++) and 0.8421 (Video Swin-B).»

NEW: «The advantage was clearest when the models were trained on Celeb-DF v2 or DeeperForensics-1.0: from these sources, SwinFusion++ was significantly better than Swin-B in all six directions and than Video Swin-B in three. From FF++ C23, the three models were statistically indistinguishable on FF++ C40 and Celeb-DF v2, and the one significant difference was the largest of all 18: on DeeperForensics-1.0, Swin-B’s ROC-AUC fell to 0.5678 [0.5250, 0.6105], while the two models with a temporal stream kept 0.8261 (SwinFusion++, +0.258 over Swin-B) and 0.8421 (Video Swin-B).»

Evidence:
- +0.2584 is the maximum ΔAUC in RQ6_architecture.
- C23→C40 and C23→CDF have no significant comparison.
- The fixed recipe is implied by the subsection heading; BO is not claimed (see S4).

### E5 (SHOULD). Block 671 (`ch4_content.py:218`). Replace the whole paragraph.

NEW: «The significant differences were stable across seeds and analysis choices. Nine of the ten had the same sign in all nine pairings of individual seeds, and the tenth (Celeb-DF v2 → FF++ C40 against Video Swin-B) in eight of nine; all ten remained significant under the family grouping recorded before scoring and under one pooled family, and no DeeperForensics-1.0-target decision changed with 175 lineage clusters (Appendix J, Table J7). Two limits apply. Transfer lowered ROC-AUC for every model, to between 0.459 and 0.976, and from DeeperForensics-1.0 to Celeb-DF v2 all three models were near chance (0.4593 to 0.6001). The three significant differences from DeeperForensics-1.0 to FF++ C23 and C40 could not be checked meaningfully on a lineage-free subset, because only 20 such test videos exist (Table 1; per-seed values in Table J3). Under matched training, SwinFusion++ therefore ranked target videos significantly better than Swin-B in seven of the nine transfer directions and than Video Swin-B in three. Whether these differences can be attributed to TLBG-HCA, rather than to the combination of two encoders, is examined under RQ4 with the topology and capacity-matched controls.»

Evidence:
- J7: largest pre-scoring Holm p 0.024; largest pooled 0.034.
- J7 note: the 175-cluster re-analysis changed no decision across the 15 DFo-target comparisons.
- The old "less degraded … in a minority of directions" is replaced by the exact tested statement.

### E6 (no edit). Blocks 680–682.

These carry the threshold-transfer disclosure. Keep them as they are; block 681 remains the single place that lists the 6 + 2 comparisons. E9 removes the duplicate listing from the answer.

### E7 (SHOULD). Block 688 (`ch4_content.py:260`). Replace the whole paragraph.

NEW: «Within datasets, the BO-selected configuration had the highest point estimates of any model evaluated on FF++ C40 (0.9941) and Celeb-DF v2 (0.9983), but none of its eight differences from the encoders was significant, so these leads are descriptive. Under transfer, it was significantly better than Swin-B in six of the nine directions and, from FF++ C23 to C40, significantly better than both encoders (+0.0123 and +0.0116). It was significantly worse than Video Swin-B from FF++ C23 to DeeperForensics-1.0 (−0.1105) and from Celeb-DF v2 to FF++ C23 (−0.0390).»

Evidence:
- Package ensembles on those test sets, all families including controls: BO is the top value.
- RQ6_configured_system: C23→C40 +0.0123 (Holm 0.0096) and +0.0116 (Holm 0.0154).

### E8 (SHOULD). Block 694 (`ch4_content.py:275`). Replace the whole paragraph.

NEW: «In distribution, under the principal fixed-recipe comparison, SwinFusion++ performed at the same near-ceiling level as standalone Swin-B and Video Swin-B. All three models reached ROC-AUC of 0.988 to 0.997, no paired ROC-AUC difference was detectable, and each paired interval lay between −0.011 and +0.009 AUC; at this ceiling, little room remained for a detectable improvement. The threshold-dependent metrics were similarly close: accuracy differed by at most three videos on FaceForensics++, and precision and recall differed from those of either encoder by at most 2.0 and 3.1 percentage points. The only supplementary accuracy and F1-score intervals that excluded zero favored SwinFusion++ (Celeb-DF v2 against Swin-B; DeeperForensics-1.0 against Video Swin-B); because the ROC-AUC differences there were not detectable, these gains are best read as threshold placement rather than better ranking.»

Note: "no paired ROC-AUC difference was detectable" still answers the "improve" question directly, so the RQ is answered and not dodged.

### E9 (SHOULD). Block 695 (`ch4_content.py:283`). Replace the whole paragraph.

NEW: «Under frozen cross-dataset evaluation, SwinFusion++ had significantly higher ROC-AUC than Swin-B in seven of the nine directions (by +0.049 to +0.258) and than Video Swin-B in three (by +0.063 to +0.084), and in those three it was significantly better than both encoders. It was not significantly lower than either encoder in any direction, although the widest interval reached −0.092, and nine of the ten significant differences had the same sign in every pairing of individual seeds. The advantage came mainly from the Celeb-DF v2 and DeeperForensics-1.0 sources; from FF++ C23, the one detectable difference was also the largest, +0.258 against Swin-B on DeeperForensics-1.0. At the frozen source thresholds, however, SwinFusion++ did not have the highest transfer accuracy, recall, or F1-score in any direction (point estimates; several margins were one or two videos), and in the supplementary paired intervals its transfer accuracy was lower than an encoder’s in 6 of 18 comparisons and higher in 2 (Table J2).»

Removed:
- the duplicated list of the 6 + 2 directions (kept in block 681);
- the all-model precision clause ("80% or higher … very few positive calls"), which is not a required disclosure. Restore it if the methodologist wants it.

### E10 (SHOULD). Block 696 (`ch4_content.py:295`). Replace the first two sentences; the BO and RQ4/RQ6 sentences are unchanged.

OLD: «The improvement that RQ1 asks about is therefore present in ranking performance under frozen transfer, in most directions against Swin-B and in three of nine against Video Swin-B. It was not detectable within datasets, and under transfer it did not carry over to threshold-dependent performance at the frozen source operating points.»

NEW: «The improvement that RQ1 asks about is therefore present in ranking performance under frozen transfer, in seven of nine directions against Swin-B and in three of nine against Video Swin-B. Within datasets, where all three models were near the ceiling, no improvement was detectable, and under transfer the ranking advantage did not carry over to threshold-dependent performance at the frozen source operating points.»

### E11 (SHOULD). Block 716 (`rq2_content.py:58`).

OLD: «while SwinFusion++ reached 0.9964 and 0.9941 (fixed recipe 0.9942 and 0.9878) on the DeepFakes subset alone; because the Tier B values pool manipulations or leave the subset unstated, they are not like-for-like.»

NEW: «while SwinFusion++ reached 0.9964 and 0.9941 (fixed recipe 0.9942 and 0.9878) on the DeepFakes subset alone. On C40, both SwinFusion++ values were higher than every C40 ROC-AUC in Tables 10, 11, and J9, and on C23 they lay within the reported range; because the Tier B values pool manipulations or leave the subset unstated, they are not like-for-like.»

Evidence:
- J9 contains 27 C40 ROC-AUC values, maximum 0.9830 (plus three frame-level values, maximum 0.8659).
- C23 range 0.5749–0.9987 contains 0.9964 and 0.9942.

### E12 (SHOULD). Block 717 (`rq2_content.py:64`).

OLD: «The BO-selected SwinFusion++ reached 98.21% and 96.07%, 1.79 and 2.14 percentage points below the highest values; the fixed recipe was 2.14 and 3.57 points below.»

NEW: «The BO-selected SwinFusion++ reached 98.21% and 96.07%, within both ranges and 1.79 and 2.14 percentage points below the highest values; the fixed recipe (97.86% and 94.64%) was also within both ranges, 2.14 and 3.57 points below.»

### E13 (MUST: forbidden word). Block 718 (`rq2_content.py:73`).

OLD: «the data support neither a claim that SwinFusion++ outperforms these established models nor the reverse.»

NEW: «the data cannot rank SwinFusion++ above or below these established models.»

Context: this is the only "outperform" in Chapter 4 or Appendix J. The scan also covered "robust", "state of the art", "equivalen", "generaliz", "superior" and "competitive". The only other hit is the required negated "do not establish equivalence", which stays.

### E14 (SHOULD). Block 720 (`rq2_content.py:78`). Replace the whole paragraph.

NEW: «On the FaceForensics++ DeepFakes C23 and C40 subsets, Celeb-DF v2, and the DeeperForensics-1.0 construction, the BO-selected SwinFusion++ reached ROC-AUC of 0.9941 to 0.9983 and accuracy of 96.07% to 98.51% (fixed recipe 0.9878 to 0.9974 and 94.64% to 98.76%). It ranked videos far better than the Xception baseline of the preliminary study on FaceForensics++ and Celeb-DF v2 (Xception ROC-AUC 0.6480 to 0.8109) and similarly on DeeperForensics-1.0, a comparison limited by the different pipeline and, for the last two datasets, by different test populations. Against previously reported results for a wider set of established detectors, its C40 ROC-AUC (0.9941; fixed recipe 0.9878) was higher than every reported value considered (highest 0.983), and its C23 ROC-AUC lay within the reported range, although almost all of these values are Tier B and not like-for-like. Its accuracy on the balanced FaceForensics++ test sets lay within the reported Tier A ranges, 1.79 and 2.14 percentage points below the highest values (fixed recipe 2.14 and 3.57), and on the DeeperForensics-1.0 standard set it lay within the reported range, near the ceiling. [Optional, S6(v): Its accuracies were obtained at thresholds fixed on source-validation data before testing, whereas each published accuracy uses its own paper's operating point.] Because those results come from other splits and protocols, they place SwinFusion++ among the listed methods on FaceForensics++ but cannot rank it against them.»

Evidence:
- Every comparative clause holds for both regimens (rule A7).
- Xception values are from T9.
- J9 maximum for C40 is 0.983.

### Group (iii), table notes

- **F1:** the J9 note addition, given in section A.

### Groups (i), (iv) and (v)

- No items from the statistician.
- The figures need no redraw: all four images match the data, and E1–E14 change no figure reference.

---

## D. For the lead after applying the edits

1. Re-run `scripts/statistician_final_compare.py` on the rebuilt accepted text. Tables are untouched, so the expected result is 0 mismatches, plus the known Table 9 artifact.
2. Run `scripts/statistician_final_prose.py`. The new numbers in E1–E14 that are not table cells are:
   - 0.0037 (C40 gap) and +0.0014 (C23→C40 vs VSB): from `statistician_final_claims.py`;
   - +0.0123 / +0.0116: from `paired_tests_optionA.csv`;
   - 0.983 and the J9 count: from J9.

   Every other number already appears in the document.
3. Fix 1 and RQ6 text are untouched, as is the block 633 rank-correction sentence.
