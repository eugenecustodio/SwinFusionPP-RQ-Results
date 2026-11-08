# Limitations draft v1 (Google Doc, CURRENT tab, Chapter 1 "Scope and Limitations of the Study")

Target: Google Doc 1gGBuvZi0CacrbfvPXl5Ppw-QZ4IiCOG9i1XwBRtpHJg, tab t.l5c18frq5wuo ("CURRENT").
Edits are applied as Google suggestions (replaceAllText, writeMode SUGGEST) so the group can accept or reject each one.
The existing list has 10 bullets (E1–E10). Source text: Drive read of 2026-11-06 17:5x.

Goal (user, 2026-11-06): complete the limitations so a three-member panel cannot find an unacknowledged weakness, while keeping SwinFusion++ in a positive light within the evidence. Each new item states the boundary, what the study did about it, and how to read the results.

Fact sources: chapter4_rq1/tables/T1.csv and T1_note.txt (test sets, clusters, lineage), KEY_NUMBERS.md, compute/COMPUTE_COST.md, CHAPTER4_NOTES.md §4–6, the CURRENT tab's own Chapter 3 (platform: lines 256–259; sampling: 317–320; sample size: Cochran, 120 target; dates: 241, 278–285).

---

## A. Changes to existing text in the section

**A1. Scope, 3rd paragraph (baselines were not retrained).** Replace the whole sentence:
- OLD: "To ensure that comparisons are meaningful and attributable to model design (rather than inconsistent preprocessing), SwinFusion++ is benchmarked relative to established baselines (e.g., CNN-LSTM and recent fusion-oriented spatio-temporal approaches), and the comparisons are conducted under aligned preprocessing and matched evaluation logic as stated in the current methodology."
- NEW: "SwinFusion++ is also benchmarked relative to established baselines (e.g., CNN-LSTM and recent fusion-oriented spatio-temporal approaches) using their previously reported results. To ensure that comparisons are meaningful and attributable to model design (rather than inconsistent preprocessing), the controlled comparison is made against standalone Swin-B and Video Swin-B, which are trained and evaluated with the same preprocessing, training recipe, and evaluation logic as SwinFusion++."

**A2. Scope, 5th paragraph (leftover chat wording).** "practical heuristic evaluation principles as reflected in your document)" → "practical heuristic evaluation principles)".

**A3. Bullet E10 (match the platform limits stated in Chapter 3, line 256).** "with a maximum file size of 250 MB and a maximum input quality of 1080p. Videos that exceed these limits" → "with a length of 10 seconds to 2 minutes, a resolution of 360p to 1080p, and a maximum file size of 250 MB. Videos outside these limits".

**A4. Stale RQ numbers after the RQ renumbering (Chapter 3, Research Design).**
- "This component addressed RQ1, RQ2, RQ3, and RQ5" → "This component addressed RQ1, RQ2, RQ3, RQ4, and RQ6"
- "This component addressed RQ4 and" → "This component addressed RQ5 and"

**A5. Chapter 3, Statistical Treatment (line 368; would contradict new item N8).** "To preserve fairness, all compared models are evaluated" → "To preserve fairness, all models trained in this study (SwinFusion++, Swin-B, and Video Swin-B) are evaluated"

---

## B. New limitation bullets (no deviation content)

Placed after E5 ("...post-processing pipelines."):

**N1.** Manipulation types. From FaceForensics++, only the DeepFakes face-swap subset is used; the Face2Face, FaceSwap, and NeuralTextures subsets are not. The three benchmarks were released between 2019 and 2020, so the results do not cover fully synthetic faces, diffusion-based video generators, lip-sync manipulation, or face-swap tools released since then.

**N2.** Population coverage. The benchmark datasets were not collected to represent Filipino subjects or Philippine media, and performance was not measured separately by age, sex, or skin tone. Equal performance across demographic groups is therefore not established.

Placed after E7 ("...evidence extraction strategy."):

**N3.** Video-level decision. In the benchmark evaluation, each video is judged from a fixed number of short face clips sampled at a reduced frame rate, and the clip scores are averaged into one video-level score. A manipulation that affects only a short part of a longer video, or an artifact that appears only between consecutive frames at the original frame rate, may therefore have a weaker effect on the final score.

**N4.** Near-ceiling in-distribution scores. Current transformer detectors, including the models compared here, reach near-perfect scores when trained and tested on the same benchmark. Differences between strong models on these benchmarks are therefore small and hard to detect, so the evidence for an architectural advantage comes mainly from cross-dataset transfer.

**N5.** Cross-dataset transfer. Every model, SwinFusion++ included, performs less well on datasets it was not trained on than on its training dataset. A transfer advantage over the standalone encoders is a relative improvement, and detection on unseen data remains an open problem.

**N6.** Test set size. The test sets contain 280 videos for each FaceForensics++ quality level, 978 for Celeb-DF v2, and 402 for DeeperForensics-1.0, and related videos were kept together in one partition. In Celeb-DF v2, all manipulated test videos come from nine identities, so its confidence intervals are approximate. Small differences between models may go undetected.

**N7.** Training repetitions. Each model is trained with three random seeds, and the reported results use the three-seed ensemble. Three seeds show whether results are stable across training runs but do not measure seed-to-seed variation precisely.

**N8.** Shared source footage. DeeperForensics-1.0 is built on FaceForensics++ source footage, and its real class in this study consists of FaceForensics++ original videos, so transfer between these two datasets is not fully independent. Subsets without shared footage were also analyzed, but they are small (20 to 60 videos for these directions).

**N9.** Comparisons with published models. Established baselines such as the CNN-LSTM models, CAST, and TSFF-Net were not retrained in this study. Their results come from their original publications, which used their own data splits, preprocessing, and evaluation units, so these comparisons place SwinFusion++ in context rather than serving as controlled head-to-head tests. The controlled comparison is with Swin-B and Video Swin-B.

**N10.** Training recipe and tuning. In the principal comparison, SwinFusion++, Swin-B, and Video Swin-B were trained with one shared fixed recipe, so none received tuning the others did not, although the shared recipe may not be the best setting for each model. Bayesian hyperparameter optimization was applied to SwinFusion++ only, so the optimized model is reported separately as a configured system and is not used to judge the architecture.

**N11.** Computational cost. SwinFusion++ runs both the Swin-B and Video Swin-B backbones, so it has about 181 million parameters, against about 87 million for each backbone, and needs more memory and time to train and run. The fusion module itself accounts for only about 6.5 million of these parameters. The model was not compressed or accelerated (for example by pruning, distillation, or quantization).

Placed after E8 ("...legal or evidentiary contexts."):

**N12.** Decision thresholds and confidence values. Each model's decision threshold was chosen on the validation data of its training dataset and kept unchanged when the model was tested on other datasets. On a dataset with a different distribution, a fixed threshold can make a detector too cautious or too permissive, so threshold-based measures (accuracy, precision, recall, and F1-score) under transfer should be read together with ROC-AUC, which does not depend on a single threshold. For the same reason, the platform's verdict and confidence value are most reliable for videos similar to the training data.

**N13.** Evidence maps. The evidence maps shown by the platform highlight the facial regions that most influenced a result. They were not validated as faithful explanations of the model's decision, and they do not identify which frames or regions were manipulated or which manipulation method was used.

**N14.** Platform and benchmark results. The detection results in Chapter 4 come from the offline benchmark evaluation. The platform's main verdict analyzes every usable frame rather than following the benchmark sampling protocol, which it applies only as a secondary check, and the platform's own detection accuracy was not measured separately. The user and expert evaluation assessed the platform's quality in use, not its detection accuracy.

Placed after E10 (end of list):

**N15.** Respondent sample. End users were drawn from the University of the East community through quota and purposive sampling, and experts from organizations in Metro Manila through purposive sampling. Because these are non-probability samples, the results describe the participating respondents and cannot be generalized to all social-media users. The sample size was computed with Cochran's formula, which assumes random selection, so its margin of error is an approximation.

**N16.** Self-reported ratings. The ISO/IEC 25010-based questionnaires measure how respondents perceived the platform during task-based sessions with test videos. Security was rated as perceived by users and experts and was not verified through penetration testing or a formal security audit, and ratings of performance efficiency may reflect the server's availability during the evaluation period (12 to 30 October 2026 for end users and 15 to 30 October 2026 for experts), which also means the ratings reflect first-time, short-term use.

---

## C. Pending the user's decision (deviation-type content; memory rule: ask before placing it outside Chapter 4)

**B1.** Other degradations and attacks. Apart from the two FaceForensics++ compression levels and cross-dataset transfer, the study does not test degradations such as blur, noise, low light, or resizing, the re-encoding applied by social-media platforms, or attacks designed to evade detection. Results for videos submitted through social-media links may therefore differ from the benchmark results.
- Requires changing the Chapter 2 Conceptual Framework promise (line 199): "and conducting robustness checks under stressors such as noise, compression, and adversarial variations" → "and checking performance under compression (FaceForensics++ C23 and C40)".
- Basis: T3.csv row "DeeperForensics-1.0 perturbation variants ... Not evaluated".

Deliberately NOT included (user said on 2026-10-07 not to disclose ablations that were never run): gamma/RandAugment ablations, controls on non-C23 datasets. Also not included: BO trial counts, C40 as a transfer source, RTX 5090 vs planned GPU.

## D. Contradictions found elsewhere in CURRENT (flag only; not part of this task)

- Gamma correction (γ = 2) described as applied (lines 197, 219, 239, 345, 434); the final pipeline used none (D-08), and line 257 says only the Increment 1 prototype used it.
- FaceNet comparison: Euclidean (lines 219, 346, 434) vs cosine (line 257).
- CURRENT Chapter 3 never mentions the fixed recipe, the three seeds, calibration, or the cluster-aware statistics that Chapter 4 uses.
