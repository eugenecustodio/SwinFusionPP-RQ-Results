# Statistician, Round 1: consistency of Chapters 1–3 with the results

**Scope.** Every quantitative or statistical statement in blocks 141–626, plus the amendments paragraph and Chapter 4's methods text.

**Checks.**
- Every OLD string below is a verified verbatim substring of its block in `CH1_TO_CH3_blocks.txt`.
- PKG = `SwinFusionPP_RQ_Results/`.

**Lead's items.**
- **Covered here:** 3, 8, 10, 11, 15 and 18, plus 5, 6 and 7, where they fall in the statistical blocks.
- **Methodologist's area, noted in E only:** 1, 9, 12, 13 and 16.

---

## A. MUST edits

**A1. Block 520: transfer sources (lead item 5).**
- **OLD:** `The second is cross-dataset transfer evaluation, in which a model trained on one dataset is tested on the remaining datasets to assess robustness under distribution shift.`
- **NEW:** `The second is cross-dataset transfer evaluation, in which a model trained on FaceForensics++ C23, Celeb-DF v2, or DeeperForensics-1.0 is tested on each of the remaining datasets to assess robustness under distribution shift.`
- **Reason:** Chapter 4 reports 9 directions; C40 is never a source (Figure 11 shows "—").
- **Evidence:** `PKG/00_Shared/statistics_raw/three_seed_mean_logit_ensemble.csv`, whose sources are ffpp_c23, celeb_df_v2 and deeperforensics_1_0 only; A-07 ("core set is 9 directions").

**A2. Block 614: perturbation conditions (lead item 6).**
- **OLD:** `For every dataset construction, compression or perturbation condition, optimization regime,`
- **NEW:** `For every dataset construction, compression condition, optimization regime,`
- **Reason:** no perturbation stratum was scored; only the 402-video unperturbed DeeperForensics-1.0 test set.
- **Evidence:** `evaluation_protocol_v020.json` (the robustness row of 2,010 videos was never scored); the heldout CSV contains test_dataset values for the 4 conditions only.

**A3. Block 504: BO trial count (lead item 3).**
- **OLD:** `A resource pilot will select the final total from 12, 16, or 20 trials per study using measured GPU-hour and storage limits, never test performance.`
- **NEW:** `The total will be 12 trials per study for C23/HQ and C40/LQ and 8 for Celeb-DF v2 and DeeperForensics-1.0, including pruned trials, set from measured GPU-hour limits and the project schedule before any test scoring, never from test performance.`
- **Evidence:**
  - `00_Shared/bayesian_optimisation/bo_summary.csv`: trials 12/12/8/8; completed 8/8/5/8; pruned 4/4/3/0.
  - A-12, dated 2026-09-30, records "about 96 h" of measured remaining GPU time and the trial cut.
  - A-16 confirms that no test scoring had happened by 2026-10-02.

**A4. Block 174: the same fact in Chapter 1.**
- **OLD:** `Before the full BO campaigns, a resource pilot will determine whether the predeclared total trial count is 12, 16, or 20 per study; the choice will be based on measured compute and storage rather than test performance.`
- **NEW:** `The total trial count will be 12 per study for C23/HQ and C40/LQ and 8 for Celeb-DF v2 and DeeperForensics-1.0, set from measured compute time and the project schedule rather than test performance.`
- **Evidence:** as A3.

**A5. Block 617: compute measures (lead item 8).** This edit applies unless the group decides to measure latency (D3).
- **OLD:** `Computational analysis will state total and trainable parameters, operations per clip, peak inference and training memory where feasible, preprocessing latency, clip inference latency, complete video latency, throughput, and checkpoint size under the declared hardware and software environment.`
- **NEW:** `Computational analysis will state total parameters, operations per clip and per video, peak training memory, training throughput, and checkpoint size under the declared hardware and software environment.`
- **Reason:** `PKG/corrected_20261028_optionA/compute/COMPUTE_COST.md` contains exactly the items in NEW. It lists three things as not measured:
  - steady-state inference latency;
  - preprocessing latency;
  - whole-video latency and deployment throughput.

  Trainable-parameter counts and inference memory are not reported either. The cold single-clip times include start-up overhead and are not a latency figure.

**A6. Block 498: hardware (lead item 7; overlaps with the methodologist).**
- **OLD:** `BF16 mixed precision on a supported H100 or A100, with the exact scaler behavior recorded;`
- **NEW:** `BF16 mixed precision on an NVIDIA RTX 5090, with the exact scaler behavior recorded;`
- **Evidence:** A-08 (the project GPU is an RTX 5090, sm_120); COMPUTE_COST.md ("measured on an NVIDIA RTX 5090 in bf16"); CHAPTER4_NOTES §4.

## B. SHOULD edits

**B1. Block 325: BO trial count.**
- **OLD:** `A capped resource pilot will estimate the cost of the four independent Optuna/TPE studies; the final per-study trial count will be fixed before full BO.`
- **NEW:** `A capped resource pilot will estimate the cost of the four independent Optuna/TPE studies; the per-study trial counts will be fixed from measured cost before any test scoring.`
- **Reason:** the Celeb-DF v2 and DeeperForensics-1.0 counts were cut while the Celeb-DF search was running (A-10 and A-12, 2026-09-30). That was "before test scoring", but not "before full BO".

**B2. Block 184: BO trial count (Chapter 1 limitations).**
- **OLD:** `The final BO trial count is therefore selected only after a cost pilot and may limit lower-priority ablations or optional external reproductions`
- **NEW:** `The final BO trial count is therefore set from measured compute cost and may limit lower-priority ablations or optional external reproductions`
- **Evidence:** A-12.

**B3. Block 313: bootstrap vs test (past tense, as the block is written).**
- **OLD:** `At least 5,000 cluster-bootstrap replicates were used to construct the principal 95% confidence intervals and paired statistical comparisons.`
- **NEW:** `At least 5,000 cluster-bootstrap replicates were used to construct the principal 95% confidence intervals, including those for paired differences, and paired differences were tested with a cluster-level permutation test.`
- **Reason:** decisions come from the rank-based permutation test (amendments paragraph; Chapter 4 "Two rules" paragraph), not from the bootstrap.

**B4. Block 614: per-seed reporting.** The alternative is D8.
- **OLD:** `Each seed will be evaluated independently, and per-seed metrics plus mean and standard deviation will be reported.`
- **NEW:** `Each seed will be evaluated independently, and per-seed ROC-AUC plus mean and standard deviation will be reported.`
- **Reason:** Table J1 tabulates per-seed ROC-AUC only. Its note says the other per-seed metrics were computed but are not tabulated.

**B5. Block 617: ECE binning.**
- **OLD:** `ECE with the declared binning method`
- **NEW:** `ECE with 15 equal-width bins`
- **Reason:** the binning is never stated in Chapters 1–3. The package used 15 equal-width bins ("the binning declared in the preliminary study").
- **Evidence:** `PKG/corrected_20261028_optionA/calibration/CALIBRATION.md` (Method).

**B6. Chapter 3 amendments paragraph (lead item 18).**
- **OLD:** `Second, the comparisons were regrouped after scoring into six Holm families:`
- **NEW:** `Second, the RQ1 and RQ6 comparisons were regrouped after scoring into six Holm families, while the RQ4 control families were unchanged:`
- **Reason:** Chapter 4 Table 2 lists 8 families, the 6 above plus the 2 control families, which are "Unchanged since before scoring". Without this edit, "six" reads as the total.
- **Block 615 itself is consistent with Chapter 4** ("Holm … default … RQ1 standalone comparisons, control comparisons, multiple datasets or targets"). Chapter 4 adds no Holm family outside these, and its threshold metrics carry no tests, so no edit is needed there.

**B7. Block 193: what calibration supports.**
- **OLD:** `Consequential use requires provenance checks, contextual verification, or specialist forensic examination.`
- **NEW:** `The validation-calibrated estimated probability is fitted on source-validation videos, so its calibration is not guaranteed for videos from unfamiliar sources. Consequential use requires provenance checks, contextual verification, or specialist forensic examination.`
- **Evidence:** CALIBRATION.md.
  - ECE is 0.009–0.036 within datasets.
  - Median ECE under transfer is 0.446.
  - In 35 of 42 transfer cells, the Brier score is worse than predicting the fake prevalence.
- **Purpose:** this keeps blocks 177 and 316 truthful whatever the app shows.

**B8. Block 625: the expert dimensions omit one survey section.**
- **OLD:** `error prevention/recovery, interpretability, consistency, transparency/help, and context`
- **NEW:** `error prevention/recovery, language/microcopy clarity, interpretability, consistency, transparency/help, and context`
- **Evidence:** the List of Figures, blocks 127–128. Expert survey Figure 49 includes "Language/Microcopy Clarity".

**B9. Block 401: sample size versus sampling design (RQ5 internal consistency).**
- **Problem:** Cochran's margin of error assumes random sampling, but blocks 407–413 use quota and purposive sampling.
- **OLD:** `Hence, the researchers will distribute approximately 150 survey forms to obtain at least 120 usable and complete responses.`
- **NEW:** `Hence, the researchers will distribute approximately 150 survey forms to obtain at least 120 usable and complete responses. Because respondents are recruited through quota and purposive sampling rather than random selection, this figure serves as a precision target for the overall mean rather than a probability-sampling margin of error.`

**B10. Blocks 326 and 367: "robustness" (overlaps with the methodologist).** Only compression robustness was assessed: within C40, and C23 → C40.
- **Block 326:**
  - **OLD:** `They will compute clustered uncertainty, paired effects, calibration, efficiency, failure, shortcut, and robustness analyses`
  - **NEW:** `They will compute clustered uncertainty, paired effects, calibration, efficiency, failure, shortcut, and cross-compression analyses`
- **Block 367:** apply the same change to "calibration, failures, and robustness separately" (OLD `and robustness separately` → NEW `and cross-compression results separately`).

**B11. Block 453: resolution strata (overlaps with the methodologist).**
- **OLD:** `This stratification supports standardized reporting and provides an interpretable basis for communicating expected performance behaviors under varying input quality conditions (also reflected in system design and user guidance).`
- **NEW:** `This stratification supports standardized metadata reporting and user guidance (also reflected in system design).`
- **Reason:** no performance is reported by resolution stratum, and the prediction files carry no resolution field, so this cannot be added.

## C. VERIFY items

**C1. Blocks 441 and 563: FaceNet distance (lead item 10).**
- **What the package says:** only CHAPTER4_NOTES §6 mentions the metric: "FaceNet uses cosine distance (Chapter 3 says Euclidean)". That comes from the web-app code review. No training-pipeline preprocessing config is in the package or the scratch copy of the code (models only).
- **If training used cosine:**
  - Block 441: OLD `FaceNet-style 512-D embeddings are computed and compared with Euclidean distance` → NEW `FaceNet-style 512-D embeddings are computed and compared with cosine distance`.
  - Block 563: OLD `FaceNet identifies consistency via 512-D embeddings and Euclidean distance.` → NEW `FaceNet identifies consistency via 512-D embeddings and cosine distance.`
- **Source needed:** the preprocessing config in the backup (e.g. the threshold-set file behind block 269's "universal primary threshold set").

**C2. Block 564: undersampling and the 70-15-15 split.**
- **OLD:** `Sampling and partitioning (random majority undersampling; 70-15-15 split; cross-dataset transfer evaluation).`
- **Proposed NEW:** `Sampling and partitioning (class → source or identity group → video → clip training selection; official group-safe split where compatible, otherwise a 70-15-15 group allocation; cross-dataset transfer evaluation).`
- **What to verify:**
  - *The sampler.* Blocks 404 and 458 declare the hierarchical sampler, and block 313 says validation and test were not undersampled. "Random majority undersampling" contradicts these, but the package does not show the training sampler.
  - *The split.* The package shows validation/test counts of 280/280 (FF++), 977/978 (Celeb-DF v2) and 192/402 (DeeperForensics-1.0) (`source_validation_operating_points_v020.csv`, n_validation_videos; Table 1). Unequal DeeperForensics validation and test counts cannot come from a 70/15/15 allocation, so an official split was probably used there. The "official where compatible" wording is true either way and matches blocks 404 and 520.
- **Overlap:** the methodologist owns lead item 13. The same wording in block 248 is fine, and Figure 1 is covered under D4.

**C3. Block 404: realized split counts.**
- **OLD:** `The final report will state the target counts, realized counts, realized percentages, class prevalence, and any unavoidable deviation caused by indivisible groups.`
- **The gap:** Chapter 4 Table 1 gives test counts and prevalence only. The package has validation counts (see C2) but no training counts.
- **Options:**
  - Take the train, validation and test counts from the split manifest in the backup and add them to Table 1.
  - Or narrow the sentence: NEW `The final report will state the test counts and class prevalence for every condition.`

**C4. Blocks 499–502: fixed-recipe values (R15; already flagged to the user).**
- **Block 499's effective batch size of 16:** unverifiable from the package. All BO winners used 8 (`bo_summary.csv`).
- **Blocks 500–502:** the learning rates, weight decay, epochs and patience are also unverified.
- **Action:** no edit until the training config is checked.

## D. USER DECISION items

**D1. Hypothesis (blocks 250–252; lead item 15).**
- **The problem:** H0/H1 name "existing CNN- or transformer-based spatio-temporal models" but no metric or test. Formally:
  - the only matched paired tests are against Video Swin-B (an existing transformer-based spatio-temporal model) and Swin-B, on ROC-AUC with Holm;
  - published models cannot be tested (block 616).
- **Recommendation (no Chapter 3 change):** RQ6 states the decision explicitly in Fix 2's terms (block 521):
  - H0 is evaluated on video-level ROC-AUC with the Holm-adjusted paired tests;
  - rejected for frozen transfer against Video Swin-B in 3 of 9 directions (and Swin-B in 7 of 9);
  - not rejected within datasets;
  - no decision against published models.
- **Alternative:** add a dated operationalization sentence to the amendments paragraph. That would be another post-scoring amendment, so the user must choose.

**D2. RQ6 statement (block 168).** "Compared to existing CNN- and transformer-based spatio-temporal models" can be answered inferentially only against the internal encoders, and descriptively against literature values. The RQ is unchanged; RQ6's text must say this.

**D3. Latency.** Either measure preprocessing, clip and whole-video latency and throughput on the deployment server (CHAPTER4_NOTES §5), or apply A5.

**D4. Figure 1 (image).** It shows:
- "Gamma correction on dark frames";
- "Handling class imbalance (undersampling)";
- "70–15–15 train-test split";
- "Robustness Testing: Performance under noise, compression, and adversarial variations". Noise and adversarial tests were not run.

The group should redraw it. The same applies to the gamma and "confidence score" text in Figures 2 and 3 (methodologist).

**D5. Expert sample size.** Chapters 1–3 never state how many experts will be recruited (blocks 373, 413, 428). The group should state the target n.

**D6. Platform vs evaluation protocol (rule 6).**
- **Clip sampling:** the app's main result samples every frame, and its 3-clip "second check" differs from the evaluated 7 clips at 2 fps (CHAPTER4_NOTES §6; evaluation_protocol_v020.json). Lead item 11: no Chapter 1–3 text states a clip count; block 457 leaves Keval to the configuration, so the text is consistent.
- **Displayed score:** "NN% sure" conflicts with block 316 ("The term confidence score will not be used").
- **Decision needed:** app or text.

**D7. Figure 7 (image).** 1.96² × 0.833² / 0.15² = 118.47, but the image shows ≈ 118.57, which is the value for s = 5/6 unrounded. Both round up to 119. Optional to redraw.

**D8. Alternative to B4.** Add the per-seed accuracy, precision, recall, specificity and F1 table to Appendix J. The data exist in `heldout_seed_metrics_rq1_rq6.csv` (plain, full_test).

## E. Notes for the other advisors

1. **Checked and consistent; no edit needed:**
   - block 433: the metadata-audit stop rule. AUC ≥ 0.65 was crossed (0.67/0.68), the D-43 response followed, and Chapter 4 reports it;
   - blocks 176 and 404: the strict lineage-free subset (n = 60, Table J3);
   - blocks 302 and 458: video logit = mean of the clip logits;
   - block 304/492: temperature fitted on source validation;
   - blocks 615 and 616: CI method, separate directions, and no literature values in tests;
   - block 433, together with Chapter 4: failure counts (0);
   - block 521 Fix 2;
   - RQ5 sample size: n0 = 118.57 → 119 → 120 (60/60 strata, matching block 588) → 150 forms at 80%; 15 user items over 4 characteristics (blocks 557, 578, 589, 619); 34 expert items (blocks 559, 582, 596).
2. **Block 615, "highest verified dependency-cluster level".** For DeeperForensics-1.0, the 175 FF++-lineage clusters are broader than the 201 pairs used. The amendments paragraph reports the 175-cluster re-analysis (no decision changed). I recommend no edit, but the lead should be ready for the question.
3. **Block 615 excludes single-seed ablations from significance claims.** RQ4 must therefore not print Tier-B Holm p-values as decisions (`tier_b_paired_effects.csv` contains them).
4. **For RQ6:** the package's RQ6 "Hypothesis decision" rejects H0 against CNN baselines using the preliminary-study test (a different pipeline and test population; registry LITERATURE_ONLY/NOT_REPORTED). Do not carry that into Chapter 4. See D1.
5. **For the methodologist (overlaps I saw):**
   - block 248, block 563 and Figure 1: undersampling and gamma (lead items 1 and 13);
   - block 188: "stratified reporting reduce…", but D-43 stratified results were not produced (item 16);
   - block 309: "documented in the appendix", which needs a check that such an appendix exists;
   - block 316's "Scan Failed / Analysis Could Not Be Completed" vs blocks 177 and 335's "Insufficient Evidence" (terminology);
   - blocks 269 and 444: the gamma ablation promise;
   - block 455: the RandAugment ablation promise.
