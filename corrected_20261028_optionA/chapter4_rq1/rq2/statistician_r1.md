# Statistician, Round 1: RQ2 comparability framework, number checks, and the preliminary-study Xception

**Script:** `team/scripts/statistician_rq2_tables.py`, written to `team/rq2/tables/` and validated before writing.
- **SwinFusion++ values:** recomputed from the raw predictions and asserted against `three_seed_mean_logit_ensemble.csv` (AUC, CI, confusion counts, accuracy, F1).
- **Xception values:** taken from `00_Shared/literature/preliminary_study_v020.csv` (preliminary manuscript, Table 7) and checked against the preliminary PDF text.

## A. Positions

**A1. No inference against any external value.** This covers published papers and the preliminary study alike.
- **No tests:** no p-values, no "significantly", and no intervals on differences.
- **What is still allowed:**
  - Our values keep their own 95% cluster-bootstrap CI.
  - External values are printed as reported; none come with intervals.
  - The text may give descriptive differences ("0.22 higher") only where the test populations match (A5).
- **Why no tests:** a paired test is impossible without common videos and predictions. An unpaired comparison is meaningless because the splits, frame sampling and crops differ.

**A2. The metric hierarchy for cross-study statements.**
1. **ROC-AUC first.** It is threshold-free and does not depend on prevalence.
2. **Accuracy second, and only with the test prevalence beside it.** Accuracy depends on both prevalence and threshold policy. Ours is at a frozen validation-Youden threshold; most papers do not state theirs.
   - On Celeb-DF v2, a rule that calls every video fake scores 86.20% on our test set.
   - The published Celeb-DF test sets have different prevalences: SFormer uses a balanced 105/105 test set, and STIL and S-MIL do not state theirs in the package record.
   - So Celeb-DF accuracies are **not comparable across studies**. For FF++, both sides are balanced (50%), so accuracy is closer but still threshold-dependent.
3. **Precision, recall and F1 are not used for cross-study comparison.** They depend on prevalence, and few papers report them.

**A3. Tiers.**

| Tier | Definition | How it is used |
|---|---|---|
| A | Same dataset, compression and manipulation subset; video-level unit | Main table |
| B | Same dataset, but the unit (frame or clip), the subset (all four manipulations, or unstated) or the level is unstated | Same table, visibly flagged, never used in a "highest/lowest" sentence |
| C | Other data | Not shown in Chapter 4 |

Ranges must never mix tiers. For example, the current write-up's "C23 98.2% vs 98.7–100%" pools TALL-Swin's all-manipulation 98.65% (Tier B) with Tier A values.

**A4. De-duplication.** A value copied by later papers (S-MIL → STIL → SFormer, e.g. I3D 92.86% → 92.9%) is listed **once**, under its original source. Otherwise ranges and counts are inflated.

**A5. The preliminary-study Xception: comparable only on FF++.** Its differences from this study (preliminary PDF, Tables 2, 3 and 7 and §4.2–4.5):

| | Preliminary Xception | This study (SwinFusion++) |
|---|---|---|
| FF++ C23 / C40 test | 280 (140/140), source-pair split 720/140/140, 70 groups | 280 (140/140), 70 source-pair clusters. **Same size and split rule; identical video lists not verified** |
| Celeb-DF v2 test | 859 (723 fake, 84.17%), 46 groups | 978 (843 fake, 86.20%), 54 clusters. **Different population** |
| DeeperForensics-1.0 test | 2,385 analyzed (2,185 fake, 91.61%); fakes span 11 perturbation variants | 402 (201 fake, 50.00%); unperturbed only. **Different population** |
| Model | Single seed (1701), at most 15 epochs, patience 4, 299 × 299 input | Three-seed ensembles; BO or the fixed recipe |
| Clip sampling | Three 16-position anchors (0/16/32) from a 48-observation bank | Seven locked 16-frame clips at 2 fps |

What this allows:
- **FF++:** a descriptive ROC-AUC difference is allowed, with the caveat "same test size and split rule, different pipeline and training budget".
- **Celeb-DF:** side-by-side values only, with the population stated. The 0.648 vs 0.998 contrast can be called "much lower on a different test population".
- **DeeperForensics:** no ranking. Xception's 0.9978 was obtained on a perturbed, 91.61%-fake population.

**A6. Xception's degenerate operating points.** These must be stated, and the affected accuracy/F1 values flagged. I derived the confusion counts from the reported accuracy and F1. Each is the **unique** integer solution given the test counts, and the Celeb-DF and DeeperForensics solutions match the PDF text.

| Test set | TP | FP | TN | FN | Recall | Specificity | Comment |
|---|---|---|---|---|---|---|---|
| C23 | 94 | 39 | 101 | 46 | 67.14% | 72.14% | |
| C40 | 104 | 36 | 104 | 36 | 74.29% | 74.29% | |
| Celeb-DF | 723 | 136 | 0 | 0 | 100.00% | 0.00% | Every video called fake (PDF: "predictions of fake for all 859 videos"; balanced accuracy 0.500). Accuracy 84.17% equals the prevalence; F1 0.9140 = 2π/(1+π). |
| DeeperForensics | 897 | 0 | 200 | 1,288 | 41.05% | 100.00% | PDF: "1,288 false negatives and no false positives". Accuracy 46.00% is below the always-fake rate of 91.61%. |

**Rule:** for these two cells, report ROC-AUC as the only performance figure and describe the decision pattern in words. Never write "Xception reached 84.17% accuracy on Celeb-DF" without "by calling every video fake".

**A7. Option A.** The BO-selected configuration is shown first, with the fixed recipe alongside. Any comparative sentence must hold for **both**, or name the one it holds for.

**A8. The Celeb-DF caveat carries over:** all 843 fakes lie in 9 identity clusters, so our intervals are approximate.

## B. Tables and figures

**Table 9. Within-dataset results of SwinFusion++ used for RQ2** (draft: `tables/T9_draft.csv` and its note).
- **Layout:** one span row per test set, giving n and fake %. Then two rows, BO-selected and fixed recipe.
- **Columns:** ROC-AUC [95% CI]; Acc; Prec; Rec; Spec; F1; balanced accuracy; FP; FN.
- **Balanced accuracy** is optional. It is derived, (Rec + Spec)/2, and adds information only for Celeb-DF (BO 98.43%, fixed 96.83%).
- **Values:** all asserted against the package.

**Table 10. Preliminary-study Xception beside SwinFusion++** (draft: `tables/T10_draft.csv` and its note).
- **Columns:** test set; Xception test videos (fake %); ROC-AUC; Acc; F1; Rec; Spec; SwinFusion++ test videos (fake %); BO ROC-AUC; fixed ROC-AUC.
- **No Δ column**, because the test populations differ in two of the four rows.

**Table 11. Published results** (owned by the methodologist).
- **Layout:** long format, one row per model × condition × metric after de-duplication (A4).
- **Columns:** condition; model; metric = value as printed; unit (video/frame/clip); subset; test population (split and n, and prevalence where stated); source (paper, table); tier.
- **SwinFusion++ (BO / fixed) appears once per condition, as a reference row.**
- **Test populations already recorded in the package that the table must show:**
  - SFormer FF++ "first 700 train / 300 test" (not the official split);
  - SFormer Celeb-DF 105/105 test (balanced);
  - SFormer DeeperForensics "unperturbed tampered + FF++ originals, 300/300 test", which is the closest construction to ours;
  - S-MIL/STIL with 20 or 16 frames per video;
  - TALL-Swin on all four FF++ manipulations (Tier B);
  - FTCN on 32-frame clips, LipForensics protocol;
  - the DeeperForensics benchmark split 7:1:2 by identity (Jiang et al. Tables 4–5, which mix perturbed and unperturbed settings).

**Appendix J9 (optional).** The Tier-B rows not needed in the text, with full protocol notes.

**Figure 14.** I recommend **no RQ2 figure**.
- The existing `fig1_vs_published.png` plots Tier A, Tier B (including frame-level values), the preliminary study and the RQ3 CNN–LSTM on one axis. That is a visual leaderboard across incomparable protocols.
- If the team wants a figure, it should show only Tier-A video-level ROC-AUC, and there are too few such points (FTCN C23 0.999/0.981; Xception C23 0.939 via FTCN; FTCN DeeperForensics 1.000) to justify one.

## C. Claims allowed and forbidden

**Allowed** (the exact strength shown; numbers verified in D):
1. **Against the preliminary Xception on FF++:** "On FF++ test sets of the same size and split rule, SwinFusion++ reached ROC-AUC 0.9964 (C23) and 0.9941 (C40), against 0.7725 and 0.8109 for the single-seed Xception of the preliminary study, an earlier pipeline with a smaller training budget." The fixed recipe gives 0.9942 and 0.9878.
2. **Celeb-DF:** "Xception's ROC-AUC was 0.6480 on its 859-video Celeb-DF v2 test set; it labeled every video fake, so its 84.17% accuracy equals the fake share." Plus SwinFusion++'s 0.9983 on its own 978-video set, with "different test populations".
3. **DeeperForensics:** "Both ranked videos almost perfectly (0.9978 on a perturbed, 91.61%-fake population; 0.9954 here); no ranking is implied."
4. **Published values: per metric, per condition, Tier A only, and naming the protocol.** Example: "Among the Tier-A video-level accuracies listed for FF++ C23 DeepFakes, the highest is 100.00% (Xception XN-avg under the S-MIL protocol); SwinFusion++ reached 98.21% (fixed recipe 97.86%) on a balanced 280-video test set with a threshold frozen on validation."
5. **The C40 ROC-AUC sentence, if kept:** "SwinFusion++'s C40 ROC-AUC (0.9941; fixed recipe 0.9878) is higher than the C40 ROC-AUC values reported for the RQ2 baselines, all of which come from Tier-B settings (FTCN 0.983, STIL 0.9712, TALL-Swin 0.9457, Xception 0.955 frame-level)." The methodologist must verify these values.

**Forbidden:**
- "Highest C40 ROC-AUC in the record" or "above every published C40 AUC". The package's own literature record has Sabir et al. at 0.9959 (C40, Tier B; RQ3 context), and CAST-B0 reports C23 AUC 1.000 (RQ4 context).
- "Better/worse than model X", "outperforms", "state of the art", "significantly", "leaderboard".
- Any Celeb-DF accuracy comparison that omits prevalence.
- Any accuracy range that mixes tiers or units.
- Calling Xception's Celeb-DF 84.17% or F1 0.9140 "performance".
- Counting a value that appears in two papers as two results.
- "Comparable to the best published results" as a ranking. The allowed wording is "within the range of published values under their own protocols". One example: our C23 AUC 0.9964 lies between FTCN's 0.981 and 0.999.

## D. Verification results

**SwinFusion++ (BO, within datasets).** All exact against the package.

| Test set | ROC-AUC [95% CI] | Acc | Prec | Rec | F1 | FP | FN |
|---|---|---|---|---|---|---|---|
| C23 | 0.9964 [0.9886, 1.0000] | 98.21% | 97.87% | 98.57% | 0.9822 | 3 | 2 |
| C40 | 0.9941 [0.9875, 0.9989] | 96.07% | 93.88% | 98.57% | 0.9617 | 9 | 2 |
| Celeb-DF | 0.9983 [0.9963, 1.0000] | 98.36% | 99.76% | 98.34% | 0.9904 | 2 | 14 |
| DeeperForensics | 0.9954 [0.9874, 1.0000] | 98.51% | 100.00% | 97.01% | 0.9848 | 0 | 6 |

- The fixed recipe equals Table 3.
- The current write-up's §1 table and "no false positives" on DeeperForensics are correct.

**Preliminary Xception.**
- 0.7725/69.64%/0.6886, 0.8109/74.29%/0.7429, 0.6480/84.17%/0.9140 and 0.9978/46.00%/0.5821 match both the CSV and PDF Table 7.
- The test populations come from PDF Table 2: Celeb-DF 136/723 analyzed; DeeperForensics 200/2,185 analyzed of 201/2,211.
- The "1,288 false negatives" figure and the all-fake Celeb-DF behavior are confirmed in the PDF text (§5.4).

**The published ranges in the current write-up, checked against `table2_published_AB.csv`.** The excluded SFormer Table 4 rows were left out.
- Xception XN-avg: C23 98.90–100% and C40 96.78–97.14% are correct. They are secondary copies of S-MIL/STIL; the two C23 values (100% in S-MIL, 98.93% in STIL) disagree for the same nominal model.
- I3D 92.86/91.07/99.23% and STIL 99.6/98.21/99.78%: correct.
- FTCN C23 AUC 0.981–0.999: correct, but 0.998 and the accuracies are Tier B.
- TALL-Swin 98.65%/0.9987 and 92.82%/0.9457: correct, Tier B.
- SFormer 98.5–99.9 and 94.82–98.15: correct.
- **Not verified against the original papers here.** That is the methodologist's task: the package flags that it once had to correct TALL-Swin, STIL, I3D, SFormer and FTCN.

**References.**
- **Present:** Carreira & Zisserman (2017), Chollet (2017), Gu et al. (2021), Haliassos et al. (2021), Jiang et al. (2020), Kingra et al. (2024), Li, Y. et al. (2020; Celeb-DF), Rössler et al. (2019), Xu et al. (2023), Zheng et al. (2021).
- **Missing, if their values are used:**
  - Li, X., Lang, Y., Chen, Y., et al. (2020), S-MIL, ACM MM. This is the original source of the I3D and XN-avg values.
  - Zi et al. (2020), WildDeepfake. It supplies Tier-B clip/frame-level values only, so I suggest not using it.
  - **Custodio et al. (2026)** must be added (user decision 1).
- The methodologist will supply verified APA entries.

## E. Questions for the team

1. **To the methodologist:** can you confirm the Celeb-DF test protocols (official 518-video list? prevalence?) for S-MIL, STIL and I3D? Without them, Celeb-DF accuracies stay uninterpretable across studies (A2).
2. **To the methodologist:** is our DeeperForensics split the official 7:1:2 identity split? Our 96 validation pairs (192 videos) and 201 test pairs (402) suggest 10%/20%. If so, the RQ2 disclosure is narrower: "unperturbed test only, with FF++ originals as the real class". The brief's "not the official protocol" then refers only to the perturbation settings. Please check against Jiang et al. (2020).
3. **To the lead:** keep Table 9 with both configurations, or show only BO and point to Table 3 for the fixed recipe? I prefer both. That is Option A, and it makes the "must hold for both" rule (A7) checkable.
4. **To the lead:** should the FF++ "same split rule" claim for the preliminary Xception be stated as "same size and split rule" (as I propose), since identical video lists cannot be verified from the package?
5. **To both:** do you agree to drop Figure 14 (B)?
