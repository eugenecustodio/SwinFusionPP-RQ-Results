# How the Round 3 must-fixes were applied (lead)

Every MUST-FIX from both reviews was applied. Where the two reviews covered the same sentence, the wordings were merged as follows.

- **Within-dataset paragraph (S1–S3 = M3a–c).** The statistician's wording was used: "incompatible with a large difference between SwinFusion++ and either encoder"; "best read as differences in where the frozen thresholds fell"; "no difference between SwinFusion++ and either encoder was detectable". This meets M3's intent.
- **Positive calls (S4 = M4).** M4's full version was used, with one addition: "Swin-B made the fewest **or tied for the fewest**" from the other two sources, because CDF → C40 was 6 vs 6.
- **ROC curve sentence (S5).** It now begins "Outside FF++ C23 → C40, …".
- **Answer to RQ1 (M5 + S6–S8).** M5's three-paragraph text was used, with these changes:
  - "but not within datasets" became "It was not detectable within datasets, and under transfer it did not carry over to threshold-dependent performance at the frozen source operating points" (S7);
  - the BO sentence now reads "significantly raised … but significantly lowered … consistent with tighter fitting to each training source" (S8);
  - "more consistent with threshold placement" became "best read as threshold placement rather than better ranking" (S6).

  The new numbers were verified by the lead:
  - precision differences ≤ 2.00 pp and recall differences ≤ 3.08 pp (T4);
  - minimum defined transfer precision 80.00% (T7);
  - positive calls 114 / 458 / 8 (T7).
- **Holm p (S9 = M1).** T9 and J5 now show "< 0.005" for CDF → DFo.
- **Notes (S10, S11, M6, M8).** The J7 note has the new floor rule, the jackknife sentence and the DFo 175-cluster sentence. The T2 pooled-grouping definition and the J1 per-seed disclosure are added.
- **Other must-fixes:**
  - M2: "Ch. 2, Review of Related Studies" in T3;
  - M7: FF++ is defined at first use.
- **Suggestions applied:**
  - statistician: S1 (American dates), S2 (run-in heading "Amendments after Test Scoring."), S3 (nine independent clusters), S4 (FF++ C23 training or validation data), S5, S6, S7;
  - methodologist: S2, S3 (McNemar wording in D-2), S5 (Title Case With/From), S6, S7, S8, S9 ("the stored paired-bootstrap p-values"), S10, S11 (bracketed labels dropped from T2), S12, S13, S14.
- **Not applied:** statistician S8 (the D-2 sentence was replaced by methodologist S3 instead). Methodologist S1 is accepted: the preliminary study is left out, and the user will be asked about it.
