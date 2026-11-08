# Autonomous decisions (v020)

The user delegated every remaining decision on 2026-09-30:

> "Independently work your way up to the Last Phase, For every decision, I want you to decide which is best direction for this please."

The authorization record is `configs/experiments/autonomous_execution_authorization_v020.json`. Each entry below states the options considered, the choice made, and the reason. Entries are appended over time and never rewritten.

## A-01 (2026-09-30): D-24, freeze of the selected configurations

**Choice:** freeze each of the four independently audited v002 study winners exactly as exported to `configs/training/bo_selected_v020/`.
- Every final run starts from the original official pretrained weights, not from a trial checkpoint.
- Seed slots are 260901, 260902 and 260903, with at most 30 epochs.

**Reason:** this is the plan's prescribed rule. Every winner already passed an independent recomputation of its scores and an exact clean-process replay. Differences between the studies' hyperparameters are not interpreted as findings about the datasets.

## A-02 (2026-09-30): D-25, RQ1 fairness and optimization regimen

**Choice:**
- The primary RQ1 evidence is the comparison of Swin-B, Video Swin-B and SwinFusion++ under the identical fixed recipe, on all four datasets with three seeds.
- The secondary evidence is the search-selected SwinFusion++, labelled as configured-system performance with unequal optimization effort.
- A paired comparison of search-selected against fixed SwinFusion++ is required on every dataset.

**Reason:** the plan recommends this option (plan.md, D-25). It keeps the causal architecture claim separate from the comparison of optimized systems.

## A-03 (2026-09-30): topology and capacity controls on every dataset

**Options considered:** run the controls only on C23, as named in plan Phases 89–91; or run them on all four datasets, as protocol v002 reserved.

**Choice:** run them on all four datasets. Mechanism claims about the architecture then hold for every dataset rather than only C23.

**Cost and scheduling:** about 20 extra GPU-hours. The non-C23 control runs are scheduled last within Phases 89–91, so they don't delay the core results.

## A-04 (2026-09-30): staged held-out evaluation

**Options considered:** evaluate every model on the test sets together at Phases 160–181; or evaluate each group of models once its training and threshold freeze are complete.

**Choice:** evaluate in stages. Each RQ can then be written as early as its evidence allows: RQ1 and RQ6 right after Phase 91, RQ2 after 118, RQ3 after 126, and RQ4 after 159.

**Safeguards:**
- Thresholds and calibration for each group are frozen from source validation only, before any test access.
- Test results are never used to re-tune anything.
- The later M7 phases reuse the frozen results.

## A-05 (2026-09-30): code placement while the Bayesian search is running

**Choice:** put new orchestration code only in `scripts/`, using explicit runtime adapters (the same pattern as retention), and leave `src/swinfusionpp` unchanged while the Phase 44–46 searches run.

**Reason:** the searches record checksums of the source files for each run. Editing `src/` would stop a trial from resuming after any restart.

## A-06 (2026-09-30): unattended execution of Phases 47–91

**Choice:** the supervisor service `thesis_phases47_91_v020` starts automatically after the Phase 43–46 searches finish, and runs:
- Phase 47: the D-24 freeze;
- Phase 48: the D-25 freeze;
- Phase 49: the 72-run ledger and the remote next-step drill;
- all 72 principal runs, core runs first and non-C23 controls last.

**Safeguards:**
- A watchdog (`thesis_m5_watchdog`) restarts the service after resumable failures.
- On completion, local weights are released only after each run's best checkpoint is verified in B2. They are restored from B2 for evaluation.
- Principal remote checkpoints have their own 300 GB ceiling.

**Reason:** GPU time is otherwise idle between the end of the searches and any manual start, and the user asked for unattended progress.

## A-07 (2026-09-30): staged RQ1/RQ6 evaluation design

**Evaluation service:** `thesis_rq1_rq6_eval_v020` (`scripts/rq1_rq6_early_v020.py`) starts when M5_COMPLETE exists, and is guarded by `thesis_eval_watchdog`.

**Operating points (registry v020a):**
- One per principal checkpoint.
- One per three-seed mean-logit ensemble, fitted on the mean source-validation logits.
- Both use the D-11 and D-12 rules only.

**Inference and scoring:**
- Inference seals the clip logits with no labels present in the process.
- A separate step then aggregates the frozen mean of seven clips per video and applies the source operating point unchanged.

**Transfer:**
- The core set is 9 directions, with sources C23, Celeb-DF and DeeperForensics and all other targets.
- Models are the RQ1 families: Swin-B, Video Swin-B, and fixed and search-selected SwinFusion++, each with 3 seeds.
- The C40-source extension (Phase 180) and the external baselines are added later.

**Overlap:**
- The primary result for each direction is the full target test set, reported with the v020 disclosure.
- A secondary strict overlap-free subset is also reported: target test videos whose global lineage never appears in the source's train or validation split.
- Measured subset sizes: C23→C40 280/280, C23→Celeb-DF 978/978, C23→DeeperForensics 60/402, DeeperForensics→C23 20/280, DeeperForensics→C40 20/280, DeeperForensics→Celeb-DF 978/978, and Celeb-DF→every target all.

**Statistics (D-40, D-19):**
- The primary paired comparisons use three-seed ensembles; per-seed intervals are also reported.
- Resampling uses 5,000 class-preserving dependency-cluster draws, with a fixed seed of 20260930.
- Cluster permutation tests use 5,000 permutations.
- Holm correction is applied separately within the RQ1 family (within-dataset) and the RQ6 family (transfer).

**Reason:** these are the plan's Phase 160, 164–179 and 183 rules, applied early to the finished principal models. Nothing is refitted later.

## A-08 (2026-09-30): M6 model set and decisions D-15, D-16, D-17, D-18, D-26, plus a D-21 amendment

**Basis:** a read-only audit of public code, licenses and weights, with URLs recorded in the session. Key facts:
- DeepfakeBench is CC BY-NC and pinned to torch 1.12, which cannot run on the RTX 5090 (sm_120).
- Its FTCN config actually builds VideoMAE.
- It publishes no trained checkpoints for any video detector.
- STIL (TFace) is Apache-2.0; TALL4Deepfake is MIT; FTCN has no license and ships inference code only.
- SFormer, CAST and ISTVT have no usable official code, and the TSFF-Net repository returns 404.
- The shared cache is 2 fps with per-frame alignment.

**D-16 (RQ2 core, one seed per model and dataset):**
- Xception (timm/Cadene ImageNet weights).
- STIL, ported from TFace (Apache-2.0).
- Inception-I3D (piergiaj port with Kinetics RGB weights), because the thesis cites Carreira & Zisserman.
- TALL-Swin (official MIT code, Swin-B IN-22k weights).
- FTCN with Temporal Transformer as a *conditional* core model. It uses a ported definition with a predeclared initialization. If the overfit or validation gates fail, it is marked BLOCKED with evidence and reported from the literature only.
- A model is labelled "reproduced" only after passing its Phase 94–98 gates.

**D-26:** DeepfakeBench is a pinned reference and a source of model definitions only, with licenses preserved and attribution given. Its data pipeline, splits, trainer and metrics are not used. CC BY-NC and unlicensed code stay out of any release.

**D-21 amendment:** add a native-rate anchor-window face cache for models that need consecutive frames (I3D, TALL-Swin, FTCN, SFormer, and the optical-flow CNN-LSTM). It has:
- consecutive native-rate frames at the same 7 normalized anchors, plus seeded training windows;
- the same detector and identity tracking as the shared cache;
- one similarity transform shared across each window (from median landmarks);
- JPEG storage, as a declared deviation.

Xception, STIL and CAST use the existing 2 fps cache.

**D-17 / D-28 (SFormer):** a transparent PyTorch reimplementation (Swin-T IN-1k, one temporal encoder block, pruning schedule) with two separate tracks:
- 4 common-protocol runs with native 20-frame windows;
- 1 paper-faithful FF++ DeepFakes source run.

All SFormer results are labelled "partial replication", and the unknown details are fixed and recorded before any training.

**D-15 (RQ3, C23 and C40):**
- Model A: Chen et al. 2022, attention plus ConvLSTM on an Xception backbone, ported from the Apache-2.0 Keras code.
- Model B: a Saikia-style optical-flow CNN-LSTM (Farneback flow with HSV encoding, VGG16), reimplemented transparently.
- Fallbacks, in order: Kuang 2022, then Liang 2023. Sabir 2019 is not used, because it is a GRU rather than an LSTM.

**D-18 (RQ4):**
- CAST: transparent reimplementation from arXiv v2 on all four datasets. It closely matches our input format and directly tests cross-attention.
- TSFF-Net: the official route is BLOCKED (the repository returns 404). Its status is LITERATURE_ONLY for C23 and C40, cross-dataset literature only for Celeb-DF, and N/A for DeeperForensics. A reimplementation happens only if time remains after the core.

**D-31:** ISTVT and other recent models are literature-only.

**Order:**
1. Harness.
2. Xception.
3. STIL.
4. CAST.
5. Native-rate cache.
6. I3D.
7. TALL-Swin.
8. SFormer.
9. Chen.
10. Saikia.
11. FTCN (last, because it is the highest risk).
12. TSFF-Net, if time allows.

GPU costs are to be measured with smoke tests before the budget is revised; the current 150–350 GPU-hour figure is unverified.

## A-09 (2026-09-30): maximum parallel use of CPU and GPU

**Instruction:** the user asked to use all GPU and CPU cores and to run in parallel any phases whose prerequisites are complete.

**Decisions:**

1. **Run by the plan's actual dependency graph, not milestone order.** Phases 92, 93, 119, 127, 139, 140 and 142 depend only on Phases 1–6 and 39, which have passed. Phases 94–98 depend on 92–93. Phase 99 onwards depends on a READY adapter plus Phase 93. M6 therefore runs alongside M4 and M5.

2. **Local space released: 66.7 GB.** Every file was verified by SHA-256 against the v019 restore manifest and is recoverable from B2. No v020 code path reads these files locally. Receipt: `reports/audit/local_release_legacy_v020.json`.
   - `checkpoints/hpo` (legacy v001 local weights);
   - `checkpoints/tests`;
   - `artifacts/preprocessing/recovery_stage_cache` (non-production coverage development).

3. **Native-rate cache built on spare CPU cores** (niced, 20 workers) while the GPU runs the search. The load average was about 2 on 32 cores beforehand.

4. **Native-window anchor rule.** The frozen rule `start = round(loc*(N-W))` is applied over the audited face-track span (the first to last recipe frame), matching the shared anchors, which are placed over valid clips. Whole-video placement put windows where no face is tracked (3 of 40 pilot videos). Pilot result on 200 videos: 200 ok, and every window has recipe landmarks inside it.

5. **Sharing the GPU.** External-model jobs may share the GPU with the search or principal training under two limits:
   - a per-process GPU memory cap, so the primary job can never run out of memory;
   - a lower CPU priority.

   Scientific results are unaffected, because every process is deterministic. Wall-clock costs measured under sharing are labelled as shared.

## A-10 (2026-09-30): user scope change to SwinFusion++, Swin-B and Video Swin-B only

**The user's instruction:** "remove any other model than SwinFusion++, Video Swin and Swin Transformer … I have existing results … I will forward you the paper (preliminary study) … we will not train any other models. Let us just focus on SwinFusion++."

The full message is recorded in `configs/experiments/scope_swinfusionpp_only_v020.json`.

**Effect on phases:**
- **Kept:** all SwinFusion++, Swin-B and Video Swin-B work.
  - The final training runs, including the topology and capacity controls (these are SwinFusion++ variants).
  - The Tier B ablations (Phases 153–159).
  - M7 evaluation of these models.
  - Phase 152, which will freeze the preliminary-study evidence.
- **Skipped (SKIPPED_APPROVED):**
  - External adapters and training: Phases 95–151.
  - External-model evaluation phases: 162, 163, 165, 166, 168, 170 and 181.
- **History:** Phases 92–94 remain PASSED as history, with their scope superseded.
- **Services and caches:**
  - The external-model training service, its watchdog, and the native-rate cache service are removed.
  - Their derived caches are deleted: a 19 GB native-window cache and an 8.9 GB disk pool.
- **Reporting:** results for external models will come from the user's preliminary-study paper. They are reported as preliminary or literature evidence, with their own units and protocols, and never mixed with this project's matched video-level results. D-15 to D-18 are superseded.

**Incident, same day:** running the native cache (20 workers) and the external pool build (12 workers) alongside the Celeb-DF search ran out of RAM. The 27 GB Celeb-DF pool lives in RAM-backed `/dev/shm`. The OOM killer sent SIGKILL to the search at 09:25. Supervisor restarted it, and it resumed trial 1 from its epoch-2 checkpoint, so about one epoch was lost and no data was lost.

**Lesson recorded:** concurrent jobs must budget RAM, including `/dev/shm` pools, and not only CPU cores or GPU memory.
- **A-10 addendum (the user):** results for the non-trained models come from each model's **official paper**, with the user's preliminary-study paper as a further source.

  **Recorded for every row:**
  - the exact dataset or version, manipulation subset, compression and protocol;
  - the metric and its unit (frame, clip or video);
  - the table or page reference.

  **Reporting:** a "published results" table kept separate from our matched results.

  **Record:** `configs/experiments/scope_swinfusionpp_only_v020_addendum01.json`.

## A-11 (2026-09-30): Tier B ablations (Phases 153–159)

**Variants:** six variants, each an exact change to the full model with identical parameters and state-dict keys. They are implemented in `scripts/tier_b_v020.py` and tested in `tests/models/test_tier_b_definitions_v020.py`.
1. `one_directional` (S←V only).
2. `no_gate`: the 16 tanh gates replaced by 1.0.
3. `no_agreement`: the |X−Y| and X⊙Y branches replaced by same-shape zeros.
4. `stages_34_only`: stages 1–2 bypassed.
5. `gamma_on`: D-08 clip-level I^(1/2).
6. `randaugment_off`.

**Gamma trigger:** the 25th percentile of BT.709 clip-mean luminance over FF++ C23 *training* clips, computed by `scripts/tier_b_gamma_trigger_v020.py` into `results/statistics/tier_b_gamma_trigger_v020.json`.
- **Reason:** D-08 requires a trigger chosen from C23 train/validation evidence and versioned before activation. FF++ has few genuinely dark clips, so an absolute threshold would likely never fire and the ablation would be vacuous.
- **Scope:** gamma applies to both training and validation clips, so preprocessing differs only in this single declared factor.

**Training:**
- FF++ C23 only, with the search-selected C23 training parameters (Phase 47 frozen registry).
- Seed 260901, labelled `exploratory_single_seed`.
- The same engine and recipe as the principal runs.

**Scheduling:** service `thesis_tier_b_v020` (guarded by `thesis_tierb_watchdog`) starts after M5_COMPLETE and once Phase 153 has passed. It may overlap with the RQ1/RQ6 evaluation, which is inference only and within the RAM and GPU budgets.

## A-12 (2026-09-30): four-day deadline

**The user's instruction:** "I only have 4 days Max to complete and make all the RQs ready to be written." The deadline is 2026-10-04 14:00 UTC.

**Remaining measured GPU time:** about 96 h, broken down as:
- Celeb-DF search: about 17 h (roughly 7 min per epoch);
- DeeperForensics search: about 6 h;
- 72 principal runs: about 77 h;
- evaluation and Tier B: about 12 h.

**Cuts made:**
- **Search trials:** Celeb-DF and DeeperForensics use 8 trials each, including the pilot; C23 and C40 keep 12. That is 4 TPE startup trials plus 3–4 guided ones. This unequal search effort is disclosed.
- **Controls:** A-03 is withdrawn. Topology and capacity controls run on C23 only, as in plan Phases 89–91, which leaves 54 principal runs.
- **Tier B:** only the four architectural variants run (Phases 154–157). Phases 158 (gamma) and 159 (RandAugment) are skipped.

**Kept:** the whole RQ1 core. That is three seeds each of Swin-B, Video Swin-B, and fixed and search-selected SwinFusion++, on all four datasets, plus the full RQ1/RQ6 evaluation, statistics and transfer grid.

**Expected result:** everything complete around Saturday night, with about 16 h of buffer.

**Record:** `configs/experiments/deadline_decision_v020.json`.

## A-13 (2026-09-30): making SwinFusion++ as strong as legitimately possible

The user asked for improvements to SwinFusion++ within the 4-day limit and without cheating.

**Decision:** no architecture or training changes, because they would invalidate the finished searches and the deadline, and any post-hoc change after seeing test results would be test tuning.

**Pre-declared, inference-only improvements:**
- horizontal-flip TTA, validated on source validation first and reported as a labelled variant beside the plain result;
- the three-seed mean-logit ensemble (already in the protocol).

**Record:** `configs/experiments/tta_predeclaration_v020.json`.

## A-14 — Tier B held-out C23 evaluation (2026-10-01)

- **Decision:** add `scripts/tier_b_heldout_v020.py` (service `thesis_tier_b_heldout_v020`, watchdog profile `tierbheld`) so the four Tier B model ablations get a held-out FF++ C23 result for RQ4; previously they had source-validation results only.
- **Method:** each variant's own source-validation operating point (D-11/D-12), frozen in `results/metrics/tier_b_operating_points_v020.parquet` before scoring; sealed label-free inference with the principal anchors; paired cluster-bootstrap ΔAUC and cluster permutation test against the full SwinFusion++ with the same seed (260901, BO C23 seed slot 1); Holm within the Tier B family.
- **Evidence level:** exploratory single seed, descriptive; no thresholds, models or choices are adjusted after test scoring.
- **Ordering:** starts after TIER_B_COMPLETE and RQ1_RQ6_EARLY_COMPLETE so it never competes for the GPU or test pools.

## A-15 — Chapter 4 writing packages (2026-10-01)

- **Decision:** `scripts/rq_packages_v020.py` builds `reports/chapter4/rq_packages_v020/` (RQ1, RQ2, RQ3, RQ4, RQ6, methods_bo); service `thesis_rq_packages_v020` rebuilds after RQ1_RQ6_EARLY_COMPLETE and after TIER_B_HELDOUT_COMPLETE.
- **Rules:** reads frozen outputs only (no refitting/re-thresholding); published results are normalised to our four conditions with comparability tiers (A closest protocol, B same data but unit/subset differs, C other data), shown as context with no statistical tests against them; the dataset named first in a published row's description decides its condition.
- **RQ5** (usability study) is out of scope for this build.

## A-16 — Presented model is BO-selected SwinFusion++ (user decision, 2026-10-02 ~19:00 PHT)

- **Decision (user):** "WHAT WE WILL BE PRESENTING IS THE SWINFUSION++ BAYESIAN OPTIMIZED, THAT IS THE SWINFUSION++." Supersedes D-25's primary claim. Record: `configs/experiments/presented_model_decision_v020.json`.
- **Made before any held-out test inference or scoring** (evaluation service still waiting for M5_COMPLETE).
- **Primary families:** RQ1 (within) and RQ6 (transfer) = SwinFusion++ (BO) vs Swin-B (fixed) and vs Video Swin-B (fixed), Holm within each.
- **Secondary / supplementary:** recipe-matched SwinFusion++ (fixed) vs baselines and BO vs fixed (RQ1_secondary, RQ6_secondary); RQ4_controls = SwinFusion++ (fixed) vs topology/capacity controls (recipe-matched ablation). Each is its own Holm family, so none dilutes the primary claim.
- **Kept:** fixed-recipe SwinFusion++ runs (Phases 86–88) — required for the recipe-matched RQ4 control comparison.
- **Disclosure:** SwinFusion++ training parameters were BO-selected on source validation; baselines use the shared fixed recipe.

## A-17 — Preliminary study added (Phase 152 addendum, 2026-10-02)

- **Source:** user-provided preliminary paper, stored at `references/preliminary/SwinFusionPP_UERJ_Revised.pdf`; extracted to `results/literature/preliminary_study_v020.csv` (132 rows; receipt `.json` binds the PDF hash).
- **Use:** Xception (4 conditions) → RQ2; CNN-LSTM (C23/C40) and the preliminary C40 paired result → RQ3; earlier SwinFusion++/Swin-B/Video Swin-B ensembles → RQ1 context; frozen C23 transfer → RQ6 context; frozen-feature fusion heads → RQ4 context.
- **Comparability:** earlier pipeline (MTCNN cache, 3 anchors, fixed recipe, no search); FF++ test size matches, Celeb-DF/DeeperForensics test populations differ. Reported as context with a distinct marker; no paired tests against v020 runs. I3D/SFormer remain published-only (blocked in the preliminary study).

## A-18 — Controls also evaluated under frozen C23 → other-dataset transfer (2026-10-03 ~15:30 PHT)

- **Decision:** the C23-trained topology and capacity controls get the same frozen transfer evaluation as SwinFusion++ (C23 → C40, Celeb-DF, DeeperForensics), inference only; paired SwinFusion++ (fixed) − control effects in a separate Holm family `RQ4_controls_transfer`.
- **Why:** C23 within-dataset is at ceiling and insensitive to a mechanism difference; transfer adds multi-dataset evidence for RQ4 at ~30–45 min GPU cost, no extra training.
- **Made before any held-out test inference** (no `results/raw_predictions_v020` existed). Source operating points unchanged; no target-label fitting.
