# Methodologist R1: consistency review of Chapters 1–3 against the results

**Scope.**
- Chapter 1 (blocks 141–202).
- Chapter 2 (blocks 203–316).
- The non-statistical parts of Chapter 3: software framework, flowchart description, research design, data, preprocessing, models, controls, ablations, baselines, platform, instruments and data gathering.
- Figures 1–3, which I viewed.

**How the edits were checked.** Every OLD string below was machine-checked as a verbatim substring of its block (`team/scripts/m_ch123_build.py`). Architecture statements were checked against the backup model code (`src/swinfusionpp/models/*.py`) and are correct as written: tanh gates, LayerNorm with mean+max pooling, the (2,1,1) depthwise adapter, d = 64/128/256/256 with 32-dim heads, 7 × 7 windows, the 0.10/0.30 dropouts, and the 1024→512→1 head. The sampler and augmentation were checked against the BO-selected configs (`sampler: class_group_video_clip`, `randaugment_v001`).

**Edit conventions.**
- No deviation framing anywhere.
- Tense is kept: Chapter 1 and Chapter 3 future or neutral present; blocks 307–313 (Chapter 2) past.
- "[delete paragraph]" means remove the whole paragraph, including its paragraph mark.

**Lead's list, covered here:** items 1, 2, 3 (174, 184, 325), 4, 6 (173), 9, 10, 11, 12, 13, 14, 16 and 17 (no edit needed).
**Left to the statistician:** items 5, 7, 8, 15 and 18; see E.

## A. MUST edits

**M-1. Block 148.**

- **OLD:** «The study will also use topology and capacity-matched controls, two CNN–LSTM comparators on FaceForensics++ C23/C40, a verified established-baseline core, component ablations,»
- **NEW:** «The study will also use topology and capacity-matched controls, published results for CNN–LSTM comparators on FaceForensics++ C23/C40 and for established baselines, component ablations,»
- **Reason:** No external model was reproduced in this study; "verified established-baseline core" and "two CNN–LSTM comparators" describe runs that do not exist. (Wording for the preliminary-study option: D-1.)
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications)

**M-2. Block 173.**

- **OLD:** «provisionally the unperturbed manipulated subset when the observed distribution supports that label; perturbation variants will otherwise remain separately identified robustness strata.»
- **NEW:** «and perturbation variants will remain separately identified and will not be used in the reported evaluations.»
- **Reason:** Perturbation strata were never scored; only the 402-video primary test set was.
- **Evidence:** evaluation_protocol_v020.json (robustness role, 2,010 videos); heldout_seed_metrics_rq1_rq6.csv (DFo test = 402 videos only)

**M-3. Block 173.**

- **OLD:** «Exact file identifiers, counts, lineage keys, and exclusions will be reported only after the filesystem and manifest audit.»
- **NEW:** «Exact file identifiers, lineage keys, and exclusions are fixed in versioned manifests; test-set counts, lineage overlap, and coverage are reported in Chapter 4.»
- **Reason:** Identifiers and full counts are not reported anywhere; Chapter 4 Table 1 reports test counts, lineage overlap, and coverage.
- **Evidence:** evaluation_protocol_v020.json ("full_frozen_split_manifest_v001"); Chapter 4 Table 1

**M-4. Block 174.**

- **OLD:** «Before the full BO campaigns, a resource pilot will determine whether the predeclared total trial count is 12, 16, or 20 per study; the choice will be based on measured compute and storage rather than test performance.»
- **NEW:** «The total trial count per study is set from measured compute time rather than test performance: 12 trials for C23/HQ and C40/LQ and 8 for Celeb-DF v2 and DeeperForensics-1.0.»
- **Reason:** Actual counts were 12/12/8/8, set from measured GPU time on 30 September 2026 (8 is not in {12, 16, 20}). Same wording as 184 and 325; statistician aligns 504.
- **Evidence:** 00_Shared/bayesian_optimisation/bo_summary.md (12, 12, 8, 8 trials; 8, 8, 5, 8 completed); autonomous_decisions_v020.md A-12

**M-5. Block 175.**

- **OLD:** «The contribution of TLBG-HCA will be examined through both a topology non-attentive control and a capacity-matched no-exchange control, together with one-directional, no-gate, no-agreement/disagreement, Stages-3–4-only, gamma-policy, and augmentation- policy ablations.»
- **NEW:** «Under RQ4, the contribution of TLBG-HCA will be examined through both a topology non-attentive control and a capacity-matched no-exchange control trained on C23/HQ, together with single-seed one-directional, no-gate, no-agreement/disagreement, and Stages-3–4-only ablations of the BO-selected C23/HQ configuration.»
- **Reason:** The gamma-policy and augmentation-policy ablations were not run; the controls are C23-only; the ablations are single-seed on the BO-selected C23 configuration; Chapter 4 places all of them under RQ4.
- **Evidence:** A-11, A-12, A-14, A-18; Chapter 4 RQ1 pointer sentence to RQ4

**M-6. Block 175.**

- **OLD:** «RQ4 will address CAST and TSFF-Net per dataset without mischaracterizing their inputs.»
- **NEW:** «RQ4 will also place CAST and TSFF-Net in context through their published results, without mischaracterizing their inputs.»
- **Reason:** CAST and TSFF-Net were not run. Their published values exist only for C23 (CAST) and C23 → Celeb-DF (both), not "per dataset".
- **Evidence:** A-10; corrected_20261028_optionA/RQ4/RQ4_RESULTS_AND_DISCUSSION.md §3

**M-7. Block 175.**

- **OLD:** «RQ6 will synthesize these within-dataset results with directional frozen transfer and the two SFormer replication tracks.»
- **NEW:** «RQ6 will synthesize these within-dataset results with directional frozen transfer and published spatio-temporal results.»
- **Reason:** The SFormer replication tracks (D-17/D-28) were superseded and not run.
- **Evidence:** A-10 ("D-15 to D-18 are superseded"); RQ6 write-up (published values only)

**M-8. Block 184.**

- **OLD:** «Four Base-sized within-dataset campaigns, four Bayesian- optimization studies, multiple controls, external baselines, and transfer tests require substantial accelerator time and storage. The final BO trial count is therefore selected only after a cost pilot and may limit lower-priority ablations or optional external reproductions»
- **NEW:** «Four Base-sized within-dataset campaigns, four Bayesian-optimization studies, multiple controls, and transfer tests require substantial accelerator time and storage. The available accelerator time therefore limits the BO trial count (12 trials for C23/HQ and C40/LQ; 8 for Celeb-DF v2 and DeeperForensics-1.0) and restricts the matched controls and component ablations to C23/HQ training.»
- **Reason:** States the actual limits without deviation framing. Removes external baselines and reproductions, which were never part of the run.
- **Evidence:** 00_Shared/bayesian_optimisation/bo_summary.md (12, 12, 8, 8 trials; 8, 8, 5, 8 completed); autonomous_decisions_v020.md A-12; A-12 (controls and Tier B cut to C23)

**M-9. Block 188.**

- **OLD:** «Lineage matching, common decoding/cropping, metadata-only shortcut tests, and stratified reporting reduce»
- **NEW:** «Lineage matching, common decoding/cropping, and metadata-only shortcut tests reduce»
- **Reason:** Metadata-stratified reporting (D-43) was not produced.
- **Evidence:** CHAPTER4_NOTES.md §4

**M-10. Block 190.**

- **OLD:** «External-baseline reproducibility. Some published methods may lack official code, weights, complete preprocessing details, compatible licenses, or the inputs needed by the common protocol. Such models will be labeled literature-only, not reported, or blocked rather than silently approximated.»
- **NEW:** «External baselines. The study trains only Swin-B, Video Swin-B, SwinFusion++, and the SwinFusion++ controls and ablations. Results for external methods are taken from their publications, keep their original datasets, protocols, and evaluation units, and are not entered into paired tests.»
- **Reason:** The limitation as written implies that reproduction was attempted. In fact no external model was trained (a scope decision). (Wording for the preliminary-study option: D-1.)
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications); block 616

**M-11. Block 198.**

- **OLD:** «(label + confidence + metadata)»
- **NEW:** «(screening label, model score or calibrated estimated probability, and metadata)»
- **Reason:** Block 316 states that the term "confidence score" will not be used.
- **Evidence:** block 316

**M-12. Block 210.**

- **OLD:** «Within this architectural direction, cross-attention is meaningful only when the participating representations are indexed compatible. Video transformers commonly convert a clip into temporally indexed tokens through frame-wise patch embedding or tubelet embedding. In Video Swin Transformer, the initial embedding reduces the temporal length, after which regular and shifted local 3D self-attention repeatedly transform each temporal position. A deep temporal token therefore remains indexed to an initial tubelet position but contains context gathered from neighboring space-time regions. For cross-stream fusion, frame-wise spatial features and tubelet-indexed temporal features should consequently be aligned at the level of temporal indices without assuming that every deep Video Swin tokens remains an isolated summary of exactly its original two frames (Arnab et al., 2021; Liu et al., 2022).»
- **NEW:** «[delete paragraph]»
- **Reason:** Near-verbatim duplicate of block 214; 210 also has the typos "indexed compatible" and "Video Swin tokens".
- **Evidence:** blocks 210 vs 214

**M-13. Block 211.**

- **OLD:** «Temporal alignment alone does not determine how the streams should exchange evidence. Global cross-attention at early high-resolution stages would create large attention matrices and would permit unrelated facial regions to interact directly. Local matched-window attention offers a more controlled alternative: approximately co-located spatial and temporal regions interact first, while the shifted-window backbones provide broader contextual propagation across layers. Bidirectional cross-attention further allows appearance evidence to retrieve motion evidence and motion evidence to retrieve appearance evidence, which is relevant when either stream may contain the stronger manipulation cue. CrossVIT and CAST provide precedents for learned interaction between complementary representations, although their stream definitions and fusion topology differ from the proposed configuration (Chen et al., 2021; Thakre et al., 2026).»
- **NEW:** «[delete paragraph]»
- **Reason:** Duplicate of block 215 ("CrossVIT" vs "CrossViT").
- **Evidence:** blocks 211 vs 215

**M-14. Block 212.**

- **OLD:** «A newly initialized fusion block can also disturb pretrained representations when its residual contribution is introduced at full strength from the first optimization step. Residual-scaling approaches such as ReZero and LayerScale motivate initializing the new path near an identity mapping and learning its contribution progressively. In SwinFusion++, zero-initialized trainable gates serve this role for the cross-attention and feed-forward residual paths: the projected backbone features are preserved at initialization, while the optimizer learns whether and how strongly cross-stream transformations should contribute (Bachlechner et al., 2021; Touvron et al., 2021).»
- **NEW:** «[delete paragraph]»
- **Reason:** Duplicate of block 216, which is the more specific version (16 gates).
- **Evidence:** blocks 212 vs 216

**M-15. Block 213.**

- **OLD:** «These architectural choices must be evaluated through controls that isolate the proposed mechanism. Deepfake comparisons are sensitive to preprocessing, data partitioning, clip aggregation, threshold selection, and implementation details; scores copied from studies that used different protocols cannot by themselves establish the value of a new fusion block. Standardized benchmark work therefore supports matched internal baselines, source-video-disjoint partitioning, one prediction per video, and explicit separation of reproduced experiments from literature-only results. In deployment, the sigmoid of a neural-network logit should likewise be treated as an uncalibrated model score unless validation-based calibration has been fitted and evaluated (Guo et al., 2017; Yan et al ., 2023).»
- **NEW:** «[delete paragraph]»
- **Reason:** Duplicate of block 218 (same argument and same citations).
- **Evidence:** blocks 213 vs 218

**M-16. Block 235.**

- **OLD:** «outputs a Real or Fake label with confidence must communicate uncertainty»
- **NEW:** «outputs a Real or Fake label with a model score or calibrated estimated probability must communicate uncertainty»
- **Reason:** Term rule in block 316.
- **Evidence:** block 316

**M-17. Block 246.**

- **OLD:** «(MTCNN for face detection/alignment, FaceNet for face verification, and gamma correction for illumination normalization).»
- **NEW:** «(MTCNN for face detection/alignment and FaceNet for face verification).»
- **Reason:** Gamma is disabled in the final pipeline.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-18. Block 248.**

- **OLD:** «where facial evidence is standardized via alignment, dark-frame correction, identity verification, and data augmentation using RandomAugment—operationalized as controlled randomized transformations (e.g., shift/rotate/noise) applied in a manner that preserves clip integrity—together with class-imbalance handling through undersampling;»
- **NEW:** «where facial evidence is standardized via alignment and identity verification, with training-only RandAugment augmentation—operationalized as controlled randomized transformations applied in a manner that preserves clip integrity—and class-balanced training sampling (class → source or identity group → video → clip);»
- **Reason:** There is no dark-frame correction. "RandomAugment" should be RandAugment (block 455). The sampler is class → group → video → clip, not undersampling (blocks 313 and 458). The unverified example operations are removed.
- **Evidence:** 00_Shared/bayesian_optimisation/swinfusionpp_*.yaml ("sampler: class_group_video_clip", "augmentation: configs/data/randaugment_v001.yaml"); blocks 313, 404, 458; CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-19. Block 249.**

- **OLD:** «benchmarking against established models, and conducting robustness checks under stressors such as compression, perturbation, resolution, and preprocessing conditions—thereby ensuring that conclusions about effectiveness are grounded not only in in-dataset accuracy but also in demonstrated robustness under distribution shift.»
- **NEW:** «comparing against published results of established models, and examining performance under compression (FaceForensics++ C23/HQ versus C40/LQ) and cross-dataset shift—so that conclusions about effectiveness rest not only on in-dataset accuracy but also on performance under distribution shift.»
- **Reason:** No perturbation, resolution, or preprocessing stressor analysis exists. "Demonstrated robustness" also overclaims, given Chapter 4 (transfer accuracy is about 50%).
- **Evidence:** Chapter 4 (C23/C40 and transfer only); no stressor results in the package

**M-20. Block 269.**

- **OLD:** «Any low-light transformation is decided at the clip level and is evaluated as an ablation.»
- **NEW:** «The final pipeline applies no low-light transformation.»
- **Reason:** Gamma is disabled and its ablation was not run.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma); A-12

**M-21. Block 309.**

- **OLD:** «are documented in the appendix»
- **NEW:** «are recorded in the versioned dataset manifest»
- **Reason:** No appendix documents file identifiers, counts, or exclusion criteria.
- **Evidence:** Appendices A–J (none contain dataset manifests); evaluation_protocol_v020.json

**M-22. Block 325.**

- **OLD:** «A capped resource pilot will estimate the cost of the four independent Optuna/TPE studies; the final per-study trial count will be fixed before full BO.»
- **NEW:** «The per-study trial count of the four independent Optuna/TPE studies will be set from measured compute time (12 trials for C23/HQ and C40/LQ; 8 for Celeb-DF v2 and DeeperForensics-1.0).»
- **Reason:** The 8-trial counts for Celeb-DF v2 and DeeperForensics-1.0 were set on 30 September while the Celeb-DF study was already running, so "fixed before full BO" is not true.
- **Evidence:** 00_Shared/bayesian_optimisation/bo_summary.md (12, 12, 8, 8 trials; 8, 8, 5, 8 completed); autonomous_decisions_v020.md A-12

**M-23. Block 325.**

- **OLD:** «The external-baseline stage will verify and, where feasible, reproduce Xception, I3D, STIL, FTCN with Temporal Transformer, TALL-Swin, SFormer, two CNN–LSTM models, and the conditionally reproducible CAST and TSFF-Net comparisons.»
- **NEW:** «External baselines (Xception, I3D, STIL, FTCN with Temporal Transformer, TALL-Swin, SFormer, CNN–LSTM models, CAST, and TSFF-Net) will not be retrained; their published results will be recorded with their datasets, protocols, and evaluation units.»
- **Reason:** No external model was reproduced.
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications)

**M-24. Block 326.**

- **OLD:** «calibration, efficiency, failure, shortcut, and robustness analyses»
- **NEW:** «calibration, efficiency, failure, and shortcut analyses»
- **Reason:** No robustness (perturbation) analysis exists. Transfer is already covered by "each approved source-to-target transfer direction".
- **Evidence:** package (no perturbation results)

**M-25. Block 334.**

- **OLD:** «applies gamma correction to dark frames when needed, »
- **NEW:** «»
- **Reason:** Neither the training pipeline nor the deployed app applies gamma.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-26. Block 336.**

- **OLD:** «The output layer will translate the computed prediction into user-readable results. The system will present a classification result, a confidence or probability score, and contextual video metadata such as filename, resolution, frame rate, duration, file size, and format. These outputs are designed as decision-support information rather than standalone forensic proof. »
- **NEW:** «»
- **Reason:** This duplicates the output-layer description at the end of block 335 and uses the banned term "confidence". The last sentence (help and transparency content) is kept.
- **Evidence:** blocks 335, 316

**M-27. Block 367.**

- **OLD:** «The fixed-recipe RQ1 runs will precede the BO cost pilot and four independent Optuna/TPE studies.»
- **NEW:** «The fixed-recipe RQ1 runs and the four independent Optuna/TPE studies will form separate campaigns.»
- **Reason:** The order is factually wrong. The BO searches (Phases 43–46) ran before the 72 principal runs, which included the fixed-recipe runs.
- **Evidence:** autonomous_decisions_v020.md A-06, A-01

**M-28. Block 367.**

- **OLD:** «External models will be audited and reproduced only when their defining inputs and mechanisms can be preserved.»
- **NEW:** «External models will not be retrained; their published results will be reported separately with their original protocols.»
- **Reason:** No external model was reproduced.
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications)

**M-29. Block 367.**

- **OLD:** «computational cost, calibration, failures, and robustness separately.»
- **NEW:** «computational cost, calibration, and failures separately.»
- **Reason:** No perturbation-robustness analysis exists.
- **Evidence:** package

**M-30. Block 404.**

- **OLD:** «The final report will state the target counts, realized counts, realized percentages, class prevalence, and any unavoidable deviation caused by indivisible groups.»
- **NEW:** «Chapter 4 reports the test-set counts and class prevalence of each condition.»
- **Reason:** Training counts and realized percentages are not in the package or in Chapter 4. (To supply them instead, see D-6.)
- **Evidence:** Chapter 4 Table 1; heldout_seed_metrics_rq1_rq6.csv

**M-31. Block 440.**

- **OLD:** «Swin-B, Video Swin-B, SFormer, and other models will apply their own verified checkpoint-specific normalization at load time.»
- **NEW:** «Swin-B and Video Swin-B will apply their own verified checkpoint-specific normalization at load time.»
- **Reason:** SFormer and the other external models were not run. Normalization is ImageNet mean/std for both backbones, so "checkpoint-specific" remains true.
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications); CHAPTER4_NOTES.md §6 (normalization)

**M-32. Block 442.**

- **OLD:** «Clip-consistent photometric handling. Low-light normalization will not be decided independently frame by frame. When retained, the trigger will be computed once for the clip and the same transformation will be applied to all frames. For Iin ∈ [0, 1] and γ = 2, the brightening convention is:»
- **NEW:** «Photometric handling. The final pipeline applies no low-light or gamma correction, for any model or dataset.»
- **Reason:** Gamma is disabled.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-33. Block 443.**

- **OLD:** «Iₒᵤₜ = Iᵢₙ¹⁄ᵞ = √Iᵢₙ»
- **NEW:** «[delete paragraph; it may be an equation object]»
- **Reason:** This is the gamma formula, which no longer applies.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-34. Block 444.**

- **OLD:** «The trigger is selected from development data only and the entire gamma policy is tested as a preprocessing ablation.»
- **NEW:** «[delete paragraph]»
- **Reason:** The gamma policy ablation was not run and gamma is disabled.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma); A-12 (Phase 158 skipped)

**M-35. Block 455.**

- **OLD:** «The final implementation will report the operation set, number of operations, magnitude, probability behavior, and random seed. Because aggressive transformations can erase authentic forensic evidence or synthesize label-correlated artifacts, the retained policy will be checked through a preprocessing ablation and applied identically to authentic and manipulated training clips.»
- **NEW:** «Because aggressive transformations can erase authentic forensic evidence or synthesize label-correlated artifacts, the same policy will be applied identically to authentic and manipulated training clips.»
- **Reason:** The RandAugment parameters are not reported anywhere, and the augmentation ablation (Phase 159) was not run.
- **Evidence:** A-12; randaugment_v001.yaml not in the package

**M-36. Block 517.**

- **OLD:** «To preserve fairness, all compared models are evaluated under aligned preprocessing and matched decision logic as far as implementation allows. Face detection and alignment, cropping, resizing, low-light correction, identity-consistency verification,»
- **NEW:** «To preserve fairness, all models trained in this study (Swin-B, Video Swin-B, SwinFusion++, and the SwinFusion++ controls) are evaluated under the same preprocessing and decision logic. Face detection and alignment, cropping, resizing, identity-consistency verification,»
- **Reason:** Published comparators were not run under the common preprocessing, and there is no low-light correction.
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications); CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-37. Block 527.**

- **OLD:** «(face detection/alignment, resizing, and low-light correction as needed)»
- **NEW:** «(face detection/alignment, identity-consistency checking, and resizing)»
- **Reason:** The deployed app applies no low-light correction; it does run a FaceNet identity check.
- **Evidence:** CHAPTER4_NOTES.md §6

**M-38. Block 530.**

- **OLD:** «Confidence Score, and»
- **NEW:** «Model score or validation-calibrated estimated probability, with its calibration status identified, and»
- **Reason:** Term rule in block 316. Whether the app follows it is a separate question (D-3).
- **Evidence:** block 316

**M-39. Block 538.**

- **OLD:** «what the confidence score means»
- **NEW:** «what the displayed score means»
- **Reason:** Term rule in block 316.
- **Evidence:** block 316

**M-40. Block 563.**

- **OLD:** «224x224 crop; gamma correction γ=2 for dark frames; FaceNet identifies consistency via 512-D embeddings and Euclidean distance.»
- **NEW:** «224x224 crop; FaceNet identity-consistency check via 512-D embeddings).»
- **Reason:** Gamma is disabled. The distance metric is unverified (V-1), so it is dropped, and the missing ")" is restored.
- **Evidence:** CHAPTER4_NOTES.md §4 (D-08 "APPROVED DISABLED"; low_light enabled: false) and §6 (deployed app applies no gamma)

**M-41. Block 564.**

- **OLD:** «(random majority undersampling; 70-15-15 split; cross-dataset transfer evaluation)»
- **NEW:** «(class → source or identity group → video → clip training sampling; compatible official or 70-15-15 group-disjoint splits; cross-dataset transfer evaluation)»
- **Reason:** The sampler is not undersampling, and validation and test sets are not undersampled (block 313).
- **Evidence:** 00_Shared/bayesian_optimisation/swinfusionpp_*.yaml ("sampler: class_group_video_clip", "augmentation: configs/data/randaugment_v001.yaml"); blocks 313, 404, 458

**M-42. Block 565.**

- **OLD:** «(RandomAugmentation training-only augmentation; Bayesian optimization)»
- **NEW:** «(training-only RandAugment augmentation; one fixed non-BO recipe for all three models; Bayesian optimization for SwinFusion++)»
- **Reason:** Fixes the term (block 455). The principal evidence is the fixed recipe (Option A), which this list omits.
- **Evidence:** 00_Shared/bayesian_optimisation/swinfusionpp_*.yaml ("sampler: class_group_video_clip", "augmentation: configs/data/randaugment_v001.yaml"); blocks 313, 404, 458; Option A

## B. SHOULD edits

**S-1. Block 175.**

- **OLD:** «RQ1 will first compare Swin-B, Video Swin-B, and SwinFusion++ under the same fixed non-BO recipe on every within-dataset condition.»
- **NEW:** «RQ1 will first compare Swin-B, Video Swin-B, and SwinFusion++ under the same fixed non-BO recipe on every within-dataset condition and under frozen transfer.»
- **Reason:** The RQ1 statement and Chapter 4 RQ1 both include cross-dataset evaluation.
- **Evidence:** block 163; Chapter 4 RQ1

**S-2. Block 173.**

- **OLD:** «The DeeperForensics- 1.0 fake class»
- **NEW:** «The DeeperForensics-1.0 fake class»
- **Reason:** Typo (stray space).
- **Evidence:** —

**S-3. Block 196.**

- **OLD:** «developed as both a robust detection model and a deployable platform»
- **NEW:** «developed as both a detection model evaluated under cross-dataset shift and a deployable platform»
- **Reason:** "Robust" overclaims, given Chapter 4: transfer accuracy is about 50%, and DFo → CDF is near chance.
- **Evidence:** Chapter 4 RQ1

**S-4. Block 228.**

- **OLD:** «EfficientNet-BiLSTM with optical flow and facial-geometry CNN–LSTM remain predeclared fallbacks when a preferred model cannot be reproduced. »
- **NEW:** «»
- **Reason:** No recurrent model was reproduced in this study, so the fallback rule is moot. Depends on D-1.
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications)

**S-5. Block 453.**

- **OLD:** «This stratification supports standardized reporting and provides an interpretable basis for communicating expected performance behaviors under varying input quality conditions (also reflected in system design and user guidance).»
- **NEW:** «This stratification is used in the platform’s input guidance and messages; model results are not reported by resolution stratum.»
- **Reason:** No resolution-stratified results exist. The strata do appear in the platform (Appendix B "Low/Medium Resolution" screens).
- **Evidence:** Appendix B Figures 21–22; package (no stratified results)

**S-6. Block 457.**

- **OLD:** «Keval and the uniformly spaced anchor rule will be selected from training/validation valid-track distributions only; test and target duration or track structure will not influence that choice.»
- **NEW:** «Keval and the uniformly spaced anchor rule will be selected from training/validation valid-track distributions only; test and target duration or track structure will not influence that choice. The final configuration uses 2 frames per second and Keval = 7 evaluation clips per video.»
- **Reason:** Chapter 4 states 7 clips at 2 fps; Chapter 3 never gives the values.
- **Evidence:** evaluation_protocol_v020.json ("mean_of_seven_locked_clip_logits"); A-07; A-08 ("shared cache is 2 fps")

**S-7. Block 458.**

- **OLD:** «When an external baseline requires a different native frame count or normalization, it will construct its model-native view from the same anchor region and disclose the adaptation rather than changing the evaluation videos. »
- **NEW:** «»
- **Reason:** No external baseline was run, so this describes an adaptation that never happened.
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications)

**S-8. Block 514.**

- **OLD:** «The full SFormer-aligned comparator inventory retained in this study therefore includes»
- **NEW:** «The full SFormer-aligned comparator inventory reviewed for this study includes»
- **Reason:** Only about ten of these roughly 40 models have results reported (RQ2/RQ6), so "retained" overpromises.
- **Evidence:** RQ6 write-up line 15

**S-9. Block 514.**

- **OLD:** «they are grouped according to the kind of evidence they emphasize and the kind of comparison they make possible.»
- **NEW:** «they are grouped according to the kind of evidence they emphasize and the kind of comparison they make possible. Published results will be reported for the subset with values on the datasets of this study: Xception, I3D, STIL, FTCN, ISTVT, TALL-Swin, SFormer, CAST, TSFF-Net, and CNN–LSTM models.»
- **Reason:** Says which comparators actually appear in Chapter 4.
- **Evidence:** RQ2, RQ4 and RQ6 write-ups

**S-10. Block 516.**

- **OLD:** «produces a measurable advantage.»
- **NEW:** «produces an advantage; because SFormer is not retrained in this study, this comparison uses its published results and is descriptive.»
- **Reason:** No paired measurement against SFormer is possible (block 616).
- **Evidence:** autonomous_decisions_v020.md A-10 (scope: only SwinFusion++, Swin-B, Video Swin-B trained; external models from publications); block 616

## C. VERIFY items

**V-1. Block 441.**

- **OLD:** «are computed and compared with Euclidean distance to enforce»
- **NEW:** «are computed and compared to enforce»
- **Reason:** The text says Euclidean, but the web-app review found cosine (max 0.55). The training-pipeline preprocessing code is not in the backup, so the metric cannot be confirmed. If the group confirms the metric, keep it and name it; otherwise use the neutral NEW text. The same applies to 563 (handled in A by dropping the metric).
- **Evidence:** CHAPTER4_NOTES.md §6

**V-2. Block 422.**

- **OLD:** «with counts shown by class and dataset.»
- **NEW:** «with counts shown by dataset in Chapter 4.»
- **Reason:** Chapter 4 shows test-set failures by dataset (all 0) but not by class or for training. Source validation had 279/280 analyzed for each FF++ condition. Training-partition failures are not in the package. If the group can supply them, keep "by class".
- **Evidence:** source_validation_operating_points_v020.csv (n_validation 280, n_analyzed 279); Chapter 4 Table 1

**V-3. Block 246.**

- **OLD:** «Python with deep-learning frameworks such as PyTorch/TensorFlow and supporting libraries»
- **NEW:** «Python with PyTorch and supporting libraries»
- **Reason:** The model code is PyTorch (src/swinfusionpp/models). Whether any preprocessing or web component uses TensorFlow is unknown. Figure 1 also lists "x-transformers library".
- **Evidence:** backup src/swinfusionpp/models/*.py (import torch)

**V-4. Block 173.**

- **OLD:** «(no edit; affects M-wording)»
- **NEW:** «—»
- **Reason:** Confirm that the 402-video primary DeeperForensics-1.0 fake class is the unperturbed manipulated subset. If so, Chapter 1 can say so definitively instead of using the neutral wording in A.
- **Evidence:** evaluation_protocol_v020.json (primary 402 vs robustness 2,010)

**V-5. Block 455.**

- **OLD:** «for geometric operations, color transformations, blur, and compression simulation»
- **NEW:** «(unchanged if confirmed)»
- **Reason:** The RandAugment operation set is in configs/data/randaugment_v001.yaml, which is not in the package. Confirm that blur and compression simulation are actually in the policy.
- **Evidence:** BO yaml "augmentation" line

**V-6. Block 404/520.**

- **OLD:** «(no edit)»
- **NEW:** «—»
- **Reason:** Which datasets used an official split? The 978-video Celeb-DF v2 test set is not the official 518-video list, which implies the 70/15/15 identity-grouped allocation. FF++ (140 + 140 test) is consistent with the official split. The lead should confirm from the split manifest before Chapter 4 RQ2/RQ6 compares with published Celeb-DF numbers.
- **Evidence:** heldout_seed_metrics (CDF test 978)

## D. USER DECISION items

**D-1. The preliminary study as a source of Xception and CNN–LSTM baselines.**
- **The problem.** RQ2, RQ3 and RQ6 (package write-ups) rely on the Xception and CNN–LSTM baselines that the group reproduced in its preliminary study. RQ3's main evidence is that study's paired C40 test (ΔAUC +0.18). The manuscript never cites or describes the preliminary study.
- **Option A: keep the preliminary results.** Add the reference and use this text in block 175:
  - OLD: «RQ2 will compare BO-selected SwinFusion++ with a verified established-baseline core that targets Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer where implementation and license audits pass. RQ3 will include two reproducible CNN–LSTM models on C23 and C40.»
  - NEW: «RQ2 will compare BO-selected SwinFusion++, with the fixed-recipe result alongside, with the Xception baseline reproduced in the authors' preliminary study and with published results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer. RQ3 will compare SwinFusion++ on C23 and C40 with the CNN–LSTM baseline reproduced in the preliminary study and with published CNN–LSTM results.»
  - Also append ", and from the authors' preliminary study for Xception and a CNN–LSTM (earlier pipeline)" after "taken from their publications" in M-10 (block 190), and add the same clause to M-1 (148), M-23/M-28 (325/367) and S-9 (514).
- **Option B: published values only.** Same OLD, with this NEW: «RQ2 will compare BO-selected SwinFusion++, with the fixed-recipe result alongside, with published results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer. RQ3 will compare SwinFusion++ with published CNN–LSTM results on C23 and C40.» RQ3 would then lose its only paired test.
- **Either way**, the two CNN–LSTMs of decision D-15 (Chen et al. and Saikia et al.) were never reproduced, so block 175's "two reproducible CNN–LSTM models" must go.

**D-2. Figures 1–3 must be redrawn by the group; images cannot be edited.**
- **Figure 1 (Conceptual Framework):**
  - "Gamma Correction" appears under Input 4 and Process 1b; remove it.
  - "RandomAug" → "RandAugment".
  - "Handling class imbalance (undersampling)" → "class-balanced sampling (class → group → video → clip)".
  - "PyTorch/TensorFlow, x-transformers library": confirm (V-3).
  - "Robustness Testing: noise, compression, and adversarial variations": only compression and cross-dataset shift were evaluated.
  - "70–15–15 train-test split" → "official group-safe split or 70/15/15".
- **Figure 2 (HIPO):**
  - 3.0 says "applies gamma correction when needed"; remove it.
  - 5.0 says "confidence/probability score", which breaks the block 316 term rule.
- **Figure 3 (Flowchart):**
  - "Gamma Correction if needed"; remove it.
  - "Optional FaceNet Identity Filter": Chapter 3 makes identity association a fixed part of the pipeline.
  - "Display Result, Confidence Score, and Metadata": term rule.
  - There is no Insufficient Evidence branch, although block 357 describes one.

**D-3. Web platform vs Chapter 1–3 text (CHAPTER4_NOTES §6).** The group decides whether to change the app or the text.
- (a) The app shows "NN% sure" as a confidence score, while blocks 177, 316, 335, 358, 530 and 538 say an identified model score or calibrated probability, with no "confidence" term.
- (b) The main result samples every frame (about 2.9 fps, many clips). The evaluated protocol is 7 locked clips at 2 fps, and the app's "Second check" uses 3 clips (blocks 335, 356–357).
- (c) The clip count is not shown (blocks 177, 316, 335, 358).
- (d) A 3-clip fallback with a warning replaces Insufficient Evidence (blocks 177, 316, 335, 357).
- (e) Successful deletions are not logged (blocks 358, 368).
- (f) FaceNet uses cosine distance (blocks 441, 563; see V-1).
- (g) **Served model.** The app's thresholds and temperatures match none of the 144 thesis operating points.
  - Blocks 171 ("operationalize the verified detector") and 368 ("record the exact model, preprocessing, threshold, and calibration versions") are not true until this is resolved.
  - Chapter 4's results describe the evaluated checkpoints only.
- (h) The site's "How it works" page says that dark frames are brightened.
- (i) The Appendix B Results Interface image shows "deepfake probability score".

**D-4. Title page date:** "MARCH 2026" (block 25). Set it to the submission month.

**D-5. RQ statements and the hypothesis (not edited, by rule).**
- **RQ4** asks about cross-attention "compared to other spatio-temporal models such as CAST and TSFF-Net". Those models exist only as published values, so RQ4's answer will rest on the internal controls. A panel may ask about this.
- **RQ5** is excluded in the package traceability file ("excluded_without_renumbering"); the user should confirm its Chapter 4 status.
- **H0** (blocks 251–252) is framed against "existing CNN- or transformer-based spatio-temporal models", but published models cannot be tested. This is the statistician's item.

**D-6. Training and validation counts.** Block 404 promised target and realized counts and percentages. Only test counts (plus validation counts from the operating-point file) are in the package. If the group can export the split-manifest counts from the B2 backup, Chapter 4 Table 1 could report them; in that case keep block 404 and drop M-30.

## E. Notes for the other advisors

**To the statistician (blocks in your range that touch my findings):**
- **498 (hardware).** Proposed NEW: «BF16 mixed precision on an NVIDIA RTX 5090, with the exact scaler behavior recorded;». Sources: COMPUTE_COST.md; BO yaml "precision: bfloat16".
- **499.** The fixed-recipe batch of 16 is unverified (the fixed-recipe config is not in the package); all four BO winners used 8.
- **504.** Use the same counts as my M-4, M-8 and M-22: 12 trials for C23/HQ and C40/LQ, 8 for Celeb-DF v2 and DeeperForensics-1.0.
- **520.** FF++ C40 was not used as a transfer source (9 directions).
- **614.** The "perturbation condition" wording conflicts with my M-2 (block 173): perturbation strata were not scored.
- **617.** Latency (preprocessing, clip, complete video) was not measured; only cold single-clip timings exist.
- **615 and the amendments paragraph.** These are yours (family names).

**To the lead:**
- **Paragraph deletions.** M-12 to M-15 (blocks 210–213) and M-33 and M-34 (443, 444) delete whole paragraphs; remove their paragraph marks. Block 443 may be an OMML equation.
- **Ordering.** M-5 to M-7 and S-1 all edit block 175; apply them in one pass. The RQ2/RQ3 sentence of block 175 waits for D-1.
- **Terms.** With M-11, M-16, M-26, M-38 and M-39, the term "confidence" no longer appears in Chapters 1–3 text (it remains in Figures 2–3; see D-2). "RandomAugment" and "RandomAugmentation" are unified as "RandAugment" (M-18, M-42), and "undersampling" now appears only in block 313, in its correct negative sense ("not … undersampled").
- **Other leftovers.** After all edits, "gamma" and "low-light" remain only in block 181 (an input-quality limitation, which is correct) and in Figures 1–3.
