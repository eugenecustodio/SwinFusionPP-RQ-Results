# CURRENT

SwinFusion++: Face-Aligned Spatio-Temporal Swin Transformer for Deepfake Detection
A Research Project
Presented to the
Faculty of the College of Computer Studies and Systems
University of the East, Manila
In Partial Fulfillment
Of the Requirements for the Degree in
Bachelor of Science in Computer Science
By
Custodio, Eugene T.
Degamo, Mary Kristine
Escueta, Keith Roger C.
San Diego, Dei Andrea E.
MARCH 2026
TABLE OF CONTENTS
TITLE                                                                                                             PAGE
Title Page i
Table of Contents ii
List of Figures iii
Chapter
1.  [THE PROBLEM AND ITS BACKGROUND 6](?tab=t.l5c18frq5wuo#heading=h.1ecsuvu9y9ua)
[Introduction 6](?tab=t.l5c18frq5wuo#heading=h.pfyir0f9in9m)
[Background of the Study 8](?tab=t.l5c18frq5wuo#heading=h.ru9voj4svo13)
[Statement of the Problem 11](?tab=t.l5c18frq5wuo#heading=h.5vtj2v7i2xym)
[Scope and Limitations of the Study 12](?tab=t.l5c18frq5wuo#heading=h.h9wfw1quzb0m)
[Significance of the Study 16](?tab=t.l5c18frq5wuo#heading=h.mau388ysov2u)
1.  [REVIEW OF RELATED LITERATURE AND STUDIES 19](?tab=t.l5c18frq5wuo#heading=h.9h54nrhtm0ay)
[Review of Related Literatures 19](?tab=t.l5c18frq5wuo#heading=h.x3g3pytm71a3)
[Review of Related Studies 24](?tab=t.l5c18frq5wuo#heading=h.py3fppy23tp5)
[Conceptual Framework 31](?tab=t.l5c18frq5wuo#heading=h.u3u4updhyj3)
[Hypothesis 33](?tab=t.l5c18frq5wuo#heading=h.rcogfqi42u7)
[Operational Definition of Terms 33](?tab=t.l5c18frq5wuo#heading=h.bkq4o5zalkan)
1.  [METHODOLOGY 38](?tab=t.l5c18frq5wuo#heading=h.7dqawqrig5qw)
[Software Design and Development Approach 38](?tab=t.l5c18frq5wuo#heading=h.8i72i63cs6xj)
  - [Software Process Module 38](?tab=t.l5c18frq5wuo#heading=h.6rtk90dv135v)
  - [Software Framework 40](?tab=t.l5c18frq5wuo#heading=h.wqarth8kzu0c)
  - [Process Flow (HIPO and System Flowchart) 43](?tab=t.l5c18frq5wuo#heading=h.acsdb9gh97b9)
[Research Design 46](?tab=t.l5c18frq5wuo#heading=h.2qdk8iclkgs5)
[Conceptual and Procedural Overview 46](?tab=t.l5c18frq5wuo#heading=h.k0rym9xdtuol)
[Study Site, Locale, and Study Duration 47](?tab=t.l5c18frq5wuo#heading=h.ozke0gubl5ax)
[Determination of Sample Size 48](?tab=t.l5c18frq5wuo#heading=h.h7hu5ohr574k)
[Sampling Design and Technique 50](?tab=t.l5c18frq5wuo#heading=h.2pdmtdnovzk1)
[The Subject 51](?tab=t.l5c18frq5wuo#heading=h.onf4aq1jaq6q)
[Model Development and Experimental Procedures 54](?tab=t.l5c18frq5wuo#heading=h.2hthbk64ye83)
[System Implementation and Platform Features Under Evaluation 62](?tab=t.l5c18frq5wuo#heading=h.ey9aby59v7nt)
[The Research Instrument 66](?tab=t.l5c18frq5wuo#heading=h.8dp8eptzwje2)
[Data Gathering Procedures 67](?tab=t.l5c18frq5wuo#heading=h.9asif55331h)
[Data Collected, Confidentiality Safeguards, and Risk Minimization 69](?tab=t.l5c18frq5wuo#heading=h.xf7aei6o2jnx)
[Statistical Treatment of Data 71](?tab=t.l5c18frq5wuo#heading=h.euc9z6k5kguf)
[REFERENCES 73](?tab=t.l5c18frq5wuo#heading=h.7b52zlp545kb)
[APPENDICES 78](?tab=t.l5c18frq5wuo#heading=h.s5v4whutezwn)
[APPENDIX A: GANTT CHART 78](?tab=t.l5c18frq5wuo#heading=h.8ba5d64g0zjn)
[APPENDIX B: HIGH-FIDELITY PROTOTYPE ](?tab=t.l5c18frq5wuo#heading=h.o5mhkyve8132)80
[APPENDIX C: USER EVALUATION SURVEY 9](?tab=t.l5c18frq5wuo#heading=h.9abj4app0ho4)3
[APPENDIX D: EXPERT EVALUATION SURVEY ](?tab=t.l5c18frq5wuo#heading=h.h5aveaiaeseb)100
[APPENDIX E: LETTER TO THE HEAD OF THE ORGANIZATION 10](?tab=t.l5c18frq5wuo#heading=h.1r4hc2grky6b)6
[APPENDIX F: CERC RESULT 10](?tab=t.l5c18frq5wuo#heading=h.nhuat0rii80n)9
[APPENDIX G: REVISION LIST 11](?tab=t.l5c18frq5wuo#heading=h.c00il9gb7h9z)3
LIST OF FIGURES
TITLE                                                                                                             PAGE
[Figure 1. Conceptual Framework 31](?tab=t.l5c18frq5wuo#heading=h.r1c0joasztca)
[Figure 2. HIPO Chart 43](?tab=t.l5c18frq5wuo#heading=h.sxxhj7zaas3z)
[Figure 3. System Flowchart 44](?tab=t.l5c18frq5wuo#heading=h.79n3hwn5dms1)
[Figure 4. Cochran’s Formula for Continuous Data 48](?tab=t.l5c18frq5wuo#heading=h.bhse2ofxrxl8)
[Figure 5. Acceptable Margin of Error in Scale Points 48](?tab=t.l5c18frq5wuo#heading=h.aaqtnribfljk)
[Figure 6. Estimated Standard Deviation 49](?tab=t.l5c18frq5wuo#heading=h.a50t21bi8rq6)
[Figure 7. Estimated Respondents 49](?tab=t.l5c18frq5wuo#heading=h.espk8wekitv3)
[Figure 8. Target Responses per Strata 49](?tab=t.l5c18frq5wuo#heading=h.yn9linw1un4s)
[Figure 9. No. of Distributed Questionnaires Formula 50](?tab=t.l5c18frq5wuo#heading=h.jsfiii4ypfb3)
[Figure 10. No. of Distributed Questionnaires 50](?tab=t.l5c18frq5wuo#heading=h.c6driiigosrz)
[Figure 11. Hero Banner 79](?tab=t.l5c18frq5wuo#heading=h.whf3buf320gd)
[Figure 12. Deepfake 101 80](?tab=t.l5c18frq5wuo#heading=h.emp9c1u4kqkf)
[Figure 13. SwinFusion++ Model 81](?tab=t.l5c18frq5wuo#heading=h.raovg67ijt8f)
[Figure 14. Uploading Interface 82](?tab=t.l5c18frq5wuo#heading=h.omwwi5uuyo5n)
[Figure 15. Video Resolution Standards 83](?tab=t.l5c18frq5wuo#heading=h.ai783vlbn74d)
[Figure 16. Quick Start Guide 83](?tab=t.l5c18frq5wuo#heading=h.klrx6qfhwau6)
[Figure 17. Processing Interface 84](?tab=t.l5c18frq5wuo#heading=h.tbbgaswc9eti)
[Figure 18. Invalid Format 85](?tab=t.l5c18frq5wuo#heading=h.kgqmu09fyzhu)
[Figure 19. Unsupported Minimum Resolution 85](?tab=t.l5c18frq5wuo#heading=h.5xhjkuz3kpfc)
[Figure 20. Unsupported Maximum Resolution 85](?tab=t.l5c18frq5wuo#heading=h.y867idhnw6d9)
[Figure 21. Low Resolution 85](?tab=t.l5c18frq5wuo#heading=h.s1muo7dpx10e)
[Figure 22. Medium Resolution 86](?tab=t.l5c18frq5wuo#heading=h.3kz5gx240rmq)
[Figure 23. Large File 86](?tab=t.l5c18frq5wuo#heading=h.elz6hgcif92k)
[Figure 24. File Too Large 86](?tab=t.l5c18frq5wuo#heading=h.q6w5l02cmswc)
[Figure 25. File Too Long 86](?tab=t.l5c18frq5wuo#heading=h.rbj3fah0qp4c)
[Figure 26. Scan Failed 86](?tab=t.l5c18frq5wuo#heading=h.qavlk5dgk8sa)
[Figure 27. Server Offline 86](?tab=t.l5c18frq5wuo#heading=h.cedexj5vobqw)
[Figure 28. Results Interface 87](?tab=t.l5c18frq5wuo#heading=h.m92zbd42ofzf)
[Figure 29. About Page 88](?tab=t.l5c18frq5wuo#heading=h.yw9l5q65zfu)
[Figure 30. Contact Us Page 88](?tab=t.l5c18frq5wuo#heading=h.4ofyzwv4wpox)
[Figure 31. FAQs Page 88](?tab=t.l5c18frq5wuo#heading=h.xbfdifmhluyz)
[Figure 32. Privacy Policy 89](?tab=t.l5c18frq5wuo#heading=h.x9y91see2ra6)
[Figure 33. Terms & Conditions 89](?tab=t.l5c18frq5wuo#heading=h.ikdb3zsepscm)
[Figure 34. Disclaimer 89](?tab=t.l5c18frq5wuo#heading=h.9zapy6uz8z67)
[Figure 35. SwinFusion++ Page 90](?tab=t.l5c18frq5wuo#heading=h.fj5w37l5fbyz)
[Figure 36. Methodology Page 90](?tab=t.l5c18frq5wuo#heading=h.7ethtzmzc7zz)
[Figure 37. API Page 91](?tab=t.l5c18frq5wuo#heading=h.6a6bdzymyjlq)
[Figure 38. User Evaluation Survey - Starting Page 94](?tab=t.l5c18frq5wuo#heading=h.8n87dybo3lta)
[Figure 39. User Evaluation Survey - Informed Assent 95](?tab=t.l5c18frq5wuo#heading=h.h8e29cw2zb4f)
[Figure 40. User Evaluation Survey - Informed Consent 95](?tab=t.l5c18frq5wuo#heading=h.m9ryfedk3ukd)
[Figure 41. User Evaluation Survey - Personal Information 96](?tab=t.l5c18frq5wuo#heading=h.z7dslsifbsxv)
[Figure 42. User Evaluation Survey - Functional Suitability 96](?tab=t.l5c18frq5wuo#heading=h.yyfk36rrw8no)
[Figure 43. User Evaluation Survey - Usability 97](?tab=t.l5c18frq5wuo#heading=h.ckmyhuougjg4)
[Figure 44. User Evaluation Survey - Performance Efficiency 97](?tab=t.l5c18frq5wuo#heading=h.bjolmo1i5sg9)
[Figure 45. User Evaluation Survey - Security, Comments and/or Suggestions 98](?tab=t.l5c18frq5wuo#heading=h.jhaba62aqgzd)
[Figure 46. Expert Evaluation Survey - Starting Page 102](?tab=t.l5c18frq5wuo#heading=h.63k74sgh9dc8)
[Figure 47. Expert Evaluation Survey - Personal Information 102](?tab=t.l5c18frq5wuo#heading=h.v1qasv2sil5v)
[Figure 48. Expert Evaluation Survey - Learnability, Task Flow,](?tab=t.l5c18frq5wuo#heading=h.8i2zs8nvtbgs)
                   [System Feedback 103](?tab=t.l5c18frq5wuo#heading=h.8i2zs8nvtbgs)
[Figure 49. Expert Evaluation Survey - Error Prevention, Error Handling & Recovery, Language/Microcopy Clarity 103](?tab=t.l5c18frq5wuo#heading=h.hjchksxsqao3)
[Figure 50. Expert Evaluation Survey - Results Interpretability, Consistency & Standard, Help/Documentation/Transparency 104](?tab=t.l5c18frq5wuo#heading=h.889t94u22vut)
[Figure 51. Expert Evaluation Survey - Context of Use, End Question,](?tab=t.l5c18frq5wuo#heading=h.gy2aks9rym89)
                 [Comments and/or Suggestions 104](?tab=t.l5c18frq5wuo#heading=h.gy2aks9rym89)
[Figure 52. Letter to the Head of Organization - Page 1 105](?tab=t.l5c18frq5wuo#heading=h.cjkzu9xzyd4u)
[Figure 53. Letter to the Head of Organization - Page 2 106](?tab=t.l5c18frq5wuo#heading=h.7azziv5ovoy)
[Figure 54. Letter to the Head of Organization - Page 3 107](?tab=t.l5c18frq5wuo#heading=h.hist70bm9mqs)
[Figure 55. CERC Result - Page 1 108](?tab=t.l5c18frq5wuo#heading=h.kxb3okbaibga)
[Figure 56. CERC Result - Page 2 109](?tab=t.l5c18frq5wuo#heading=h.la1eq5nwao98)
[Figure 57. CERC Result - Page 3 110](?tab=t.l5c18frq5wuo#heading=h.i22g0ddf4xez)
[Figure 58. CERC Result - Page 4 111](?tab=t.l5c18frq5wuo#heading=h.v5fr8n2rib7f)
# Chapter 1 – THE PROBLEM AND ITS BACKGROUND
## _Introduction_
Digital video is widely treated as persuasive evidence–shared across social platforms, used in personal and institutional decision-making, and often assumed to “speak for itself.” This assumption is increasingly fragile. Advances in neural media synthesis have made it possible to generate or alter videos in ways that can convincingly mimic real human faces, expressions, and speech-related motion. As a result, deepfakes are no longer a novelty; they represent a practical threat to information integrity, identity protection, and verification workflows that depend on trust in visual media.
As manipulation quality improves, deepfake detection can no longer rely primarily on obvious, visible artifacts. Contemporary deepfakes may appear coherent frame-by-frame, and common real-world transformations–such as compression, resizing, and re-encoding–can further weaken superficial forensic signals. In this setting, detection becomes a video understanding problem, not just an image classification task. Reliable detection must account for both what the face looks like (spatial evidence) and how it behaves over time (temporal evidence), especially under conditions that differ from the training data.
Despite sustained progress, a central limitation remains: many detectors emphasize spatial appearance cues or treat temporal modeling as a loosely attached stage, which can underuse the structured relationship between appearance and motion that authentic video naturally follows. Few approaches explicitly learn interaction between spatial features and temporal dynamics in a way that is designed for robustness under distribution shift. This gap matters because deepfake cues may be weak, may appear at different scales, and may only become meaningful when motion and appearance are interpreted together rather than independently.
To address this gap, this study proposes SwinFusion++, a face-aligned spatio-temporal deepfake detection framework that couples a Swin Transformer-based spatial stream with a Video Swin Transformer-based temporal stream. The core architectural contribution is a hierarchical cross-attention fusion mechanism that enables structured interaction between the two streams across representation stages. This is not merely a convenience for feature combination. Hierarchical cross-attention is necessary because consistency in authentic video is multi-scale: fine-grained facial evidence and higher-level motion context should constraints jointly, SwinFusion++ is designed to better detect manipulations that evade detectors relying on isolated spatial cues or shallow temporal aggregation.
This study validates SwinFusion++ through a rigorous evaluation protocol using widely used benchmark datasets–FaceForensics++ (HQ/LQ) deepfake subsets, Celeb-DF (v2) and DeeperForensics 1.0–including both in-distribution testing and cross-dataset transfer evaluation to assess generalization under distribution shift. In addition, the research operationalizes the model through a web-based detection platform and evaluates the deployed system using ISO/IEC 25010-based user assessment, complemented by expert review, to measure not only detection performance but also usability-and deployment-relevant quality characteristics.
## _Background of the Study_
The rapid maturation of neural media synthesis has shifted the deepfake problem from a curiosity to a systematic risk for information integrity, digital forensics, and biometric security. Contemporary generators– spanning GAN-based pipelines and increasingly, diffusion-based models– can produce facial reenactment and full-frame video synthesis with photorealistic texture, coherent lighting, and plausible motion. As generation quality improves and post-processing becomes more sophisticated, the detection problem has evolved into an adversarial arms race: artifacts that once served as reliable signatures (e.g., boundary inconsistencies, color mismatch, or obvious blending) are progressively suppressed, redistributed, or made to resemble natural variation. Consequently, the central scientific challenge in deepfake detection is no longer merely spotting conspicuous defects, but rather discerning subtle, distributed inconsistencies that arise from imperfect modeling of identity, physiology, geometry and temporal dynamics.
Historically, a large portion of detection research has been dominated by Convolutional Neural Networks (CNNs). CNN-based detectors are well matched to local texture cues and short-range spatial correlations, and they have been effective when manipulations introduce localized artifacts–compression anomalies, blending seams, or frequency distortions. However, the inductive biases that make CNNs robust for local pattern recognition can become limiting for modern deepfakes. In particular, standard CNN hierarchies tend to emphasize locality and progressively pooled abstractions, which can dilute fine-grained forensic traces and underrepresent long-range dependencies (e.g., global facial geometry, lighting coherence across regions, or cross-part correlations such as eyes-mouth-cheeks). Moreover, many deepfake failures manifest as weak, spatially dispersed signals whose discriminative power emerges only when context is integrated across larger receptive fields and across time. This motivates the shift toward architectures that can represent both local forensics cues and global consistency constraints without sacrificing resolution.
Vision Transformers (ViTs) provide a principled mechanism to model long-range interactions via self-attention, enabling direct coupling between distant image regions and facilitating global reasoning that CNNs often approximate only indirectly. Yet, naive global attention scales poorly with input resolution and video length, creating practical barriers for deepfake detection, where subtle artifacts may require high resolution spatial evidence and temporally dense sampling. Put differently, the very regimes in which forensic traces are most informative (higher resolution, longer temporal context) are also those in which standard transformer attention becomes computationally and memory intensive. This tension has driven the emergence of hierarchical and windowed transformer families that retain transformer-style global reasoning while managing complexity through structured locality.
Among these, the Swin Transformer family is particularly relevant to forensic analysis because it explicitly operationalizes multi-scale representation learning while using shifted-window attention to expand effective receptive fields across layers. The hierarchical design supports feature pyramids analogous to strong CNN backbones, while the windowing strategy offers a tractable approximation to global attention that is compatible with higher resolutions. For video, Swin-style extensions further provide a structured way to capture spatiotemporal dependencies by applying attention over local 3D neighborhoods, enabling the model to represent motion-sensitive patterns without incurring the prohibitive cost of fully global space–time attention. These properties align well with the demands of deepfake detection: the detector must remain sensitive to fine spatial artifacts (micro-texture, subtle warping, and boundary statistics) while simultaneously enforcing coherence constraints that are inherently global and temporal (identity consistency, illumination continuity, motion plausibility, and physiological dynamics).
Nevertheless, applying transformers to deepfake video detection remains non-trivial. First, deepfakes can be locally convincing yet globally inconsistent, meaning detection requires a representation that is simultaneously high-resolution and context-aware. Second, the most discriminative cues are often cross-modal in nature within the visual stream: spatial appearance cues and temporal motion cues interact. For example, a manipulation may preserve per-frame realism but introduce temporal “phase” errors—slight asynchrony between lip motion and facial musculature, unnatural micro-motion, or inconsistent head–background parallax. Conversely, temporal smoothness can be enforced while compromising subtle spatial statistics. Architectures that treat spatial and temporal modeling as loosely coupled stages may therefore underutilize the joint structure of the problem, failing to learn the specific correspondences between where artifacts occur and how they evolve.
Motivated by these observations, this study proposes SwinFusion++, a spatiotemporal deepfake detection framework that explicitly couples spatial evidence and temporal dynamics. The proposed design extracts rich multi-scale spatial features using a Swin-based image backbone and complementary temporal representations using a Video Swin-based backbone. Crucially, rather than merely concatenating or late-fusing these representations, SwinFusion++ introduces a cross-attention fusion mechanism that learns structured interactions between appearance and motion features. This fusion is intended to model the conditional dependencies that characterize realistic video—i.e., how motion patterns should modulate spatial appearance and how spatial structures constrain plausible motion—thereby enabling the detector to identify subtle, temporally consistent manipulations that evade artifact-only or context-only approaches. In doing so, the study aims to advance deepfake detection toward models that are computationally feasible at meaningful resolutions while being architecturally aligned with the true spatiotemporal nature of video forgery.
## _Statement of the Problem_
Building on the preceding discussion, this study proposes SwinFusion++, a face‑aligned spatio‑temporal deepfake detection framework that combines Swin Transformer spatial representations with Video Swin Transformer temporal representations and integrates both streams through hierarchical cross‑attention fusion to better capture subtle spatio‑temporal inconsistencies in manipulated videos.
The primary objective of this research is to develop and evaluate SwinFusion++, a spatio-temporal architecture for deepfake detection. Given this context, the study seeks to answer the following research questions:
RQ1: To what extent does SwinFusion++ improve video-level deepfake detection performance compared with standalone Swin Transformer and standalone Video Swin Transformer under in-distribution and cross-dataset evaluation, in terms of Accuracy, Precision, Recall, F1-Score, and ROC-AUC?
RQ2: What is the performance of SwinFusion++ relative to established baselines when evaluated on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0?
RQ3: How does the performance of SwinFusion++ compare to CNN-LSTM models on the FaceForensics++ (HQ/LQ) dataset?
RQ4: Does the hierarchical cross-attention between Swin and Video Swin improve detection performance compared to other spatio-temporal models such as CAST and TSFF-Net?
RQ5: How do users evaluate the usability and performance of the SwinFusion++ platform?
RQ6: Does SwinFusion++ improve deepfake detection performance compared to existing CNN- and transformer-based spatio-temporal models, both within datasets and across diverse datasets?
## _Scope and Limitations of the Study_
Scope
This study develops and evaluates SwinFusion++, a spatio-temporal deepfake detection architecture that fuses spatial Swin Transformer features and temporal Video Swin Transformer features through a hierarchical cross-attention mechanism. The scope of this study is twofold: (1) to develop and benchmark SwinFusion++ under controlled experimental conditions, including in‑distribution evaluation and cross‑dataset transfer protocols; and (2) to demonstrate practical value through the implementation and evaluation of a deployable web‑based deepfake detection platform.
On the model development and benchmarking side, the study uses publicly available benchmark datasets for deepfake video detection–FaceForensics++(HQ/LQ) deepfake subsets, Celeb-DF (v2) and DeeperForensics-1.0–treating each video as a supervised sample with ground-truth labels (authentic vs. manipulated). The model’s effectiveness is assessed using standard performance metrics, including those appropriate for binary detection and comparative analysis. To specifically address real-world robustness and distribution shift, the evaluation includes both in-distribution evaluation (train/test within the same dataset) and cross-dataset transfer evaluation (train on one dataset and test on others).
SwinFusion++ is also benchmarked relative to established baselines (e.g., CNN-LSTM and recent fusion-oriented spatio-temporal approaches) using their previously reported results. To ensure that comparisons are meaningful and attributable to model design (rather than inconsistent preprocessing), the controlled comparison is made against standalone Swin-B and Video Swin-B, which are trained and evaluated with the same preprocessing, training recipe, and evaluation logic as SwinFusion++.
On the deployment side, the study implements a lightweight web interface/API that operationalizes SwinFusion++ for user-accessible inference. The platform is designed as an interactive workflow (Upload → Processing → Results), supports core user functions (video upload, standardized preprocessing/inference, and results presentation), and returns interpretable outputs including a classification label (Real/Fake), confidence score, and contextual metadata.
On the human evaluation side, the implemented platform is evaluated using an ISO/IEC 25010-based user assessment, focusing on functional suitability, usability, performance efficiency, and security, complemented by expert-oriented usability/interaction assessment aligned with ISO guidance (e.g., interaction and usability concepts and practical heuristic evaluation principles). End-user respondents are drawn from the University of the East (UE) community, while expert evaluators are sourced from cybersecurity practitioners within Metro Manila, with evaluation conducted through remote/online procedures to reflect ordinary context-of-use conditions.
Limitations
  - The model’s performance may vary based on the quality of deepfake videos. It is likely to perform well on high-resolution, high-quality deepfakes but may struggle with low-resolution or noisy videos, where subtle manipulation artifacts can be difficult to detect.
  - This study focuses exclusively on video-based deepfake detection and does not consider audio manipulations. As a result, the model may not be effective in detecting multimodal deepfakes that combine both video and audio manipulations.
  - Video-level decision. In the benchmark evaluation, each video is judged from a fixed number of short face clips sampled at a reduced frame rate, and the clip scores are averaged into one video-level score. A manipulation that affects only a short part of a longer video, or an artifact that appears only between consecutive frames at the original frame rate, may therefore have a weaker effect on the final score, and short clips, low-frame-rate footage, or videos with little facial motion give the temporal stream less evidence.
  - Performance and processing time may be affected by the input video’s duration, frame rate, and file size, since longer/higher-FPS videos require more frames to be analyzed. Detection may also degrade under heavy compression and other quality losses (e.g., blur/noise/low-light), which can mask the visual artifacts the model relies on.
  - The study’s findings are based on public benchmark datasets; performance may vary when applied to real-world videos with unseen manipulation methods, diverse capture devices, or post-processing pipelines.
  - Manipulation types. From FaceForensics++, only the DeepFakes subset is used; the other manipulation subsets, such as Face2Face, FaceSwap, and NeuralTextures, are not. All three benchmarks therefore contain face swaps only, and because they were released in 2019 and 2020, the results do not cover expression reenactment, lip-sync manipulation, fully synthetic faces, diffusion-based video generation, or face-swap tools released after 2020.
  - Population coverage. The benchmark datasets were not collected to represent Filipino subjects or Philippine media, and performance is not measured separately by age, sex, or skin tone. Equal performance across demographic groups is therefore not established.
  - Shared footage. DeeperForensics-1.0 creates its manipulated videos by swapping new faces into FaceForensics++ videos, and its real class in this study consists of those FaceForensics++ originals, so transfer between these two datasets is not fully independent; subsets without shared footage are analyzed but are small (20 to 60 videos for these directions). Transfer from FaceForensics++ C23 to C40 tests the same videos under stronger compression rather than a new dataset. In addition, the face-preprocessing rules were developed on training videos, some of which share footage with held-out videos, and frames from some held-out videos were viewed, without labels or scores, during face-quality review.
  - The model’s performance may be affected by face detection and alignment reliability; failures under occlusion, extreme head pose, or poor lighting may reduce detection accuracy.
  - Face-centric evidence focus. The SwinFusion++ pipeline relies on face detection/alignment and therefore prioritizes face-centered manipulations. Videos where manipulation is primarily non-facial (e.g., body/scene edits) or where faces are not consistently detectable may not be well-served by the system’s evidence extraction strategy.
  - Benchmark ceiling and transfer. When trained and tested on the same benchmark, the three models compared in this study all score close to the maximum, so differences between them within a single benchmark are small and hard to detect. Every model, SwinFusion++ included, performs less well on datasets it was not trained on. Differences between the models are therefore more informative under cross-dataset transfer, and any transfer advantage is relative to the compared encoders; detection on unseen data remains an open problem.
  - Statistical precision. The test sets contain 280 videos for each FaceForensics++ quality level, 978 for Celeb-DF v2, and 402 for DeeperForensics-1.0, with related videos kept in the same partition. All manipulated Celeb-DF v2 test videos come from nine identities, so its confidence intervals are approximate, and most of its test videos are manipulated, so its accuracy is read together with ROC-AUC. SwinFusion++, Swin-B, and Video Swin-B are each trained with three random seeds and evaluated as three-seed ensembles, which show whether results are stable across training runs but do not measure seed-to-seed variation precisely. Small differences between models may therefore go undetected.
  - Published comparisons. Established baselines, including the CNN-LSTM models, CAST, and TSFF-Net, are not retrained; their results are taken from published papers and from the research team’s preliminary study (Custodio et al., 2026), which use their own data splits, preprocessing, and evaluation units, so these comparisons place SwinFusion++ in context rather than serving as controlled head-to-head tests.
  - Training recipe and tuning. In the principal comparison, SwinFusion++, Swin-B, and Video Swin-B are trained with one shared fixed recipe, so none receives tuning the others do not, although the shared recipe may not be the best setting for each model. Bayesian hyperparameter optimization is applied to SwinFusion++ only, so the optimized model is reported separately as a configured system and is not used to judge the architecture.
  - Model size and cost. SwinFusion++ runs both backbones, so it has about 181 million parameters, against about 87 million for Swin-B and 88 million for Video Swin-B, and needs about twice the training memory of one backbone; the fusion module itself adds only about 6.5 million parameters. Inference latency on the deployment server is not benchmarked, and the model is not compressed (for example, by pruning, distillation, or quantization). Because two encoders are combined, part of an advantage over a single encoder may come from the combination rather than from the fusion module; Chapter 4 examines this under RQ4.
  - Decision thresholds and confidence values. Each model’s decision threshold is chosen on the validation data of its training dataset and kept unchanged when the model is tested on other datasets. On a dataset with a different distribution, a fixed threshold can make a detector too cautious or too permissive, so threshold-based measures (accuracy, precision, recall, and F1-score) under transfer are read together with ROC-AUC, which does not depend on a single threshold. For the same reason, the platform’s verdict and confidence value are most reliable for videos similar to the training data.
  - Binary decision support, not forensic proof. The platform produces a probabilistic classification output (Real/Fake with confidence and metadata). This is decision support for screening and verification workflows, but it does not, by itself, constitute definitive proof of authenticity for legal or evidentiary contexts.
  - Evidence maps. The evidence maps shown by the platform highlight the facial regions that most influenced a result. They are not validated as faithful explanations of the model’s decision, and they do not identify which frames or regions were manipulated or which manipulation method was used.
  - Platform and benchmark results. The detection results in Chapter 4 come from the offline benchmark evaluation, which scores seven fixed clips per video. The platform instead analyzes the whole video for its verdict, so its outputs can differ from the benchmark results, and its own detection accuracy is not measured. The detector recommendations and the Auto option’s selection rules describe the typical content of each training dataset and are not evaluated. The user and expert evaluation assesses the platform’s quality in use, not its detection accuracy.
  - Prototype deployment constraints. Inference time and throughput are dependent on the deployment environment (server hardware, concurrency, and upload bandwidth). The platform is evaluated as a functional research prototype and may require additional engineering for high-traffic production environments (e.g., load balancing, rate limiting, hardened storage policies, and formal penetration testing).
  - The deployed web-based prototype accepts one video per submission only, with a length of 10 seconds to 2 minutes, a resolution of 360p to 1080p, and a maximum file size of 250 MB; links are accepted only for public videos from TikTok, Facebook, X, or Reddit. Longer, larger, or higher-resolution videos must be trimmed, compressed, or downscaled before upload, and shorter or lower-resolution videos cannot be checked. This limitation is set to keep upload handling, preprocessing, and inference within a manageable range for a research prototype and to prevent batch-style or high-throughput use that falls outside the intended scope of the study.
  - Respondent sample. End users were drawn from the University of the East community, aged 15 to 59, through quota and purposive sampling, and experts from organizations in Metro Manila through purposive sampling. Because these are non-probability samples, the results describe the participating respondents and cannot be generalized to all social-media users. The sample size was set with Cochran’s formula, which assumes random sampling; with quota and purposive sampling, it served as a planning target, and no sampling margin of error is claimed for the results.
  - Self-reported ratings. The ISO/IEC 25010-based questionnaires record how respondents perceived the platform during short, first-time, task-based sessions with researcher-provided or authorized test clips; during the evaluation period, the built-in sample clips were all deepfakes. Security is rated as perceived and is not verified through penetration testing or a formal security audit; uploads pass through third-party hosting and GPU services, and their automatic deletion is not independently audited. Performance-efficiency ratings reflect the server’s speed and availability between 12 and 30 October 2026, including start-up delays after idle periods.
## _Significance of the Study_
Deepfake harms are not evenly distributed. In many real-world contexts, the individuals most vulnerable to deception are not necessarily those most capable of verifying media authenticity. Because SwinFusion++ is developed as both a robust detection model and a deployable platform evaluated for usability and software quality, its significance is inherently societal, technical, and institutional—bridging detection performance with real-world adoptability.
Older Generations and Not Digitally Literate Users. Older generations and individuals with limited digital literacy are disproportionately exposed to manipulation risks because they are more likely to treat video as persuasive evidence and less likely to have the tools or technical familiarity needed for verification. By developing a detection system that can be deployed through an accessible web platform and designed to communicate outputs clearly (label + confidence + metadata), this study contributes toward stronger safeguards against malicious deepfake use–reducing risks of deception, misinformation exposure, identity theft, harassment, and reputational harm.
General Public and Social Media Users. Beyond older adults, the general public and social media users benefit from tools that can support everyday authenticity checks, particularly in high-velocity information environments where manipulated videos can circulate faster than human review processes. The study’s emphasis on cross-dataset evaluation strengthens the practical relevance of the detector for online settings, where the manipulation source and generation pipeline are rarely known in advance.
Cybersecurity, Digital Forensics, and Law Enforcement Stakeholders. For cybersecurity teams and law enforcement stakeholders, deepfakes increasingly intersect with online fraud, impersonation, and disinformation operations. This study contributes to a deployable detection approach that can support investigative triage and risk assessment when synthetic media is suspected, especially when rapid initial screening is required before deeper forensic examination.
Media and Entertainment Industry, Content Integrity, and Platform Trust. Media organizations and production stakeholders face practical concerns around content integrity, reputational harm, and unauthorized manipulation of audiovisual assets. A web-deployable detector that emphasizes usability and interpretability can support workflows for authenticating content, identifying suspicious material early, and strengthening trust in media assets and publishing pipelines.
Educational Institutions and Future Researchers. Academically, this study contributes by consolidating (a) a spatio-temporal transformer-based fusion approach designed for robustness, (b) a structured benchmarking protocol emphasizing cross-dataset transfer, and (c) a human-centered software evaluation layer grounded in recognized standards. As such, the work can serve as a reference point for future research on multimodal deep learning, spatio-temporal modeling, robustness under distribution shift, and human-centered deployment of machine learning systems.
# Chapter 2 – REVIEW OF RELATED LITERATURE AND STUDIES
## _Review of Related Literatures_
Deepfake detection research sits at the intersection of synthetic media generation, digital video forensics, and deployable human-facing systems. Recent deepfake generators can produce photorealistic facial content under common online conditions such as compression, resizing, and re-encoding, which complicates authenticity judgments that historically relied on human perception and obvious editing artifacts (Dolhansky et al., 2020; Rössler et al., 2019). Consequently, contemporary detection must be framed not only as a classification task, but also as a robustness problem under distribution shift, where detectors must generalize across datasets, manipulation families, and post-processing pipelines (Jiang et al., 2020; Li et al., 2020). At the same time, practical solutions increasingly take the form of web-accessible tools, which means that software quality, usability, performance efficiency, and security become part of the overall research contribution (International Organization for Standardization [ISO], 2018; ISO, 2023).
Foreign and local literature first converge on the idea that deepfakes weaken the traditional credibility of video as evidence. Deepfakes are commonly defined as AI-enabled media manipulations that synthesize or alter identity-relevant content, especially faces, in ways that can appear realistic to ordinary viewers. Because manipulated videos can now be created at scale and redistributed through heavily compressed platforms, visual plausibility alone is no longer a reliable indicator of authenticity. This concern is likewise reflected in the Philippine context, where local literature has begun to frame deepfakes as a practical threat to political discourse, public trust, and reputational safety, while educational studies note that users encounter AI-generated audio-visual content with varying levels of understanding and verification ability (Dolhansky et al., 2020; Rössler et al., 2019; Matern et al., 2019; Wang et al., 2020; Estrellado et al., 2025; Tadena et al., 2025).
This erosion of visual credibility becomes more serious as generative modeling continues to improve. GAN-based pipelines first raised the realism of facial synthesis and manipulation, while diffusion-based models further enhanced perceptual fidelity, texture realism, and visual coherence (Goodfellow et al., 2014; Ho et al., 2020; Li et al., 2020). As a result, many earlier artifact cues have become less stable across generator families and post-processing conditions. Thus, the literature increasingly argues that detectors must be evaluated not only against a fixed manipulation type, but also under conditions in which manipulation quality and generation pipelines vary substantially. In turn, this has encouraged the shift from narrow, hand-engineered signatures toward learning-based detectors that can exploit subtle, distributed, and evolving evidence (Dolhansky et al., 2020; Chen et al., 2022; Jiang et al., 2020).
Because of this shift, digital video forensics now treats authenticity as a multi-scale spatio-temporal problem rather than a purely visual one. Authentic videos are constrained not only by local texture statistics, but also by global facial structure, region-to-region coherence, lighting continuity, motion stability, and physiological behavior across time. Therefore, deepfake detection increasingly depends on combining local texture irregularities, higher-level semantic or geometric consistency, and sequence-level continuity. This perspective is important because a deepfake may appear realistic in isolated frames while still violating the relationships that should remain stable across the full clip. For this reason, the most relevant literature consistently presents detection as joint reasoning over appearance and motion rather than independent frame classification (Güera & Delp, 2018; Haliassos et al., 2021; Chen et al., 2022; Montserrat et al., 2020).
In direct relation to the present study, the literature also shows why transformer-based modeling has become especially important. Attention mechanisms enable direct modeling of long-range dependencies, which is valuable in deepfake forensics because authenticity cues may involve relationships among distant facial regions rather than only local defects (Vaswani et al., 2017). However, fully global attention is expensive at high resolutions and long sequence lengths, which are precisely the conditions needed to preserve subtle forensic traces. Hierarchical and window-based transformers address this limitation by balancing detail preservation and contextual reasoning. The Swin Transformer achieves this through shifted-window attention and multi-scale representations, while the Video Swin Transformer extends the same principle to spatio-temporal neighborhoods (Liu et al., 2021; Liu et al., 2022). Building on this direction, recent literature also emphasizes cross-attention fusion, where one feature stream conditions another so that spatial appearance cues and temporal dynamics can constrain and validate each other more effectively than in simple concatenation schemes (Thakre et al., 2025; Zhao et al., 2023; Zhang et al., 2024).
Even with stronger architectures, the literature repeatedly warns that high accuracy within a single dataset can be misleading. FaceForensics++, Celeb-DF (v2), and DeeperForensics-1.0 are important not only because they are widely used, but also because each stresses a different aspect of the detection problem. FaceForensics++ highlights the effect of compression, Celeb-DF increases realism and reduces obvious artifacts, and DeeperForensics-1.0 introduces perturbations that reflect real-world degradation. Together, these datasets show that a detector may appear strong while actually relying on shortcuts tied to collection quirks, compression settings, or preprocessing routines. Thus, cross-dataset transfer testing and perturbation-stressed evaluation are now treated as necessary safeguards against overestimating real-world robustness (Rössler et al., 2019; Li et al., 2020; Jiang et al., 2020; Geirhos et al., 2020).
Furthermore, the literature highlights that robust detection is not only a matter of model architecture, but also of evidence quality. Because many deepfake manipulations are face-centered, face alignment and identity-consistency checks are commonly used to reduce background noise, stabilize the spatial reference frame, and prevent wrong-face drift across frames. Methods such as MTCNN support reliable face detection and landmark-based alignment, while FaceNet-style embeddings can help maintain within-video identity consistency. Accordingly, preprocessing becomes an operational requirement rather than a minor convenience, since weak or inconsistent facial evidence can distort both spatial representation learning and temporal reasoning (Zhang et al., 2016; Schroff et al., 2015; Jiang et al., 2020; Montserrat et al., 2020).
Local literature further strengthens the relevance of deployable deepfake detection in the Philippine setting. Studies and policy discussions indicate that synthetic media now intersects with misinformation, identity deception, and public distrust, which makes verification tools socially relevant beyond technical experimentation (Estrellado et al., 2025). At the same time, unequal ICT access and differences in digital skill across age groups mean that a web-based detector must be evaluated not only for predictive output, but also for learnability, clarity, efficiency, and accessibility in ordinary use conditions. In this sense, local literature supports the use of structured software quality and usability frameworks, particularly ISO 9241-11 and ISO/IEC 25010, because system value depends not only on algorithmic performance but also on whether users can understand the workflow and correctly interpret the result (Albert et al., 2021; Tadena et al., 2025; Urera & Balahadia, 2019; ISO, 2018; ISO, 2023).
Finally, the Philippine legal and ethical context adds another layer of importance to deployable systems. Proposed measures such as House Bill No. 10567 and House Bill No. 3214 show growing recognition that deepfakes can cause harms beyond ordinary misinformation, while the Data Privacy Act of 2012 makes privacy-by-design directly relevant to systems that accept uploaded videos. In research settings, Philippine Health Research Ethics Board (PHREB) guidance and youth-related protections under Republic Act No. 8044 reinforce the need for consent, assent, risk minimization, and careful handling of participant data and media. Therefore, the literature as a whole points toward a clear gap: there is a need for a deepfake detection approach that is spatio-temporal, computationally practical, robust across datasets, and operationalized through a usable and privacy-conscious platform suited to its local context. This gap directly supports the proposed SwinFusion++ framework, which combines face-aligned preprocessing, hierarchical spatial and temporal transformer modeling, cross-attention-based evidence fusion, and standards-informed platform evaluation (Republic Act No. 10173, 2012; Republic Act No. 8044, 1995; PHREB, 2022; House Bill No. 10567, 2024; House Bill No. 3214, 2025).
## _Review of Related Studies_
Deepfake detection has evolved from a simple forensic task, looking for obvious editing mistakes, into a much harder problem of generalizing across space and time. Today’s generators, first mostly GAN-based and now increasingly diffusion-based, can create videos that look realistic frame by frame, remain stable across time, and still pass through heavy platform processing such as compression, resizing, and re-encoding. In this environment, there is rarely one clear artifact that consistently reveals manipulation. Instead, the useful clues are often subtle, scattered across different facial areas, dependent on motion, and easily distorted by video compression. Because of this, modern detectors must combine fine spatial traces, global structure, and temporal coherence. This is exactly the setting that motivates SwinFusion++, which aims to preserve high-resolution facial detail while learning long-range spatio-temporal relationships efficiently.
The studies most directly related to SwinFusion++ are those that employ spatio-temporal transformers and cross-attention-based fusion. Zheng et al. (2021) explored temporal coherence for more general video face forgery detection, while Zhao et al. (2023) proposed ISTVT, an interpretable spatial-temporal video transformer that highlights inter-frame inconsistency. Likewise, CAST applies multi-head cross-attention between spatial and temporal streams and reports strong cross-dataset results, while TSFF-Net shows that attention-based fusion across complementary feature domains can improve detection over single-branch or shallow-fusion designs (Thakre et al., 2025; Zhang et al., 2024). These studies are important because they shift the problem from simple feature extraction to evidence interaction, showing that the detector must learn how one cue reweights or validates another under varying conditions.
Supporting this direction, several studies demonstrate the value of transformers and hierarchical attention for deepfake forensics. Khan and Dai (2021), Deng et al. (2023), Lin et al. (2023), and Wodajo and Atnafu (2021) show that attention-based or hybrid CNN-transformer models can improve global representation learning and detection performance by modeling long-range relationships across facial regions. These studies reinforce two important points. First, authenticity cues are not always local, since coherence among distant parts of the face can be as informative as micro-artifacts. Second, hierarchical or window-based attention is practical because it preserves fine detail while managing the cost of high-resolution analysis. At the same time, many of these models still place transformers after CNN bottlenecks or treat temporal reasoning as secondary, which helps explain why a more unified dual-transformer design remains necessary.
Earlier temporal studies also provide strong empirical support for the present research. Güera and Delp (2018) showed that recurrent neural networks can detect deepfakes from frame sequences, Masi et al. (2020) used a two-branch recurrent design to capture inter-frame dependencies, Montserrat et al. (2020) proposed Automatic Face Weighting to reduce the influence of irrelevant facial regions, and Haliassos et al. (2021) argued that realistic lip motion is difficult to synthesize consistently and therefore highly informative. Chen et al. (2022) further demonstrated that spatio-temporal attention and convolutional LSTMs can improve detection by reasoning jointly about spatial artifacts and temporal dependencies. Collectively, these studies show that authenticity must be assessed not only by whether each frame appears realistic, but also by whether the motion trajectory, identity continuity, and physiological behavior remain plausible across the entire sequence.
Frame-level spatial studies remain valuable because they established that visually convincing deepfakes can still differ statistically from authentic content. Guo et al. (2020) argued that generators leave traces in the residual domain, Kumar et al. (2020) showed that ResNet-based models can detect reenactment cues, Wang et al. (2020) proposed FakeSpotter to distinguish real and synthetic faces through neuron behavior, and Kingra et al. (2023) used a Siamese design to emphasize source-camera-noise discrepancies. These studies prove that frame-based evidence matters, especially when manipulation introduces subtle spatial irregularities. Nevertheless, they also reveal a consistent limitation: strong frame-level accuracy does not guarantee that a detector can capture sequence-level inconsistency or generalize under realistic platform transformations such as compression, blur, and re-encoding.
Related studies on residual and frequency-based evidence further support a multi-cue perspective. Guarnera et al. (2020) examined convolutional traces associated with GAN generation, while Kohli and Gupta (2021) used frequency-domain cues to detect manipulated facial videos. These studies demonstrate that a deepfake may successfully reproduce facial appearance while still failing to replicate the statistical signature of natural imaging pipelines. However, they also show why cue fragility remains a concern, because compression, resizing, and re-encoding can distort the very frequency patterns these models depend upon. For this reason, their broader contribution lies in strengthening the argument that robust detection should not rely on one evidence domain alone, but should learn how different signals complement one another under varying video conditions.
Foundational artifact-based studies remain important because they first established deepfake detection as a problem of violated real-world constraints. Li and Lyu (2018) detected face-warping artifacts, Li et al. (2018) used abnormal eye blinking as a temporal cue, and Matern et al. (2019) showed that manipulated faces often contain visible inconsistencies in edges and facial details. These studies proved that deepfakes often fail not because a single frame looks implausible, but because blending, geometry, and physiological behavior are imperfectly enforced. Even so, later studies reveal the weakness of depending on a single signature, since improvements in generation quality and heavy post-processing can suppress or imitate those cues. Therefore, these early works are best understood as the starting point of a progression that later moved toward multi-scale and spatio-temporal learning.
Local studies and Philippine-based evidence make the deployment side of the present study more concrete. Albert et al. (2021) show that access to computers and internet use vary widely across age groups in the Philippines, which directly affects how realistic a web-based deepfake detection platform can be under ordinary conditions. This evidence matters because system success cannot be measured by model accuracy alone. The platform must also remain understandable, efficient, and usable across mixed devices, internet conditions, and levels of digital familiarity. In this respect, local findings support evaluating SwinFusion++ as a public-facing decision-support tool rather than as an isolated technical model.
Philippine practice in software evaluation also supports the study’s methodological design. Urera and Balahadia (2019) provide a local precedent for structured system evaluation, while ISO 9241-11 and ISO/IEC 25010 strengthen the choice to assess functional suitability, usability, performance efficiency, security, and interaction capability in a defined context of use. These studies and frameworks are relevant because a deepfake detector that outputs a Real or Fake label with confidence must communicate uncertainty, guide user interpretation, and support error recovery. As a result, the evaluation of the deployed SwinFusion++ platform appropriately extends beyond interface appearance to include task clarity, feedback visibility, interpretability, and context-of-use readiness (Urera & Balahadia, 2019; ISO, 2018; ISO, 2023; ISO/IEC 25000, n.d.).
Local legal and ethical frameworks likewise influence the present study. Republic Act No. 8044 and PHREB guidance are relevant because the study includes youth participants and online human evaluation, while Republic Act No. 10173 is directly relevant to data handling for uploaded media. In addition, ongoing policy discussions reflected in House Bill No. 10567 and House Bill No. 3214 indicate that deepfake governance is becoming an increasingly important concern in the Philippines. These local sources show that responsible deployment requires privacy safeguards, transparent instructions, consent procedures, and limits on how uploaded videos are processed and retained. Thus, local studies and frameworks extend the discussion from detection accuracy to lawful and ethical operationalization (Republic Act No. 8044, 1995; PHREB, 2022; Republic Act No. 10173, 2012; House Bill No. 10567, 2024; House Bill No. 3214, 2025).
Taken together, the related studies show a consistent progression from narrow artifact detection to integrated spatio-temporal reasoning and deployment-aware evaluation. Early detectors established important forensic cues, spatial and temporal models improved performance, and recent transformer and cross-attention studies moved closest to the requirements of the present research. However, many prior systems still rely on shallow fusion, CNN bottlenecks, limited robustness testing, or narrowly defined deployment assumptions. Local studies then add a second layer to the gap by showing that, in the Philippine context, a useful deepfake detector must also be usable, interpretable, privacy-conscious, and evaluated under realistic access conditions. This combined technical and socio-technical gap justifies SwinFusion++ as both a hierarchical spatio-temporal fusion model and a web-based decision-support platform (Chen et al., 2022; Zhao et al., 2023; Thakre et al., 2025; Albert et al., 2021; ISO, 2023).
## Conceptual Framework
[image]
#### Figure 1. Conceptual Framework
The conceptual framework is structured as an Input–Process–Output (IPO) model that clarifies how the SwinFusion++ deepfake detection system is developed, validated, and interpreted in a traceable way. The Input component specifies the study’s core resources: benchmark datasets (FaceForensics++, Celeb-DF, and DeeperForensics-1.0), pre-trained backbones (Swin Transformer Base and Video Swin Transformer Base), implementation tools (Python with deep-learning frameworks such as PyTorch/TensorFlow and supporting libraries), and key preprocessing components (MTCNN for face detection/alignment and FaceNet for face verification).
These inputs are transformed in the Process component through three connected stages: (1) Data Preparation, where facial evidence is standardized via alignment and identity verification, with training-only RandAugment augmentation—operationalized as controlled randomized transformations applied in a manner that preserves clip integrity—and class-balanced training sampling (class → source or identity group → video → clip); (2) Model Training, where spatial and temporal representations are learned by fine-tuning the Swin (spatial) and Video Swin (temporal) branches, extracting features from both streams, and integrating them through a cross-attention fusion block before producing a binary Real–Fake decision; and (3) Optimization, where a shared fixed training recipe is used for the architecture comparison, Bayesian hyperparameter optimization (Optuna/TPE) tunes the training settings of SwinFusion++ as a separately reported configured system, and the experimental protocol is operationalized using official or 70–15–15 group-disjoint splits and a cross-dataset evaluation setup, with performance measured using ROC-based and standard classification metrics (ROC, accuracy, precision, recall, and F1-score).
The Output component consists of (a) a trained SwinFusion++ model capable of detecting deepfakes and (b) comparative findings that position its performance against baseline CNN- and transformer-based detectors, including evidence of how well it generalizes across datasets. Finally, the Evaluation component serves as the study’s validation and feedback layer by quantifying performance using the stated metrics, testing generalization via train-on-one/test-on-others transfer, benchmarking against established models, and conducting robustness checks under stressors such as noise, compression, and adversarial variations—thereby ensuring that conclusions about effectiveness are grounded not only in in-dataset accuracy but also in demonstrated robustness under distribution shift.
## _Hypothesis_
H0: SwinFusion++ does not improve deepfake detection performance compared to existing CNN- or transformer-based spatio-temporal models.
H1: SwinFusion++ improves deepfake detection performance compared to existing CNN- or transformer-based spatio-temporal models.
## _Operational Definition of Terms_
Deepfake
In this study, a deepfake refers to any video sample whose ground-truth label is “manipulated” in the selected benchmark datasets. Operationally, it represents synthetic or AI-altered facial content designed to mimic authentic video appearance and is treated as the Fake class in binary classification experiments.
Authentic Video
In this study, an authentic video refers to any video sample labeled “real/authentic” in the benchmark datasets. Operationally, it is treated as the Real class instance used for supervised model training and evaluation.
Ground-Truth Label
In this study, the ground-truth label refers to the dataset-provided reference class annotation (authentic vs. manipulated). Operationally, it serves as the training supervision target and the standard reference for computing all reported performance metrics.
Supervised Sample
In this study, a supervised sample refers to a single labeled video instance treated as one example in the experimental pipeline. Operationally, each supervised sample is processed through the same face-aligned preprocessing workflow and is evaluated by comparing the model’s output against its ground-truth label.
Benchmark Datasets
In this study, benchmark datasets refer to the public datasets used as experimental sources of labeled authentic and deepfake videos: FaceForensics++ (HQ/LQ) deepfake subsets, Celeb‑DF (v2), and DeeperForensics‑1.0. Operationally, these datasets define the sample pool for training/testing and provide standardized conditions for comparative and robustness evaluation.
HQ/LQ (High Quality / Low Quality) in FaceForensics++
In this study, HQ/LQ refers to the two quality conditions of FaceForensics++ used as distinct evaluation stressors. Operationally, HQ and LQ represent higher- versus lower-quality/compression regimes used to test whether the detector remains effective under quality degradation.
Deepfake Detection
In this study, deepfake detection refers to the computational task of classifying a video sample into one of two classes (Real or Fake) by learning discriminative evidence from face-centered spatio-temporal cues. Operationally, detection performance is assessed under both in-distribution and cross-dataset transfer settings using standard binary classification metrics.
Face‑Aligned Preprocessing Pipeline
In this study, the face-aligned preprocessing pipeline refers to the standardized procedure used to convert raw videos into consistent face-centered inputs for modeling. Operationally, it includes: (a) frame-wise extraction, (b) face detection and alignment using MTCNN, (c) cropping and resizing to 224 x 224 pixels, (d) identity-consistency filtering using FaceNet-style 512-D embeddings compared across frames to reduce mismatched or unstable face tracks, and (e) grouping of the aligned face crops into 16-frame clips sampled at 2 frames per second.
Clip/Sequence
In this study, a clip/sequence refers to a temporally ordered set of frames treated as a single input unit for spatio-temporal modeling. Operationally, clips preserve temporal order so the model can learn time-dependent consistency cues (motion coherence and evolving artifacts) rather than relying only on independent frame evidence.
SwinFusion++
In this study, SwinFusion++ refers to the proposed face-aligned spatio-temporal deepfake detection architecture. Operationally, it is implemented as a dual-stream transformer framework that extracts spatial evidence using a Swin-based backbone, extracts temporal evidence using a Video Swin-based backbone, and produces a final binary classification through a learned fusion mechanism.
Spatial Stream (Swin Transformer Stream)
In this study, the spatial stream refers to the Swin Transformer-based component that extracts hierarchical multi-scale spatial features from aligned face crops. Operationally, it emphasizes spatial forensic cues such as subtle texture irregularities, blending remnants, and spatial inconsistency patterns relevant to manipulation detection.
Temporal Stream (Video Swin Transformer Stream)
In this study, the temporal stream refers to the Video Swin Transformer-based component that models spatio-temporal dependencies across clips/sequences. Operationally, it captures motion- and continuity-related cues (e.g., temporal coherence, identity stability across frames, and evolving artifacts) that are not reliably detected from single frames alone.
Hierarchical Cross‑Attention Fusion
In this study, hierarchical cross-attention fusion refers to the fusion mechanism in SwinFusion++ that enables structured interaction between spatial tokens and temporal tokens across representation stages. Operationally, it is used to learn how appearance and motion evidence should constrain one another in authentic videos—and how deepfakes violate these constraints—beyond what simple feature concatenation can capture.
Evaluation Protocols and Class Balancing
In this study, evaluation is operationalized through two complementary protocols and a balancing procedure: (a) Class-Balanced Training Sampling is applied during training: clips are drawn by class, then by source or identity group, video, and clip, so that both classes contribute equally, while the validation and test sets keep their original class proportions; (b) In-Distribution Evaluation uses the dataset’s official split where it provides a compatible, group-safe one and otherwise a 70-15-15 group-disjoint split (70% training, 15% validation, 15% test) within the same dataset; and (c)  Cross-Dataset Transfer Evaluation trains the model on one dataset and tests it on other datasets to assess robustness under distribution shift (difference in sources, manipulation pipelines, and quality/perturbations). Performance is reported using Accuracy, Precision, Recall, F1-Score, and ROC-AUC under these protocols.
System Output and ISO/IEC 25010‑Based Platform Evaluation
In this study, the system output refers to what the deployed SwinFusion++ platform displays after inference. Operationally, it provides: (a) a classification label (Real/Fake), (b) a confidence score (probabilistic output associated with the predicted class), and (c) contextual video metadata (e.g., filename, duration, frame rate, resolution, file size, and format). These outputs are treated as decision support for screening and verification workflows rather than standalone forensic proof. The deployed platform is evaluated operationally using an ISO/IEC 25010‑based Likert assessment, focusing on functional suitability, usability, performance efficiency, and security, supplemented by expert usability/interaction feedback as described in the methodology.
# Chapter 3 – METHODOLOGY
## Software Design and Development Approach
### Software Process Module
This study adopted the Incremental Process Model (Pressman & Maxim, 2020) for the development of the SwinFusion++ platform. This approach was appropriate because the study developed both a research model and a deployable web-based software artifact, which allowed each part of the system to be built, tested, and delivered in working portions. Each increment followed the five framework activities of the model: communication, planning, modeling, construction, and deployment. The feedback gathered at the end of each increment served as input to the next. Research and documentation activities, including the drafting of chapters, the ethics review, and the defenses, were carried out in a parallel track outside the software process (Appendix A). 
REFERENCE: Pressman, R. S., & Maxim, B. R. (2020). *Software engineering: A practitioner’s approach* (9th ed.). McGraw-Hill Education. 
The first increment, Core Platform and Spatial Inference, was carried out from December 2025 to March 2026. During communication and planning, the researchers gathered requirements from the literature and adviser consultations, and defined the scope, input limits, schedule, and ethical constraints of the system. During modeling, they designed the architecture layers, the HIPO chart, the system flowchart, the branding, and the page wireframes. During construction, the researchers acquired the datasets and implemented the face-aligned preprocessing pipeline (MTCNN face detection, alignment and cropping, gamma correction, and FaceNet identity verification), and developed the Swin Transformer spatial stream. They then built the front-end pages, namely the Home page with a Deepfake 101 section, the Scanner page, the SwinFusion++ page, and the Methodology page, while the About, API, Contact Us, FAQs, and Legal pages were prepared as placeholders. The upload, preprocessing, and spatial inference functions were integrated through a FastAPI backend, which was shared publicly through ngrok during this increment. The resulting prototype accepted MP4, MOV, and WebM videos of up to 250 MB and displayed the probability that a video was fake, the video properties, and a visual overlay of the facial regions that influenced the result. The prototype then underwent interface consistency, navigation, and inference-flow testing using sample videos of different resolutions. The increment was deployed as a working prototype during the proposal defense on 28 March 2026, and the panel’s feedback (Appendix G) became the requirements of the next increment.
The second increment, Full SwinFusion++ Model, was carried out from March to September 2026. The researchers translated the panel revisions into model and service requirements; planned the training schedule, compute resources, and evaluation protocol; and designed the Video Swin temporal branch and the hierarchical cross-attention fusion. Construction covered the completion of data preprocessing for the declared datasets, the development of the temporal stream and the TLBG-HCA fusion module, the stability testing and debugging of the full pipeline, model training, and Bayesian hyperparameter optimization. The model was then evaluated under in-distribution and cross-dataset conditions, and the results were reviewed with the adviser before deployment. 
The third increment, Integrated Deployment and Evaluation, was carried out from September to November 2026. The researchers consulted the adviser on the deployment, survey procedure, and respondent quotas, and planned the hosting, test clips, recruitment, and survey schedule. They then designed the integration of the detectors with the web service, including the API endpoints, service components, detector selection, link input, and error-handling flow. During construction, the four detectors were connected to the backend inference service on a GPU server, and the front-end was redesigned into its final set of pages: the Home, How it works, Models, API, About, Scan a video, FAQs, Blog, Contact, Privacy, Terms, and Disclaimer pages. Two features were also added for user convenience: an Auto option that selected a detector based on the visual quality of the video, and the submission of videos through social media links. The integrated service underwent end-to-end system testing and was opened to respondents and experts on 12 October 2026. End-users evaluated the service from 12 to 30 October 2026, and cybersecurity experts from 15 to 30 October 2026. During the evaluation period, the researchers provided support and fixes for GPU availability, link sources, and interface updates. The collected responses were then analyzed from 31 October to 3 November 2026 to complete the human evaluation phase.
The selected approach was incremental because the system was developed and validated in working portions, with each increment producing a usable deliverable: a working prototype, an evaluated model, and an evaluated web service. It was also iterative because the feedback from each deployment, namely the panel’s revisions, the adviser’s review of the model results, and the support provided during the evaluation, was carried into the subsequent work on the system.
### Software Framework
The software framework of the SwinFusion++ web service followed a modular web-based architecture composed of the presentation layer, the application and control layer, the preprocessing layer, the inference layer, and the output layer. This structure separated user interaction from internal computation while maintaining a clear path from upload to result. Table X summarizes the tools used in each layer.
|  |  |
| :- | :- |
| Layer | Tools |
| Presentation | HTML, CSS, and JavaScript; Node.js build script for minification |
| Application and control | Python 3.12, FastAPI, Uvicorn, PyAV, yt-dlp |
| Preprocessing | PyTorch, facenet-pytorch (MTCNN and FaceNet InceptionResnetV1), torchcodec |
| Inference | PyTorch, torchvision |
| Hosting and storage | Render (web service), Vast.ai Serverless GPU (NVIDIA RTX 5090), Backblaze B2 (model weights) |

Table I.* Tools Used per Layer*
The presentation layer contained the user interface pages of the service, namely the Home, How it works, Models, API, About, Scan a video, FAQs, Blog, Contact, Privacy, Terms, and Disclaimer pages. Collectively, these pages introduced the problem domain, explained the detection process and the available detectors at a user-appropriate level, provided the scanning interface, and disclosed help, limitations, privacy practices, and use conditions. 
The application and control layer managed page navigation, input checking, user feedback, and communication between the interface and the backend inference service. Before a scan, users selected one of the four detectors or the Auto option, and submitted a video either by uploading a file or by pasting a link to a public video from TikTok, Facebook, X, or Reddit. The layer validated each video before processing and accepted only readable MP4, MOV, WebM, or MKV files that were 10 seconds to 2 minutes long, 360p to 1080p in resolution, and no larger than 250 MB. Accepted videos joined a queue in which at most three scans ran on the GPU at the same time, and users could see their position in the queue and cancel a scan while waiting. If an upload was interrupted, the service informed the user so that the video could be uploaded again, and a scan already in progress could be resumed after the page was reloaded. This layer was important because the service was evaluated not only for its technical output but also for its usability, operability, and clarity of interaction. 
The preprocessing layer standardized each video before inference. After a video was submitted, the service decoded its frames, detected faces using MTCNN, retaining detections with a confidence of at least 0.90, and aligned each detected face to a standard face template using five facial landmarks, producing a 224 × 224-pixel crop. FaceNet embeddings were then compared using cosine distance to track the same person across frames and prevent background faces from being analyzed. When no face, or too few frames with a usable face, could be found, the service did not produce a Real or Deepfake result and instead displayed a message explaining why the video could not be analyzed. In the Increment 1 prototype, gamma correction (γ = 2) was additionally applied to dark frames. 
The inference layer contained the SwinFusion++ detection engine. The service analyzed every frame in which the tracked face appeared by dividing the video into short clips at the frame spacing used during each detector’s training, so that the whole video contributed to the result. The clip scores were averaged into a single video-level probability, which was compared with the detector’s own decision threshold to classify the video. As a secondary check, the service also scored the video using the same sampling protocol applied in the benchmark evaluation and reported whether the two results agreed. 
The output layer translated the computed prediction into user-readable results. The service presented the verdict as “Likely Deepfake” or “Likely Real,” together with a confidence value expressing how far the score fell from the detector’s threshold. It also displayed a timeline of scores across the video, evidence maps that highlighted the facial regions that most influenced the result, the outcome of the secondary check, the detector used, and contextual video metadata such as the file name, duration, frame rate, resolution, format, and file size. These outputs were designed as decision-support information rather than standalone forensic proof. The help and transparency content on the surrounding pages further guided users in interpreting the result responsibly. 
The web service was hosted on Render, which delivered its traffic through Cloudflare over an encrypted connection, while inference was performed on a GPU server rented through Vast.ai. The model weights were stored in a private Backblaze B2 bucket and downloaded by the GPU server at startup. The service’s API keys were kept on the server and were never exposed to the browser. 
###   
Process Flow (HIPO and System Flowchart)
HIPO of the SwinFusion++ System
[image]
#### Figure 2. HIPO Chart
System Flowchart
[image]
#### Figure 3. System Flowchart
System Flowchart Description
The service flow started when the user accessed the website and opened the Scan a video page. The user first selected one of the four detectors or the Auto option, and then submitted a video either by uploading a file or by pasting a link to a public video. The service checked whether the submission was successful, that is, whether the upload was completed or the linked video was fetched. If the submission failed, the service displayed an error message, and the user could either submit the video again or end the session. If the submission succeeded, the service checked whether the video met the declared requirements on format, length, resolution, and file size. Videos that did not meet these requirements were likewise returned to the user with an error message. If the video was accepted and the Auto option had been chosen, the service selected a detector based on the visual quality of the video; otherwise, the detector chosen by the user was retained. The video then waited in the scan queue, where the user could cancel the scan if needed.
When the scan started, the service extracted the frames of the video and detected faces using MTCNN. If no usable face was found, the service displayed a message explaining that the video could not be analyzed, and the user could again submit another video or end the session. If a usable face was found, the video proceeded to preprocessing, in which each face was aligned to a 224 × 224 crop using five facial landmarks and the same person was tracked across frames using FaceNet embeddings. The standardized facial evidence was then forwarded to the SwinFusion++ inference model, which performed dual-stream inference by extracting hierarchical spatial features through the spatial Swin Transformer stream and modeling motion-related dependencies through the temporal Video Swin Transformer stream. The outputs of both streams were then integrated through hierarchical cross-attention fusion. The service scored clips across the whole video, averaged the clip scores, and classified the video as Likely Deepfake or Likely Real. The service then displayed the verdict together with the confidence value, the score timeline, the evidence maps, and the contextual video metadata, after which the uploaded video was deleted. After viewing the result, the user could scan another video or end the session.
## Research Design
This study adopted a mixed-method research design integrating two analytically distinct but conceptually linked components:
1.  Quantitative experimental–comparative evaluation of SwinFusion++, a face-aligned spatio-temporal transformer deepfake detector that fuses (i) Swin Transformer spatial representations and (ii) Video Swin Transformer temporal representations through a hierarchical cross-attention fusion mechanism. This component addressed RQ1, RQ2, RQ3, RQ4, and RQ6 and was carried out during the model development work of Increments 1 and 2; and
2.  Descriptive evaluative assessment of the deployed SwinFusion++ web service, using structured end-user and expert evaluations grounded in ISO/IEC 25010-based quality characteristics and interaction-capability/usability dimensions, supplemented by a thematic analysis of the respondents’ open-ended comments. This component addressed RQ5 and was carried out during the deployment and evaluation activities of Increment 3.
The mixed-method structure was warranted because the study’s research questions were dual in nature: (a) to establish the technical validity and comparative performance of the proposed detector under controlled benchmarking conditions, and (b) to establish the practical adequacy of the implemented software artifact, that is, whether intended users could understand, operate, and trust the service in a realistic context of use. The quantitative benchmark results and Likert-scale ratings measured performance and perceived quality, while the qualitative comments explained the reasons behind the users’ and experts’ ratings. 
## Conceptual and Procedural Overview
Methodologically, the study proceeded in three linked phases, which were carried out across the three increments of the software process (Appendix A): 
1.  Model Phase (Algorithmic Evaluation). Benchmark training and evaluation were performed using public deepfake video datasets (FaceForensics++ HQ/LQ deepfake subsets, Celeb-DF v2, and DeeperForensics-1.0), with both in-distribution evaluation and cross-dataset transfer testing to assess generalization. This phase was carried out in Increments 1 and 2.
2.  System Phase (Deployment). A web interface and API operationalized the trained detectors as a user-accessible web service, supporting video submission by file upload or public link, detector selection, preprocessing, inference, and results presentation, including the verdict, confidence, evidence maps, and contextual video metadata. This phase was carried out in Increments 1 and 3.
3.  Human Evaluation Phase (Usability and Quality Assessment). End-users evaluated the perceived quality of the service using an ISO/IEC 25010-based Likert questionnaire, while experts evaluated interaction capability and usability through a structured, multi-dimension Likert instrument. The open-ended comments of both groups were analyzed thematically. This phase formed the deployment and feedback activities of Increment 3.
## Study Site, Locale, and Study Duration
The study was conducted from 1 December 2025 to 14 November 2026 (Appendix A). The declared study locale and participant sourcing were as follows:
  - End-user respondents: members of the University of the East (UE) community, evaluated through a remote/online procedure from 12 to 30 October 2026; and
  - Expert evaluators: cybersecurity experts and IT practitioners from organizations within Metro Manila also evaluated through a remote/online procedure from 15 to 30 October 2026.
The human-participant evaluation was conducted outside a laboratory setting. Participants used their own devices (desktop, laptop, or mobile) and their typical internet connection. This was methodologically appropriate because the web service was designed to function under ordinary real-world conditions, including varying bandwidth, device constraints, and levels of user familiarity. 
## Determination of Sample Size
[image]
#### Figure 4. Cochran’s Formula for Continuous Data
For this study, the alpha level was set to 0.05 (95% confidence level); thus, t = 1.96 for large populations. Following common practice cited by Bartlett et al. (2001), the acceptable margin of error for continuous data was set at 3%. Since the survey used a 5-point Likert scale, the acceptable margin of error in scale points was computed as:[image]
[image]
#### Figure 5. Acceptable Margin of Error in Scale Points
In the absence of pilot data, Bartlett et al. (2001) recommend estimating the standard deviation of a rating scale by dividing the inclusive range of the scale by 6. Thus, the estimated standard deviation was:
[image]
#### Figure 6. Estimated Standard Deviation
Substituting these values into Cochran’s continuous-data formula yielded: [image]
[image]
#### Figure 7. Estimated Respondents
The computed value was rounded up to the next whole number; therefore, the minimum required number of completed survey responses was 119. For practicality, the study targeted 120 completed responses, allocated disproportionately across the two age strata: 90 respondents aged 15–30 and 30 respondents aged 31–59. The larger youth allocation reflected the composition of the University of the East community, in which students, most of whom fall within the 15–30 bracket, make up the majority of members. The 31–59 stratum was assigned 30 respondents, consistent with Roscoe’s (1975) rule of thumb, which remains recommended in recent sample size reviews (Memon et al., 2020), that each subsample should contain at least 30 respondents. At this size, the mean ratings of the 31–59 stratum had an estimated margin of error of ±0.30 scale points at a 95% confidence level, which was adequate for the descriptive summaries used in this study. 
[image]
Figure 8.* Target Responses per Strata*
References: 
Roscoe, J. T. (1975). *Fundamental research statistics for the behavioral sciences* (2nd ed.). Holt, Rinehart and Winston. 
Memon, M. A., Ting, H., Cheah, J.-H., Ramayah, T., Chuah, F., & Cham, T. H. (2020). Sample size for survey research: Review and recommendations. *Journal of Applied Structural Equation Modeling, 4*(2), i–xx.[ https://doi.org/10.47263/jasem.4(2)01](https://doi.org/10.47263/jasem.4(2)01) 
To account for possible nonresponse and incomplete survey forms, the researchers planned to distribute more questionnaires than the required minimum. As recommended by Bartlett et al. (2001), the number of distributed questionnaires was adjusted using:
[image]
#### Figure 9. No. of Distributed Questionnaires Formula
Assuming an anticipated response/completion rate of 80%, the required number of distributed questionnaires was calculated as follows:[image]
#### Figure 10. No. of Distributed Questionnaires
Hence, the researchers planned to distribute approximately 150 survey forms to obtain at least 120 usable and complete responses.
## Sampling Design and Technique
Dataset Sampling (Model Evaluation)
For the Model component:
  - Class-Balanced Training Sampling is used for training: clips are drawn by class, then by source or identity group, video, and clip, so that real and manipulated videos contribute equally. The validation and test sets keep their original class proportions.
  - Each dataset is partitioned with its official split where it provides a compatible, group-safe one; otherwise, a 70–15–15 group-disjoint split (70% training, 15% validation, 15% testing) is applied. Videos that share a source video, an identity, or derived versions are kept in the same partition.
  - To test generalization, the study also performs cross‑dataset transfer evaluation in nine directions: models trained on FaceForensics++ C23, Celeb-DF v2, and DeeperForensics-1.0 are each tested on the other test sets (distribution-shift testing).
Respondent Sampling
End-user sampling used: 
  - Quota sampling to ensure representation across two age strata, with quotas of 90 respondents aged 15–30 (Youth) and 30 respondents aged 31–59 (Working-age adults); and
  - Purposive sampling to ensure that participants could meaningfully evaluate the service by completing the required tasks.
Expert Sampling
Expert evaluators were recruited through purposive sampling, defined as selecting respondents with professional practice in cybersecurity or information technology. The study invited cybersecurity experts and IT practitioners from organizations within Metro Manila, such as software engineers, developers, technical consultants, and IT managers. Experience in artificial intelligence, computer vision, cybersecurity, or UI/UX was considered an advantage but was not required. This technique was used to ensure that the expert review produced practice-informed judgments and actionable recommendations regarding the SwinFusion++ web service’s interaction capability and usability, drawing on the evaluators’ professional familiarity with how software services are built, operated, and used.
## The Subject
Experimental Subjects
The experimental subjects are labeled video samples obtained from three public benchmarks commonly used for deepfake detection research:
  - FaceForensics++ (HQ/LQ) deepfake subsets
  - Celeb-DF (v2)
  - DeeperForensics-1.0
Each video is treated as a supervised sample with ground-truth labels (authentic vs. manipulated) as provided by the datasets. The frozen test sets contain 280 videos for each FaceForensics++ quality level (140 manipulated and 140 authentic), 978 videos for Celeb-DF v2 (843 manipulated and 135 authentic), and 402 videos for DeeperForensics-1.0 (201 of each class). In DeeperForensics-1.0, the authentic class consists of the FaceForensics++ original videos into which its manipulated faces were swapped.
Survey Subjects - The Users
The respondents of the study were end-users who could actually use the SwinFusion++ web service. After completing the required interaction with the service (e.g., uploading a deepfake video and receiving the detection result), participants answered a 5-point Likert questionnaire covering functional suitability, usability, performance efficiency, and security. This approach aligned with ISO/IEC 25010:2023 because software quality is evaluated with respect to specified users and a defined context of use, supporting assessment across different user backgrounds such as age (International Organization for Standardization [ISO], 2023; ISO/IEC 25000, n.d.). 
Respondents were classified into two strata: youth (15–30 years old; n = 90) and working-age adults (31–59 years old; n = 30). The youth stratum was based on the Philippines’ legal definition under Republic Act No. 8044 (Republic Act No. 8044, 1995). Since this stratum included minors (15–17 years old), parent/guardian consent and minor assent were obtained, consistent with PHREB guidance for internet research involving minors (Philippine Health Research Ethics Board [PHREB], 2022). 
Respondents were limited to ages 15–59 to ensure that participants could realistically access and use a web-based service and complete the required tasks (i.e., navigating the website, uploading a video, and interpreting results) before answering the ISO/IEC 25010-based Likert questionnaire. Only about 13% of individuals aged 55 and above reported access to a computer (Albert et al., 2021, p. 35), and only about 18% reported internet use, which may limit their ability to complete website tasks consistently (Albert et al., 2021, p. 87). Individuals aged 14 and below were excluded because ICT skill indicators are lower among those aged 10–14 (23.1%) than among those aged 15–24 (46.7%), suggesting that younger users may have less consistent baseline capacity for independent online evaluation (Albert et al., 2021, p. 45).
Survey Subjects - The Experts
For the expert usability review, the study recruited cybersecurity experts and IT practitioners from organizations within Metro Manila. IT practitioners were included to provide a practice-based perspective from professionals who build, operate, and support software services in their work. Cybersecurity practitioners were included because earlier cybersecurity human-factors research treats experts as practitioners performing real-world cyber defense or information assurance tasks, who develop specialized workflow knowledge and tool-based decision-making from operational experience (D’Amico et al., 2005). Experimental work has also shown that cybersecurity expertise, operationalized through domain knowledge and experience in network operations and information security, supports stronger performance in detecting malicious activity (Ben-Asher & Gonzalez, 2015).  A total of fourteen (14) experts participated in the evaluation. This number exceeded the three to five evaluators that Nielsen and Landauer (1993) found sufficient to identify most usability problems in an interface, allowing the review to capture a broad range of professional perspectives. 
Reference: Nielsen, J., & Landauer, T. K. (1993). A mathematical model of the finding of usability problems. In Proceedings of the INTERACT ‘93 and CHI ‘93 Conference on Human Factors in Computing Systems (pp. 206–213). Association for Computing Machinery.[ https://doi.org/10.1145/169059.169166](https://doi.org/10.1145/169059.169166)
## Model Development and Experimental Procedures
Data Acquisition and Integrity
Datasets are obtained from official repositories or authorized distribution channels. Data handling is restricted to research evaluation purposes, and the workflow is structured to ensure reproducibility through consistent preprocessing and fixed evaluation protocols.
Face-Aligned Preprocessing Pipeline
To standardize facial evidence and reduce spurious noise caused by inconsistent detection, each video is processed through a defined face-alignment and normalization pipeline:
1.  Frame-wise extraction. Videos are processed frame-by-frame to obtain candidate facial evidence.
2.  Face detection and alignment. MTCNN is used to detect the primary face per frame. 
3.  Cropping and Resizing. Detected faces are cropped and resized to 224x224 pixels for standardized model input. 
4.  Identity-consistency verification. FaceNet-style 512-D embeddings are computed for each detected face and compared across frames to keep the same person throughout the video, which prevents drift to background faces; inconsistent detections are filtered. 
5.  Clip construction. Aligned face crops are sampled at 2 frames per second and grouped into 16-frame clips. For evaluation, each video is represented by seven clips at fixed positions along its tracked face span, and the seven clip logits are averaged into one video score.
Resolution Stratification
To ensure consistent handling of portrait and landscape videos and avoid misclassification based on width-height ordering, video resolution is operationalized using the shorter frame dimension:
$r=min(width,height)$
Videos are categorized as:
  - High: $r\ ≥\ 720\ px$
  - Medium: $360\ ≤\ r<\ 720\ px$
  - Low: $r\ ＜\ 360\ px$
This stratification provides an interpretable basis for communicating expected performance behaviors under varying input quality conditions (also reflected in system design and user guidance).
Data Augmentation
To reduce overfitting and improve invariance to nuisance transformations common in real‑world video, the training pipeline applies RandAugment (Cubuk et al., 2020) as the sole augmentation policy, applied only to the training split. To preserve spatio‑temporal validity, augmentation parameters are applied consistently within a clip, avoiding artificial temporal jitter that would be introduced by frame‑inconsistent transformations.
SwinFusion++ Model Architecture (Operational Description)
Deepfake identification in this study is treated as a video-level spatio-temporal verification task rather than as a frame-by-frame image classification problem. The identification process begins by converting each input video into temporally ordered face-centered evidence. Frames are first extracted, the primary face is detected and aligned using MTCNN, each detected face is cropped and resized to 224 × 224 pixels, and FaceNet-style embeddings are used to enforce identity consistency across consecutive frames so that background faces, unstable detections, or wrong-face drift are not mistakenly analyzed as the target subject (Zhang et al., 2016; Schroff et al., 2015). This preprocessing stage is methodologically important because deepfake cues are often subtle and can easily be confounded by poor alignment, luminance variation, occlusion, or inconsistent face tracking. During training, augmentation is applied only to the training split and is kept consistent within each clip so that artificial temporal jitter is not introduced into the sequence.
After preprocessing, the standardized face crops are grouped into temporally ordered clips for spatio-temporal analysis. The spatial stream, based on the Swin Transformer, learns hierarchical multi-scale appearance evidence, including subtle texture irregularities, blending remnants, boundary inconsistencies, abnormal shading, and geometry-level distortions. In parallel, the temporal stream, based on the Video Swin Transformer, learns motion-sensitive evidence such as identity continuity, micro-motion stability, lip-motion plausibility, and the evolution of artifacts across adjacent frames. The central assumption is that authentic videos are not defined by realism in isolated frames alone; they must also preserve consistency between facial appearance and facial motion over time. Accordingly, SwinFusion++ does not treat spatial and temporal cues as two independent feature sets, but fuses them through hierarchical cross-attention so that appearance evidence can be reweighted by motion evidence, and motion evidence can be constrained by spatial structure (Liu et al., 2021; Liu et al., 2022; Kingra et al., 2024).
The final decision stage produces a clip-level fake probability and aggregates clip-level outputs into a single video-level classification. In operational terms, the deepfake identification process of the study therefore consists of four linked stages: (1) face-centered evidence standardization, (2) dual-stream spatio-temporal feature extraction, (3) hierarchical interaction between appearance and motion representations, and (4) video-level Real/Fake decision making. This formulation is consistent with the current direction of deepfake forensics, where reliable detection increasingly depends on jointly reasoning over intra-frame artifacts and inter-frame inconsistencies rather than relying on a single visible cue (Güera & Delp, 2018; Haliassos et al., 2021; Chen et al., 2022; Kingra et al., 2024).
Training Regimens and Hyperparameter Optimization
Two training regimens are used. In the fixed-recipe regimen, Swin-B, Video Swin-B, and SwinFusion++ are trained on each of the four dataset conditions (FaceForensics++ C23 and C40, Celeb-DF v2, and DeeperForensics-1.0) with one shared training recipe that was set before training and is not tuned for any model: AdamW with a binary cross-entropy loss on logits, gradient clipping, a linear warm-up followed by cosine decay, progressive unfreezing of the pretrained backbones, and at most 30 epochs with early stopping and checkpoint selection on source-validation video-level ROC-AUC, with the same learning rates, weight decay, batch size, augmentation, and class-balanced sampling for every model. Because no model receives tuning that the others do not, this regimen provides the principal architecture comparison for RQ1.
In the optimized regimen, the training settings of SwinFusion++ are tuned separately for each dataset by Bayesian optimization with Optuna and its tree-structured Parzen estimator (Akiba et al., 2019; Bergstra et al., 2011), with median pruning of unpromising trials. The search covers training settings only, namely the learning rates of the newly initialized modules and of the pretrained backbones, weight decay, batch size, and the unfreezing schedule; the architecture itself is not changed. Each study maximizes source-validation video-level ROC-AUC and uses 12 trials for FaceForensics++ C23 and C40 and 8 trials for Celeb-DF v2 and DeeperForensics-1.0, the first four of which sample the search space at random. The selected configuration of each study is retrained from the original pretrained weights.
Because only SwinFusion++ is tuned, the BO-selected model is reported as a configured system: it is compared with the fixed-recipe Swin-B and Video Swin-B separately from the architecture comparison, and the paired difference between BO-selected and fixed-recipe SwinFusion++ measures the effect of the optimization.
Every principal model, namely Swin-B, Video Swin-B, fixed-recipe and BO-selected SwinFusion++, and the two matched controls described below, is trained three times, with the seeds 260901, 260902, and 260903. Each seed is evaluated on its own, and the video-level logits of the three seeds are averaged into a three-seed ensemble, which serves as the principal output of each model.
For every model and training dataset, the decision threshold is set on source-validation videos only, at the value that maximizes Youden’s J (sensitivity plus specificity minus one), and a calibration temperature is fitted to the same validation logits (Guo et al., 2017). Both are frozen before any test video is scored and are applied unchanged to the within-dataset test set and to every transfer target, so no test or target labels are used for any choice.
Two matched controls, trained on FaceForensics++ C23 under the fixed recipe, examine whether a gain comes from the cross-attention exchange or from combining two backbones. The topology control removes the cross-attention and its gated feed-forward layers while keeping the adapters, projections, evidence construction, pooling, and classifier, and the capacity-matched control replaces each exchange block with per-stream modules of matching size that pass no information between the streams. Both are evaluated within C23 and under frozen transfer from C23. Four single-seed component variants of the BO-selected C23 model (one-directional attention, no gates, no agreement and disagreement evidence, and fusion in stages 3 and 4 only) are reported descriptively.
Before training, a metadata-only audit tested whether file metadata alone, without the image content, could separate authentic from manipulated videos. Because raw file metadata carried such a signal in two of the datasets, all models are trained and evaluated only on the rebuilt face-clip cache, and the audit is repeated on that cache (Chapter 4).
Comparative Baselines and Benchmarking Logic
Model comparison in this study is designed as a multi-family benchmark rather than as a single-baseline test. The comparison follows the broader benchmarking logic demonstrated in SFormer so that any claimed improvement of SwinFusion++ can be interpreted against spatial detectors, classical CNN-based spatio-temporal detectors, video/transformer-oriented detectors, and explicit generalization baselines rather than against only one competing architectural style (Kingra et al., 2024). Because the declared dataset scope of the present study is limited to the FaceForensics++ HQ/LQ DeepFake subset, Celeb-DF v2, and DeeperForensics-1.0, the comparison adopts SFormer’s model families while remaining within the datasets formally included in this thesis.
The full SFormer-aligned comparator inventory retained in this study therefore includes Xception-based baselines (including XN-avg and Xception/XceptionNet), MesoInception-4, FWA, FWA-DS, Capsule/Capsule-Forensics, EfficientNet variants (including Enet-B4 and Enet-Att), LBPNet, SiamNet, Multi-task, Two-Stream, Multi-attention, PRRNet, Swin-T, CViT, VixNet, MSVT, I3D, SlowFast, TEI, ADDNet-3D, S-MIL, S-MIL-T, F3-Net, STIL, FTCN, VTN, ViViT, VidTr, DFDT, ISTVT, Gaze features, Xception-LSTM, EfficientNet-BiLSTM with optical flow, frame-temporality two-stream spatial+temporal CNN, CNN-LSTM, facial-geometry CNN-LSTM, and SFormer itself (Kingra et al., 2024). In methodological terms, these models are not treated as an undifferentiated list; they are grouped according to the kind of evidence they emphasize and the kind of comparison they make possible.
The first group consists of strong frame-level and spatial detectors, such as Xception-based detectors, EfficientNet-based detectors, Capsule-Forensics, LBPNet, and SiamNet. These models test whether local artifact cues, texture statistics, or source-camera-noise discrepancies are already sufficient for robust detection without explicit sequence reasoning (Chollet, 2017; Tan & Le, 2019; Nguyen et al., 2019; Kingra et al., 2022; Kingra et al., 2023). The second group consists of CNN-LSTM style or motion-aware spatio-temporal detectors, such as Xception-LSTM, EfficientNet-BiLSTM with optical flow, generic CNN-LSTM, facial-geometry CNN-LSTM, gaze-feature methods, and frame-temporality two-stream models. These models test whether any gain of SwinFusion++ can be explained simply by adding temporal recurrence or motion features to CNN-extracted spatial features (Güera & Delp, 2018; Chen et al., 2022; Liang et al., 2023). The third group consists of video and transformer-oriented comparators, such as I3D, SlowFast, TEI, STIL, FTCN, VTN, ViViT, VidTr, DFDT, ISTVT, VixNet, CViT, MSVT, and SFormer. These models provide a stronger comparison set because they examine whether global attention, multi-scale video reasoning, or hybrid CNN-transformer design can match or exceed the proposed model.
Among all comparators, SFormer is treated as the closest conceptual benchmark. This is because SFormer is also an end-to-end spatio-temporal transformer detector and similarly uses a Swin-based spatial module; however, SFormer performs temporal analysis through a transformer encoder operating on spatially extracted features, whereas SwinFusion++ extends that inspiration by introducing a Video Swin temporal stream and hierarchical cross-attention fusion between the spatial and temporal branches (Kingra et al., 2024; Liu et al., 2021; Liu et al., 2022). For this reason, comparison against SFormer is especially important: it does not merely ask whether the proposed model is better than CNN baselines, but whether the specific extension from an SFormer-style end-to-end spatio-temporal transformer to a dual-stream Swin/Video Swin cross-attentive design produces a measurable advantage.
None of these comparators is retrained in this study. Their results are taken from published papers and from the research team’s preliminary study (Custodio et al., 2026), and each value is recorded with its dataset, manipulation subset, compression, protocol, evaluation unit, and source table. Values obtained on the same dataset, manipulation subset, compression, and video-level unit as this study form Tier A; values that pool the four FaceForensics++ manipulations, leave the subset unstated, or score frames form Tier B. These values are reported as context and are not entered into statistical tests against SwinFusion++; the controlled comparisons of the study are those with Swin-B and Video Swin-B trained under the same recipe.
To preserve fairness, all models trained in this study (SwinFusion++, Swin-B, and Video Swin-B) are evaluated under aligned preprocessing and matched decision logic as far as implementation allows. Face detection and alignment, cropping, resizing, identity-consistency verification, class balancing, clip construction, train-validation-test splitting, and video-level aggregation are standardized so that observed differences can be attributed mainly to architecture and feature-learning behavior rather than to inconsistent data handling. This is especially important in deepfake detection because a detector may appear strong by exploiting dataset-specific shortcuts or preprocessing artifacts instead of learning manipulation-relevant evidence that transfers across datasets and quality conditions (Geirhos et al., 2020).
Evaluation Protocol and Performance Metrics
Model performance is reported at the video level, with ROC-AUC as the primary measure and PR-AUC, Accuracy, Precision, Recall, Specificity, and F1-Score as secondary measures, and with confusion matrices, False Positive Rate (FPR), and False Negative Rate (FNR) used as diagnostic indicators when interpreting error tendencies. Accuracy alone is not treated as sufficient because a model may appear strong on a single dataset while still failing to generalize or while committing a problematic pattern of false positives or false negatives. Precision is important because a fake prediction should not be triggered too easily on authentic content; Recall is important because manipulated videos that evade detection directly weaken the practical value of the detector; F1-Score summarizes the Precision–Recall trade-off; and ROC-AUC evaluates discrimination behavior across thresholds rather than at a single operating point. Confusion matrices, ROC curves, FPR, and FNR are used to examine whether a model is conservative, over-sensitive, or brittle under quality degradation and dataset shift (Rössler et al., 2019; Li et al., 2020; Jiang et al., 2020; Kingra et al., 2024).
Evaluation is conducted under two complementary conditions. The first is in-distribution evaluation, where training, validation, and testing are performed within the same dataset using the dataset’s official split where it provides a compatible, group-safe one and otherwise a 70-15-15 group-disjoint split. The second is cross-dataset transfer evaluation, in which a model trained on FaceForensics++ C23, Celeb-DF v2, or DeeperForensics-1.0 is tested on the other test sets with its source threshold unchanged (nine directions) to assess robustness under distribution shift. Because FaceForensics++ provides High Quality and Low Quality versions, results are also separated by compression level to test whether a model retains effectiveness when visible artifacts are weakened by re-encoding or degradation. Video-level aggregation is applied consistently across compared models so that the unit of analysis remains the whole video rather than an isolated frame (Rössler et al., 2019; Li et al., 2020; Jiang et al., 2020; Kingra et al., 2024).
Within this protocol, a model will be interpreted as strong only if it satisfies three conditions: it performs competitively within each in-distribution benchmark, it remains stable across FaceForensics++ quality levels, and it transfers better to unseen datasets than competing baselines. Each condition is judged against the matched internal baselines, Swin-B and Video Swin-B trained under the identical fixed recipe, using the video-level paired comparisons with Holm correction described under Statistical Treatment of Data. Literature-only values provide context but are not used to decide whether a condition is met. Thus, the evaluation does not ask only which model obtains the highest single accuracy score. More importantly, it asks which model most consistently learns manipulation-relevant evidence that survives changes in dataset source, manipulation pipeline, and video quality.
## System Implementation and Platform Features Under Evaluation
A web interface and API were implemented to operationalize SwinFusion++ as a user-accessible web service. The service was designed as an interactive workflow consisting of three explicit stages, Upload → Processing → Results, a structure that was directly evaluated in the expert instrument. 
Core User Functions
The web service supported the following functions: 
  - Detector Selection. Before each scan, users selected one of four detectors or the Auto option, which selected a detector based on the visual quality of the video.
  - Video Submission. The service accepted one video per scan, submitted either by uploading a file or by pasting a link to a public video from TikTok, Facebook, X, or Reddit. Supported formats were MP4, MOV, WebM, and MKV. Each video had to be 10 seconds to 2 minutes long, 360p to 1080p in resolution, and no larger than 250 MB. Files that were unsupported, corrupted, or outside these limits were rejected before preprocessing and inference.
  - Automated Preprocessing and Inference using the standardized pipeline (face detection, landmark-based alignment and resizing, and identity tracking across frames).
  - Results Presentation, including:
      - the verdict (“Likely Deepfake” or “Likely Real”);
      - a confidence value expressing how far the score fell from the detector’s threshold;
      - a timeline of scores across the video;
      - evidence maps highlighting the facial regions that most influenced the result;
      - the outcome of a secondary check and the detector used; and
      - contextual video metadata (e.g., file name, duration, frame rate, resolution, file size, and format).
Detector Options
The service offered four detectors, each trained on a different benchmark dataset so that users could match the detector to the type of video being checked (Table X). Veni HQ was trained on FaceForensics++ C23 (high quality) and was intended for sharp videos taken directly from a camera or phone or downloaded without heavy compression. Veni LQ was trained on FaceForensics++ C40 (low quality) and was intended for blurry or heavily compressed videos, such as those sent through messaging applications or downloaded from social media. Vici was trained on DeeperForensics-1.0 and was intended for poorly lit, grainy, or noisy recordings. Vidi was trained on Celeb-DF v2 and was intended for convincing deepfakes without obvious blur or color mismatch. 
|  |  |  |
| :- | :- | :- |
| Detector | Training Dataset | Recommended For |
| Veni HQ | FaceForensics++ C23  | Sharp videos with visible skin and hair detail  |
| Veni LQ | FaceForensics++ C40 | Blurry, blocky, or re-shared videos  |
| Vidi  | Celeb-DF v2  | Polished deepfakes without obvious artifacts |
| Vici | DeeperForensics-1.0  | Dark, grainy, or noisy recordings  |

Table II.* Detector Options of the SwinFusion++ Web Service*
Automatic Detector Selection 
In addition to the four detectors, the service provided an Auto option for user convenience, which selected a detector based on the visual quality of the uploaded video. The service measured a sample of frames from the video and evaluated three conditions in order, with the first condition met determining the selection: videos that were dark, shaky, or grainy were assigned to Vici; videos that were blurry, heavily compressed, or low in resolution were assigned to Veni LQ; and all remaining videos were assigned to Vidi. Veni HQ was not selected automatically, since a clean video alone could not indicate whether a deepfake was highly polished. The measurement was performed in the browser for files that the browser could play, and on the server for videos submitted through links or files that the browser could not read; when a video could not be measured, Vidi was used by default. The cut-off values for these conditions were set manually as initial estimates and were not evaluated as part of this study. Therefore, the Auto option was treated as a usability feature of the service rather than a component of the detection model.
Sample Videos
To let participants try the service without supplying their own videos, the Scan a video page offered researcher-provided sample clips taken from the benchmark datasets. During the evaluation period, the samples consisted of deepfake clips from FaceForensics++, Celeb-DF v2, and DeeperForensics-1.0, and a sample was never offered to a detector that had been trained on the same dataset. Real clips from the same datasets were added after the evaluation period.
Interaction-Capability Features
Because the expert evaluation explicitly rated learnability, feedback visibility, error prevention and recovery, interpretability, and context-of-use behaviors, the service was designed to make these properties observable during use, including:
  - Learnability Cues: a clear purpose statement on every page; an obvious upload entry point with drag-and-drop or click-to-choose; an explicit display of the accepted formats and limits; plain-language descriptions of when to use each detector; and an example result shown before the user’s first scan.
  - System Feedback: an upload progress percentage; the user’s position in the queue; processing stage messages (e.g., while fetching a video from a link); and expectation-setting messages on processing time, including notice that the first check after a quiet period could take several minutes while the server started.
  - Error Prevention: validation of format, length, resolution, and file size before processing began, supported by a guide explaining which video resolutions produced dependable results.
  - Error Handling and Recovery: plain-language error messages explaining what happened and what the user should do next (e.g., “OriginAI’s server couldn’t be reached. Try again in a moment.”); a message explaining why a video without a usable face could not be analyzed; the option to cancel a scan while waiting; and the ability to resume a scan after reloading the page.
  - Results Interpretability: a reminder that the verdict was “a hint, not proof” and that users should also check where the video came from; a confidence value tied to the detector’s threshold; evidence maps; the secondary check; and warnings when only a few frames could be used.
  - Help and Transparency: accessible help content, including the How it works, Models, FAQs, Blog, and Disclaimer pages, sample videos, and clear disclosure of intended use, typical processing time, and limitations.
  - Context-of-Use Readiness: layouts that adjusted to phone, tablet, and desktop screens; understandable loading states on slow connections; and baseline accessibility features, such as screen-reader labels, visible keyboard focus, reduced motion for users who requested it, and a light or dark theme.
Privacy-by-Design Handling of Uploaded Media 
Because the service involved file upload, it implemented a privacy-by-design approach. Uploaded videos were sent to the server over an encrypted connection and were used strictly to generate the on-screen detection output; they were never used to train, tune, or test the detectors. The uploaded file was deleted as soon as the check finished, whether or not it succeeded. The result and its evidence images were kept for up to one hour under a random link known only to the user’s browser, so that the page could display them even after a reload, and were deleted afterwards. The service did not require accounts and did not use cookies, advertisements, or tracking scripts. The hosting and GPU providers processed videos only to deliver the check. Participants were instructed not to upload personal videos; instead, they used researcher-provided non-personal test clips or authorized non-sensitive clips. 
#### Disallowed Videos
The Terms of Use of the web service limited checks to videos that users owned or had permission to use, and prohibited using the service to:
  - harass, impersonate, defame, or secretly monitor anyone;
  - overload the service, get around its limits, or interfere with its servers;
  - copy, extract, or redistribute the detectors; and
  - present a result as forensic proof or an official certification.
[In addition, participants were instructed not to upload:]
  - Personal or private videos submitted without the uploader’s authority or without a lawful and ethical basis for analysis;
  - Videos involving minors in sensitive, exploitative, or sexual contexts;
  - Sexually explicit or non-consensual intimate content, including synthetic sexual content or involuntary fake pornography;
  - Videos that expose personal identifiers, login credentials, financial information, or other confidential data;
  - Videos centered on graphic violence, torture, self-harm, or death-focused material not required for approved research testing; and
  - Copyrighted or otherwise unauthorized material submitted without permission from the rights holder.
## The Research Instrument
Survey Subjects - The Users
The research instrument will consist of a structured questionnaire. Before answering the evaluation items, respondents will provide basic information such as age (and name, optional). The main part of the survey contains ISO/IEC 25010-based evaluation items focusing on four key characteristics: Functional Suitability, Usability, Performance Efficiency, and Security. These characteristics are chosen to assess the experiences of the respondents in using the website. A total of fifteen (15) items will be answered through a 5-point likert scale (1: Poor to 5: Excellent). Additionally, the survey is adapted from Urera and Balahadia (2019) while tailoring its contents to fit the requirements of the study.
Survey Subjects - The Experts
The expert evaluation instrument is a 34‑item structured Likert questionnaire with open‑ended comment fields. It was designed using established usability frameworks that define usability as dependent on the user, their goals, and the context of use; therefore, several items include space for experts to comment on task flow, points of confusion, and whether the interface supports successful completion of the website’s main tasks (ISO, 2018). In addition, the items are aligned with the ISO/IEC 25010 family’s interaction‑capability sub‑characteristics—especially learnability, operability, and user error protection—so experts can evaluate whether users can learn the site quickly, control it easily, and avoid or recover from common errors (ISO/IEC 25000, n.d.). Finally, several item statements reflect heuristic evaluation principles (e.g., visibility of system status, consistency, error prevention, and help/documentation) to help experts identify usability issues and recommend concrete interface improvements (Nielsen, J., 2024).
## Data Gathering Procedures
Model Evaluation Procedure
1.  Dataset Acquisition from official repositories/authorized sources.
2.  Preprocessing using the face-aligned pipeline (MTCNN face detection; 224x224 crop; FaceNet 512-D embeddings to keep the same identity across frames; 16-frame clips sampled at 2 frames per second). 
3.  Sampling and partitioning (class-balanced training sampling; official or 70-15-15 group-disjoint splits; cross-dataset transfer evaluation in nine directions).
4.  Training and hyperparameter tuning (training-only RandAugment augmentation; a shared fixed recipe for Swin-B, Video Swin-B, and SwinFusion++; Optuna/TPE Bayesian optimization of the SwinFusion++ training settings; three seeds per model; thresholds and calibration frozen on source validation).
5.  Evaluation and reporting using ROC-AUC, PR-AUC, Accuracy, Precision, Recall, Specificity, and F1-Score under in-distribution and cross-dataset conditions, followed by the statistical analyses described under Statistical Treatment of Data.
End-User Data Gathering Procedure
1.  Eligibility screening: the form first asks whether the participant is below 18; minors proceed through assent + parent/guardian consent flow, while adults proceed through informed consent. 
2.  Informed consent/assent is obtained before participation, with voluntariness and withdrawal rights explicitly stated. 
3.  Participant receive:
    1.  The system link, and
    2.  Standardized task instructions (upload a test clip, view output, then answer the survey).
4.  Participants perform core actions:
    1.  Access the SwinFusion++ interface, 
    2.  Upload a non-personal test video (researcher-provided or authorized), 
    3.  View classification output and metadata,
    4.  Complete the 15-item ISO/IEC 25010-based questionnaire and optional comment field.
Expert Data Gathering Procedure
1.  Experts read the information sheet and provide informed consent.
2.  Experts conduct a task‑based walkthrough designed to make the rated properties observable (upload discoverability, format clarity, progress/status messaging, error prevention/recovery, interpretability, help content, mobile responsiveness where feasible).
3.  Experts complete the 34‑item structured Likert questionnaire and provide qualitative suggestions via the open‑ended comment fields.
## Data Collected, Confidentiality Safeguards, and Risk Minimization
Data Collected (Data Minimization)
End-users:
  - G-Mail account (for deduplication / one submission per respondent),
  - Full name (optional),
  - Age bracket (15-30 or 31-59),
  - 15 Likert responses, and
  - Optional comments.
Experts:
  - G-Mail account (deduplication; verified submission),
  - Full name (optional),
  - Professional position/title,
  - Years of experience category (0-1,2-3,4-6,7-10,11+),
  - 34 Likert responses, and
  - Optional comments.
Confidentiality, Storage, and Access Control
All survey outputs (exports, cleaned datasets, analysis files) are stored in a restricted-access Google Drive research folder with:
  - Access limited to named custodians (research team)
  - Disabled public link sharing, and
  - Strengthened account safeguards (strong passwords and 2FA)
To reduce re-identification risk:
  - Consent/assent forms are stored separately from response datasets, 
  - Analytic datasets are de-identified using participant codes and strata labels, and
  - Any linkage key (if temporarily needed for validation) is stored separately and destroyed after cleaning/validation.
Handling of Uploaded Media
Participants and experts are instructed to use non-personal test videos (researcher-provided or authorized). Uploaded files are used only for inference and are not retained as part of the research dataset; where feasible, the system deletes uploads immediately after processing.
Retention and Secure Disposal
De-identified datasets and consent materials are retained only as long as necessary to complete analysis and reporting (typically up to one academic year after final reporting), after which secure disposal is performed via permanent deletion from Google Drive (Including clearing Trash/Bin) and destruction of any physical documents (if any exist).
## Statistical Treatment of Data
Model Evaluation
For each dataset and evaluation protocol (in-distribution and cross-dataset), the study reports:
  - ROC-AUC (primary) and PR-AUC, which do not depend on a threshold, and Accuracy, Precision, Recall, Specificity, F1-Score, and the numbers of false positives and false negatives at the frozen source-validation threshold, 
  - Confusion matrices to analyze error asymmetries, and
  - ROC curves to characterize threshold behavior.
Comparative analysis is performed under matched preprocessing and evaluation conditions to attribute differences to model design rather than pipeline inconsistency.
All inferential analyses use one score per video. A video’s score is the mean of the logits of its seven evaluation clips, and the principal score of each model is the three-seed ensemble, the mean of the three seeds’ video logits. Per-seed results are reported as supplementary evidence, and the seeds are never pooled as if they were additional videos.
Ninety-five percent confidence intervals for ROC-AUC and for differences in ROC-AUC are obtained by a stratified cluster bootstrap with 5,000 resamples. The resampling unit is the dependency cluster, that is, all test videos that share a source video or, in Celeb-DF v2, a target identity, so that related videos are always drawn together. Clusters that contain manipulated videos and clusters that contain only authentic videos are resampled separately, so every resample contains both classes, and the intervals are the 2.5th and 97.5th percentiles of the resampled values.
Models are compared on the same test videos through the difference in ROC-AUC (ΔAUC, SwinFusion++ minus the comparator), whose paired interval uses the same resampled clusters for both models. Each difference is tested with a two-sided cluster-level permutation test with 5,000 permutations, adapted from the rank-based test of Bandos et al. (2005): each model’s video scores are converted to ranks, and in each permutation the two models’ ranks are exchanged within randomly chosen clusters. The p-value is the share of permutations, counting the observed arrangement, whose absolute difference is at least as large as the observed one.
Comparisons are grouped into families, and Holm’s (1979) step-down adjustment holds the family-wise error rate at α = 0.05 within each family. The families are (a) fixed-recipe SwinFusion++ against fixed-recipe Swin-B and Video Swin-B within datasets (m = 8) and (b) under frozen transfer (m = 18), which together form the principal architecture comparison; (c) BO-selected SwinFusion++ against the same encoders, the configured-system comparison (m = 8 within datasets and m = 18 under transfer); (d) BO-selected minus fixed-recipe SwinFusion++, the optimization effect (m = 4 and m = 9); and (e) fixed-recipe SwinFusion++ against the two matched controls (m = 2 within FaceForensics++ C23 and m = 6 under transfer from C23). A difference is called significant when its Holm-adjusted p-value is below 0.05. A non-significant difference is reported as no detectable difference rather than as equivalence, because no equivalence test is performed.
The null hypothesis is decided separately for each paired comparison made on the same test videos, chiefly SwinFusion++ against Swin-B and Video Swin-B: it is rejected in favor of SwinFusion++ when the Holm-adjusted p-value is below 0.05 and the ROC-AUC difference favors SwinFusion++. Previously reported results of other models are not tested, so no hypothesis decision is made against them.
Differences in accuracy, precision, recall, and F1-score between paired models are summarized with paired cluster-bootstrap 95% intervals, without p-values. Further supplementary analyses, also without p-values, check how far the conclusions depend on particular choices: the smallest ROC-AUC difference each within-dataset comparison could detect with 80% power, the agreement in sign of each difference across the nine pairings of individual seeds, re-analysis of DeeperForensics-1.0 targets with 175 broader lineage clusters, re-analysis of Celeb-DF v2 targets leaving out one identity cluster at a time, the ratio of jackknife to bootstrap standard errors, results on the strict subsets of target videos that share no footage with the source data, and the mean transfer ROC-AUC of each model.
McNemar’s test is not used, because every test set contains clusters of related videos, so one independent paired decision per cluster cannot be assumed. DeLong’s test for correlated ROC curves is not used for the same reason, because it treats videos as independent.
Calibration is described with the frozen source-validation temperature, using the Brier score, the expected calibration error with 15 equal-width bins, and reliability diagrams, separately for each dataset and transfer direction. Computational cost is reported as total parameters, floating-point operations per clip and per video, peak training memory, training throughput, and checkpoint size, measured on an NVIDIA RTX 5090 in bfloat16 precision. Previously reported results are summarized by comparability tier with their original dataset, subset, compression, protocol, and evaluation unit, and are not entered into paired tests.
Changes after test scoring. The stratified cluster resampling and the permutation test with 5,000 permutations were specified on 30 September 2026, before any test video was scored. Four changes were made after scoring; none altered a model, a threshold, or a test set. First, the permutation test as first specified exchanged raw ensemble logits between models whose logits had different scales, which violated the exchangeability the test requires, so it was replaced by the rank-based version described above. The correction changed 10 of the 65 architecture, configured-system, and optimization-effect decisions; among the 26 architecture comparisons, it removed one significant difference favoring SwinFusion++ and added two. The original values are reported with the supplementary tables (Appendix J), and Holm decisions based on the paired-bootstrap p-values agreed with those of the corrected test in all 73 paired comparisons. Second, the comparisons were regrouped after scoring into the families listed above; the architecture conclusions were identical under the grouping recorded before scoring and under one pooled family, and only the optimization effect within Celeb-DF v2 depended on the grouping (Holm-adjusted p = 0.021 in its own family and 0.077 pooled). Third, an interim decision, made before scoring, to present the BO-selected configuration as the primary model was reverted to the plan described above, in which the fixed-recipe comparison is principal; both regimens are reported in full. Fourth, the supplementary analyses listed above were added.
End-User Survey
For each ISO/IEC 25010-based characteristic (Functional suitability, Usability, Performance Efficiency, Security), the study computes:
  - Weighted mean and standard deviation
  - Overall and per-dimension summaries, and
  - Stratified summaries by age group
Where appropriate for instrument quality, internal consistency reliability (e.g., Cronbach’s alpha by dimension) may be computed to assess whether items within a dimension behave coherently.
Expert Survey
Expert Likert responses are summarized by dimension (means and dispersions), providing a diagnostic profile of learnability, task flow clarity, feedback quality, error prevention/recovery, interpretability, consistency, transparency/help, and context‑of‑use readiness.
Open‑ended comments are analyzed via thematic synthesis, grouping recurring recommendations into actionable categories (e.g., “progress/status messaging,” “limitations/uncertainty communication,” “format constraints and pre‑validation,” “results explanation,” “mobile responsiveness,” “accessibility”). Themes are then mapped back to the rated dimensions to produce coherent, evidence‑linked improvement recommendations.
# REFERENCES
Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 2623–2631). Association for Computing Machinery. https://doi.org/10.1145/3292500.3330701
Albert, J. R. G., Quimba, F. M. A., Tabuga, A. D., Mirandilla-Santos, M. G., Rosellon, M. A. D., Vizmanos, J. F. V., Cabaero, C. C., & Muñoz, M. S. (2021). *Expanded data analysis and policy research for National ICT Household Survey 2019* (PIDS Discussion Paper Series No. 2021-20). Philippine Institute for Development Studies. <https://pidswebs.pids.gov.ph/CDN/PUBLICATIONS/pidsdps2120.pdf> 
Bandos, A. I., Rockette, H. E., & Gur, D. (2005). A permutation test sensitive to differences in areas for comparing ROC curves from a paired design. Statistics in Medicine, 24(18), 2873–2893. https://doi.org/10.1002/sim.2149
Bartlett, J. E., II, Kotrlik, J. W., & Higgins, C. C. (2001). Organizational research: Determining appropriate sample size in survey research. *Information Technology, Learning, and Performance Journal, 19*(1), 43–50.
Ben-Asher, N., & Gonzalez, C. (2015). Effects of cyber security knowledge on attack detection. *Computers in Human Behavior, 48*, 51–61. <https://doi.org/10.1016/j.chb.2015.01.039> 
Bergstra, J. S., Bardenet, R., Bengio, Y., & Kégl, B. (2011). Algorithms for hyper-parameter optimization. In Advances in Neural Information Processing Systems (Vol. 24, pp. 2546–2554). https://proceedings.neurips.cc/paper_files/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html
Chen, B., Li, T., & Ding, W. (2022). Detecting deepfake videos based on spatiotemporal attention and convolutional LSTM. *Information Sciences, 601*, 58–70. <https://doi.org/10.1016/j.ins.2022.04.014> 
Chollet, F. (2017). Xception: Deep learning with depthwise separable convolutions. In* Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition* (pp. 1251–1258). <https://doi.org/10.1109/CVPR.2017.195> 
Cubuk, E. D., Zoph, B., Shlens, J., & Le, Q. V. (2020). RandAugment: Practical automated data augmentation with a reduced search space. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (pp. 702–703).
Custodio, E. T., Degamo, M. K., Escueta, K. R. C., San Diego, D. A. E., & Sarmiento, M. J. F. (2026). SwinFusion++: Face-aligned spatio-temporal Swin Transformer for deepfake detection [Unpublished manuscript]. College of Computer Studies and Systems, University of the East–Manila.
Deng, L., Wang, J., & Liu, Z. (2023). Deepfake video detection based on EfficientNet and vision transformer. *Neural Processing Letters, 55*(6), 7057–7076. <https://doi.org/10.1007/s11063-023-11249-6> 
Dolhansky, B., Bitton, J., Pflaum, B., Lu, J., Howes, R., Wang, M., & Canton Ferrer, C. (2020). *The DeepFake Detection Challenge (DFDC) dataset* [Preprint]. arXiv. <https://doi.org/10.48550/arXiv.2006.07397> 
D’Amico, A. D., Whitley, K., Tesone, D., O’Brien, B., & Roth, E. (2005). Achieving cyber defense situational awareness: A cognitive task analysis of information assurance analysts. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 49*(3), 229–233. <https://doi.org/10.1177/154193120504900304> 
Esperanza, J., Marquez, J. F., & Sy, R. A. (2025). Hybrid convolutional-recurrent neural networks (CNN-RNN) model with temporal attention and particle swarm optimization for deepfake video detection. *Isabela State University Linker: Journal of Engineering, Computing and Technology, 2*(1), 99–115. <https://doi.org/10.65141/ject.v2i1.n8> 
Estrellado, C. J. P., Millar, G. B., Rey, F. I., & Arcinas, M. M. (2025). Deepfakes, of prey? Precursors and eclipses to the macrocosm Philippine politics. *International Review of Social Sciences Research, 5*(3), 26–53. <https://doi.org/10.53378/irssr.353234> 
Geirhos, R., Jacobsen, J.-H., Michaelis, C., Zemel, R., Brendel, W., Bethge, M., & Wichmann, F. A. (2020). Shortcut learning in deep neural networks. *Nature Machine Intelligence, 2*, 665–673. <https://doi.org/10.1038/s42256-020-00257-z> 
Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A. C., & Bengio, Y. (2014). Generative adversarial nets. In* Advances in Neural Information Processing Systems* (Vol. 27, pp. 2672–2680). <https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html> 
Guarnera, L., Giudice, O., & Battiato, S. (2020). *Deepfake detection by analyzing convolutional traces* [Preprint]. arXiv. <https://arxiv.org/abs/2004.10448> 
Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. In Proceedings of the 34th International Conference on Machine Learning (Vol. 70, pp. 1321–1330). PMLR. https://proceedings.mlr.press/v70/guo17a.html
Guo, Z., Yang, G., Chen, J., & Sun, X. (2020). *Fake face detection via adaptive manipulation traces extraction network* [Preprint]. arXiv. <https://doi.org/10.48550/arXiv.2005.04945> 
Güera, D., & Delp, E. J. (2018). Deepfake video detection using recurrent neural networks. In* 2018 15th IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS)* (pp. 1–6). IEEE. <https://doi.org/10.1109/AVSS.2018.8639163> 
Haliassos, A., Vougioukas, K., Petridis, S., & Pantic, M. (2021). Lips don’t lie: A generalisable and robust approach to face forgery detection. In* Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 5039–5049).
Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of Statistics, 6(2), 65–70.
Ho, J., Jain, A., & Abbeel, P. (2020). *Denoising diffusion probabilistic models* [Preprint]. arXiv. <https://arxiv.org/abs/2006.11239> 
House Bill No. 10567, *Deepfake Accountability and Transparency Act*, 19th Cong., 2nd Reg. Sess. (Phil. 2024). <https://docs.congress.hrep.online/legisdocs/basic_19/HB10567.pdf> 
House Bill No. 3214, *Deepfake Regulation Act*, 20th Cong., 1st Reg. Sess. (Phil. 2025). <https://docs.congress.hrep.online/legisdocs/basic_20/HB03214.pdf> 
International Organization for Standardization. (2018). *ISO 9241-11:2018: Ergonomics of human-system interaction*—Part 11: Usability: Definitions and concepts. https://www.iso.org/standard/63500.html
International Organization for Standardization. (2023). *ISO/IEC 25010:2023: Systems and software engineering*—Systems and software Quality Requirements and Evaluation (SQuaRE)—Product quality model (2nd ed.). <https://www.iso.org/standard/78176.html> 
ISO/IEC 25000. (n.d.). *Interaction capability*. ISO 25000. Retrieved February 14, 2026, from <https://www.iso25000.com/index.php/en/iso-25000-standards/iso-25010/61-interaction-capability> 
Jiang, L., Li, R., Wu, W., Qian, C., & Loy, C. C. (2020). DeeperForensics-1.0: A large-scale dataset for real-world face forgery detection. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 2889–2898). <https://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_DeeperForensics-1.0_A_Large-Scale_Dataset_for_Real-World_Face_Forgery_Detection_CVPR_2020_paper.html> 
Khan, S. A., & Dai, H. (2021). *Video transformer for deepfake detection with incremental learning* [Preprint]. arXiv. <https://arxiv.org/abs/2108.05307> 
Kingra, S., Aggarwal, N., & Kaur, N. (2022). LBPNet: Exploiting texture descriptor for deepfake detection. *Forensic Science International: Digital Investigation, 42–43*, Article 301452. <https://doi.org/10.1016/j.fsidi.2022.301452> 
Kingra, S., Aggarwal, N., & Kaur, N. (2023). SiamNet: Exploiting source camera noise discrepancies using Siamese network for deepfake detection. *Information Sciences, 645*, Article 119341. <https://doi.org/10.1016/j.ins.2023.119341> 
Kingra, S., Aggarwal, N., & Kaur, N. (2024). SFormer: An end-to-end spatio-temporal transformer architecture for deepfake detection. *Forensic Science International: Digital Investigation, 51*, Article 301817. <https://doi.org/10.1016/j.fsidi.2024.301817> 
Kohli, N., & Gupta, S. (2021). Detecting DeepFake, FaceSwap and Face2Face facial forgeries using frequency CNN. *Multimedia Tools and Applications, 80*(21–22), 33589–33616. <https://doi.org/10.1007/s11042-020-10420-8> 
Kumar, P., Vatsa, M., & Singh, R. (2020). Detecting Face2Face facial reenactment in videos. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision* (pp. 2589–2597). <https://openaccess.thecvf.com/content_WACV_2020/html/Kumar_Detecting_Face2Face_Facial_Reenactment_in_Videos_WACV_2020_paper.html> 
Laureta, M. P., Atienza, J. M. M., & Tapel, J. L. B. (2025). Deepfake speech detection: Identifying AI-generated and real human voices using hybrid convolutional neural network and long short-term memory model. *Isabela State University Linker: Journal of Engineering, Computing and Technology, 2*(1), 34–51. <https://doi.org/10.65141/ject.v2i1.n3> 
Li, Y., & Lyu, S. (2018). *Exposing deepfake videos by detecting face warping artifacts* [Preprint]. arXiv. <https://arxiv.org/abs/1811.00656> 
Li, Y., Chang, M.-C., & Lyu, S. (2018). In ictu oculi: Exposing AI-created fake videos by detecting eye blinking. In *2018 IEEE International Workshop on Information Forensics and Security (WIFS)* (pp. 1–7). IEEE. <https://doi.org/10.1109/WIFS.2018.8630787> 
Li, Y., Yang, X., Sun, P., Qi, H., & Lyu, S. (2020). Celeb-DF: A large-scale challenging dataset for DeepFake forensics. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 3204–3213). <https://doi.org/10.1109/CVPR42600.2020.00327> 
Liang, P., Liu, G., Xiong, Z., Fan, H., Zhu, H., & Zhang, X. (2023). A facial geometry based detection model for face manipulation using CNN-LSTM architecture. *Information Sciences, 633*, 370–383. <https://doi.org/10.1016/j.ins.2023.03.079> 
Lin, J., Huang, Z., Luo, W., & Lu, W. (2023). Deepfake detection in videos using multi-scale convolution and vision transformer. *Digital Signal Processing, 134*, 103895. <https://doi.org/10.1016/j.dsp.2022.103895> 
Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., & Guo, B. (2021). Swin Transformer: Hierarchical vision transformer using shifted windows. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 10012–10022). <https://openaccess.thecvf.com/content/ICCV2021/html/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.html> 
Liu, Z., Ning, J., Cao, Y., Wei, Y., Zhang, Z., Lin, S., & Hu, H. (2022). Video Swin Transformer. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 3202–3211). <https://doi.org/10.1109/CVPR52688.2022.00320> 
Masi, I., Killekar, A., Mascarenhas, R. M., Gurudatt, S. P., & AbdAlmageed, W. (2020). Two-branch recurrent network for isolating deepfakes in videos. In A. Vedaldi, H. Bischof, T. Brox, & J.-M. Frahm (Eds.), *Computer Vision – ECCV 2020* (pp. 667–684). Springer. <https://doi.org/10.1007/978-3-030-58571-6_39> 
Matern, F., Riess, C., & Stamminger, M. (2019). Exploiting visual artifacts to expose deepfakes and face manipulations. In *2019 IEEE Winter Applications of Computer Vision Workshops (WACVW)* (pp. 83–92). IEEE. <https://doi.org/10.1109/WACVW.2019.00020> 
Montserrat, D. M., Hao, H., Yarlagadda, S. K., Baireddy, S., Shao, R., Horvath, J., Bartusiak, E., Yang, J., Guera, D., Zhu, F., & Delp, E. J. (2020). Deepfakes detection with automatic face weighting. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops* (pp. 668–669). <https://openaccess.thecvf.com/content_CVPRW_2020/html/w39/Montserrat_Deepfakes_Detection_With_Automatic_Face_Weighting_CVPRW_2020_paper.html> 
Nguyen, H. H., Yamagishi, J., & Echizen, I. (2019). Capsule-forensics: Using capsule networks to detect forged images and videos. In *2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)* (pp. 2307–2311). IEEE.
Nielsen, J. (2024, January 30). *10 usability heuristics for user interface design*. Nielsen Norman Group. <https://www.nngroup.com/articles/ten-usability-heuristics/> 
Philippine Health Research Ethics Board. (2022). *National ethical guidelines for health and health-related research (2022)*. Philippine Council for Health Research and Development. <https://www.pchrd.dost.gov.ph/publications/2022-national-ethical-guidelines/> 
Republic Act No. 10173, *Data Privacy Act of 2012* (Phil. 2012). <https://privacy.gov.ph/data-privacy-act/> 
Republic Act No. 8044, *Youth in Nation-Building Act* (Phil. 1995). <https://lawphil.net/statutes/repacts/ra1995/ra_8044_1995.html> 
Rössler, A., Cozzolino, D., Verdoliva, L., Riess, C., Thies, J., & Nießner, M. (2019). FaceForensics++: Learning to detect manipulated facial images. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 1–11). <https://doi.org/10.1109/ICCV.2019.00009> 
Schroff, F., Kalenichenko, D., & Philbin, J. (2015). FaceNet: A unified embedding for face recognition and clustering. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition* (pp. 815–823). <https://doi.org/10.1109/CVPR.2015.7298682> 
Tadena, E. B., Libron, C. I., Aquino, J., Aringo, S. C., Buhian, K. B., Dean, J. K., Manajero, I. P., & Tulang, G. A. (2025). Unveiling the Matrix: Lived Experiences of Senior High School STEM Pre-computer Studies Learners on AI-generated audio-visual contents. *International Journal of Multidisciplinary Educational Research and Innovation, 3*(2), 254–266. <https://doi.org/10.17613/xz58n-fsk36> 
Tan, M., & Le, Q. V. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In *Proceedings of the 36th International Conference on Machine Learning* (pp. 6105–6114). PMLR.
Thakre, A., Nagwekar, O., Talekar, V., & Biswas, A. S. (2025). *CAST: Cross-attentive spatio-temporal feature fusion for deepfake detection* [Preprint]. arXiv. <https://arxiv.org/abs/2506.21711> 
Urera, F. L. J., & Balahadia, F. F. (2019). ICTeachMUPO: An evaluation of information e-learning module system for faculty and students. *International Journal of Computing Sciences Research, 3*(1), 163–188. <https://doi.org/10.25147/ijcsr.2017.001.1.31> 
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems* (Vol. 30, pp. 5998–6008). <https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html> 
Wang, R., Juefei-Xu, F., Ma, L., Xie, X., Huang, Y., Wang, J., & Liu, Y. (2020). FakeSpotter: A simple yet robust baseline for spotting AI-synthesized fake faces. In *Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence* (pp. 3444–3451). <https://doi.org/10.24963/ijcai.2020/476> 
Wodajo, D., & Atnafu, S. (2021). *Deepfake video detection using convolutional vision transformer* [Preprint]. arXiv. <https://doi.org/10.48550/arXiv.2102.11126> 
Zhang, H., Hu, C., Min, S., Sui, H., & Zhou, G. (2024). TSFF-Net: A deep fake video detection model based on two-stream feature domain fusion. *PLOS ONE, 19*(12), e0311366. <https://doi.org/10.1371/journal.pone.0311366> 
Zhang, K., Zhang, Z., Li, Z., & Qiao, Y. (2016). Joint face detection and alignment using multitask cascaded convolutional networks. *IEEE Signal Processing Letters, 23*(10), 1499–1503. <https://doi.org/10.1109/LSP.2016.2603342> 
Zhao, C., Zhang, X., Gao, W., & Zheng, N. (2023). Interpretable spatial-temporal video transformer for deepfake detection. *IEEE Transactions on Information Forensics and Security, 18*, 1335–1348. <https://doi.org/10.1109/TIFS.2023.3239223> 
Zheng, T., Li, Y., & Yu, L. (2021). *Exploring temporal coherence for more general video face forgery detection* [Preprint]. arXiv. <https://arxiv.org/abs/2108.06693> 
# APPENDICES
#### APPENDIX A
GANTT CHART
[image][image][image][image]
#### APPENDIX B
HIGH-FIDELITY PROTOTYPE
Home Page[image]
#### Figure 11. Hero Banner
This is the first thing that users will see upon entering the website. When the user clicks on the “VERIFY VIDEO” button, they will be directed to the Upload Page where they can start checking their video’s authenticity. The navigation bar also serves as a guide for users and will remain the same throughout the pages.
[image]
#### Figure 12. Deepfake 101
This section provides users information about deepfake. It covers a definition, the difference between AI-generated and deepfake content, and clues whether the content has been faked or manipulated.
[image]
#### Figure 13. SwinFusion++ Model
This section introduces the model that will be integrated into the website. When the user clicks on the “LEARN MORE” button, they will be directed to the SwinFusion++ page, which includes more information about the model. Additionally, the footer presents more pages that users may find helpful in case they want to know more about the website.
Scanner Page[image]
#### Figure 14. Uploading Interface
This is where users will be directed after clicking on the “VERIFY BUTTON,” which can be either found on the hero banner or the navigation bar. Here, the users can upload their video, but they can use the sample videos we will be providing in case they do not have one. Below this interface will be sections to guide users on what video resolution works best for the model and a simple step-by-step process in using the website.
[image]
#### Figure 15. Video Resolution Standards
[image]
#### Figure 16. Quick Start Guide
Processing Interface[image]
#### Figure 17. Processing Interface
This is what the users will see after uploading a video. If the upload is successful, they will be directed to the Results Page; otherwise, they will see an error message.
Error Messages
If a user uploads a video that does not meet the requirements of the website when it comes to uploading, the following error messages will appear, prompting them to upload a new video or proceeding with caution:
|  |  |
| :- | :- |
| [image]    Figure 18. *Invalid Format* | [image]    Figure 19. *Unsupported Minimum Resolution* |
| [image]    Figure 20. *Unsupported Maximum Resolution* | [image]    Figure 21. *Low Resolution* |

|  |  |
| :- | :- |
| [image]    Figure 22. *Medium Resolution* | [image]    Figure 23. *Large File* |
| [image]    Figure 24. *File Too Large* | [image]    Figure 25. *File Too Long* |
| [image]    Figure 26. *Scan Failed* | [image]    Figure 27. *Server Offline* |

Results Interface
[image]
#### Figure 28. Results Interface
This interface will show users the results of their uploaded video, which was processed by the system. An analysis report will be displayed with the deepfake probability score, which will show a high score if the video is found to be fake and a low score if not. The metadata of the video will also be provided. When the user wants to scan another video, they can click on the “SCAN ANOTHER VIDEO” button, directing them back to the Scanner Page.
Support Pages
|  |  |
| :- | :- |
| [image]    Figure 29. *About Page* | [image]    Figure 30. *Contact Us Page* |
| [image]    Figure 31. *FAQs Page* |  |

Legal Page
|  |  |
| :- | :- |
| [image]    Figure 32. *Privacy Policy* | [image]    Figure 33. *Terms & Conditions* |
| [image]    Figure 34. *Disclaimer* |  |

Technical Pages
|  |  |
| :- | :- |
| [image]    Figure 35. *SwinFusion++ Page* | [image]    Figure 36. *Methodology Page* |
| [image]    Figure 37. API Page |  |

#### APPENDIX C
USER EVALUATION SURVEY
Part 1.0. Participant Eligibility
  - Are you below 18 years old?
      - Yes → Informed Assent Form
      - No → Informed Consent Form
Part 1.1. Informed Assent Form
  - Parent/Guardian’s Email Address
  - Notice of Assent
Part 1.2. Informed Consent Form
  - Notice of Consent
Part 2. Personal Information
  - UE Institutional Email Address
  - Full Name (Optional)
  - Age Bracket
      - 15-30 years old
      - 31-59 years old
Part 3. Survey Questionnaire
Instruction: Please rate each statement using the scale: 5 = Excellent, 4 = Good, 3 = Acceptable, 2 = Poor, 1 = Very Poor.
1.  Functional Suitability:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Statement | 5 | 4 | 3 | 2 | 1 |
| The availability of expected features (e.g., uploading, results, and video info). |  |  |  |  |  |
| The accuracy of the website in showing the correct results. |  |  |  |  |  |
| The usefulness of the website in helping you find out whether a video is real or fake. |  |  |  |  |  |

1.  Usability:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Statement | 5 | 4 | 3 | 2 | 1 |
| The clarity of the website’s purpose at first glance. |  |  |  |  |  |
| The speed at which you are able to figure out how to use the website, even if you are in a hurry. |  |  |  |  |  |
| The ease of clicking buttons, finding menus, and moving around the website. |  |  |  |  |  |
| The ability of the website to prevent you from making mistakes (e.g., uploading the wrong file). |  |  |  |  |  |
| The overall design and user-friendliness of the website interface. |  |  |  |  |  |
| The capability of the website to work for everyone, regardless of their experience level or physical needs. |  |  |  |  |  |

1.  Performance Efficiency:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Statement | 5 | 4 | 3 | 2 | 1 |
| The speed of the website in processing a video and showing results. |  |  |  |  |  |
| The smoothness of the website’s performance without lags or slowing your device. |  |  |  |  |  |
| The ability of the website to handle large videos or process multiple tasks without crashing. |  |  |  |  |  |

1.  Security:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Statement | 5 | 4 | 3 | 2 | 1 |
| The ability of the website to keep uploaded videos and results private. |  |  |  |  |  |
| The protection of the website over your data from being changed or hacked by others. |  |  |  |  |  |
| The certainty that the “Real or Fake” result you receive is genuine and has not been tampered with or faked. |  |  |  |  |  |

1.  Comments and/or Suggestions
GOOGLE FORM
|  |
| :- |
| [image]    Figure 38. User Evaluation Survey - Starting Page |

|  |  |
| :- | :- |
| [image]    Figure 39. User Evaluation Survey - Informed Assent | [image]    Figure 40. User Evaluation Survey - Informed Consent |

|  |  |
| :- | :- |
| [image]    Figure 41. *User Evaluation Survey - Personal Information* | [image]    Figure 42. User Evaluation Survey - Functional Suitability |

|  |  |
| :- | :- |
| [image]    Figure 43. User Evaluation Survey - Usability | [image]    Figure 44. User Evaluation Survey - Performance Efficiency |

|  |
| :- |
| [image]    Figure 45. User Evaluation Survey - Security & Comments and/or Suggestions |

#### APPENDIX D
EXPERT EVALUATION SURVEY
Part 1. Informed Consent Form
  - Email addresses will be collected to ensure that there will only be one (1) submission per respondent. Additionally, only verified email addresses will be accepted to maintain the integrity of the research and ensure the validity of the collected data.
Part 2. Personal Information
  - Organizational/Institutional Email Address
  - Full Name (Optional)
  - Current Professional Position/Title
  - Years of Experience (0-1 year, 2-3 years, 4-6 years, 7-10 years, 11+ years)
Part 3. Survey Questionnaire
Instruction: Please rate each aspect using the scale: 5 = Strongly Agree, 4 = Agree, 3 = Neutral, 2 = Disagree, 1 = Strongly Disagree.
1.  Learnability:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| On the first visit, it is clear what SwinFusion++ does. |  |  |  |  |  |
| On the first visit, it is clear where to upload a video. |  |  |  |  |  |
| On first visit, it is clear what file types/requirements are accepted. |  |  |  |  |  |

1.  Task Flow:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| The steps from Upload → Processing → Results are easy to follow. |  |  |  |  |  |
| The flow feels efficient (no confusing or redundant steps). |  |  |  |  |  |
| At each stage, it is obvious what to do next. |  |  |  |  |  |

1.  System Feedback:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| During upload, the system clearly shows progress. |  |  |  |  |  |
| During processing, the system clearly shows status/stage (what it’s doing). |  |  |  |  |  |
| The system sets expectations about how long upload/processing may take. |  |  |  |  |  |

1.  Error Prevention:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| Supported formats are clearly communicated before upload. |  |  |  |  |  |
| Limits (max size/duration) are clearly communicated before upload. |  |  |  |  |  |
| The system warns/pre-validates common issues before processing starts (wrong file, too large, etc.). |  |  |  |  |  |

1.  Error Handling & Recovery:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| If an error occurs, the message is understandable to non-experts. |  |  |  |  |  |
| If an error occurs, the message explains what happened (in plain language). |  |  |  |  |  |
| If an error occurs, the message clearly tells the user what to do next. |  |  |  |  |  |

1.  Language / Microcopy Clarity:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| Labels and instructions are understandable for general (non-technical) users. |  |  |  |  |  |
| Technical terms are avoided or clearly explained. |  |  |  |  |  |
| Buttons/labels clearly match the action they perform. |  |  |  |  |  |

1.  Results Interpretability:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| The Results screen clearly explains what the classification label means. |  |  |  |  |  |
| The Results screen clearly explains what the confidence score means. |  |  |  |  |  |
| The Results screen communicates uncertainty/limitations appropriately. |  |  |  |  |  |
| The Results screen provides clear next steps (what to do after seeing the result). |  |  |  |  |  |

1.  Consistency & Standard:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| Navigation and page structure are consistent across the site. |  |  |  |  |  |
| Buttons and controls look/behave consistently across the site. |  |  |  |  |  |
| The interface follows common web conventions (placement, naming, behavior). |  |  |  |  |  |

1.  Help / Documentation / Transparency:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| Help content (FAQ/tooltips/examples) is easy to find when needed. |  |  |  |  |  |
| The site provides enough transparency (formats, typical time, limitations, intended use). |  |  |  |  |  |
| A short walkthrough or examples would significantly reduce user confusion. |  |  |  |  |  |

1.  Context of Use:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| The site is usable on mobile (responsive layout, readable text, touch-friendly). |  |  |  |  |  |
| The site behaves well on slow/unstable internet (loading states, retry, no confusion). |  |  |  |  |  |
| Accessibility basics are handled well (readability, contrast, clear focus, etc.). |  |  |  |  |  |

1.  End Question:
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Aspect | 5 | 4 | 3 | 2 | 1 |
| Overall, SwinFusion++ is easy to use for first-time users. |  |  |  |  |  |
| Overall, the system feedback + results are clear enough for non-experts. |  |  |  |  |  |
| Overall, the interface meets typical usability expectations for a web tool. |  |  |  |  |  |

1.  Comments and/or Suggestions
GOOGLE FORM
|  |  |
| :- | :- |
| [image]    Figure 46. Expert Evaluation Survey - Starting Page, Informed Consent | [image]    Figure 47. Expert Evaluation Survey - Personal Information |

|  |  |
| :- | :- |
| [image]    Figure 48. Expert Evaluation Survey - Learnability, Task Flow, System Feedback | [image]    Figure 49. Expert Evaluation Survey - Error Prevention, Error Handling & Recovery, Language/Microcopy Clarity |

|  |  |
| :- | :- |
| [image]    Figure 50. Expert Evaluation Survey - Results Interpretability, Consistency & Standard, Help/Documentation/Transparency | [image]    Figure 51. Expert Evaluation Survey - Context of Use, End Question, Comments and/or Suggestions |

#### APPENDIX E
LETTER TO THE HEAD OF ORGANIZATION
|  |
| :- |
| [image] |

#### Figure 52. Letter to the Head of Organization - Page 1
|  |
| :- |
| [image] |

#### Figure 53. Letter to the Head of Organization - Page 2
|  |
| :- |
| [image] |

#### Figure 54. Letter to the Head of Organization - Page 3
#### APPENDIX F
CERC RESULT
|  |
| :- |
| [image] |

#### Figure 55. CERC Result - Page 1
|  |
| :- |
| [image] |

#### Figure 56. CERC Result - Page 2
|  |
| :- |
| [image] |

#### Figure 57. CERC Result - Page 3
|  |
| :- |
| [image] |

#### Figure 58. CERC Result - Page 4
#### APPENDIX G
REVISION LIST
Panel No. 1
1.  Limitations: video size/quantity (HD) and disallowed videos.
2.  Modify SOP to include performance, significance, and user experience.
3.  Deeply discuss deepfake identification process and model comparisons.
4.  Include user experience evaluation using ISO.
5.  Consult the adviser [about] the SOP.
6.  Explain what happens in the background within the software.
[image]
Panel No. 2
1.  Ensure a clear methodology and align the Gantt chart.
2.  Focus on older generations as primary beneficiaries.
3.  Change wording from “system” to “service”.
4.  Address network interruption during upload.
5.  Include OOP concepts relevant to services.
[image]
Panel No. 3
1.  Define “High Resolution” and “Low Resolution”.
[image]
#### APPENDIX H
Turnitin Results - Similarity Report
[image]
#### APPENDIX I
Turnitin Results - AI Report

