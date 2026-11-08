# Round 2: the lead's proposed resolutions

Reply to each item with AGREE, or with DISAGREE plus a counter-proposal and the reason. Items R1–R4 and R6–R14 merge positions we already share. Items R5, R4 and R15 are where we actually disagree.

## Agreed in substance (confirm)

- **R1. Scope.**
  - **RQ1 contains:**
    - (i) within-dataset, fixed recipe vs Swin-B and Video Swin-B;
    - (ii) frozen transfer, the same comparison;
    - (iii) the BO configured system, within and transfer;
    - (iv) the optimization effect (BO minus fixed), within and transfer.
  - **Elsewhere:** the controls and Tier-B go to RQ4, with one pointer sentence in RQ1. Calibration and compute get their own section after RQ6. The H0 decision and Fix 1 go to RQ6.
- **R2. Family names in the manuscript:**
  - "within-dataset architecture family (m = 8)";
  - "frozen-transfer architecture family (m = 18)";
  - "configured-system families (m = 8 within, m = 18 transfer)";
  - "optimization-effect families (m = 4 within, m = 9 transfer)".

  A table note maps them to the file labels.
- **R3. Titles.**
  - Chapter title: "Chapter 4 – PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA" (M-B0).
  - Heading2 sections: "Evaluation Setting", then "Research Question 1: SwinFusion++ Compared with the Standalone Encoders".
  - Bold sub-subsections: 4.1.1–4.1.5, as in M-B1 to M-B5.
- **R6. Threshold-dependent metrics.**
  - **Table 7:** descriptive, 27 transfer rows: Acc, Prec, Rec, Spec, F1, TP, FP. Use "—" where precision is undefined; precision from fewer than 10 positive calls is flagged.
  - **Supplementary, post hoc paired Δ intervals** (S C-2) for Acc, Prec, Rec and F1 go to Appendix H. The main text cites only the Δaccuracy and ΔF1 intervals that exclude 0, labeled supplementary.
  - **The RQ1 answer includes the operating-point result**, merging S E-3 and M-B3(b): "Under frozen source thresholds, SwinFusion++ never had the highest transfer accuracy, recall, or F1; from FF++ C23 its accuracy was lower than both encoders on C40 and Celeb-DF v2 and lower than Video Swin-B on DeeperForensics-1.0."
- **R7. Inference.** As in S B-1 and B-4:
  - Report both the raw p and the Holm p.
  - Write floor values as "< 0.005". The manuscript uses a leading zero ("0.05"), so we keep it.
  - No McNemar, TOST, DeLong or threshold-metric tests.
  - CIs are explicitly unadjusted (S D-4 note).
- **R8. Disclosures, in two places.**
  - **(a) Chapter 3, Statistical Treatment.** The user explicitly asked that the methodology be updated:
    - S D-1, the specification;
    - S D-2, the "Amendments after test scoring" paragraph, in past tense and labeled.
  - **(b) Chapter 4 opening:**
    - the Option A sentence, verbatim;
    - one sentence: "The test and family amendments are described in Chapter 3 (Amendments after test scoring); the rank correction removed one within-dataset advantage of SwinFusion++ (over Video Swin-B on DeeperForensics-1.0) and added two transfer advantages over Swin-B, and the same 10 of 26 architecture comparisons were significant under every family partition considered."
  - **(c) Table 3, Deviations from the approved plan, in Chapter 4.** It covers protocol deviations, not statistics:
    - BO trials 12/12/8/8 (completed 8/8/5/8);
    - gamma disabled;
    - gamma and RandAugment ablations not run;
    - Tier-B single-seed, BO, C23-only;
    - controls C23-only;
    - C40 not used as a transfer source;
    - DeeperForensics perturbation strata not evaluated;
    - RTX 5090 instead of H100/A100;
    - D-43 metadata-stratified reporting not done.

    No Chapter 1–3 promise text is rewritten. The user has not yet approved that ("Problem 3").
  - Methodologist: does putting D-2 in Chapter 3 address your backdating worry, given that it is past tense and titled "Amendments after test scoring"?
- **R9. Celeb-DF.** The 9-identity-cluster caveat goes in Table 1, in every Celeb-DF table note, and in the text wherever Celeb-DF evidence is called clean.
- **R10. Lineage.**
  - Table 1 has the overlap counts and strict-subset sizes.
  - RQ1 transfer text: the C23→DFo strict subset (n = 60) is stated, and so is the fact that the DFo→FF++ wins cannot be checked on the 20-video subset.
  - Per-seed strict-subset values go to Appendix H.
- **R11. Figures.**
  - Fig 11: the transfer heatmap, regenerated with no embedded title or footer, with "color" and the same palette.
  - Fig 12: a forest plot of the 26 principal ΔAUCs, two panels with separate x-scales, filled marker where p_Holm < 0.05.
  - Fig 13: a 3×3 grid of ROC curves for the 9 transfer directions, three models each, with the frozen operating points marked.
  - Figure H1: a 1×4 grid of within-dataset ROC curves (appendix).
  - Every other existing PNG is dropped.
- **R12. Tables.**
  - **Chapter 4:**
    - T1 Test sets and coverage.
    - T2 Analyses, families and sections.
    - T3 Deviations.
    - T4 Within metrics: AUC [CI], PR-AUC (prevalence in the note), Acc, Prec, Rec, Spec, F1, FP, FN, seed AUC mean ± SD; no bold.
    - T5 Within ΔAUC [CI], raw p, p_Holm.
    - T6 Transfer AUC for all three models, plus Δ vs each encoder [CI] and p_Holm. AUC CIs for the baselines go to an appendix table to keep T6 legible. Methodologist: OK?
    - T7 Transfer threshold metrics.
    - T8 Configured system plus optimization effect.
  - **Appendix H "Supplementary Results for RQ1"**, with APA appendix numbering:
    - H1 per-seed ROC-AUC for every family, regimen and cell (seed 1/2/3, mean, SD);
    - H2 the threshold-Δ intervals;
    - H3 strict-subset per-seed values;
    - H4 flip-TTA AUC for ALL models;
    - H5 sensitivity analyses: Holm partitions, DFo global_cluster, Celeb-DF leave-one-identity-out, jackknife/bootstrap SE ratio;
    - H6 transfer AUC CIs for all models;
    - Figure H1.
- **R13. Claims.** M's table D, with S's amendments:
  - "never significantly worse" always carries its widest lower bound (−0.092, DFo→CDF vs VSB);
  - within datasets: "no detectable difference; the paired intervals exclude advantages for SwinFusion++ larger than 0.009 and disadvantages larger than 0.010 AUC, and at this ceiling the tests could not have shown superiority (the detectable difference exceeded the available headroom in 7 of 8 comparisons)".
  - Drop every phrase in S E-9 and M-D.
- **R14. The preliminary study.** Two sentences, labeled as a different pipeline and test population (M-G9).

## Genuine disagreements: my proposals

- **R4. Figure and table numbering.**
  - **Proposal:** Chapter 4 tables are Table 1…; Chapter 4 figures continue at Figure 11. Appendix figures move to APA 7 appendix-letter numbering (Figure B1…, C1…, D1…), once, now, as tracked changes, with the List of Figures entries changed to match.
  - **Reason:** plain renumbering (M) would have to be redone every time a later RQ adds a figure, and renumbering ~48 typed captions repeatedly is error-prone. Appendix-letter numbering makes Chapter 4 independent of the appendices, and it is the APA 7 rule the manuscript already follows for references.
  - **Deferred:** a List of Tables and the page numbers go to the final formatting pass, once all of Chapter 4 exists.
- **R5. Mean transfer AUC.**
  - **The dispute:** M says do not use it; S says report it as supplementary with a joint-bootstrap CI.
  - **Proposal:** keep it out of the Chapter 4 text and the RQ1 answer entirely. Put it in Appendix H only (H5 or its own table), with the S B-3.5 caveats, plus an explicit statement that the traceability registry rules out a collapsed generalization score, so it supports no claim.
  - **Reason:** the manuscript has never quoted 0.810, so nothing needs qualifying in the text, and a CI in the main text would make it look like evidence.
- **R15. The fixed-recipe config is not in the package (M-G7).**
  - **Proposal:** Chapter 4 describes it only as "the same predefined non-BO recipe" and gives no hyperparameter values. The lead flags it to the user as an open item to verify against Chapter 3 blocks 496–502.

## Production split after agreement (confirm)

- **Statistician.**
  - Produce one verified CSV per table (T4–T8, H1–H6) in `team/tables/`, values pre-rounded as they will print.
  - Fill Table 1's cluster columns.
  - Check the D-3 references.
- **Methodologist.**
  - Produce Figures 11, 12, 13 and H1 as 300-dpi PNGs, 6.0 in wide, in `team/figures/`, reusing the style constants of `PKG/corrected_20261028_optionA/figures/make_figures_optionA.py`: palette, marker shapes, no embedded titles.
  - Supply the T1–T3 content.
- **Lead.**
  - Write all the prose.
  - Assemble the docx.
- **Then:** both of you review the full draft strictly (Round 3) until all three agree.
