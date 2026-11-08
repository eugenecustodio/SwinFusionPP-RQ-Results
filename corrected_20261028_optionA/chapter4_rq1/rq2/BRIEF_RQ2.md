# RQ2 brief (lead). Same team, same rule: all three advisors must agree.

**RQ2 (block 164):** "What is the performance of SwinFusion++ relative to established baselines when evaluated on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0?"

## User decisions (binding)

1. **Cite the preliminary study** as an unpublished manuscript. Its Xception (and, for RQ3, CNN–LSTM) results may be used, clearly labeled as an earlier pipeline. Add this reference: Custodio, E. T., Degamo, M. K., Escueta, K. R. C., San Diego, D. A. E., & Sarmiento, M. J. F. (2026). *SwinFusion++: Face-aligned spatio-temporal Swin Transformer for deepfake detection* [Unpublished manuscript]. College of Computer Studies and Systems, University of the East–Manila.
2. **Option A.** External comparisons use the BO-selected SwinFusion++, with the fixed-recipe result alongside. Chapter 1, block 175 now reads: "RQ2 will compare BO-selected SwinFusion++, with the fixed-recipe result alongside, with previously reported results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer."
3. **No deviation tables or "than planned" wording** anywhere in Chapter 4.
4. **Everything from RQ1 stands:** the conventions, the claim rules and AGREED_PLAN.md.

## Manuscript state

- **Chapter 4 now:** an opening with Tables 1–2, then RQ1 with Tables 3–8 and Figures 11–13. RQ2 goes after the RQ1 answer, so it starts at **Table 9 and Figure 14**.
- **Appendix J:** has J1–J8 and J1, and is titled "Supplementary Results for Research Question 1". RQ2 supplementary tables continue at J9; propose a new title if needed.
- **The current text:** `team/ch123/CURRENT_CH4_AND_APPXJ.md` (before the Chapter 1–3 edits; Chapter 4 itself is unchanged since).
- **The Chapter 1–3 edits** just applied: `team/ch123/edits_agreed.json` (68 edits; e.g. "previously reported results" wording).

## Inputs

PKG = `/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/`.
- **The current write-up:** `PKG/corrected_20261028_optionA/RQ2/RQ2_RESULTS_AND_DISCUSSION.md` and `results/table2_published_AB.csv` (with `optionA_20261028_note`).
- **Older RQ2 files:** `PKG/RQ2/results/*` (table1_ours, table1b_preliminary_baselines, table2/3 published, fig1_vs_published.png).
- **Literature data:** `PKG/00_Shared/literature/` (official_paper_results_v020.csv/.md, literature_normalised.csv, preliminary_study_v020.csv, preliminary_study_paper.pdf). Read the PDF with `pdftotext`.
- **SwinFusion++ numbers:** Tables 3 and 7 in Chapter 4, and the CSVs in `team/tables/` (T4 = fixed recipe within; T8 = BO vs encoders; the BO within metrics are in `00_Shared/statistics_raw/three_seed_mean_logit_ensemble.csv`).
- **Manuscript text and references:** `team/ch123/CH1_TO_CH3_blocks.txt`; the references are blocks 627–769 of `team/../manuscript_text.txt`, i.e. `.../scratchpad/ch4/manuscript_text.txt`.

## Questions every memo must answer (your role decides the depth)

1. **What RQ2 can legitimately claim.**
   - Published values come from other splits, crops, frame counts and evaluation units, so no tests are possible.
   - The preliminary Xception is a different pipeline and different models; check whether its test populations match.
   - Decide how tiers A/B/C are presented, and which "best published" statements are allowed.
2. **Which published values to show, with their exact source** (paper, table, setting, unit).
   - **Verify the values quoted in the text against the original papers** where accessible (arXiv/CVF open access via WebFetch). The package already had to correct TALL-Swin, STIL, I3D, SFormer and FTCN values once.
   - Every cited paper must be in the manuscript's References. List any that are missing, with a full APA entry verified via Crossref or the publisher.
3. **Tables and figures:** a minimal set, with columns. Should `fig1_vs_published.png` be remade in the house style?
4. **Threshold-dependent metrics.** RQ2 does not name metrics, but published papers mostly report accuracy and AUC. Say how to treat them.
5. **Disclosures specific to RQ2.** For example:
   - only one baseline was run locally, and in an earlier pipeline;
   - the DeeperForensics construction is not the official protocol;
   - the Celeb-DF test set has 978 videos, not the official 518.

## Roles

- **Statistician:** the comparability framework; what may be compared and how (descriptive differences, ranges, no p-values); a check of every number against the package files; the preliminary study's population and pipeline differences (from its PDF); and the reporting of Xception's degenerate operating points (e.g. all-fake on Celeb-DF).
- **Methodologist:**
  - the structure (subsections with Philippine-format introduce/describe/interpret);
  - the tables and figures;
  - claim wording, allowed and forbidden;
  - verification of the published values against the original papers, by spot-checking at least every value the text will quote;
  - reference coverage, with full APA entries for any missing references.

## Output

Write `team/rq2/<role>_r1.md` with sections: A. Positions; B. Tables/figures spec; C. Claims allowed/forbidden; D. Verification results (numbers, sources, references); E. Questions for the team.

Final reply: under 150 words.
