# AGREED PLAN: Chapter 4 opening and RQ1 (all three advisors, after Round 2)

Status: agreed by the lead, the statistician and the methodologist. Anything not listed here follows the R1–R15 file as amended by both Round 2 memos.

## Rulings

1. **Scope.** RQ1 contains:
   - the within-dataset and frozen-transfer comparisons, fixed recipe vs Swin-B and Video Swin-B;
   - the BO configured system, within and transfer;
   - the optimization effect (BO − fixed), within and transfer.

   The controls and Tier B go to RQ4, with one pointer sentence. Calibration and compute get their own section after RQ6. The H0 decision and Fix 1 go to RQ6.
2. **Family names in the text:**
   - within-dataset architecture family (m = 8);
   - frozen-transfer architecture family (m = 18);
   - configured-system families (m = 8 / 18);
   - optimization-effect families (m = 4 / 9).

   A table note maps these to the file labels.
3. **Chapter title** "Chapter 4 – PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA". Heading2 sections "Evaluation Setting" and "Research Question 1: SwinFusion++ Compared with the Standalone Encoders". Bold sub-subsections 4.1.1–4.1.5.
4. **Numbering.**
   - Chapter 4 tables: Table 1… with captions above.
   - Chapter 4 figures: continue at Figure 11.
   - Appendix figures are relabeled with APA 7 appendix-letter numbers: B1–B27, C1–C8, D1–D6, E1–E3, F1–F4. Apply this to all 48 captions (some sit in table cells) and the matching List of Figures lines, and align the mismatched List of Figures titles (e.g. 45 and 46).
   - The supplementary appendix is **Appendix J** (H and I are the Turnitin reports). Its tables are J1… and its figure J1.
   - The List of Tables and page numbers wait for the final formatting pass.
5. **Mean transfer AUC:** in Appendix J only, as point means (0.810 / 0.785 / 0.700 / 0.762) with no interval, plus the registry caveat ("no collapsed generalization score") and the S B-3.5 caveats. It does not appear in the Chapter 4 text.
6. **Threshold metrics.**
   - Table 7 is descriptive.
   - The paired Δ intervals are supplementary (Table J2).
   - The text reports the intervals that exclude 0 in BOTH directions:
     - transfer accuracy: 6 lower and 2 higher for SwinFusion++;
     - within datasets: 2 higher for SwinFusion++ (Celeb-DF vs Swin-B, with the 9-cluster caveat; DFo vs Video Swin-B).
   - Agreed RQ1-answer sentence: "Under frozen source thresholds, SwinFusion++ never had the highest transfer accuracy, recall, or F1-score (point estimates; several margins were one or two videos). In supplementary paired intervals, its transfer accuracy was lower than an encoder's in 6 of 18 comparisons (both encoders from FF++ C23 to C40 and to Celeb-DF v2; Video Swin-B from FF++ C23 to DeeperForensics-1.0 and from Celeb-DF v2 to C23) and higher in 2 (Swin-B from Celeb-DF v2 to C23 and to DeeperForensics-1.0)."
7. **Inference.**
   - ΔAUC [95% unadjusted percentile CI, stratified cluster bootstrap, 5,000 draws], plus the raw rank-permutation p and the Holm-adjusted p.
   - A Holm p at the family floor is written "< 0.005". A raw p below 0.001 is written "< 0.001". All other p-values get 3 decimals.
   - Nothing else is tested: no McNemar, TOST, DeLong or threshold-metric tests.
8. **Disclosures.**
   - **(a) Chapter 3.** Block 615 is NOT rewritten. A new past-tense paragraph, "Amendments after test scoring", goes after block 615 and must cover:
     - a dated sentence on the stratified resampling and the 5,000-permutation specification fixed before scoring;
     - (i) the rank correction, as "a cluster-level adaptation of the rank-based approach of Bandos et al. (2005)". It changed conclusions in both directions (one significant SwinFusion++ advantage removed, two added) — not "direction-neutral" — and the original-test values are in Appendix J. Holm decisions from the paired-bootstrap p-values agreed in all 73 comparisons; this is a decisions-only sentence, with no bootstrap p printed;
     - (ii) the families: "regrouped after scoring into six families". Under the partition recorded before scoring and under one pooled family, the architecture conclusions were identical. The one grouping-dependent result is BO − fixed within Celeb-DF (0.021 vs 0.077);
     - (iii) a cross-reference to the Option A reversion (Chapter 4);
     - (iv) the supplementary analyses, with no p-values: threshold-metric Δ intervals, minimum detectable difference, cross-seed sign agreement, DFo global_cluster, Celeb-DF leave-one-identity-out, the jackknife/bootstrap SE ratio, and point-mean transfer AUC;
     - (v) why McNemar was not used.
     - Counts must state their basis (10 of 65 RQ1/RQ6 comparisons changed under the correction).
   - **(b) Chapter 4 opening:**
     - the Option A sentence, verbatim;
     - one sentence naming the rank-correction effect ("removed one significant difference favoring SwinFusion++ (within DeeperForensics-1.0, vs Video Swin-B) and added two (Celeb-DF v2→C23 and DeeperForensics-1.0→Celeb-DF v2, vs Swin-B)");
     - a pointer to Chapter 3's amendments.
   - **(c) Table 3, Deviations,** in Chapter 4 (protocol deviations, not statistics).
9. **Celeb-DF.**
   - Say "split by target identity", never "identity-disjoint".
   - State that source-identity closure could not be verified.
   - The test set is 978 videos with all 843 fakes in 9 identity clusters, so intervals are approximate. This caveat goes in Table 1 and in every Celeb-DF note.
10. **Lineage.**
    - Table 1 gives the overlap counts and strict-subset sizes.
    - The text gives C23→DFo, n = 60, as seed means with no interval.
    - The DFo→FF++ wins cannot be checked on the 20-video subset.
11. **Claims.**
    - **Within datasets:** "no detectable difference; each paired 95% interval lay between −0.011 and +0.009 AUC; at this ceiling the tests had less than 80% power to detect even the largest gain the ceiling allowed in 7 of 8 comparisons."
    - **Transfer vs Video Swin-B:** "significantly higher in 3, no detectable difference in 6, significantly lower in none". "Never significantly worse" always carries its widest lower bound, −0.092 (DFo→CDF vs VSB).
    - **C23→DFo:** "consistent with". No causal claim about TLBG-HCA.
    - **Forbidden:** "equivalent", "tied" (in RQ1), "robust", "generalizes", and the S E-9 phrases.
12. **Preliminary study:** two sentences, labeled as a different pipeline and test population.
13. **Fixed recipe:** no hyperparameter values are printed. The lead flags verification to the user.

## Tables (pre-rounded strings; U+2212 for minus; signed Δ)

The source for each is the statistician's CSVs in `team/tables/`.

| ID | Layout | Columns |
|---|---|---|
| T1 | 4 rows (test sets), by the methodologist | Test set; videos (fake/real); clusters; coverage; preprocessing failures; test videos sharing lineage with other conditions' train/val; strict subset(s) |
| T2 | analyses → families → section, by the methodologist | Analysis; models/regimen; family (m); grouping status; section |
| T3 | deviations, by the methodologist | Planned (Chapter 3); what was done; reason/decision ID; consequence for interpretation |
| T4 | Within, fixed recipe. One span row per test set ("FF++ C23 — 280 videos (140 fake), 70 clusters"), then 3 model rows. | Model; ROC-AUC [95% CI]; PR-AUC; Acc (%); Prec (%); Rec (%); Spec (%); F1; FP; FN; seed AUC mean ± SD |
| T5 | Within ΔAUC, 8 rows, long | Test set (shown on the first row of each pair); comparator; ΔAUC; 95% CI; raw p; Holm p |
| T6 | Transfer architecture, 18 rows, long | Direction (first row of each pair); comparator; SwinFusion++ AUC; comparator AUC; ΔAUC; 95% CI; raw p; Holm p |
| T7 | Transfer threshold metrics. One span row per direction (with fake prevalence), 3 model rows. | Model; PR-AUC; Acc (%); Prec (%); Rec (%); Spec (%); F1; TP; FP. Precision is "—" when there are 0 positive calls; it is flagged when there are fewer than 10. |
| T8 | Configured system, 26 rows, long (13 conditions × 2 comparators) | Condition; comparator; BO SwinFusion++ AUC; comparator AUC; ΔAUC; 95% CI; raw p; Holm p |
| T9 | Optimization effect, 13 rows | Condition; BO AUC; fixed AUC; ΔAUC; 95% CI; raw p; Holm p |
| J1 | Per-seed ROC-AUC, 52 rows (13 cells × SF++ fixed, SF++ BO, Swin-B, VSB) | Training → test; model; seed 1; seed 2; seed 3; mean ± SD; ensemble |
| J2 | Threshold-metric paired Δ, 26 rows, fixed recipe | Condition; comparator; ΔAcc [CI]; ΔPrec [CI]; ΔRec [CI]; ΔF1 [CI] ("n.e." when not estimable) |
| J3 | Strict lineage-free subsets, per seed | Direction (n); model; seed 1; seed 2; seed 3; mean |
| J4 | Flip-TTA vs plain ROC-AUC, all models, 13 rows | Cell; then plain / TTA for SF++ fixed, Swin-B, VSB, SF++ BO |
| J5 | Original raw-logit permutation vs corrected rank test, all 65 RQ1/RQ6 comparisons | Family; comparison; ΔAUC; raw-logit p; Holm (original); rank p; Holm (rank); decision changed? |
| J6 | Within-dataset sensitivity, 8 rows | Test set; comparator; SE(ΔAUC); MDD (α = 0.05); MDD (α = 0.05/8); headroom |
| J7 | Robustness of the 10 significant architecture differences | Comparison; Holm p under Option A / pre-scoring / pooled-26; seed sign agreement (x/9); DFo global_cluster Holm p (DFo targets only, else "—"); Celeb-DF leave-one-identity-out Δ range (CDF targets only, else "—") |
| J8 | Transfer ROC-AUC [95% CI] for all four model/regimens, 9 rows + an unweighted mean row (point only) | Direction; SF++ fixed; Swin-B; VSB; SF++ BO |

## Figures (methodologist; 300 dpi; 6.0 in wide; no embedded title or footer; palette and markers from make_figures_optionA.py; American spelling)

- **Fig 11.** The transfer ROC-AUC heatmap for the three fixed-recipe models, regenerated from the ensemble CSV.
- **Fig 12.** A forest plot of the 26 principal ΔAUCs [95% CI].
  - Two panels with separate x-scales: within datasets (8) and transfer (18). Rows are grouped by condition, with the comparator distinguished by marker shape and color.
  - Filled marker = Holm p < 0.05; open marker = not significant.
  - A dashed line marks 0.
  - Numbers come from the statistician's T5/T6 CSVs.
- **Fig 13.** A 3 × 3 grid of ROC curves for the 9 transfer directions, three fixed-recipe models each, with each model's frozen operating point marked. Use the statistician's ROC CSV.
- **Fig J1.** A 1 × 4 grid of within-dataset ROC curves, from the same source.
