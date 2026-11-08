# Lead: merged edit list for Chapters 1–3, Round 2

All MUST and SHOULD items from both memos are merged here. Where both of you proposed an edit to the same sentence, one wording was chosen; see the "src" column. Baseline sentences (C1, C8–C10, C13, C26, C31, C36, C52, C53) use "previously reported results", which is true whether or not the group later cites its preliminary study (D-1), so they do not prejudge D-1.

**Not applied (left for the user):** S-B9 (sample-size caveat: internal, not a results inconsistency); every D item; V-4, V-5 and V-6 (no edit). The amendments-paragraph edit (S-B6) is applied by regenerating that paragraph.

**C1** (M-1 (neutral to D-1)). No external model was retrained in this study (A-10).
- OLD: «The study will also use topology and capacity-matched controls, two CNN–LSTM comparators on FaceForensics++ C23/C40, a verified established-baseline core, component ablations,»
- NEW: «The study will also use topology and capacity-matched controls, previously reported results for CNN–LSTM comparators on FaceForensics++ C23/C40 and for established baselines, component ablations,»

**C2** (M-2). Perturbation strata were never scored.
- OLD: «provisionally the unperturbed manipulated subset when the observed distribution supports that label; perturbation variants will otherwise remain separately identified robustness strata.»
- NEW: «and perturbation variants will remain separately identified and will not be used in the reported evaluations.»

**C3** (M-3). Matches Chapter 4 Table 1.
- OLD: «Exact file identifiers, counts, lineage keys, and exclusions will be reported only after the filesystem and manifest audit.»
- NEW: «Exact file identifiers, lineage keys, and exclusions are fixed in versioned manifests; test-set counts, lineage overlap, and coverage are reported in Chapter 4.»

**C4** (S-A4 = M-4). Typo (S-2).
- OLD: «The DeeperForensics- 1.0 fake class»
- NEW: «The DeeperForensics-1.0 fake class»

**C5** (S-A4 = M-4). Actual BO budgets 12/12/8/8 (bo_summary; A-12).
- OLD: «Before the full BO campaigns, a resource pilot will determine whether the predeclared total trial count is 12, 16, or 20 per study; the choice will be based on measured compute and storage rather than test performance.»
- NEW: «The total trial count will be 12 per study for C23/HQ and C40/LQ and 8 for Celeb-DF v2 and DeeperForensics-1.0, set from measured compute time and the project schedule before any test scoring rather than from test performance.»

**C6** (S-1). RQ1 covers cross-dataset evaluation (block 163; Chapter 4).
- OLD: «RQ1 will first compare Swin-B, Video Swin-B, and SwinFusion++ under the same fixed non-BO recipe on every within-dataset condition.»
- NEW: «RQ1 will first compare Swin-B, Video Swin-B, and SwinFusion++ under the same fixed non-BO recipe on every within-dataset condition and under frozen transfer.»

**C7** (M-5). Gamma/augmentation ablations not run; controls C23-only; Tier B single-seed (A-11, A-12, A-14, A-18).
- OLD: «The contribution of TLBG-HCA will be examined through both a topology non-attentive control and a capacity-matched no-exchange control, together with one-directional, no-gate, no-agreement/disagreement, Stages-3–4-only, gamma-policy, and augmentation- policy ablations.»
- NEW: «Under RQ4, the contribution of TLBG-HCA will be examined through both a topology non-attentive control and a capacity-matched no-exchange control trained on C23/HQ, together with single-seed one-directional, no-gate, no-agreement/disagreement, and Stages-3–4-only ablations of the BO-selected C23/HQ configuration.»

**C8** (D-1 neutral wording (lead)). No baseline retrained in this study; wording true whether or not the preliminary study is cited (D-1).
- OLD: «RQ2 will compare BO-selected SwinFusion++ with a verified established-baseline core that targets Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer where implementation and license audits pass. RQ3 will include two reproducible CNN–LSTM models on C23 and C40.»
- NEW: «RQ2 will compare BO-selected SwinFusion++, with the fixed-recipe result alongside, with previously reported results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer. RQ3 will compare SwinFusion++ on C23 and C40 with previously reported CNN–LSTM results.»

**C9** (M-6). CAST/TSFF-Net not run (A-10).
- OLD: «RQ4 will address CAST and TSFF-Net per dataset without mischaracterizing their inputs.»
- NEW: «RQ4 will also place CAST and TSFF-Net in context through their previously reported results, without mischaracterizing their inputs.»

**C10** (M-7). SFormer replication tracks superseded (A-10).
- OLD: «RQ6 will synthesize these within-dataset results with directional frozen transfer and the two SFormer replication tracks.»
- NEW: «RQ6 will synthesize these within-dataset results with directional frozen transfer and previously reported spatio-temporal results.»

**C11** (M-8 (≈ S-B2)). Actual limits (A-12).
- OLD: «Four Base-sized within-dataset campaigns, four Bayesian- optimization studies, multiple controls, external baselines, and transfer tests require substantial accelerator time and storage. The final BO trial count is therefore selected only after a cost pilot and may limit lower-priority ablations or optional external reproductions»
- NEW: «Four Base-sized within-dataset campaigns, four Bayesian-optimization studies, multiple controls, and transfer tests require substantial accelerator time and storage. The available accelerator time therefore limits the BO trial count (12 trials for C23/HQ and C40/LQ; 8 for Celeb-DF v2 and DeeperForensics-1.0) and restricts the matched controls and component ablations to C23/HQ training»

**C12** (M-9). D-43 stratified reporting not produced.
- OLD: «Lineage matching, common decoding/cropping, metadata-only shortcut tests, and stratified reporting reduce»
- NEW: «Lineage matching, common decoding/cropping, and metadata-only shortcut tests reduce»

**C13** (M-10 (neutral to D-1)). No external model trained (A-10; block 616).
- OLD: «External-baseline reproducibility. Some published methods may lack official code, weights, complete preprocessing details, compatible licenses, or the inputs needed by the common protocol. Such models will be labeled literature-only, not reported, or blocked rather than silently approximated.»
- NEW: «External baselines. The study trains only Swin-B, Video Swin-B, SwinFusion++, and the SwinFusion++ controls and ablations. Results for external methods are taken from previously reported work, keep their original datasets, protocols, and evaluation units, and are not entered into paired tests.»

**C14** (S-B7). Transfer calibration is poor (median ECE 0.446; CALIBRATION.md).
- OLD: «Consequential use requires provenance checks, contextual verification, or specialist forensic examination.»
- NEW: «The validation-calibrated estimated probability is fitted on source-validation videos, so its calibration is not guaranteed for videos from unfamiliar sources. Consequential use requires provenance checks, contextual verification, or specialist forensic examination.»

**C15** (S-3). "Robust" overclaims (Chapter 4).
- OLD: «developed as both a robust detection model and a deployable platform»
- NEW: «developed as both a detection model evaluated under cross-dataset shift and a deployable platform»

**C16** (M-11). Term rule (block 316).
- OLD: «(label + confidence + metadata)»
- NEW: «(screening label, model score or calibrated estimated probability, and metadata)»

**C17** (M-12). DELETE PARAGRAPH starting «Within this architectural direction, cross-attention is meaningful only when the participa…». Verbatim duplicate of block 214.

**C18** (M-13). DELETE PARAGRAPH starting «Temporal alignment alone does not determine how the streams should exchange evidence. Glob…». Duplicate of block 215.

**C19** (M-14). DELETE PARAGRAPH starting «A newly initialized fusion block can also disturb pretrained representations…». Earlier draft of block 216.

**C20** (M-15). DELETE PARAGRAPH starting «These architectural choices must be evaluated through controls that isolate the proposed m…». Earlier draft of block 218.

**C21** (S-4). No recurrent model reproduced in this study.
- OLD: «EfficientNet-BiLSTM with optical flow and facial-geometry CNN–LSTM remain predeclared fallbacks when a preferred model cannot be reproduced. »
- NEW: «»

**C22** (M-16). Term rule.
- OLD: «outputs a Real or Fake label with confidence must communicate uncertainty»
- NEW: «outputs a Real or Fake label with a model score or calibrated estimated probability must communicate uncertainty»

**C23** (M-17 + V-3). Model code is PyTorch.
- OLD: «Python with deep-learning frameworks such as PyTorch/TensorFlow and supporting libraries»
- NEW: «Python with PyTorch and supporting libraries»

**C24** (M-17). Gamma disabled (D-08).
- OLD: «(MTCNN for face detection/alignment, FaceNet for face verification, and gamma correction for illumination normalization).»
- NEW: «(MTCNN for face detection/alignment and FaceNet for face verification).»

**C25** (M-18). No gamma; RandAugment; sampler class_group_video_clip.
- OLD: «where facial evidence is standardized via alignment, dark-frame correction, identity verification, and data augmentation using RandomAugment—operationalized as controlled randomized transformations (e.g., shift/rotate/noise) applied in a manner that preserves clip integrity—together with class-imbalance handling through undersampling;»
- NEW: «where facial evidence is standardized via alignment and identity verification, with training-only RandAugment augmentation—operationalized as controlled randomized transformations applied in a manner that preserves clip integrity—and class-balanced training sampling (class → source or identity group → video → clip);»

**C26** (M-19). No stressor analyses; "demonstrated robustness" overclaims.
- OLD: «benchmarking against established models, and conducting robustness checks under stressors such as compression, perturbation, resolution, and preprocessing conditions—thereby ensuring that conclusions about effectiveness are grounded not only in in-dataset accuracy but also in demonstrated robustness under distribution shift.»
- NEW: «comparing against previously reported results of established models, and examining performance under compression (FaceForensics++ C23/HQ versus C40/LQ) and cross-dataset shift—so that conclusions about effectiveness rest not only on in-dataset accuracy but also on performance under distribution shift.»

**C27** (M-20). Gamma disabled; ablation not run.
- OLD: «Any low-light transformation is decided at the clip level and is evaluated as an ablation.»
- NEW: «The final pipeline applies no low-light transformation.»

**C28** (M-21). No such appendix.
- OLD: «are documented in the appendix»
- NEW: «are recorded in the versioned dataset manifest»

**C29** (S-B3). Decisions come from the permutation test.
- OLD: «At least 5,000 cluster-bootstrap replicates were used to construct the principal 95% confidence intervals and paired statistical comparisons.»
- NEW: «At least 5,000 cluster-bootstrap replicates were used to construct the principal 95% confidence intervals, including those for paired differences, and paired differences were tested with a cluster-level permutation test.»

**C30** (M-22 (≈ S-B1)). Counts cut on 2026-09-30 during BO (A-12).
- OLD: «A capped resource pilot will estimate the cost of the four independent Optuna/TPE studies; the final per-study trial count will be fixed before full BO.»
- NEW: «The per-study trial counts of the four independent Optuna/TPE studies will be set from measured compute time and the project schedule before any test scoring (12 trials for C23/HQ and C40/LQ; 8 for Celeb-DF v2 and DeeperForensics-1.0).»

**C31** (M-23 (neutral to D-1)). No external model reproduced (A-10).
- OLD: «The external-baseline stage will verify and, where feasible, reproduce Xception, I3D, STIL, FTCN with Temporal Transformer, TALL-Swin, SFormer, two CNN–LSTM models, and the conditionally reproducible CAST and TSFF-Net comparisons.»
- NEW: «External baselines (Xception, I3D, STIL, FTCN with Temporal Transformer, TALL-Swin, SFormer, CNN–LSTM models, CAST, and TSFF-Net) will not be retrained in this study; their previously reported results will be recorded with their datasets, protocols, and evaluation units.»

**C32** (M-24 (= S-B10)). No perturbation-robustness analysis.
- OLD: «calibration, efficiency, failure, shortcut, and robustness analyses»
- NEW: «calibration, efficiency, failure, and shortcut analyses»

**C33** (M-25). Gamma disabled.
- OLD: «applies gamma correction to dark frames when needed, »
- NEW: «»

**C34** (M-26). Duplicates block 335; banned term.
- OLD: «The output layer will translate the computed prediction into user-readable results. The system will present a classification result, a confidence or probability score, and contextual video metadata such as filename, resolution, frame rate, duration, file size, and format. These outputs are designed as decision-support information rather than standalone forensic proof. »
- NEW: «»

**C35** (M-27). Order was the reverse (A-01, A-06).
- OLD: «The fixed-recipe RQ1 runs will precede the BO cost pilot and four independent Optuna/TPE studies.»
- NEW: «The fixed-recipe RQ1 runs and the four independent Optuna/TPE studies will form separate campaigns.»

**C36** (M-28 (neutral to D-1)). No external model reproduced.
- OLD: «External models will be audited and reproduced only when their defining inputs and mechanisms can be preserved.»
- NEW: «External models will not be retrained; their previously reported results will be reported separately with their original protocols.»

**C37** (M-29 (= S-B10)). No perturbation-robustness analysis.
- OLD: «computational cost, calibration, failures, and robustness separately.»
- NEW: «computational cost, calibration, and failures separately.»

**C38** (S-C3 / M-30). Only test counts are reported (Table 1); see D-6.
- OLD: «The final report will state the target counts, realized counts, realized percentages, class prevalence, and any unavoidable deviation caused by indivisible groups.»
- NEW: «The final report will state the test-set counts and class prevalence for every condition.»

**C39** (V-2). Training-partition failures not available.
- OLD: «with counts shown by class and dataset.»
- NEW: «with counts shown by dataset in Chapter 4.»

**C40** (M-31). External models not run.
- OLD: «Swin-B, Video Swin-B, SFormer, and other models will apply their own verified checkpoint-specific normalization at load time.»
- NEW: «Swin-B and Video Swin-B will apply their own verified checkpoint-specific normalization at load time.»

**C41** (V-1). Metric unverified (Euclidean vs cosine).
- OLD: «are computed and compared with Euclidean distance to enforce»
- NEW: «are computed and compared to enforce»

**C42** (M-32). Gamma disabled.
- OLD: «Clip-consistent photometric handling. Low-light normalization will not be decided independently frame by frame. When retained, the trigger will be computed once for the clip and the same transformation will be applied to all frames. For Iin ∈ [0, 1] and γ = 2, the brightening convention is:»
- NEW: «Photometric handling. The final pipeline applies no low-light or gamma correction, for any model or dataset.»

**C43** (M-33). DELETE PARAGRAPH starting «Iₒᵤₜ = Iᵢₙ¹⁄ᵞ = √Iᵢₙ…». Gamma formula no longer applies.

**C44** (M-34). DELETE PARAGRAPH starting «The trigger is selected from development data only and the entire gamma policy is tested a…». Gamma ablation not run.

**C45** (S-5 (≈ S-B11)). No resolution-stratified results.
- OLD: «This stratification supports standardized reporting and provides an interpretable basis for communicating expected performance behaviors under varying input quality conditions (also reflected in system design and user guidance).»
- NEW: «This stratification is used in the platform’s input guidance and messages; model results are not reported by resolution stratum.»

**C46** (M-35). Parameters not reported; ablation not run.
- OLD: «The final implementation will report the operation set, number of operations, magnitude, probability behavior, and random seed. Because aggressive transformations can erase authentic forensic evidence or synthesize label-correlated artifacts, the retained policy will be checked through a preprocessing ablation and applied identically to authentic and manipulated training clips.»
- NEW: «Because aggressive transformations can erase authentic forensic evidence or synthesize label-correlated artifacts, the same policy will be applied identically to authentic and manipulated training clips.»

**C47** (S-6). Matches Chapter 4 (evaluation_protocol_v020.json).
- OLD: «Keval and the uniformly spaced anchor rule will be selected from training/validation valid-track distributions only; test and target duration or track structure will not influence that choice.»
- NEW: «Keval and the uniformly spaced anchor rule will be selected from training/validation valid-track distributions only; test and target duration or track structure will not influence that choice. The final configuration uses 2 frames per second and Keval = 7 evaluation clips per video.»

**C48** (S-7). No external baseline run.
- OLD: «When an external baseline requires a different native frame count or normalization, it will construct its model-native view from the same anchor region and disclose the adaptation rather than changing the evaluation videos. »
- NEW: «»

**C49** (A6 (S) = M). Actual hardware (A-08).
- OLD: «BF16 mixed precision on a supported H100 or A100, with the exact scaler behavior recorded;»
- NEW: «BF16 mixed precision on an NVIDIA RTX 5090, with the exact scaler behavior recorded;»

**C50** (A3 (S)). bo_summary; A-12; A-16.
- OLD: «A resource pilot will select the final total from 12, 16, or 20 trials per study using measured GPU-hour and storage limits, never test performance.»
- NEW: «The total will be 12 trials per study for C23/HQ and C40/LQ and 8 for Celeb-DF v2 and DeeperForensics-1.0, including pruned trials, set from measured compute time and the project schedule before any test scoring, never from test performance.»

**C51** (S-8). Only a subset has reported results.
- OLD: «The full SFormer-aligned comparator inventory retained in this study therefore includes»
- NEW: «The full SFormer-aligned comparator inventory reviewed for this study includes»

**C52** (S-9). Which comparators appear.
- OLD: «they are grouped according to the kind of evidence they emphasize and the kind of comparison they make possible.»
- NEW: «they are grouped according to the kind of evidence they emphasize and the kind of comparison they make possible. Previously reported results will be given for the subset with values on the datasets of this study: Xception, I3D, STIL, FTCN, ISTVT, TALL-Swin, SFormer, CAST, TSFF-Net, and CNN–LSTM models.»

**C53** (S-10). No paired test vs SFormer possible.
- OLD: «produces a measurable advantage.»
- NEW: «produces an advantage; because SFormer is not retrained in this study, this comparison uses its previously reported results and is descriptive.»

**C54** (M-36). Only internal models share the pipeline; no low-light correction.
- OLD: «To preserve fairness, all compared models are evaluated under aligned preprocessing and matched decision logic as far as implementation allows. Face detection and alignment, cropping, resizing, low-light correction, identity-consistency verification,»
- NEW: «To preserve fairness, all models trained in this study (Swin-B, Video Swin-B, SwinFusion++, and the SwinFusion++ controls) are evaluated under the same preprocessing and decision logic. Face detection and alignment, cropping, resizing, identity-consistency verification,»

**C55** (A1 (S)). C40 never a source (9 directions).
- OLD: «The second is cross-dataset transfer evaluation, in which a model trained on one dataset is tested on the remaining datasets to assess robustness under distribution shift.»
- NEW: «The second is cross-dataset transfer evaluation, in which a model trained on FaceForensics++ C23, Celeb-DF v2, or DeeperForensics-1.0 is tested on each of the remaining datasets to assess robustness under distribution shift.»

**C56** (M-37). App applies no low-light correction.
- OLD: «(face detection/alignment, resizing, and low-light correction as needed)»
- NEW: «(face detection/alignment, identity-consistency checking, and resizing)»

**C57** (M-38). Term rule (block 316).
- OLD: «Confidence Score, and»
- NEW: «Model score or validation-calibrated estimated probability, with its calibration status identified, and»

**C58** (M-39). Term rule.
- OLD: «what the confidence score means»
- NEW: «what the displayed score means»

**C59** (M-40). Gamma disabled; metric unverified; restores ")".
- OLD: «224x224 crop; gamma correction γ=2 for dark frames; FaceNet identifies consistency via 512-D embeddings and Euclidean distance.»
- NEW: «224x224 crop; FaceNet identity-consistency check via 512-D embeddings).»

**C60** (M-41 (≈ S-C2)). Sampler is not undersampling.
- OLD: «(random majority undersampling; 70-15-15 split; cross-dataset transfer evaluation)»
- NEW: «(class → source or identity group → video → clip training sampling; compatible official or 70-15-15 group-disjoint splits; cross-dataset transfer evaluation)»

**C61** (M-42). Term; Option A.
- OLD: «(RandomAugmentation training-only augmentation; Bayesian optimization)»
- NEW: «(training-only RandAugment augmentation; one fixed non-BO recipe for all three models; Bayesian optimization for SwinFusion++)»

**C62** (A2 (S)). No perturbation stratum scored.
- OLD: «For every dataset construction, compression or perturbation condition, optimization regime,»
- NEW: «For every dataset construction, compression condition, optimization regime,»

**C63** (S-B4). Table J1 is ROC-AUC only.
- OLD: «Each seed will be evaluated independently, and per-seed metrics plus mean and standard deviation will be reported.»
- NEW: «Each seed will be evaluated independently, and per-seed ROC-AUC plus mean and standard deviation will be reported.»

**C64** (S-B5). Binning never stated.
- OLD: «ECE with the declared binning method»
- NEW: «ECE with 15 equal-width bins»

**C65** (A5 (S)). Latency not measured (COMPUTE_COST.md); reverse if the group measures it (D3).
- OLD: «Computational analysis will state total and trainable parameters, operations per clip, peak inference and training memory where feasible, preprocessing latency, clip inference latency, complete video latency, throughput, and checkpoint size under the declared hardware and software environment.»
- NEW: «Computational analysis will state total parameters, operations per clip and per video, peak training memory, training throughput, and checkpoint size under the declared hardware and software environment.»

**C66** (S-B8). Expert survey section omitted.
- OLD: «error prevention/recovery, interpretability, consistency, transparency/help, and context»
- NEW: «error prevention/recovery, language/microcopy clarity, interpretability, consistency, transparency/help, and context»

