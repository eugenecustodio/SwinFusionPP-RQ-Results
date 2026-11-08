# Common brief: SwinFusion++ thesis, Chapter 4 RQ1 advisory team

## Who and what
- **The thesis.** Undergraduate CS thesis, University of the East–Manila (Philippines), group GRP9: "SwinFusion++: Face-Aligned Spatio-Temporal Swin Transformer for Deepfake Detection".
- **The manuscript** has Chapters 1–3 plus appendices, and no Chapter 4 yet. The panel approved Chapters 1–3 as a proposal, written in future tense.
- **The team** is three strict PhD-level advisors who must AGREE on everything that goes into Chapter 4 RQ1 and into the methodology updates:
  - **Lead advisor:** coordinates, writes the Chapter 4 text and edits the manuscript.
  - **Statistician.**
  - **Evaluation methodologist / thesis examiner.**
- **Your role:** be strict. Flag anything a defense panel would attack. Prefer honest, defensible claims over flattering ones. The standard is PhD-level rigor, scaled to what an undergraduate group can execute and defend.

## Files (READ-ONLY. Do not modify anything outside the team folder.)
- **Manuscript text**, extracted with numbered top-level blocks: `/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/manuscript_text.txt`. Format: `[block] (style) text`; `<TABLE>` marks a table.
  - Chapter 1 starts at block 141.
  - RQs are at blocks 163–168. Scope is at 171–177.
  - Chapter 3 starts at block 317. The evaluation protocol is around 495–522, including the "strong only if" criterion at 521.
  - Statistical Treatment of Data is at blocks 612–626. References start at block 627; Chapter 4 will be inserted just before it.
- **Results package:** `PKG = /home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/`
  - `PKG/corrected_20261028_optionA/` is the CURRENT analysis. Start with its `README.md`. It contains:
    - `RQ1/RQ1_RESULTS_AND_DISCUSSION.md` and `RQ1/results/*`;
    - `RQ6/...`;
    - `paired_tests_optionA.csv` (all 73 paired tests and their Holm families);
    - `calibration/`, `compute/`, `figures/RQ1/*.png`, `figures/RQ6/*.png`, `scripts/`;
    - `CHAPTER4_NOTES.md` (things that must go into Chapter 4).
  - `PKG/00_Shared/statistics_raw/`:
    - `heldout_seed_metrics_rq1_rq6.csv`: per-seed metrics, coverage and failures.
    - `three_seed_mean_logit_ensemble.csv`: ensemble metrics and cluster-bootstrap AUC CIs.
    - `paired_cluster_effects*.csv`.
    - `cluster_bootstrap_intervals.csv`.
    - `source_validation_operating_points_v020.csv`: frozen thresholds and temperatures.
  - `PKG/00_Shared/protocol_and_decisions/`: `autonomous_decisions_v020.md`, `evaluation_protocol_v020.json`, `rq_traceability.yaml`, `presented_model_decision_v020.json`, `tta_predeclaration_v020.json`.
  - `PKG/corrected_20261004/` is the earlier correction. The rank-based permutation fix (Bandos-style) is documented there.
  - `PKG/_originals_before_corrections_20261004/` is the originals. Context only.
- **Raw video-level test predictions** (plain variant, every model and seed): `/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/b2dl/Thesis_Code_final_20261004/results/raw_predictions_v020/<train>_to_<test>/principal_<family>_<train>_<regimen>_s<1|2|3>_v002.video_predictions.parquet`
  - Columns: video_id, label (1 = fake), video_logit, analysis_status, predicted_class, calibrated_probability, model_score_uncalibrated, dependency_cluster, source_group, global_cluster.
  - Families: swin_b, video_swin_b, swinfusionpp, topology_control, capacity_control. Tier-B single-seed ablations: tierb_*.
  - Regimens: fixed_no_bo, dataset_specific_bo.
  - The ensemble is z = mean of the three seed logits, then sigmoid(z / T_ensemble). The threshold is from the operating-points file (kind three_seed_ensemble, run_id NOT ending in `__tta`). `PKG/corrected_20261028_optionA/scripts/calibration.py` shows how to load and self-check these.
- **Python:** `/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/venv/bin/python -I` (pandas, numpy, pyarrow, matplotlib).
  - Put scripts in `/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts/` and outputs in `/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/`.
  - Before reporting any NEW number, first reproduce a stored number (for example an ensemble AUC or a paired ΔAUC CI) to prove your loader is right.

SCRATCH = /tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad

## Decisions already made by the user (do NOT relitigate)
1. **Option A framing.**
   - The fixed-recipe comparison (Swin-B, Video Swin-B and SwinFusion++, all with the same non-BO recipe) is the principal architecture evidence.
   - The BO-selected SwinFusion++ is a separately labeled "configured system" with unequal optimization effort.
   - The optimization effect (BO minus fixed SwinFusion++) is its own family.
   - The required disclosure sentence for Chapter 4 is: "Results are reported according to the analysis plan in Chapter 3. An interim decision to present the BO-selected configuration as primary was reverted to the approved plan; all comparisons under both regimens are reported."
2. **The "strong only if" criterion (block 521) stays as written.** Its verdict text ("Fix 1", in `CHAPTER4_NOTES.md` section 1) is reserved for the RQ6 discussion or Chapter 5, not RQ1, unless the team argues otherwise.
3. **Wording.** Use "statistically indistinguishable / no detectable difference", never "equivalent", unless a valid equivalence analysis is done and justified.
4. **Data.** There is no re-test of C23→DeeperForensics; the package values stand.
5. **Known deviations that must be disclosed:**
   - BO used 12 trials for C23/C40 but only 8 for Celeb-DF and DeeperForensics; Chapter 3 says 12/16/20.
   - The gamma and RandAugment ablations were not run.
   - Gamma correction was disabled in the final pipeline.
   - The Tier-B component ablations are single-seed, BO-regimen, C23-only.

## Rules
- **Every number must be traceable** to a package file or to a script you ran. Never estimate or invent.
- **Write clearly and concisely**, in American spelling. Use the past tense for results.
- **Methodology changes:** Chapter 3 was approved as a pre-specified plan. Any statistic added after the results were seen must be labeled honestly as supplementary or post hoc. It must not be backdated as pre-declared.
- **Do not edit** the .docx, the package, or memory files. Only the lead advisor edits the manuscript.
