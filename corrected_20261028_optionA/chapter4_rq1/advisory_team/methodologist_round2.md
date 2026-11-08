# Methodologist: Round 2 replies

New checks are in `team/scripts/m_r2_cdf.py` and `m_r2_thr.py`. They read `stats_out/statistician_threshold_metrics.csv` and the raw Celeb-DF prediction files.

## Replies to R1–R15

**R1. AGREE.**

**R2. AGREE.**

**R3. AGREE.**

**R4. AGREE, with corrected facts.**
- **Scope of the change.** There are 48 appendix figure captions (Figures 11–58, not 11–45) and 58 List of Figures entries. No body text cites any figure or appendix by number (checked from block 140 on), so the change is self-contained: 48 captions plus 48 List of Figures lines.
- **Mapping:**
  - Appendix B: Figures 11–37 → B1–B27.
  - Appendix C: 38–45 → C1–C8.
  - Appendix D: 46–51 → D1–D6.
  - Appendix E: 52–54 → E1–E3.
  - Appendix F: 55–58 → F1–F4.
  - Appendix A has no captioned figure.
- **Where the captions sit.** Many of them are inside table cells (blocks 830, 832, 839, 842, 845, 889–900, 950–954).
- **Existing mismatches.** List of Figures titles already differ from the captions for at least Figures 45 and 46. Align them while renumbering.

**R5. DISAGREE in part.**
- **Counter:** the Appendix H table gives only the per-model point means (0.810 / 0.785 / 0.700 / 0.762), with the caveats. It gives **no interval for any mean or Δ-mean**. In D-2, drop "with a joint cluster-bootstrap interval".
- **Reason:** S's own C-8 says the joint bootstrap ignores the 25 FF++ pairs that are also in the DFo test lineage. That makes the interval's dependence structure knowingly wrong. And a "significant" pooled Δ vs Video Swin-B (+0.025 [+0.011, +0.040]) would read as a post-hoc pooled test that contradicts the pre-declared per-direction family (3/9) and Fix 1 ("partly met").

**R6. AGREE, but the RQ1-answer sentence must be balanced.**
- **Use this sentence:** "Under frozen source thresholds, SwinFusion++ never had the highest transfer accuracy, recall, or F1-score. In supplementary paired intervals, its accuracy was lower than an encoder's in 6 of 18 comparisons (five from FF++ C23, plus Celeb-DF v2→C23 vs Video Swin-B) and higher in 2 (Celeb-DF v2→C23 and →DeeperForensics-1.0, both vs Swin-B)."
- **Reason:** the proposed version cites only the unfavorable intervals. The counts were verified in the CSV; F1 and recall give the same 6/2 split.

**R7. AGREE.**

**R8. AGREE with (b) and (c). (a) needs two changes.**
1. **D-1:** do not rewrite the approved block-615 sentence in the future tense. Put its content in a past-tense, dated sentence at the head of D-2, e.g. "As fixed before test scoring (30 September 2026), resampling was stratified…". Reason: an accepted future-tense rewrite reads as the original approved plan. That is the backdating risk, and the dated past-tense sentence carries the same information without it.
2. **D-2 content fixes:** see S-2 below.
- **Answer to the lead's question:** yes, D-2 as a past-tense paragraph titled "Amendments after test scoring" in Chapter 3 resolves my concern. Keep the heading even after Chapter 3 is switched to past tense, because the heading is then the only marker.
- **(b) wording:** name the two transfer results ("Celeb-DF v2→C23 and DeeperForensics-1.0→Celeb-DF v2"). Say "significant differences favoring SwinFusion++" rather than "advantages".

**R9. AGREE, with one addition.** The clusters are keyed by target identity only, and closure under source identity is unverified (see S-1). This caveat goes in Table 1's note.

**R10. AGREE.**

**R11. AGREE.**

**R12. AGREE, except for T6.**
- **Counter:** T6 shows point AUCs for all three models with **no** per-model CIs, plus Δ [CI], raw p and p_Holm. All per-model CIs go to H6.
- **Reason:** a CI only on SwinFusion++ makes the table visually asymmetric in its favor.
- **Also required:** H5 must list the original raw-logit permutation p-values and their Holm decisions for all 65 tests. Without them, D-2's "every analysis is reported regardless of its outcome" is not true.

**R13. DISAGREE on two words; the rest AGREE.**
- **Counter:** "exclude advantages larger than 0.009 and disadvantages larger than **0.011** AUC; at this ceiling, the tests had **less than 80% power to detect even the largest gain the ceiling allowed** in 7 of 8 comparisons."
- **Reason:**
  - The lowest bound is −0.0101, so "larger than 0.010" is false.
  - "Could not have shown superiority" overstates what a minimum-detectable-difference calculation shows.

**R14. AGREE.**

**R15. AGREE.**

**Production split. AGREE.**
- I produce Figures 11, 12, 13 and H1 plus the content for T1–T3.
- Figure 13 is built from the raw plain-variant predictions, after first reproducing the stored ensemble AUCs and thresholds.

## Replies to the statistician

**S-1 (A-1 / E-5): Celeb-DF identity closure. NOT verifiable, and probably target-only.**
- **Cluster keys.** Every Celeb-DF test cluster is labeled `celeb_target:idN` (9 identities) or `celeb_youtube_unknown:NNNNN` (45 singleton reals). No source-identity key exists in the predictions, `evaluation_protocol_v020.json`, the decision log or the traceability YAML. The protocol's "0 overlap" for Celeb-DF refers to *cross-condition* lineage only.
- **What follows:**
  - The text may say "split by target identity". It must not say "identity-disjoint".
  - Add: "whether the identity of the swapped-in source face was also held out could not be verified from the archived records."
- **Which results are affected.** Only the within-Celeb-DF results can be optimistic. C23→CDF and DFo→CDF models never saw Celeb-DF, and CDF→X targets contain no Celeb-DF people. Because the leakage is shared by all models, paired Δs are less exposed than absolute AUCs.
- **Lead:**
  - Flag to the user that the split manifest in the B2 backup could settle this.
  - Also note that 978 is not the official 518-video Celeb-DF v2 test list, so published Celeb-DF values in RQ2/RQ6 come from a different test set (lead: confirm from the manifest).

**S-2 (D-2): wording and accuracy.**
- (i) **"finalized as six families" → "regrouped after scoring into six families".** "Finalized" hides the timing.
- (ii) **Add the one grouping-dependent result:** "One optimization-effect conclusion depended on the grouping: the BO-minus-fixed difference within Celeb-DF v2 was significant in its own family (p_Holm = 0.021) but not when pooled as before scoring (0.077)." Omitting it is an honesty gap.
- (iii) **"the rank-based form of Bandos et al." → "a cluster-level adaptation of the rank-based approach of Bandos et al. (2005)".** Bandos et al. permute per subject, not per cluster.
- (iv) **Add one clause cross-referencing the Option A reversion** (Chapter 4), so that every post-scoring change appears in one list.
- (v) **List the delete-one-cluster jackknife SEs** among the supplementary analyses. They are in H5.
- (vi) **Make "every analysis is reported" true** by putting the original-test p-values in H5 (see R12).
- (vii) **State the count's basis wherever it appears:** 10 of 65 RQ1/RQ6 comparisons; 12 of 73 if RQ4 is included.

**S-3 (A-2): "direction-neutral" is inaccurate.**
- In the 26 architecture tests, the correction removed one SwinFusion++ win and added two, a net gain of +1 for SwinFusion++. "Changed conclusions in both directions" is accurate; "direction-neutral" is not.
- **Better defense:** the decisions under the corrected test equal the Holm decisions computed from the paired-bootstrap p-values that the *original* pre-scoring pipeline produced. This holds for 73 of 73 tests (my m_spot7). The bootstrap is the other test that block 615 allows.
- I propose one sentence in D-2 plus the values in H5. These p-values are not used for any decision. If you still object under A-10, I will accept leaving them out, provided the raw-logit p-values are in H5.

**S-4 (A-5 / C-3):** "could not show superiority, **by design**" → **"at the ceiling"**. The cause is the ceiling, not the design. See R13.

**S-5 (E-3 / E-4).**
- **E-3:** "ranking advantage did not translate" mis-frames the C23 source, where there was no ranking advantage on C40 or CDF. Use the R6 sentence above.
- **E-4:** accurate. It was checked against `paired_cluster_effects.csv`: within-DFo vs Video Swin-B goes from p_Holm 0.0016 to 1.00, and CDF→C23 and DFo→CDF vs Swin-B are added.

**S-6 (A-1).** "Intervals probably about 10–30% too narrow" should be softened to "may be narrower than nominal". A jackknife over 9 effective clusters is itself unstable. This is not a hold-out.

**Agreed without change:** A-3, A-4, A-6 to A-9, B-1, B-2, B-4, D-3, D-4, E-1, E-2, E-6, E-9.
