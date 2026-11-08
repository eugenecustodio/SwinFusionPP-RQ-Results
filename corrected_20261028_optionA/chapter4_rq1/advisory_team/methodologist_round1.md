# Methodologist / examiner — Round 1 memo (Chapter 4 opening + RQ1)

**Item IDs:** M-A1… (scope), M-B0 = opening and M-B1–B5 = §4.1.1–4.1.5, M-C T1–T8 / Fig 11–13, M-D1–D11 (rows), M-E1–E13, M-F1–F7, M-G1–G10.

All numbers below were checked against `00_Shared/statistics_raw/` or `paired_tests_optionA.csv`. Scripts: `team/scripts/m_spot1.py` to `m_spot7.py`. PKG = `corrected_20261028_optionA/` unless stated.

---

## A. Scope decisions

**M-A1. RQ1 reports both within-dataset AND frozen-transfer comparisons against Swin-B and Video Swin-B.**
- RQ1's wording requires cross-dataset evaluation.
- `rq_traceability.yaml` (pre-registration) lists `directional_frozen_transfer_core` under RQ1's matrix roles and tables (`fixed_architecture`, `optimized_system`, `directional_transfer`).
- Chapter 1 block 175 ("RQ6 will synthesize these within-dataset results with directional frozen transfer") is compatible with this: RQ6 *synthesizes* the transfer evidence; it does not own it.

**M-A2. RQ6 reuses the RQ1 transfer tables by cross-reference and does not reprint them.** RQ6 adds the published-model context, the Fix 1 verdict, and the H0 decision.

**M-A3. The topology/capacity controls and the Tier-B ablations go in RQ4, not RQ1.**
- RQ4 asks whether the hierarchical cross-attention helps. The traceability registry's RQ4 claim is "Test TLBG-HCA using topology and capacity controls".
- Chapter 1 block 175 and Chapter 3 block 614 place the "contribution analysis" in the RQ1 paragraph. Resolve this without rewriting the approved scope:
  - add one sentence in RQ1: "Whether these differences can be attributed to TLBG-HCA is examined in RQ4";
  - add the RQ→evidence map (Table 2, see C).

**M-A4. The configured-system comparison and the optimization effect stay in RQ1, both within-dataset and transfer.**
- Chapter 1 block 175 promises "a second table" for RQ1.
- D-25/A-02 requires a paired BO-vs-fixed comparison on every dataset.
- Present both in one table (Table 8).

**M-A5. Relabel the families by content, not by RQ; the structure is unchanged.**
- The names: *Architecture–within (m = 8)*, *Architecture–transfer (18)*, *Configured system–within/–transfer (8/18)*, *Optimization effect–within/–transfer (4/9)*, *Controls–within/–transfer (2/6)*, and *Tier B (descriptive)*.
- A table note maps each name to its file label, so it stays traceable.
- Calling the transfer family "RQ6_architecture" inside the RQ1 section would confuse the panel.

**M-A6. Calibration, compute cost and the metadata-shortcut audit are not RQ1 content.** Put calibration and compute in a section after RQ6, titled "Calibration and Computational Cost", which RQ1 cross-references. Put the audit in the Chapter 4 opening.

**M-A7. H0 (blocks 251–252) concerns "existing CNN- or transformer-based spatio-temporal models", so the H0 decision belongs in RQ6.** RQ1 reports per-test decisions only.

**M-A8. Agree: Fix 1 stays out of RQ1.** RQ1's facts must be stated so that Fix 1 follows from them without contradiction.

---

## B. Section blueprint (Chapter 4 through RQ1)

**Chapter 4 – PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA** (Heading1, matching "Chapter 3 – METHODOLOGY").

### M-B0. Opening (Heading2 "Evaluation Setting"), about 1.5 pages

1. **Purpose and order.** RQ1–RQ4 and RQ6. RQ5 is reported separately.
2. **Disclosure.** The Option A sentence, verbatim. Then two further sentences:
   - "Comparison families were regrouped to match this plan after test scoring; all architecture conclusions are identical under the grouping in force before scoring."
   - "Deviations from the Chapter 3 plan are listed in Table 3."
3. **Set-up, in one paragraph.**
   - Models and three seeds (260901–260903); three-seed mean-logit ensembles.
   - The evaluation unit is one video: 7 locked clips × 16 aligned 224×224 frames at 2 fps, video logit = mean of the clip logits.
   - The threshold maximizes Youden's J on source validation (ties go to the lower threshold); the temperature is fitted on source validation.
   - Frozen transfer, with no target labels used.
   - The plain variant is used throughout; flip-TTA is in the Appendix.
4. **Table 1. Test sets and coverage** (see C), followed by a coverage paragraph:
   - 100% coverage. There were no preprocessing failures and no Insufficient-Evidence outcomes in any test set.
   - Source-validation coverage was 279/280 for C23 and C40, 977/977 for Celeb-DF and 192/192 for DeeperForensics.
5. **Data-integrity paragraph.**
   - Lineage overlap.
   - Preprocessing-rule development exposure: 67 of 247 development rows share lineage with held-out rows, 15 of them physically identical.
   - 157 held-out videos were shown label-blind during the face-quality review.
   - The metadata-shortcut audit result.
6. **Table 2. Analyses, families and where they are reported**, and **Table 3. Deviations from the approved plan**, each with a brief introduction.
7. **Statistics reminder, 3–4 sentences.**
   - ΔAUC uses a paired cluster bootstrap with an unadjusted 95% CI, and a rank-based cluster permutation with Holm correction.
   - Inference is conditional on the trained ensembles; training-seed spread is shown descriptively.
   - Threshold-free and threshold-dependent results are kept separate.
   - Celeb-DF's fake prevalence is 86.2%, which is the trivial-accuracy baseline.

### 4.1 RQ1 (Heading2), restating the RQ

**M-B1. 4.1.1 In-distribution performance under the fixed recipe.** Table 4 (metrics) and Table 5 (paired ΔAUC). Findings:
- (a) All nine AUCs fall between 0.9878 and 0.9974, and none of the 8 paired differences is significant (all p_Holm = 1.00). The 95% CIs exclude a SwinFusion++ advantage larger than 0.009 AUC.
- (b) The SwinFusion++ point estimate is lower in 6 of 8 comparisons, which is descriptive. On C40, all three SwinFusion++ seeds (0.9841–0.9874) were below all three Video Swin-B seeds (0.9886–0.9931).
- (c) Correct classifications (descriptive, no test):
  - C23 and C40: 0–3 videos apart.
  - DeeperForensics: SwinFusion++ +4 vs Swin-B and +7 vs Video Swin-B.
  - Celeb-DF: SwinFusion++ +23 vs Swin-B and −5 vs Video Swin-B.
- (d) The ceiling leaves little room to detect differences.

**M-B2. 4.1.2 Frozen cross-dataset transfer under the fixed recipe.** Table 6, Figure 11 (heatmap) and Figure 12 (forest plot of all 26 principal ΔAUCs). Findings:
- (a) **Against Swin-B:** significantly higher in 7 of 9 directions (+0.049 to +0.258).
- (b) **Against Video Swin-B:** significantly higher in 3 of 9 (+0.063 to +0.084).
- (c) **Never significantly worse** than either encoder. There are 5 negative estimates; the largest is −0.016 [−0.041, +0.009] (C23→DeeperForensics vs Video Swin-B).
- (d) **Dependence on the source:**
  - From Celeb-DF and DeeperForensics: better than Swin-B in 6 of 6 directions and than Video Swin-B in 3 of 6.
  - From C23: tied on C40 and Celeb-DF.
  - The only C23 win is against Swin-B on DeeperForensics.
- (e) **Swin-B collapsed on C23→DeeperForensics** (0.568 [0.525, 0.611]). The collapse persists on the 60-video lineage-free subset (seed means: Swin-B 0.532, SwinFusion++ 0.736, Video Swin-B 0.787).
- (f) **Absolute transfer AUC is modest:** 0.59–0.98. DeeperForensics→Celeb-DF is near chance for all three models (0.459 / 0.588 / 0.600).
- (g) **Seed check:**
  - In all 7 directions where SwinFusion++ beat Swin-B, every SwinFusion++ seed exceeded every Swin-B seed.
  - Against Video Swin-B this held in 2 of 3. On Celeb-DF→C40 the seed ranges overlap (Video Swin-B 0.704–0.808; SwinFusion++ 0.801–0.839).

**M-B3. 4.1.3 Threshold-dependent metrics under transfer.** Table 7 and Figure 13 (ROC curves with the frozen operating points marked). Findings:
- (a) **At the source thresholds every model became conservative.**
  - Specificity was 0.911–1.000.
  - Recall was 0–63.7% in all directions except C23→C40 (79.3–87.1%).
  - Accuracy was about 50% on the balanced targets.
  - From DeeperForensics to Celeb-DF, accuracy was 13.8–15.2%, which is roughly 1 − prevalence.
- (b) **SwinFusion++ did not have the highest accuracy, recall or F1 in any of the 9 directions.** Video Swin-B was highest in 7 and Swin-B in 2.
  - SwinFusion++'s high precision and specificity reflect the fewest positive calls.
  - Precision computed from 1–8 positive calls is not interpretable. In three cells Swin-B made no positive call at all, so precision is undefined.
- (c) **Where AUC stayed at or above about 0.8, the curves show that ranking was retained and the operating point was misplaced.** Fixing that would require target labels, which the design excludes. Cross-reference the calibration section.

**M-B4. 4.1.4 Configured system and optimization effect.** Table 8. Findings:
- (a) **Within datasets, the BO-selected configuration did not differ significantly from either encoder** (8 of 8 non-significant). Its highest point AUCs on C40 (0.9941) and Celeb-DF (0.9983) are descriptive only.
- (b) **Under transfer:**
  - Better than Swin-B in 6 of 9 directions.
  - Better than Video Swin-B only on C23→C40 (+0.0116).
  - Worse than Video Swin-B on C23→DeeperForensics (−0.1105) and Celeb-DF→C23 (−0.0390).
- (c) **BO-selected minus fixed SwinFusion++:**
  - Up on C40 (+0.0063), Celeb-DF (+0.0031, a result that depends on the family grouping) and C23→C40 (+0.0102).
  - Down in 5 transfer directions (−0.041 to −0.104).
  - Caveats: unequal search effort (12/12/8/8 trials) and a near-saturated objective (best validation AUC 0.9977–0.9994).

**M-B5. 4.1.5 Answer to RQ1** (one paragraph, using only the claims in D). Then:
- an optional two-sentence comparison with the preliminary study, labelled as a different pipeline and test population;
- pointers to RQ4 (attribution) and RQ6 (the criterion verdict).

**Philippine format.** Each table and figure is introduced by number, then described with its key numbers, then interpreted in 2–4 sentences.

---

## C. Tables and figures

### Caption conventions (from the manuscript)
- **Figures.**
  - Caption below the image, Heading4 style, "Figure N. Title in Title Case", no final period (e.g., "Figure 14. Uploading Interface").
  - Numbering is continuous through the document, and the captions are typed (the snapshot has no SEQ fields).
  - Chapter 4 figures therefore start at **Figure 11**. The appendix figures (now 11–58) and the List of Figures must be renumbered in one pass at the end.
- **Tables.**
  - The manuscript has no captioned tables, so Chapter 4 starts at **Table 1**.
  - Caption **above** the table, same style: "Table N. Title in Title Case".
  - Put a "Note." paragraph below each table covering the abbreviations, CI method, family, class counts and the definitions FPR = 1 − specificity and FNR = 1 − recall.
  - Add a List of Tables.
- **Remove the embedded titles** from all PNGs ("RQ1 · …"). The caption carries the title. Fix "colour" → "color".
- **Do not bold "best" values** in tables of statistically indistinguishable results. Mark significance only, with an asterisk in the Δ tables.

### Tables (new compilations, all from existing CSVs)

| # | Content | Source |
|---|---|---|
| T1 | Per test set: videos (fake/real), dependency clusters, coverage, preprocessing failures, test videos sharing lineage with other conditions' train/val (C23 260/280, C40 260/280, DFo 382/402, CDF 0/978), strict-subset sizes for affected directions | `heldout_seed_metrics_rq1_rq6.csv`, `evaluation_protocol_v020.json`, A-07 |
| T2 | Analysis → models/regimen → family (m) → declared before scoring? → section | `paired_tests_optionA.csv`, A-07/A-16, framing JSON |
| T3 | Deviations (list in E) | decisions log, CHAPTER4_NOTES |
| T4 | Within, fixed recipe: AUC [CI], Acc, Prec, Rec, Spec, F1, FP, FN, seed AUC mean ± SD. The FP/FN columns satisfy the confusion-matrix promise. | `three_seed_mean_logit_ensemble.csv` (= `RQ1/results/table1`) |
| T5 | Within paired ΔAUC [CI], p_Holm, 4 × 2 | `table2_paired_within_architecture` |
| T6 | Transfer: AUC [CI] for **all three** models (the package gives a CI for SwinFusion++ only) + ΔAUC [CI], p_Holm vs each encoder; 9 rows | ensemble CSV + `table3b` |
| T7 | Transfer threshold metrics, 27 rows: Acc, Prec, Rec, Spec, F1, TP/FP. Undefined values shown as "—" with a note. | `table3_transfer_all_metrics` (fixed-recipe rows) |
| T8 | Configured system + optimization effect, 13 rows: BO AUC, Δ vs Swin-B, Δ vs Video Swin-B, Δ BO−fixed [CI], each with p_Holm | `table1b`, `table2b`, `table3c`, RQ1 write-up §4 |
| App. | Per-seed metrics for every model and cell (Chapter 3 block 614 requires it); PR-AUC/FPR/FNR; flip-TTA for **all** models; strict-subset per-seed values | `heldout_seed_metrics…csv` |

### Figures

| Decision | File | Notes |
|---|---|---|
| **KEEP → Fig 11** | `figures/RQ1/fig2_transfer_all_models.png` | The best existing figure, because it shows the absolute level and the source pattern. Remove the title and fix "colour". |
| **MAKE → Fig 12** | Forest plot of the 26 principal ΔAUCs with 95% CIs. Two panels with separate x-scales (within ±0.012; transfer −0.05 to +0.32); rows ordered by direction; filled marker = p_Holm < .05. | Replaces `fig1_within_ci` and `RQ6/fig1b_delta…`, since inference is on paired Δ and marginal-CI overlap invites a fallacy |
| **MAKE → Fig 13** | 3 × 3 small-multiple ROC curves for the 9 transfer directions, three models each, with each model's frozen operating point marked | Delivers the ROC curves promised at block 519 and is the only figure that *explains* the AUC-vs-accuracy split |
| MAKE → Appendix | 1 × 4 within-dataset ROC curves | Promised at block 519, uninformative at the ceiling |
| DROP | `fig1_within_ci.png` | Redundant with T4; marginal-CI overlap is not the test |
| DROP | `fig2_transfer_swinfusionpp/_swin_b/_video_swin_b.png`, `RQ6/fig1_matrix_swinfusionpp.png` | Duplicates; `fig1_matrix` is identical to `fig2_transfer_swinfusionpp` |
| DROP | `fig1b_within_ci_configured_system.png`, `fig2b_transfer_swinfusionpp_bo.png`, `RQ6/fig1c…configured_system.png` | T8 suffices for a secondary analysis |
| NO | Per-seed dot plot, confusion-matrix images | Per-seed values go in an appendix table plus one sentence; confusion counts go in T4/T7. 39 matrix images would be padding. |

---

## D. Claims allowed and forbidden

| Finding | Allowed wording (maximum strength) | Forbidden |
|---|---|---|
| M-D1. Within | "statistically indistinguishable; no detectable difference (8/8, p_Holm = 1.00); 95% CIs exclude SwinFusion++ gains above 0.009 AUC; all models near the ceiling" | "equivalent", "comparable", "on par", "matches"; bolded "best" on DFo; "differ by only a few videos" (wrong for Celeb-DF vs Swin-B: 23 videos) |
| M-D2. Transfer vs Swin-B | "significantly higher ROC-AUC in 7 of 9 directions" | "outperforms Swin-B in transfer" without the count |
| M-D3. Transfer vs Video Swin-B | "higher in 3, statistically tied in 6, significantly lower in none" | "better than Video Swin-B"; "never worse" (say "never significantly worse"; the data allow −0.041) |
| M-D4. C23→DFo Swin-B | "Swin-B's AUC fell to 0.568; the two models with a temporal stream retained 0.83–0.84; the pattern persisted on the lineage-free subset. This is *consistent with* temporal evidence transferring better in this direction." | "temporal modeling causes / explains"; Swin-B and Video Swin-B also differ in pretraining and input handling |
| M-D5. Threshold collapse | "at frozen source thresholds, all models were conservative (specificity ≥ 0.91, recall mostly < 64%); SwinFusion++ never had the highest transfer accuracy, recall or F1" | "threshold effect, not a ranking failure" applied to every direction. DFo→CDF fails on ranking too. |
| M-D6. BO trade-off | "the BO-selected configuration raised AUC on C40, Celeb-DF* and C23→C40 and lowered it in five transfer directions, *consistent with* tighter fitting to the source" (*grouping-dependent) | "BO overfits"; "BO improves the model"; attributing the effect to any single hyperparameter |
| M-D7. Mean transfer AUC 0.810 | **Do not use.** At most a descriptive table footer. | Any use as evidence. The traceability registry for RQ6 states "no collapsed generalization score", and block 616 requires the directions to stay separate. |
| M-D8. Architecture | "the dual-stream system" | Any causal TLBG-HCA language ("cross-attention enables/captures") in RQ1. RQ4's C23 controls tie or beat the full model, and no controls exist for the Celeb-DF/DFo sources where the gains occur. |
| M-D9. General | "less degraded under transfer than Swin-B" | "robust", "generalizes", "improves cross-dataset robustness" (RQ6 write-up line 128). Transfer accuracy is about 50% and transfer ECE has a median of 0.446. |
| M-D10. Platform | — | Implying that these results describe the deployed web app. Its thresholds and temperatures match none of the 144 operating points (CHAPTER4_NOTES §6). |
| M-D11. TTA | Appendix, all models | Quoting a TTA number in the text (the write-up's "0.8847" is selective) |

---

## E. Mandatory disclosures and gaps

**In the opening or Table 3:**
1. **The Option A sentence, verbatim, plus the regrouping sentence.**
   - The Option A split into architecture (8/18) and optimization (4/9) families happened after scoring; block 615 says families are declared before labels are examined.
   - All architecture and configured-system decisions are identical under the pre-scoring and pooled groupings. Only BO vs fixed within Celeb-DF changes (0.021 vs 0.077).
2. **Post-hoc change of test (not in the brief; mandatory).**
   - The pre-declared cluster permutation swapped raw logits across models with different scales. It was replaced after scoring by a rank-based version (Bandos et al., 2005).
   - Under the original test, 3 of the 26 architecture decisions would differ.
   - The paired-bootstrap p-values, the other test Chapter 3 allows, give **the same Holm decisions as the rank test in all 73 comparisons**. This is a supplementary check that I computed now; label it as such.
3. **BO trials:** 12/12/8/8 (8/8/5/8 completed), against the 12/16/20 declared, because of the deadline (A-12).
4. **Gamma correction** was disabled (D-08), although Chapter 3 says it was applied. The gamma and RandAugment ablations were not run.
5. **Tier B:** single seed, BO regimen, C23 only. Block 615 excludes such runs from significance claims, so the RQ4 table should drop or footnote its p_Holm column.
6. **Controls:** C23 only (A-03 withdrawn by A-12).
7. **C40 as a transfer source was not run.** That leaves 9 of 12 directions; block 520 implies all of them.
8. **Lineage counts beside every result.** The protocol forbids "silently omitting overlap counts".
   - Lineage-clean directions (strict subset = full set, A-07): C23→C40, C23→CDF, all three Celeb-DF-source directions, and DFo→CDF.
   - C23→DFo has a 60-video clean subset, which supports the result.
   - DFo→C23 and DFo→C40 (strict subset of only 20 videos) cannot be verified. That covers 2 of the 7 wins over Swin-B and 1 of the 3 over Video Swin-B.
9. **Preprocessing-development exposure and the 157 held-out videos shown during the quality review.**
10. **Hardware:** RTX 5090, whereas block 498 says H100/A100.
11. **Three seeds; inference conditional on the trained models.**
12. **DeeperForensics perturbation (robustness) strata were not evaluated** (blocks 173 and 614). Descope this in one line.
13. **Metadata audit.** It was run (D-43), but the D-43 source-metadata-stratified reporting was not done. The audit file is not in the package; copy it in before citing it.

**Promised by Chapter 3 for RQ1 but missing from the package:**
- ROC curves (Fig 13 and the Appendix).
- Confusion matrices (FP/FN columns).
- FPR/FNR (note, Appendix).
- PR-AUC (Appendix).
- Per-seed tables (Appendix).
- The fixed-recipe training config. Its absence matters: the lead must confirm it equals blocks 496–502 (LR 1e-4/1e-5, wd 0.05, batch 16, ≤ 30 epochs, patience 6). All BO winners used batch 8.
- The latency measurements (compute section).

---

## F. Spot-check results

**Verified exactly:**
- Table 1 within: all 12 rows × 7 metrics plus seed SDs.
- All 27 transfer AUCs and the three means (0.8099 / 0.7002 / 0.7848).
- All 73 ΔAUCs equal the ensemble AUC differences (max error 2e-16).
- The CIs and rank p-values match `paired_cluster_effects_rank_corrected.csv`.
- Holm recomputed per Option A family matches (max diff 0).
- The C23→CDF full-metrics table, including PR-AUC.

**Inconsistencies:**
1. RQ1 write-up §2: "none of its **six** negative point estimates". There are **five**.
2. "Accuracy differs by only a few videos" is false for Celeb-DF: SwinFusion++ had 956 correct, Swin-B 933 and Video Swin-B 961.
3. `table4_tta_variant` reports TTA for SwinFusion++ only, but baseline TTA exists in the CSV. This is selective.
4. "p_Holm = 0.004" is the **floor**: 18 × 1/5001.
5. **CI/test discordance.**
   - DFo→C23 vs Video Swin-B: CI [+0.008, +0.082] but p_Holm = 0.15. The CIs are unadjusted.
   - Configured system within Celeb-DF vs Video Swin-B: raw rank p = 0.204 while the CI [+0.0001, +0.0058] excludes 0. This disagreement is at the raw level.
6. **The "7 clips unverified" flag in COMPUTE_COST is resolvable.** `evaluation_protocol_v020.json` says "mean_of_seven_locked_clip_logits" (A-07), and 7 × 795.17 = 5.57 TFLOPs.
7. **The PNGs have British spelling and embedded titles,** and two of them are duplicates.

---

## G. Positions and questions

**For the statistician:**
- **M-G1.** Either report Holm-consistent (simultaneous) intervals, or state explicitly in every Δ table note that the CIs are unadjusted. I prefer the latter plus one sentence on DFo→C23.
- **M-G2.** Explain the bootstrap-vs-rank-permutation disagreement at the ceiling (F-5). Do you accept "bootstrap-p Holm gives identical decisions in 73/73 cases" as the supplementary robustness statement?
- **M-G3.** No new inferential tests on threshold metrics (no post-hoc McNemar). Block 615 allows McNemar only when there is one decision per cluster, and the FF++ clusters hold 4 videos each. Do you agree?
- **M-G4.** Is "95% CIs exclude gains > 0.009 AUC" acceptable without a TOST? I think it is, as a compatibility statement.
- **M-G5.** How should the floor p-values be written (= .004 vs ≤ .004)? And should we mention percentile-bootstrap behavior at the AUC = 1 boundary?

**For the lead:**
- **M-G6.** Confirm renumbering Figures 11–58 at the end (typed captions), and confirm adding a List of Tables.
- **M-G7.** Confirm that the fixed-recipe config matches Chapter 3, or source it.
- **M-G8.** Opening tables: are three acceptable? T3 could move to Chapter 3 as a tracked "Deviations" subsection, but I prefer Chapter 4, because amending the approved Chapter 3 risks looking like backdating.
- **M-G9.** Keep or cut the preliminary-study paragraph? I'd keep two sentences.
- **M-G10.** Heads-up for RQ6: the RQ6 write-up's "H0 rejected against reproduced CNN baselines" rests on preliminary-study models with a different pipeline. Reword it there.
