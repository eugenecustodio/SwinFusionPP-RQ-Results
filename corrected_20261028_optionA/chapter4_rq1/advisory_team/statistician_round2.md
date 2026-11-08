# Statistician, Round 2: replies to R1–R15

The new checks behind this memo are in `scripts/statistician_r2_checks.py`. Their output is in `stats_out/statistician_r2_bootstrap_p_check.csv`.

## Replies to the proposed resolutions

**R1 Scope.** AGREE.

**R2 Family names.** AGREE.

**R3 Titles.** AGREE. This is outside my remit.

**R4 Numbering.** AGREE (the appendix-letter numbering in APA 7). It has no statistical consequence.

**R5 Mean transfer AUC.** AGREE, amended. Appendix H shows the four means *without* an interval. My joint-bootstrap CI stays in `stats_out` for defense questions only.
- *Reason:* the registry (`rq_traceability.yaml`, RQ6 limitations) says "no collapsed generalization score". An interval would make the mean look like a pre-declared endpoint. This reverses my S B-3.5.

**R6 Threshold metrics.** AGREE with T7 and Appendix H2. Two amendments to the text:
- **(a) Report the zero-excluding Δ intervals in both directions, not only the unfavorable ones.**
  - *Transfer accuracy:* the intervals excluded zero in 8 of 18 comparisons. In 6, SwinFusion++ was lower: C23→C40 (both encoders), C23→CDF (both), C23→DFo vs Video Swin-B, and CDF→C23 vs Video Swin-B. In 2, it was higher: CDF→C23 and CDF→DFo, both vs Swin-B.
  - *Within datasets:* 2 of 8 excluded zero, both higher for SwinFusion++: Celeb-DF vs Swin-B and DFo vs Video Swin-B.
  - Citing only one side would be selective reporting.
- **(b) Qualify the merged RQ1 sentence.** Proposed wording: "SwinFusion++ never had the highest transfer accuracy, recall, or F1 (point estimates; several margins were one or two videos); the supplementary paired intervals showed lower accuracy than both encoders from FF++ C23 to C40 and Celeb-DF v2, and than Video Swin-B from FF++ C23 to DeeperForensics-1.0 and from Celeb-DF v2 to C23."

**R7 Inference.** AGREE.
- Write floor values as "< 0.005". This covers the floors 0.002 (m = 8 or 9) and 0.004 (m = 18).
- For the defense: at the Monte Carlo 95% upper bound with zero exceedances (about 3/5000 raw), the floor values stay at or below 0.011, so all remain significant.

**R8 Disclosures.**
- **(a)** AGREE. Add one sentence to the end of D-2's first point: "Holm decisions computed from the paired-bootstrap p-values, the other procedure allowed in this section, agreed with the rank-based test in all 73 comparisons (Appendix H)."
- **(b)** AGREE.
- **(c)** AGREE. The statistical amendments belong in D-2, not in Table 3.

**R9 Celeb-DF.** AGREE.
- The table-note text: "intervals are approximate: all fake videos lie in 9 identity clusters".
- In H5, the jackknife/bootstrap SE ratio (0.99–1.32 on Celeb-DF, mean 1.15) is reported to support that note.

**R10 Lineage.** AGREE. State that the strict-subset values are per-seed only, with no ensemble and no interval.

**R11 Figures.** AGREE, with one note on Fig 12. The caption note must say: "intervals are unadjusted; filled markers denote p_Holm < 0.05". Otherwise the open marker for DFo→C23 vs Video Swin-B, whose interval excludes 0, looks like an error.

**R12 Tables.** AGREE, with two amendments:
1. **T6 and T8 also carry the raw p.** This keeps them consistent with T5 and R7.
2. **H5 must also contain the analyses that D-2 promises:**
   - minimum detectable difference vs headroom (C-3);
   - cross-seed sign agreement (C-7);
   - the rank-correction impact (the 3 architecture decisions that changed);
   - the bootstrap-p Holm check (73/73).

   Otherwise D-2 promises analyses that appear nowhere.

**R13 Claims.** DISAGREE on one number.
- **The problem:** "disadvantages larger than 0.010" is false. The C40 vs Video Swin-B interval reaches −0.01005, so it contains disadvantages slightly larger than 0.010.
- **Counter-proposal:** "each paired 95% interval lay between −0.011 and +0.009 AUC". The envelope is exactly [−0.0101, +0.0085].
- **The rest of R13:** AGREE, including the −0.092 rule and the headroom clause.

**R14 Preliminary study.** AGREE.

**R15 Recipe config not in the package.** AGREE. Do not print any value that has not been verified.

**Production split.** AGREE, with one addition. The methodologist's Figures 12 and 13 should read *my* verified table CSVs (T5, T6, T8, and an ROC/operating-point CSV I will add) rather than re-extracting the numbers. Then each number has only one source.

## Replies to the methodologist's memo

**M-E2 / M-G2: the bootstrap-p Holm claim (73/73).**
- **Verified.** The stored bootstrap p-values, with Holm applied in the Option A families, give the same decisions as the rank test in 73 of 73 comparisons.
- **Both positions can stand.** What I ruled out was *printing bootstrap p-values* as results; that would be a second set of p-values to choose from. A one-sentence statement that the *decisions* agree is a robustness check, and it supports the rank correction.
- **The bootstrap p-values themselves stay out of every table**, for three reasons:
  1. 21 of the 73 equal exactly 0.
  2. Near the ceiling, up to 12% of bootstrap draws give ΔAUC = 0 exactly, so the values depend on how those ties are counted. I reproduce the stored values to within 0.021, not exactly.
  3. Under a mid-p tie rule, one decision would differ: BO vs fixed within C23 (Holm 0.047 vs 0.148).
- **Disclosure:** the R8(a) sentence above, plus the tie-rule caveat in the H5 note.
- **Why intervals and tests disagree at the ceiling (M-G2):** the 4 discordant cases have CI lower bounds within 0.002 of zero, and 3 of them are on Celeb-DF, where the bootstrap SE is too small by up to 32%.

**M-G4 / M-B1(a), "CIs exclude gains above 0.009": AGREE**, as a compatibility statement that needs no TOST, because no margin is claimed. Conditions:
- say "each paired interval" (the intervals are unadjusted);
- always pair it with the lower bound (−0.011, per R13);
- keep the headroom clause, because on C23 vs Swin-B, for example, a gain above 0.0035 is impossible anyway;
- never paraphrase it as "equivalent within 0.009".

**M-G5.**
- **Floors:** "< 0.005", per R7.
- **Boundary:** yes, one sentence in the T4 and H6 notes: "Intervals that reach 1.0000 reflect bootstrap draws with perfect separation; near the ceiling, percentile intervals are approximate." Do not switch to BCa now, because that would be another post hoc change.

**M's D table.**
- **D1:** add "each paired interval" and the −0.011 lower bound.
- **D3:**
  - In RQ1, use "no detectable difference in 6", not "statistically tied". The Fix 1 wording stays as the user fixed it, in RQ6.
  - The widest lower bound is **−0.092** (DFo→CDF), not −0.041.
- **D4:** "persisted on the lineage-free subset" needs "(seed means, n = 60, no interval)".
- **D5:** needs the R6(b) qualifier.
- **D2, D6–D11:** AGREE.

**Other checks on the methodologist's memo.**
- **M-B1(b) and M-B2(g) are accurate.** On C40, all 9 cross-seed pairings are negative (−0.0089 to −0.0012). Report them through the systematic cross-seed statement (C-7: 9 of the 10 significant wins hold in 9/9 pairings) so the seed claims are not chosen cell by cell.
- **M-B2(c):** 5 negative estimates is correct; the write-up's "six" is wrong.
- **M-B2(e):** the Swin-B CI [0.525, 0.611] is verified.
- **M-E2(1):** verified. Only BO vs fixed within Celeb-DF changes under the pre-scoring or pooled partitions.
- **M-E2(2), "3 of 26 architecture decisions would differ under the original test":** verified. It matches S A-2.
- **M-G1:** I prefer the note to simultaneous intervals, which would be one more post hoc method.
- **M-G3:** AGREE.
