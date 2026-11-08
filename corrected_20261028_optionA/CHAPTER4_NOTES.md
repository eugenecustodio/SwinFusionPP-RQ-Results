# Chapter 4 — notes to carry over (saved 2026-10-28)

## 1. Fix 1 — REQUIRED in Chapter 4 (RQ6 discussion) or Chapter 5 (conclusions)

This is the verdict against the Chapter 3 criterion: *"a model will be interpreted as strong only if it satisfies three conditions…"*. Fix 2, which defines how that criterion is judged, has already been added to Chapter 3 of the manuscript (`../../GRP9-P3-SwinFusion++_ Face-Aligned Spatio-Temporal Swin Transformer for Deepfake Detection.docx`) as a tracked change by "Claude".

Text to use:

> Against the criterion stated in Chapter 3, the fixed-recipe SwinFusion++ met the first two conditions: it was competitive within every benchmark and stable across FaceForensics++ quality levels. It met the third condition against Swin-B, with significantly better transfer in seven of nine directions. It met the third condition only partly against Video Swin-B: better in three directions, statistically tied in six, and worse in none.

Supporting numbers are in `RQ6/RQ6_RESULTS_AND_DISCUSSION.md`, interpretation item 7:

| Condition | Evidence | Verdict |
|---|---|---|
| (a) Competitive within each benchmark | ROC-AUC 0.988–0.997 on all four datasets | Met |
| (b) Stable across FF++ quality levels | Within C40 0.988; C23 → C40 0.976, on par with the encoders | Met |
| (c) Transfers better than competing baselines | Against Swin-B, significantly better in 7 of 9 directions. Against Video Swin-B, better in 3, tied in 6, worse in 0. | Met vs Swin-B, partly met vs Video Swin-B |

Do not change the Chapter 3 criterion to make it pass. The panel approved it.

## 2. Option A disclosure — REQUIRED in Chapter 4

> Results are reported according to the analysis plan in Chapter 3. An interim decision to present the BO-selected configuration as primary was reverted to the approved plan; all comparisons under both regimens are reported.

## 3. Other Chapter 4 items still open

- **Deviation to disclose.** Bayesian optimization used 8 trials for Celeb-DF and DeeperForensics; Chapter 3 declares 12, 16 or 20.
- **Promised but not run.** The gamma-policy and RandAugment ablations. Either state in one line that they were descoped, or remove the promise from Chapters 1 and 3.
- **Promised in Chapter 3 but not yet reported.** Calibration (Brier score, ECE), computational cost, and the metadata-only shortcut audit.
- **Available in the data but not yet written up.** The strict overlap-free DeeperForensics subset (60 videos) and the coverage and preprocessing-failure columns, both in `../00_Shared/statistics_raw/heldout_seed_metrics_rq1_rq6.csv`.
- **Hypothesis.** Report the H0 decision for each comparison. The text is in the RQ6 write-up, under *Hypothesis decision*.
- **Final-manuscript edits to Chapter 3.** Switch it to past tense, and update the title-page date.

## 4. Found in the project backup (Backblaze), 2026-10-28

- **The metadata shortcut audit was run** before training (23 Aug).
  - **First result:** raw file metadata separated real from fake on Celeb-DF (validation AUC 0.67) and DeeperForensics (0.68). That crossed the stop rule; FF++ stayed at about 0.50.
  - **Response (decision D-43):** the model receives only the rebuilt 224×224, 16-frame, 2-fps face clips. The re-run audit gave AUC 0.50 on every dataset (PASS).
  - **To do:** report it in Chapter 4. D-43 also requires results broken down by source metadata.
- **Gamma correction was disabled in the final pipeline** (decision D-08). Revise every place where the manuscript says gamma is applied.
  - **Web app:** its code is on a group member's computer. Check whether the deployed app applies gamma, because the model was trained without it.
- **Compute cost was measured** on an RTX 5090. SwinFusion++'s full parameter count and FLOPs, and the latency per video, still need to be filled in.

## 5. Calibration and compute cost — now computed (2026-10-30)

- **Calibration:** `calibration/CALIBRATION.md`.
  - **Within datasets:** good (ECE 0.009–0.036).
  - **Under transfer:** poor for every model (median ECE 0.446; worse than guessing the fake rate in 35 of 42 cells).
  - **Report in Chapter 4,** and state as a limitation that the platform's calibrated probability holds only for videos like the training data.
- **Compute cost:** `compute/COMPUTE_COST.md`.
  - **SwinFusion++:** 180.9 M parameters and 795 GFLOPs per 16-frame clip (5.57 TFLOPs per video).
  - **Compared with the backbones:** about twice the training memory of one backbone and 0.40–0.47× its training speed. The fusion module itself adds only about 6.5 M parameters and 20 GFLOPs.
  - **Latency was not properly measured.** Say so, or measure it on the deployment server.
- **Per-video FLOPs:** 7 clips per video is confirmed by `evaluation_protocol_v020.json` ("mean_of_seven_locked_clip_logits"). The app's 3-clip "Second check" resembles the preliminary study's three-anchor protocol; it is not the thesis evaluation protocol.

## 6. Web app check (2026-10-30, review of the app code on a groupmate's computer)

- **Gamma:** the deployed app applies none, which matches training. The γ = 2.0 rule (mean brightness < 0.35) exists only in the old local version (`website/backend/inference.py`), which the manuscript seems to describe. The site's "How it works" page also wrongly says dark frames are brightened.
- **Which model is served — UNRESOLVED.** The review said the four detectors are three Video Swin-B checkpoints plus DFD-FCG (Han et al., 2025); the user says that is a typo and they are SwinFusion++. Either way, the app's temperatures (1.9925 / 2.5595 / 1.3956) and thresholds (0.5248 / 0.4893 / 0.8322) match none of the 144 thesis operating points, and seeds 3109 / 2203 appear nowhere in the package (1701 is the preliminary-study seed). So the served checkpoints look like a different training run from the reported results. Quick test: SwinFusion++ has 180.9 M parameters (≈0.72 GB fp32 weights); Video Swin-B has 87.6 M (≈0.35 GB).
- **Other mismatches with Chapter 3:**
  - The main result samples every frame (about 2.9 fps, many clips); the evaluated protocol (3 clips) is only the "Second check".
  - The number shown is "NN% sure", which is effectively a confidence score; Chapter 3 says that term will not be used.
  - The clip count is not shown.
  - Successful deletions are not logged.
  - A 3-clip fallback with a warning replaces Insufficient Evidence in some cases.
  - The "Example Result" is a stored sample.
  - FaceNet uses cosine distance (Chapter 3 says Euclidean).
- **Not a problem:** normalization. torchvision's weights for both Swin-B and Video Swin-B use the ImageNet mean/std, so "checkpoint-specific normalization" is ImageNet for both.
- **Latency:** the Render site is suspended by the account owner. The only timings are past GPU-only ones (2.4 s for a 16 s clip on an RTX 4090; about 27 s average on a 5090).


## 7. Chapter 4 opening + RQ1 WRITTEN into the .docx (2026-10-30)

Tracked changes by "Claude". The production files are in `chapter4_rq1/`.

**Inserted:**
- Chapter 4 "PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA": Evaluation Setting (Tables 1–2), then RQ1 (Tables 3–8, Figures 11–13).
- The Chapter 3 paragraph "Amendments after Test Scoring".
- References: Bandos et al. (2005) and Holm (1979).
- Appendix figures renumbered B1–F4 (APA 7).
- New Appendix J (Tables J1–J8, Figure J1).

**Already covered:** the Option A sentence (verbatim) and the rank-correction disclosure.

**Removed at the user's request (2026-10-30):** the Deviations table and every deviation wording in Chapter 4. The user does not want deviations in Chapter 4. Its content (BO trials, gamma disabled, ablations not run, controls C23-only, C40 not a source, DFo perturbation strata, RTX 5090, D-43 stratified reporting) is kept in `chapter4_rq1/tables/T3.csv` in case it is placed elsewhere later, e.g. the Problem 3 approach in Chapter 3 or the Chapter 5 limitations.

**Still to do:**
- **RQ2–RQ4:** RQ4 gets the controls and Tier B.
- **RQ6:** cross-reference the RQ1 transfer tables; Fix 1 and the H0 decision go here.
- **Calibration and compute section,** after RQ6.
- **RQ5.**
- **Final formatting pass:**
  - update the TOC field;
  - add Figures 11–13 and J1 to the List of Figures;
  - add a List of Tables;
  - fix page numbers.

**Open items for the user:**
1. **Fixed-recipe config:** verify that it matches the Chapter 3 hyperparameters. It is not in the package, and Chapter 4 prints no values.
2. **Metadata audit:** copy `reports/audit/metadata_shortcut_audit_v001.md` into the package. Chapter 4 cites its numbers.
3. **Celeb-DF split manifest:** check it. The test clusters are keyed by target identity only; source-identity closure is unverified. The test set has 978 videos, not the official 518, which matters for RQ2/RQ6 comparisons with published values.
4. **Preliminary study:** it was left out because the manuscript never cites it. Add it, with a reference, under RQ6 or in Chapter 5 if wanted.
5. **Web-app checkpoint hashes:** still pending (section 6).

## 8. Chapters 1–3 consistency pass (2026-10-31)

**What changed.** 68 tracked edits by "Claude", agreed by all three advisors. The list is in `chapter4_rq1/ch1_3_consistency/edits_agreed.json` and `LEAD_MERGED_EDITS_R2.md`.
- **Gamma / low-light:** removed everywhere. The text now says the final pipeline applies none.
- **BO trials:** 12/12/8/8, "set from measured compute time and the project schedule before any test scoring".
- **External baselines:** described as "previously reported results", not retrained in this study. The wording stays neutral until the preliminary-study decision.
- **Ablations, controls, transfer:** gamma and RandAugment ablations dropped; controls and Tier B are C23-only and single-seed; C40 is not a transfer source; perturbation strata are not used.
- **Hardware and compute:** RTX 5090. The compute promise is narrowed to what was measured (no latency).
- **Clips:** 7 clips at 2 fps stated.
- **ECE:** 15 bins.
- **Per-seed reporting:** ROC-AUC.
- **"Confidence score" wording:** removed.
- **Chapter 2:** four duplicate paragraphs deleted.
- **Sampler and RandAugment:** wording fixed; "undersampling" removed.
- **FaceNet distance metric:** dropped, because it is unverified.
- **Amendments paragraph:** now says "RQ1 and RQ6 comparisons … six families, while the RQ4 control families were unchanged".

**Decisions only the group can make** (images and platform behavior cannot be fixed in the text):
1. Whether to cite the preliminary study. RQ2/RQ3 use its Xception and CNN–LSTM results, and RQ3's only paired test comes from it.
2. Redraw Figures 1–3. They still show gamma, RandomAug, undersampling, a 70–15–15 split, noise/adversarial "robustness testing" and "confidence score", and the flowchart has no Insufficient Evidence branch.
3. Web app vs Chapter 3:
   - the "NN% sure" display;
   - every-frame sampling and the 3-clip fallback;
   - clip count not shown;
   - deletions not logged;
   - the served model (pending hashes);
   - the "How it works" page.
4. The title-page date ("MARCH 2026").
5. Measure latency, or keep the narrowed compute promise.
6. Train/validation counts. Export them from the split manifest if block 404's promise should be kept in full.
7. Verify the FaceNet metric (cosine?) and the fixed-recipe hyperparameters (blocks 499–502).
8. Expert sample size, which is never stated.
9. Hypothesis decision rule for RQ6. Suggested: video-level ROC-AUC with the Holm-adjusted paired tests; inferential only against the internal encoders.
10. RQ4 relies on the internal controls only, because CAST and TSFF-Net are published values. RQ5 is marked "excluded" in the traceability file; confirm its status.
11. Optional: sample-size caveat (quota/purposive vs Cochran); Figure 7 rounding (118.47 vs 118.57).

## 9. RQ2 written (2026-10-31)

Tracked changes; three-advisor consensus. The files are in `chapter4_rq1/rq2/` (plan, memos, tables T9, T10, J9, KEY_NUMBERS_RQ2).

**Inserted:**
- the RQ2 section after RQ1: Table 9 (SwinFusion++ BO and fixed vs the preliminary-study Xception) and Table 10 (previously reported values, Tier A/B);
- no figure; the old fig1_vs_published.png must not be used;
- Appendix J is retitled "…Research Questions 1 and 2", with J9 holding the full list of published values (31 included, every exclusion with its reason);
- references: Custodio et al. (2026) [Unpublished manuscript] and X. Li et al. (2020), S-MIL.

**User decision (2026-10-31):** cite the preliminary study as an unpublished manuscript.

**Package errors found (do NOT use them; fix in the package or paper if reused):**
- `RQ2/results/table2_published_AB.csv` rows 27, 28 and 45:
  - FTCN 0.999 and 0.981 and Xception 0.939 are cross-manipulation results, not within-dataset C23;
  - the RQ2 write-up's "FTCN AUC 0.981–0.999" repeats this error, and so does `figures/RQ2/fig1_vs_published.png`.
- DeeperForensics "Xception 77% / I3D 79%" are hidden-set values; the standard test set gives 100%.
- "Highest C40 AUC in the record" is false: Sabir et al. report 0.9959.

**Next:** RQ3, which can now use the preliminary-study CNN–LSTM paired test (cite Custodio et al., 2026); then RQ4, RQ6, calibration/compute, RQ5.

## 10. RQ2 expanded with more comparison models (2026-10-31)

At the user's request; three-advisor consensus. The files are in `chapter4_rq1/rq2_expansion/` (memos, verified value CSVs, tables, references; `work/` holds the open-access source PDFs used for verification).

**Rule:** previously reported results only. Nothing was retrained (no GPU, no data access). The complete-source rule applies: every row of each comparison table used is in J9, and rows are left out only by a stated category, never by value.

**Table 10 (Tier A; same subset, compression and video level), 12 models:**
- Xception, D-FWA, CNN–LSTM, ResNet+LSTM, C3D, I3D, TSN, TEI, S-MIL-T, ADDNet-3D, STIL, SFormer.
- The DeeperForensics-1.0 standard set is now Tier A (matches this study's construction).

**Table 11 (new, Tier B; pooled manipulations or frame level), 28 rows from 5 sources:**
- All of TALL Table 2, plus LipForensics Table 4, Masi Table 2, FF++ Table 4 and FTCN.

**J9:** 234 values, 108 of them excluded with a reason code.

**Errors found in published comparison tables** (flagged in J9 and the notes):
- STIL misquotes DeepRhythm (0.987 is its DFD value).
- TALL's Two-branch AUCs are Masi's frame-level values.
- TALL's MesoNet and Xception accuracies equal Rössler's frame-level values.
- Face X-ray values differ between LipForensics and TALL.

**Not re-verified (paywalled):** SFormer and ISTVT.

**Also changed:**
- 19 new references, Crossref-verified and inserted in alphabetical order.
- Chapter 1/3 edits C8, C31 and C52 updated to the expanded model list.
- The RQ2 prose now uses ranges, with no vote counts; the accuracy gaps (BO 1.79/2.14, fixed 2.14/3.57) are unchanged.

## 11. Final check of RQ1/RQ2, positive framing, and whole-paper format (2026-11-01)

Three-advisor consensus. The files are in `chapter4_rq1/final_check/`.

**Re-verification.**
- All 65 paired tests and 52 ensemble intervals were recomputed from the raw predictions: exact.
- All 20 tables, every prose number and the four figures were re-checked: no errors.

**Framing.** RQ1 and RQ2 now lead with the tested strengths:
- significantly higher transfer ROC-AUC than Swin-B in 7/9 directions and than Video Swin-B in 3/9, significantly above both encoders in those 3, and never significantly lower;
- the largest difference, +0.258, from C23 to DFo;
- BO with the highest point AUC on C40 and Celeb-DF;
- RQ2: C40 ROC-AUC above the reported range, and accuracy within the reported Tier A ranges.

All required caveats are kept, once each. "Outperforms" was removed.

**Format.** Applied as tracked changes:
- 59 Chapter 1–3 edits (APA initials, the Thakre year, the uncited Kuang removed, BO/TPE/ROC-AUC/PR-AUC/BCE/ECE/MTCNN defined, the Akiba/Bergstra/Cubuk/Holm citations added, broken compounds fixed);
- List of Figures entries 11–13 and J1, a new List of Tables, and the front-matter line;
- the Güera reference reordered;
- note quotes and abbreviations, and J9 locators.

**USER items (Word, or the group's decision):**
1. TOC: use "Update page numbers only", then type the Chapter 4, Appendix H–J and "Review of Related Literature" lines. A full update would pull in about 49 captions.
2. Page numbers for the new List of Figures and List of Tables entries.
3. Restyle the empty heading paragraphs as Normal (Heading 2 at "blank" headings; Heading 4 before Appendix H).
4. Title-page date ("MARCH 2026").
5. Appendix I has no content.
6. Cite or delete Esperanza et al. (2025) and Laureta et al. (2025).
7. Add DOIs or URLs to 12 references.
8. Kuang et al. (2022) was removed as uncited; restore it if the group has the reference.
9. Add callouts for Figures 1–10.
10. Appendix caption formatting (C1–F4 labels not bold, D–F not centered); Appendix H/I titles in caps.
11. Center REFERENCES/APPENDICES if the template requires it.
12. Copy the metadata-audit report into the package.
