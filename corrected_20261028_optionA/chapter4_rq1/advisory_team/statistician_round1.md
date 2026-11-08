# Statistician, Round 1: statistics for RQ1 and the Chapter 3 update

**Loader validated.** `scripts/statistician_validate.py` reproduced the package exactly (tolerance 1e-12):
- all 65 RQ1/RQ6 paired tests: ΔAUC, CI, rank-permutation p and Option A Holm p;
- all 52 ensemble AUC CIs, the per-seed AUCs and the seed mean/SD;
- all 52 ensemble confusion matrices (z ≥ frozen ensemble threshold) and PR-AUCs.

**How the package resamples.** The "class-preserving" bootstrap of A-07 is a **stratified cluster bootstrap**: clusters with no fake video are drawn first, then clusters that contain a fake (seed 20260930, 5,000 draws). The permutation test uses seed 20260931. The cluster column is **`dependency_cluster`**, which is the same partition as `source_group` in every test set; `global_cluster` differs only for DeeperForensics. Every number below is in `stats_out/statistician_*.csv`.

---

## A. Audit findings

**A-1 (HIGH) Celeb-DF rests on 9 identity clusters, not 978 videos.**

| Test set | Videos | Clusters | Structure |
|---|---|---|---|
| FF++ C23 / C40 | 280 | 70 | Source pairs of 4 videos (2 real, 2 fake). C23 and C40 share the same 70 clusters. |
| DeeperForensics | 402 | 201 | Real–fake pairs |
| Celeb-DF | 978 | 54 | 45 clusters are single real videos. All 843 fakes sit in 9 identity clusters (33–197 fakes each, plus 90 reals). |

Every Celeb-DF-target result (within-CDF, C23→CDF, DFo→CDF) therefore has 9 independent units for the fake class.
- **Bootstrap SEs are too small on Celeb-DF.** The delete-one-cluster jackknife SE is 0.99–1.32× the bootstrap SE there (mean 1.15); on the other test sets the ratio is 0.84–1.05. The Celeb-DF intervals are probably about 10–30% too narrow.
- **The permutation p-values are still exact.**
- **No architecture conclusion changes.** The only significant Celeb-DF-target architecture result is DFo→CDF vs Swin-B. It stays between +0.112 and +0.148 whichever identity cluster is removed.
- **Required in the text:** never present 978 as the effective n, and attach this caveat to the "cleanest evidence" claim.

**A-2 (HIGH; must be disclosed) Two changes were made after test scoring.**
1. **The rank-based permutation test replaced the pre-declared raw-logit test.**
   - *Why it was needed:* the raw swap violated exchangeability because the models' logit scales differ.
   - *It is direction-neutral:* in the 26 fixed-recipe architecture tests it removed one SwinFusion++ win (within-DFo vs Video Swin-B, p_Holm 0.0016 → 1.00) and added two (CDF→C23 and DFo→CDF vs Swin-B).
   - *Overall,* 10 of 65 conclusions changed (`statistician_rank_correction_impact.csv`). That direction-neutrality is the defense.
2. **The Option A Holm families were set after scoring,** while block 615 says families will be "declared before test labels are examined". The mitigation is that the **same 10 of 26** architecture tests are significant under Option A (8/18), under the pre-scoring partition (A-16; 12/27), and in one pooled family of 26 (C-4).

**A-3 (MEDIUM) Threshold metrics have no uncertainty attached, and two write-up statements are wrong.**
- **"Accuracy differs by only a few videos" (within-dataset).** On Celeb-DF, SwinFusion++ and Swin-B differ by 23 videos, and the paired interval excludes 0.
- **"Collapse for every model" (transfer).** This hides a model-specific pattern. From C23, SwinFusion++'s frozen threshold was the most conservative, and its accuracy was lower than both encoders on C23→C40 and C23→CDF, with paired intervals excluding 0 (C-2), even where AUC was tied.

**A-4 (MEDIUM) "Never significantly worse" is not non-inferiority.** Among the non-significant comparisons, the CI lower bounds reach:
- −0.028 and −0.030 on C23→CDF;
- −0.041 on C23→DFo vs VSB;
- −0.032 on CDF→C23 vs VSB;
- **−0.092 on DFo→CDF vs VSB.**

Also, "every interval overlaps" (per-model CIs) is not a valid test; only the paired CI counts.

**A-5 (MEDIUM) The within-dataset tests could not show superiority, by design.** For the 8 tests:
- the minimum detectable ΔAUC (80% power, two-sided α = 0.05/8) is 0.0030–0.0123;
- the largest possible gain (1 − baseline AUC) is 0.0034–0.0117;
- the detectable difference exceeds that headroom in **7 of 8** tests.

So "no detectable difference" is neither evidence of equality nor evidence against SwinFusion++.

**A-6 (LOW–MEDIUM) DeeperForensics resampling level.**
- **What the plan implies.** Block 615 says broader groups are used "when they subsume multiple related sources". `global_cluster` does this: it merges 26 of the 201 DFo pairs through shared FF++ lineage, leaving 175 clusters.
- **Re-run result.** Re-running all 15 DFo-target tests at that level changed no Holm conclusion in any family. CI bounds moved by ≤ 0.0025 and raw p by ≤ 0.035.
- **Recommendation.** Disclose this as a sensitivity analysis; do not switch the primary analysis after scoring.

**A-7 (LOW) Validity checks pass.**
- **Resampling units.** Correct (the problem in A-1 is the count, not the unit).
- **Permutation test.**
  - It is a valid paired test: within-model ranks are swapped together for every video in a cluster, with the +1 correction, two-sided on |Δ|.
  - Its null is exchangeability, which is slightly stronger than equal AUC (Bandos' design).
  - The minimum raw p is 1/5001, so the Holm floor is 0.0036 when m = 18. 8 of the 10 significant architecture results sit at that floor; report them as "< 0.005".
  - The Monte Carlo SE of each raw p is ≤ 0.007, and no decision is near a boundary.
- **Holm.** Valid under any dependence. Families that follow the claims (within vs transfer; architecture vs configured system vs optimization effect) are defensible.
- **p = 1.00.** Plausible. The raw p-values in RQ1_architecture run from 0.198 to 0.925, and 8 × 0.198 > 1, so step-down caps every value at 1.00. Print the raw p next to it.

**A-8 (LOW) CI and test disagree in four places, none in the architecture families.**
- **Where:** three Celeb-DF configured-system/optimization tests (explained by A-1) and BO−fixed within C23 (lower bound +0.00005).
- **Why:** the CIs are unadjusted. This is also why DFo→C23 vs VSB has CI [+0.008, +0.082] but p_Holm = 0.15.
- **Fix:** table notes must say the intervals are unadjusted and that Holm decides.

**A-9 (LOW) Scope of inference.**
- The inference is conditional on the trained ensembles. It generalizes to new test videos, not to retraining.
- With 3 seeds, the true SD could be anywhere from 0.5× to 6.3× the observed SD (95% CI). "Seed stability is comparable" must become a description, not a finding.

**A-10 (LOW) Housekeeping.** Never report the unused `bootstrap_two_sided_p` column (it would be a second test). The reference list has no statistics references; see D-3.

---

## B. Analysis set for RQ1

**B-1 IN, pre-declared and inferential.**
- Ensemble ROC-AUC with a stratified cluster-bootstrap CI.
- Paired ΔAUC with its CI.
- Rank-based permutation p, with Holm within the six Option A families.
- Both the raw p and p_Holm.

**B-2 IN, pre-declared and descriptive (blocks 519 and 614).**
- Accuracy, precision, recall, specificity, F1, FPR, FNR and confusion matrices.
- **PR-AUC.** Pre-declared in 614 but missing from most RQ1 tables. Always show it with the prevalence baseline. For example, DFo→CDF Swin-B has PR-AUC 0.841 against a prevalence of 0.862, with ROC-AUC 0.459.
- Per-seed AUC mean ± SD and range.
- The strict overlap-free subsets promised in block 176 (n = 60 for C23→DFo; n = 20 for DFo→FF++), per seed, with no tests.

**B-3 IN, supplementary (post hoc, labeled as such, no p-values, no Holm).**
1. **Paired ΔAccuracy, ΔPrecision, ΔRecall and ΔF1 CIs** for the 26 fixed-recipe comparisons.
   - RQ1 asks "to what extent ... improve", which is a difference, so these are paired Δ, not per-model CIs.
   - Main text discusses accuracy and F1; the full table goes in an appendix.
   - Mark precision "not estimable" where a model flagged too few videos (0–6 in several CDF- and DFo-source directions).
   - Under transfer, read these as operating-point transfer, not discrimination.
2. **Minimum detectable difference vs headroom,** plus a CI-bound reading. The intervals exclude SwinFusion++ advantages larger than +0.0002 to +0.0085 and disadvantages larger than −0.0005 to −0.0101.
3. **Cross-seed sign agreement,** to answer "is it one lucky seed?"
4. **Dependence robustness:** the Holm partitions, DFo at `global_cluster`, and Celeb-DF leave-one-identity-out.
5. **Mean transfer AUC,** reported descriptively with a joint-bootstrap interval. It must be shown with:
   - the caveats: unweighted; directions share sources and test sets; it summarizes this grid, not a population of domains; not pre-declared; never used for the H0 decision;
   - the per-direction pattern alongside it, because the FF++-source directions are tied.

**B-4 OUT.**
- **McNemar.** The Chapter 3 condition fails: clusters hold 2, 4 or 1–207 videos. The paired cluster ΔAccuracy CI replaces it.
- **Equivalence, TOST or non-inferiority.** Any margin would be chosen post hoc. Use CI bounds and the "no detectable difference" wording instead.
- **Observed-effect post hoc power.** It adds nothing to the p-value; the minimum detectable difference uses only the SE.
- **Formal tests on threshold metrics or PR-AUC.** They were not declared, they would add more than 100 tests, and the metrics are confounded by where the threshold falls.
- **DeLong.** It ignores the clustering, and running a second test invites cherry-picking.
- **Target-fitted ("oracle") thresholds, even as diagnostics.** The protocol forbids them.
- **Seed-level tests** (n = 3).
- **Balanced accuracy and MCC.** Not declared.

---

## C. New computations (`scripts/statistician_*.py` → `stats_out/`)

**C-1 Validation.** See the top of this memo. The threshold-metric loop reuses the package's bootstrap draws, and its ΔAUC CIs again matched all 65 tests.

**C-2 Threshold-metric Δ, fixed recipe** (SwinFusion++ minus baseline; `statistician_threshold_metrics.csv`).

*Within dataset.* In 6 of 8 comparisons every interval includes 0 and |ΔAcc| ≤ 0.011. Two favor SwinFusion++. In both, the ranking difference is not significant, so the gain is a matter of where the threshold falls.

| Comparison | ΔAccuracy | ΔRecall | ΔF1 |
|---|---|---|---|
| Celeb-DF vs Swin-B (9-cluster caveat) | +0.024 [+0.001, +0.051] | +0.031 [+0.006, +0.060] | +0.014 [+0.001, +0.032] |
| DFo vs Video Swin-B | +0.017 [+0.005, +0.032] | +0.030 [+0.005, +0.060] | +0.018 [+0.005, +0.034] |

*Transfer.* ΔAccuracy intervals that exclude 0:

| Direction | vs Swin-B | vs Video Swin-B |
|---|---|---|
| **Lower for SwinFusion++** | | |
| C23→C40 | −0.032 [−0.061, −0.004] | −0.032 [−0.054, −0.011] |
| C23→CDF | −0.081 [−0.135, −0.018] | −0.071 [−0.132, −0.012] |
| C23→DFo | — | −0.065 [−0.087, −0.042] |
| CDF→C23 | — | −0.071 [−0.104, −0.043] |
| **Higher for SwinFusion++** | | |
| CDF→C23 | +0.032 [+0.011, +0.057] | — |
| CDF→DFo | +0.017 [+0.005, +0.032] | — |

From the CDF and DFo sources, every model flagged at most 60 videos as fake (recall 0–0.42). Accuracy there mainly reflects the share of real videos.

**C-3 Within-dataset sensitivity** (`statistician_within_sensitivity.csv`).

| Quantity | Range over the 8 tests |
|---|---|
| SE of ΔAUC | 0.0008–0.0034 |
| Minimum detectable ΔAUC, α = 0.05 | 0.0024–0.0096 |
| Minimum detectable ΔAUC, α = 0.05/8 | 0.0030–0.0123 |
| Headroom (1 − baseline AUC) | 0.0034–0.0117 |

The detectable difference exceeds the headroom in 7 of 8 tests. The exception is C23 vs VSB (0.0030 vs 0.0049).

**C-4 Holm partitions** (`statistician_holm_partitions.csv`).
- The same 10 of 26 tests are significant under all three partitions.
- The largest pooled p_Holm among them is 0.034 (CDF→C23 vs Swin-B).
- DFo→C23 vs VSB is never significant (p_Holm 0.152 / 0.209 / 0.304).

**C-5 to C-6** are covered under A-6 and A-1 (`statistician_dfo_global_cluster.csv`, `statistician_cdf_loo_identity.csv`, `statistician_jackknife_vs_bootstrap.csv`).

**C-7 Seed robustness** (`statistician_seed_robustness.csv`).
- 9 of the 10 significant architecture differences have the same sign in all 9 cross-seed pairings. CDF→C40 vs VSB agrees in 8/9 (minimum −0.0067). No significant claim depends on ensembling.
- Within-DFo vs VSB agrees in 9/9 yet is not significant. The limit within datasets is test-set sampling, not seed noise.

**C-8 Mean transfer AUC over 9 directions** (`statistician_mean_transfer.csv`). Joint bootstrap, seed 20261030; FF++ targets share one draw of their clusters. It ignores the 25 FF++ pairs that are also in the DFo test lineage.

| Model or difference | Mean transfer AUC [95% CI] |
|---|---|
| SwinFusion++ (fixed recipe) | 0.810 [0.796, 0.825] |
| Video Swin-B | 0.785 [0.769, 0.801] |
| Swin-B | 0.700 [0.685, 0.717] |
| BO-selected SwinFusion++ | 0.762 [0.747, 0.778] |
| Δ fixed SF++ − VSB | +0.025 [+0.011, +0.040] |
| Δ fixed SF++ − Swin-B | +0.110 [+0.095, +0.125] |
| Δ BO − fixed SF++ | −0.048 [−0.059, −0.036] |

---

## D. Methodology text (Chapter 3, Statistical Treatment)

**Tense.** Blocks 612–617 stay in future tense as the approved plan. Do not edit "Formal comparison families will be declared before test labels are examined" or the McNemar sentence. The one amendment paragraph (D-2) is **past tense on purpose**, so nothing added after scoring reads as pre-declared.

**D-1 (block 615; a specification, not a change).** The cluster-level stratified draws and the 5,000 permutations were fixed before scoring (A-07). "Percentile" and "two-sided" describe the code as it was run.

Replace: "Paired model differences will use paired cluster bootstrap or a predeclared cluster-level permutation test."

With: "Resampling will be stratified so that clusters containing at least one fake video and clusters containing only real videos are drawn separately, and intervals will be 95% percentile intervals. Paired ROC-AUC differences will be estimated with a paired cluster bootstrap that applies each draw to both models and will be tested with a two-sided cluster-level permutation test of 5,000 permutations that exchanges the two models' scores for all videos in a cluster together."

**D-2 (insert a new paragraph after block 615).**

"**Amendments after test scoring.** The following changes were made after the held-out test results were known. None altered a model, checkpoint, threshold, temperature, or test set, and every analysis is reported regardless of its outcome. First, the predeclared permutation test exchanged raw ensemble logits between models whose logit scales differed, which violates the exchangeability that the test requires. It was replaced by the rank-based form of Bandos et al. (2005), in which each model's video scores are converted to within-model ranks before the exchange. ROC-AUC differences and bootstrap intervals were unchanged, and the correction changed conclusions in both directions (Chapter 4). Second, the Holm families were finalized as six families: the fixed-recipe architecture comparisons within datasets (m = 8) and under frozen transfer (m = 18); the configured-system comparisons of BO-selected SwinFusion++ with the fixed-recipe Swin-B and Video Swin-B within datasets (m = 8) and under transfer (m = 18); and the optimization effect, BO-selected minus fixed-recipe SwinFusion++, within datasets (m = 4) and under transfer (m = 9). The partition recorded before scoring and a single pooled family of all 26 architecture comparisons gave identical architecture conclusions. Third, supplementary analyses without p-values or multiplicity adjustment were added: paired cluster-bootstrap intervals for differences in accuracy, precision, recall, and F1-score at the frozen thresholds; the smallest within-dataset ROC-AUC difference detectable with 80% power; the sign agreement of each ensemble difference across the nine cross-seed pairings; an unweighted mean transfer ROC-AUC over the nine directions with a joint cluster-bootstrap interval; and re-analyses with the broader lineage clusters for DeeperForensics-1.0 (175 instead of 201) and with each Celeb-DF v2 identity cluster removed in turn. These analyses describe the size and robustness of effects and were not used to decide any hypothesis. McNemar's test was not reported because no test set met the condition of one independent decision per cluster."

**D-3 (References, APA).** Add:
- Bandos, A. I., Rockette, H. E., & Gur, D. (2005). A permutation test sensitive to differences in areas for comparing ROC curves from a paired design. *Statistics in Medicine, 24*(18), 2873–2893. https://doi.org/10.1002/sim.2149 *(lead: verify the DOI)*
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70.

**D-4 (Chapter 4 table note, for the lead).** "Intervals are 95% percentile intervals from 5,000 stratified cluster-bootstrap draws and are not adjusted for multiplicity. p_Holm is from the rank-based cluster permutation test (5,000 permutations); '< 0.005' marks the smallest attainable value. FF++ C23 and C40: 280 videos in 70 source-pair clusters; Celeb-DF v2: 978 videos in 54 clusters, with all 843 fake videos in 9 identity clusters; DeeperForensics-1.0: 402 videos in 201 source-pair clusters."

---

## E. Positions and questions for the team

**E-1 (to the methodologist).** The 18 fixed-recipe transfer tests against the encoders are **RQ1 evidence**, because RQ1 names cross-dataset evaluation. Present them under RQ1 as the "frozen-transfer architecture family (m = 18)", and have RQ6 cross-reference them. Do you agree to rename `RQ6_architecture` in the Chapter 4 text?

**E-2 (to the lead). No equivalence wording.**
- Within datasets: "no detectable difference; the intervals exclude differences larger than about 0.01 AUC".
- "Never significantly worse" must carry its widest lower bound (−0.092, DFo→CDF vs VSB).

**E-3 (to both). The answer to RQ1 must include the operating-point result (C-2).** Proposed sentence: "Under frozen thresholds, SwinFusion++'s ranking advantage did not translate into higher accuracy. From FF++ C23, its accuracy was lower than both encoders on C40 and Celeb-DF and lower than Video Swin-B on DeeperForensics."

**E-4 (to the lead). Mandatory disclosure sentence on the rank correction,** next to the Option A disclosure: "The correction removed one within-dataset advantage of SwinFusion++ (over Video Swin-B on DeeperForensics) and added two transfer advantages over Swin-B."

**E-5 (to both). The Celeb-DF 9-cluster caveat** goes in the dataset description and in every Celeb-DF table note. Question to the methodologist: was the Celeb-DF split closed under both the source and the target identity of each fake? The clusters are keyed by target identity, and the video IDs are hashed, so I cannot check.

**E-6 (to the methodologist). Table layout.**
- **Main tables:** AUC [CI], PR-AUC with prevalence, the threshold metrics, seed mean ± SD, Δ [CI], raw p and p_Holm.
- **Appendix:** the threshold-Δ table and the per-seed tables.
- **No bold "best" marks** in the within-dataset tables.

**E-7 (to both).** Should the mean-transfer interval (C-8) be reported as supplementary? I say yes, with the B-3.5 caveats. Option A already quotes 0.810, so it cannot be left unqualified.

**E-8 (to the lead). Where does D-2 go?**
- Chapter 3 (my preference): past tense, labeled.
- Or the start of Chapter 4, with a pointer from Chapter 3.

**E-9 (to the methodologist). Phrases to drop from the RQ1 write-up:**
- "accuracy differs by only a few videos";
- "every interval overlaps";
- "seed stability is comparable";
- "temporal evidence appears to be what transfers" (an untested causal gloss).
