# Final check, round 1: methodologist

**Verdict.**
- (a) **Format audit of the whole paper.**
  - Numbering is clean. Tables 1–11 and J1–J9 run in sequence. So do Figures 1–13, B1–B27, C1–C8, D1–D6, E1–E3, F1–F4 and J1. There are no duplicate numbers.
  - Every in-text "Table N"/"Figure N" reference points to an item that exists.
  - The prose uses American spelling throughout. The only British forms ("Towards", "generalisable") are inside published reference titles and must stay.
  - Chapter 4 and Appendix J have no hyphen-minus before a number. Every minus sign is U+2212.
  - The defects found fall into five groups:
    1. A missing List of Tables, and a List of Figures without Figures 11–13 and J1.
    2. A TOC field that will fill with caption lines when updated.
    3. Citation and reference mismatches, one of them a year error.
    4. APA initials used in Chapter 4 but not in Chapters 1–3.
    5. Thirteen broken compounds left over from PDF line breaks ("zero- initialized").
  - **Totals:** 48 MUST and 19 SHOULD text edits, all in `methodologist_edits.json`. Every OLD string was checked to occur exactly once in its block (`scripts/m_final_edits_verify.py`: 79 checked, 0 failures; 12 were later withdrawn in favor of the statistician's edits). There are also 6 table/CSV items, 3 front-matter items and 9 Word-only user items.
- (b) **Statistician's framing list (E1–E14).**
  - I agree with all 14 edits and with the S1–S7 rulings.
  - Five edits need small amendments (E2, E4, E11, E13/E14, and E12 for "percentage points"). Two of the amendments are **MUST**: E2 and E4 say "the three models were statistically indistinguishable", but Swin-B vs Video Swin-B was never tested.
  - I withdraw 11 of my own framing drafts because E1–E14 cover them. Two remain (P5, P12).
- The examiner's overall view is in part B.

Scripts (all in `team/scripts/`): `m_fmt_audit.py` (captions, references, LoF), `m_fmt_audit2.py` (abbreviations, naming), `m_fmt_audit3.py` (spelling, minus signs, ranges, spacing), `m_fmt_audit4.py` (figure callouts, quotation marks, percentage points, first uses), `m_fmt_cites.py` (citations ↔ references), `m_fmt_initials.py` (APA initials), `m_fmt_ctx.py`, `m_final_edits_verify.py`. XML checks were run on my own unzip of `render/thesis_current_accepted.docx` (`scratchpad/final_check_m/x/`).

---

## A. Format audit: findings and edits

### What passed (no action)

- **Chapter headings.**
  - All four chapters use Heading 1, centered, in the form "Chapter N – TITLE", with an en dash.
  - Chapter 4's Heading 2s ("Evaluation Setting"; "Research Question 1: …"; "Research Question 2: …") use the same paragraph format as the Chapter 3 Heading 2s.
  - The run-in subsection headings (bold, justified, not a heading style) match the Chapter 3 convention ("Model Evaluation Procedure").
- **Captions.**
  - Every Chapter 4 and Appendix J caption is Heading 4, centered, with a bold-italic label and an italic title. This matches Figures 1–10 and B1–B27.
  - Table captions sit above the table and figure captions below the image. This follows the thesis convention.
  - Notes start with an italic "Note." at 10 pt.
- **Callouts.**
  - Every Table 1–11 and Figure 11–13 is called out in the text before it appears.
  - Tables J1–J9 are called out through "Tables J1 to J8" and "Table J9" (block 1147).
- **Numbers.**
  - Signed differences use U+2212.
  - Ranges in prose use words ("from 0.198 to 0.925") or an en dash ("0–0.2").
  - Leading zeros are used consistently throughout (0.021, 0.9941). The style is unchanged, because a change would touch hundreds of values.
- **Spelling.** No British spelling appears in the prose.
- **Abbreviations defined at first use.**
  - TLBG-HCA (block 146), FPR and FNR (519) and PHREB (222) are defined.
  - FF++ is defined at its first use, in block 631 ("FaceForensics++ [FF++]"), and BO is defined again there for Chapter 4.
  - CDF, DFo, C23 and C40 are defined in the Table 5–8 notes and in the Figure 11 note.

### (i) Chapter 1–3 text, via the edit list

The exact OLD → NEW strings are in `team/final_check/methodologist_edits.json` (ids F*, S*). Their content is summarized here.

**MUST**

- **F1. Block 209: wrong year.** "(Thakre et al., 2025;" → "(Thakre et al., 2026;".
  - The reference is Thakre et al. (2026), *Knowledge-Based Systems*, 338.
  - Blocks 215 and 226 already cite 2026.
- **F2. Block 228: a citation with no reference.** "Kuang et al., 2022; " → "" (deleted).
  - No Kuang entry exists in the References.
  - The package has no bibliographic record: `literature_normalised.csv` lists only a second-author Kuang (Song et al., 2026), and `autonomous_decisions_v020.md` mentions "Kuang 2022" only as an RQ3 fallback.
  - USER: if the user can supply the full reference, restore the citation and add the entry instead of deleting it.
- **F3–F4. Block 228: narrative citations without a year.**
  - "family of Chen et al. and" → "family of B. Chen et al. (2022) and".
  - "CNN–LSTM family of Saikia et al." → "CNN–LSTM family of Saikia et al. (2022)".
- **F5. Block 559.** "(Nielsen, J., 2024)" → "(Nielsen, 2024)". There is only one Nielsen, so APA uses no initial.
- **F6–F8. Three references are never cited. Each is cited at the natural place, which also defines BO and TPE at first use:**
  - **F6, block 148.** "after one independent Optuna/TPE study for each condition." → "after one independent Bayesian optimization (BO) study for each condition, run in Optuna (Akiba et al., 2019) with its Tree-structured Parzen Estimator (TPE; Bergstra et al., 2011)."
    - BO is first used in block 159 and is otherwise never defined in Chapters 1–3.
  - **F7, block 455.** "The automated policy will be identified by its standard name, RandAugment, and cited accordingly." → "The automated policy will be RandAugment (Cubuk et al., 2020)."
    - The current sentence promises a citation that is never given.
  - **F8, block 615.** "Holm adjustment will be the default" → "Holm adjustment (Holm, 1979) will be the default".
    - Block 521, the "strong only if" criterion, is not touched.
- **F9. Block 433: ROC-AUC is never spelled out anywhere in the paper.** Block 433 is its first use outside the RQ statements, which cannot be edited.
  - "A validation ROC-AUC of at least" → "A validation area under the receiver operating characteristic curve (ROC-AUC) of at least".
- **F10a–v. APA 7 §8.20 initials, 22 edits.** Chapter 4 already uses initials, so Chapters 1–3 must match. Six first-author surnames belong to more than one person in the References (number of different initials: Li 4, Wang 4, Zhang 3, Zhao 2, Chen 2, Guo 2).
  - "Li et al., 2020" (blocks 205, 207, 219, 519, 520) is genuinely ambiguous: L., X. and Y. Li all have 2020 entries. In all five places the context is the dataset triad (FF++, Celeb-DF, DeeperForensics), so the source is the Celeb-DF paper.

  | Block(s) | OLD | NEW |
  |---|---|---|
  | 205, 207, 219, 519, 520 | Li et al., 2020 | Y. Li et al., 2020 |
  | 206 / 231 | Wang et al., 2020 / Wang et al. (2020) | R. Wang et al., 2020 / R. Wang et al. (2020) |
  | 207, 208, 515 / 228 / 230 | Chen et al., 2022 / (Chen et al., 2022; / Chen et al. (2022) | B. Chen … |
  | 215 | Chen et al., 2021 | C.-F. R. Chen et al., 2021 |
  | 218 / 231 | Guo et al., 2017 / Guo et al. (2020) | C. Guo et al., 2017 / Z. Guo et al. (2020) |
  | 209, 226 | Zhao et al., 2023 | C. Zhao et al., 2023 |
  | 209, 227 / 220 | Zhang et al., 2024 / Zhang et al., 2016 | H. Zhang et al., 2024 / K. Zhang et al., 2016 |
  | 233 | Li and Lyu (2018) / Li et al. (2018) | Y. Li and Lyu (2018) / Y. Li et al. (2018) |

- **F11a–m. Broken compounds from PDF line breaks, 13 edits.**
  - "cross- attention" (blocks 146 and 215); "corre- sponding" (147, → "corresponding"); "source- selected" (148).
  - "temporal- consistency" (225); "zero- initialized" (226); "spatio- temporal-attention" (228); "temperature- scaled" (304).
  - "FaceNet- style" and "clip- consistent" (323); "materi- alize" (367, → "materialize"); "non- attentive" (367); "Cross- compression" (616).
  - In each case the space after the hyphen is removed. "higher- versus lower-quality" (block 265) is a correct suspended hyphen and stays.
- **F12a–c. Naming.**
  - "Video-Swin-B" → "Video Swin-B" in blocks 226, 237 and 291.
  - "Video Swin-B" appears 38 times elsewhere.

**SHOULD**

- **S1, block 505.** "Ties will be resolved by higher PR-AUC, lower validation BCE," → "Ties will be resolved by higher area under the precision–recall curve (PR-AUC), lower validation binary cross-entropy (BCE),". This is the first use of both abbreviations.
- **S2, block 614.** "expected calibration error will be added" → "expected calibration error (ECE) will be added". Block 617 uses "ECE".
- **S3, block 191.** "may cause MTCNN or identity association to fail" → "may cause the multi-task cascaded convolutional network (MTCNN) face detector or identity association to fail".
- **S4a–c. "Celeb-DF (v2)" → "Celeb-DF v2"** in blocks 219, 263 and 418.
  - The form "Celeb-DF v2" appears 84 times.
  - In block 263 the OLD text uses non-breaking hyphens (U+2011): "Celeb‑DF (v2)". The JSON entry encodes this.
- **S5, block 204 (Heading 2).** "Review of Related Literatures" → "Review of Related Literature". The TOC line changes when the field is updated.
- **S6, block 394.** "the number of distributed questionnaire may be adjusted" → "questionnaires".
- **S7a–d. Double spaces:** three in block 404 and one in block 487 ("representation  so that"). The XML confirms that block 487 has no dropped equation.
- **S8 (USER/lead). Figures 1–10 are never called out in the text.**
  - APA 7 requires every figure to be referred to by number.
  - Add a short callout before each one, for example "Figure 1 presents the conceptual framework." in the paragraph under "Conceptual Framework" (block 243).
  - Figures 4–10 follow lead-in sentences such as "the estimated standard deviation is:". These can become "…is shown in Figure 6:".
  - No JSON entry is given, because the lead-in wording is the user's choice.
- **S9. Reference order.** "Güera, D., & Delp, E. J. (2018)" (block 777) must come before "Guo, C." (block 773) and "Guo, Z." (block 775). APA orders letter by letter, and "Gue" precedes "Guo".
- **S10 (USER DECISION). Two references are never cited, and were not cited in the original manuscript either.**
  - Esperanza et al. (2025), block 761, and Laureta et al. (2025), block 815.
  - Either cite them where the user intended (likely the local-studies part of Chapter 2) or delete both entries. One of the two must happen; APA requires every reference to be cited.
- **S11 (USER). Thirteen references have no DOI or URL:** blocks 729, 735, 743, 747, 751, 779, 787, 847, 871, 875, 893 and 907. Block 753, the unpublished preliminary study, is fine without one.
  - Add the DOI or URL where one exists. Several CVF and NeurIPS papers in the list already carry their open-access URL, so this is a consistency issue.
  - I did not supply links, because none can be traced in the package.

### (ii) Chapter 4/Appendix J prose, via the content files

**MUST**

- **G2, block 1147. Figure J1 is never called out.** "(Tables J1 to J8)" → "(Tables J1 to J8 and Figure J1)".
- **E13, block 718: the forbidden word "outperforms".** I accept the statistician's NEW text, which replaces my own draft G1.

**SHOULD (format)**

- **G3, block 639.** "another condition's" → "another condition’s". Chapter 4 otherwise uses the curly apostrophe (17 times), as Chapters 1–3 do.
- **G5, block 632.** "…the predeclared horizontal-flip variant is reported in Appendix J." → "…in Appendix J, Table J4."
- **G6, block 633.** "…are described in Chapter 3 under Amendments after Test Scoring." → "…Test Scoring, and the original and corrected tests are compared in Appendix J, Table J5."
  - This is the sentence before the rank-correction sentence. The rank-correction sentence itself is unchanged.
  - Optional: G5 and G6 give J4 and J5 explicit callouts in addition to the range in block 1147.
- **G7, block 652.** In the last sentence, which is identical in E1 NEW: "…near the ceiling of the metric on every test set." → "…on every test set (ROC curves in Appendix J, Figure J1)."
- **G8, block 1146.** "Supplementary Results for Research Questions 1 and 2" → "SUPPLEMENTARY RESULTS FOR RESEARCH QUESTIONS 1 AND 2". This matches the title lines of Appendices A–G. Appendices H and I are a user item (v).
- **E12 amendment.** In the E12 NEW text, "2.14 and 3.57 points below" → "2.14 and 3.57 percentage points below". This replaces my G4. The chapter uses "percentage points" everywhere else.

**Framing items of mine that remain** (all the others are withdrawn; see B):

- **P5 (SHOULD), block 682.** "For an unseen dataset, the frozen screening label is therefore much less informative than the ranking results suggest, for all three models." → "For all three models, the frozen screening label on an unseen dataset is therefore much less informative than the ranking results suggest."
  - Placing "all three models" first stops the sentence reading as a SwinFusion++-specific weakness.
  - The disclosure is unchanged.
- **P12 (SHOULD), the last sentence of block 720 (also the last sentence of E14).** "they place SwinFusion++ among the listed methods on FaceForensics++ but cannot rank it against them." → "they place SwinFusion++ in the same high range as the listed methods on FaceForensics++ and DeeperForensics-1.0, without ranking it against them."
  - With E13, the RQ2 section would otherwise say "cannot rank" twice in three paragraphs.
  - The DeeperForensics-1.0 clause is supported by block 717: 98.51% (fixed recipe 98.76%) lies within the range 98.50–100.00.

### (iii) Table CSVs and notes

- **MUST. J9.csv, Source column, 4 rows.** "Zhang et al. (2024)" → "H. Zhang et al. (2024)". These are the TSFF-Net rows, Table 3, PDF p. 11. This matches the initials convention in block 700 and F10.
- **SHOULD. J9.csv, mechanical fixes:**
  - Locators: "PDF p.N" → "PDF p. N" (233 cells; 53 cells already use the spaced form), and "p.9-10" → "pp. 9–10" (1 cell).
    - Suggested regex on the Source column: `\bp\.(?=\d)` → `p. `, then `p\. 9-10` → `pp. 9–10`.
  - Model column, 4 rows: "XceptionNet (Rossler et al. 2019)" → "XceptionNet (Rössler et al., 2019)".
  - Secondary sources (APA "as cited in"), 2 + 3 rows:
    - "de Lima et al. (2020), via Saikia et al. (2022), Saikia et al. 2022 Table IV" → "de Lima et al. (2020), as cited in Saikia et al. (2022), Table IV".
    - "Rössler et al. (2019), Sabir et al. Table 1" → "Rössler et al. (2019), as cited in Sabir et al. (2019), Table 1".
    - de Lima et al. is not in the References, which is correct for a secondary citation only in the "as cited in" form.
  - Straight quotes in 22 cells (e.g. row 'De Lima et al. [39]', row "XceptionNet [4]", column 'FF++ [34]') → curly double quotes “…”.
- **SHOULD. Straight quotes and apostrophes in notes.** Chapters 1–3 use only curly quotes (26 pairs, 0 straight).
  - Tables 5, 7 and 8: "< 0.005" → “< 0.005”. Table 6: "—" → “—”. Table J7: "< 0.005" → “< 0.005”. The source note files with straight quotes are `tables/T6_note.txt`, `T7_note.txt`, `T8_note.txt`, `T9_note.txt` and `J7_note.txt`; check them against the lead's file-to-table mapping.
  - Table 1 note (`T1_note.txt`): "source's" → "source’s".
  - Figure 13 note (`figures/captions.md`): "model's" → "model’s".
- **SHOULD. Column abbreviations not defined in table notes** (APA 7 §7.14; SD, CI and p need no definition).
  - Table 3: add "Acc = accuracy; Prec = precision; Rec = recall; Spec = specificity; FP = false positives; FN = false negatives."
  - Table 6: the same sentence, without FN if that column is absent.
  - Table 9: "Acc = accuracy; Rec = recall; Spec = specificity."
  - Tables 10 and 11: "Acc = accuracy."
  - Optional: "FF++ = FaceForensics++" in the Table 1, 3, 4 and 9–11 notes.
- **Agree: the statistician's F1 addition to the J9 note.**

### (iv) Front matter

- **MUST. The List of Figures is manual text, not a field.**
  - Insert after "Figure 10. No. of Distributed Questionnaires" (block 87):
    - Figure 11. Transfer ROC-AUC of the Fixed-Recipe Models by Training and Test Dataset
    - Figure 12. Paired Differences in ROC-AUC Between Fixed-Recipe SwinFusion++ and Each Encoder
    - Figure 13. ROC Curves Under Frozen Cross-Dataset Transfer With the Frozen Operating Points
  - Insert after "Figure F4. CERC Result - Page 4" (block 137):
    - Figure J1. Within-Dataset ROC Curves of the Fixed-Recipe Models
  - Page numbers come from Word after repagination.
- **MUST. Add a "LIST OF TABLES" page after the List of Figures**, in the same layout (centered caps heading, "TITLE … PAGE" header line, tab leader). Entries, with titles exactly as captioned:
  - Table 1. Test Sets, Dependence Structure, and Coverage
  - Table 2. Analyses, Comparison Families, and Where They Are Reported
  - Table 3. Within-Dataset Performance of the Fixed-Recipe Models
  - Table 4. Paired ROC-AUC Differences Within Datasets, Fixed Recipe
  - Table 5. Paired ROC-AUC Differences Under Frozen Transfer, Fixed Recipe
  - Table 6. Threshold-Dependent Metrics Under Frozen Transfer, Fixed Recipe
  - Table 7. BO-Selected SwinFusion++ Compared With the Fixed-Recipe Encoders
  - Table 8. Optimization Effect: BO-Selected Minus Fixed-Recipe SwinFusion++
  - Table 9. SwinFusion++ and the Preliminary-Study Xception Baseline
  - Table 10. Previously Reported Tier A Results on the Benchmarks of This Study
  - Table 11. Previously Reported Tier B Results on FaceForensics++
  - Table J1. Per-Seed ROC-AUC for Every Model, Regimen, and Test Condition
  - Table J2. Supplementary Paired Differences in Threshold-Dependent Metrics, Fixed Recipe
  - Table J3. ROC-AUC on the Strict Lineage-Free Subsets, by Seed
  - Table J4. Plain and Horizontal-Flip ROC-AUC for All Models
  - Table J5. Original Raw-Logit and Corrected Rank-Based Permutation Tests
  - Table J6. Within-Dataset Sensitivity: Detectable Difference and Available Headroom
  - Table J7. Robustness of the Ten Significant Architecture Differences
  - Table J8. Transfer ROC-AUC With 95% Intervals for All Models
  - Table J9. Previously Reported Values Considered for Research Question 2
  - Note: the title of Table J7 contains "Robustness". This is the APA technical sense (sensitivity checks), not the forbidden claim "robust detector", so I recommend no change. If the team prefers, "Sensitivity of the Ten Significant Architecture Differences" is an equally accurate title.
- **MUST. The front-matter list in blocks 29–31** ("Title Page i / Table of Contents ii / List of Figures iii"): add the line "List of Tables" with its page number.

### (v) Word-only items for the user

1. **MUST (USER DECISION). Updating the TOC.**
   - The TOC is a field: `TOC \h \u \z \t "Heading 1,1,…,Heading 4,4,…"`.
   - About 49 captions are Heading 4 (all table and figure captions in Chapter 4 and Appendix J, Figures 1–10, B1–B7, B18, E1–E3 and F1–F4), alongside the Appendix A–J headings.
   - A Word "Update entire table" will therefore put every one of those captions into the TOC. The present TOC was evidently hand-edited: it has no captions, chapter lines without the "Chapter N –" prefix, and "APPENDIX A: GANTT CHART" merged into one line.
   - It also lacks Chapter 4 and Appendices H–J.
   - **Recommended:** right-click → Update Field → "Update page numbers only". Then type in, in the same style:
     - "PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA";
     - "Evaluation Setting";
     - "Research Question 1: SwinFusion++ Compared With the Standalone Encoders";
     - "Research Question 2: SwinFusion++ Compared With Established Baselines";
     - "APPENDIX H: TURNITIN RESULTS – SIMILARITY REPORT", "APPENDIX I: …" and "APPENDIX J: SUPPLEMENTARY RESULTS FOR RESEARCH QUESTIONS 1 AND 2";
     - the corrected "Review of Related Literature" (S5).
   - **Alternative:** update the entire table, then delete the caption lines. This must be repeated after every later update.
2. **MUST. Restyle the empty heading paragraphs as Normal:** Heading 2 at blocks 242, 359 and 611, and Heading 4 at block 988. Do not delete them, in case they carry page breaks. Otherwise any TOC update produces blank entries.
3. **MUST. Page numbers** for the new LoF, LoT and TOC entries after repagination.
4. **USER DECISION. Title page date** (block 25) still reads "MARCH 2026". Set it to the actual submission or defense month.
5. **USER. Appendix I** ("Turnitin Results - AI Report", block 1143) has no content: block 1144 is empty. Insert the report, or remove the appendix and its TOC line.
6. **SHOULD. Appendix title lines.**
   - Make the titles of H and I all caps, like A–G, with an en dash: "TURNITIN RESULTS – SIMILARITY REPORT" and "TURNITIN RESULTS – AI REPORT".
   - This goes with G8 for Appendix J.
7. **SHOULD. Appendix figure captions.**
   - Figures C1–C8 and D1–F4 have a non-bold label. All other captions have a bold label.
   - D1–D6, E1–E3 and F1–F4 are not centered.
   - Apply the Figure 1 or B1 caption format.
8. **SHOULD. LoF entries D3 and D6** are wrapped with hard returns plus spaces (blocks 125–126 and 129–130). Replace these with one paragraph and a hanging indent so repagination does not break them.
9. **SHOULD.** "REFERENCES" is justified and "APPENDICES" is left-aligned. All chapter headings are centered. Center both, unless the department template says otherwise.
10. **For the user's awareness (no edit now).** Table 2 ("RQ4"; "Section after RQ6"), block 671 ("examined under RQ4") and block 696 ("under RQ4 … under RQ6") point to sections that are not in the document yet. They must exist before submission, or those cells and sentences must be edited.
11. **No figure redraw is needed.** The statistician checked all four images against the data, and no edit here changes a figure.

---

## B. The examiner's view of the statistician's framing list

**Overall.**
- The list does what the user asked without dropping anything we must disclose. Each change leads with the tested transfer result, states each caveat once and after its finding, and removes the duplicated 6 + 2 listing.
- From a panel's side, the edits are safe because every new strength is a test-backed or descriptive statement, labeled as such.

**Item-by-item.**

| Edit | View | Note |
|---|---|---|
| E1 (652) | AGREE | "within 0.0037 of the highest" is true (C40 0.9915 − 0.9878). The six-of-eight disclosure is kept in E2. Add G7 to its last sentence. |
| E2 (657) | AGREE WITH AMENDMENTS (1 MUST, 3 SHOULD) | **MUST:** "the three models were therefore statistically indistinguishable in ROC-AUC" → "SwinFusion++ was therefore statistically indistinguishable from both encoders in ROC-AUC". Only SwinFusion++ vs each encoder was tested; Swin-B vs Video Swin-B never was. **SHOULD:** "which rules out a large difference in either direction" → "which is incompatible with a large difference in either direction" (the signed-off wording; "rules out" reads as proof). **SHOULD:** "these gains reflect where the frozen thresholds fell" → "these gains are best read as differences in where the frozen thresholds fell" (an inference, so keep the hedge). **SHOULD:** drop ", and no accuracy interval excluded zero in an encoder’s favor". It is literally true, but Table J2 prints C23 vs Video Swin-B as [−2.50, 0.00] for accuracy and [−0.0250, 0.0000] for F1, so a reader will see an edge case, and the clause adds no strength. |
| E3 (669) | AGREE | "In these three directions, it was significantly better than both encoders" is verified: the three significant Video Swin-B directions are among the seven Swin-B ones. |
| E3-B | AGREE; it replaces my P3 | I accept the statistician's S3 ruling that a bare "5 of 9" tally is out. Optional wording: "…but its lead over the runner-up, Video Swin-B, was not significant in either direction (…)". In C23 → C40 the lead over Swin-B was not significant either, so "the runner-up" avoids implying otherwise. |
| E4 (670) | AGREE WITH MUST AMENDMENT | "From FF++ C23, the three models were statistically indistinguishable on FF++ C40 and Celeb-DF v2" → "From FF++ C23, SwinFusion++ was statistically indistinguishable from both encoders on FF++ C40 and Celeb-DF v2". Same reason as E2. "+0.258 … the largest of all 18" is verified. |
| E5 (671) | AGREE; it replaces my P4 | "stable across seeds and analysis choices" is acceptable, because it avoids "robust" and names its evidence (Table J7). |
| E6 | AGREE | Block 681 stays the single place for the 6 + 2 list. |
| E7 (688) | AGREE; it replaces my P6 | Broader than my "four models compared here", and the statistician verified it against every ensemble on those test sets, including the controls. My check against Table J1: C40 0.9941 > 0.9915 > 0.9883 > 0.9878; Celeb-DF v2 0.9983 > 0.9958 = 0.9958 > 0.9951. |
| E8 (694) | AGREE; it replaces my P7 | The verb of RQ1 is still answered explicitly in E10 ("no improvement was detectable"), so the answer does not dodge the question. |
| E9 (695) | AGREE; it replaces my P8 | Dropping the all-model precision clause is fine: it is not a required disclosure, and block 680 keeps the conservative-threshold result. |
| E10 (696) | AGREE; it replaces my P9 | — |
| E11 (716) | AGREE WITH SHOULD AMENDMENT | Use range wording and limit the comparison to the chapter tables. "On C40, both SwinFusion++ values were higher than every C40 ROC-AUC in Tables 10, 11, and J9" → "On C40, both SwinFusion++ values lay above the reported range (highest 0.983, FTCN)". J9 holds the rows we excluded as non-comparable, so citing them as a yardstick contradicts the tiering. Range wording also matches how C23 is described ("within the reported range") and cannot be read as a vote count. I verified the C40 maximum in J9.csv: 0.9830. |
| E12 (717) | AGREE; it replaces my P10/P11 for this block | Write "percentage points" in place of "points" (see (ii)). |
| E13 (718) | AGREE; it replaces my G1 | — |
| E14 (720) | AGREE WITH SHOULD AMENDMENTS | (1) "was higher than every reported value considered (highest 0.983)" → "lay above the reported range (highest 0.983)", for the same reason as E11. (2) **Include** the optional S6(v) sentence. Its neutral form is true (block 632) and states a real protocol strength. (3) Apply P12 to the last sentence. |

**Rulings S1–S7.**
- I agree with all of them, including:
  - rejecting "collapsed" (S4);
  - requiring exact values in place of "about 2 points" (S6 iv);
  - rejecting "unlike most published operating points" (S6 v);
  - keeping the unweighted mean transfer AUC (0.8099) in Appendix J only (S7).
- I had considered citing that mean in the prose and drop the idea. A mean across heterogeneous directions invites the question "why average AUCs across different targets?"
- On S4, the C23 → DFo strength belongs to "the two models with a temporal stream", and SwinFusion++ (0.8261) was below Video Swin-B (0.8421) there. The wording in E4 keeps this right.

**F2 (metadata-audit traceability).** I agree. The user should copy `metadata_shortcut_audit_v001.md` into the package. No text change is needed.

**Checks on all accepted framing edits combined:**
- **Option A disclosure:** block 633's first sentence is untouched.
- **Rank-correction sentence:** untouched.
- **Celeb-DF caveat:** kept in the Table 1 note, block 638 and E2.
- **Threshold-transfer result:** kept in blocks 680–682, E9 and E10.
- **BO caveats:** blocks 692 and 696 unchanged.
- **Forbidden words:** none. "equivalence" appears only in the required negation. "robust" appears only in the Table J7 title (see (iv)).
- **The six RQ statements:** untouched.
- **Block 521:** untouched.

---

## C. For the lead

1. Apply the (i) edits from `methodologist_edits.json` (59 entries: 47 MUST, 12 SHOULD) through the Chapter 1–3 edit-list mechanism.
   - Apply F10j after F2, in either order; the strings do not overlap.
   - S4b contains U+2011.
2. Apply the (ii) items together with the statistician's E1–E14, including the amendments in part B.
   - G7 and P12 use OLD strings that exist both in the current text and in the E1/E14 NEW text.
3. After rebuilding, re-run `scripts/m_fmt_audit.py`, `m_fmt_cites.py` and `m_fmt_initials.py`. The expected result:
   - the only unresolved reference item is Esperanza/Laureta (S10);
   - "LoF missing: [11, 12, 13, J1]" clears only after the user's front-matter edit;
   - "captioned but never referenced" leaves only Figures 1–10 (S8, user).
