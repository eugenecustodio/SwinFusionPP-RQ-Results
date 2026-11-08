# Lead advisor — Round 1 positions

Numbered so you can reply "agree/disagree with L-n".

## Manuscript mechanics (facts I checked in the docx XML)

- **L-1. Placement.** Chapter 4 is inserted after block 626, the last Chapter 3 paragraph, which already ends with a page break. It goes before block 627 (REFERENCES). Chapter 4 ends with a page break.
- **L-2. Formatting.** Match the existing house style:
  - Chapter heading: style Heading1, centered, "Chapter 4 – RESULTS AND DISCUSSION". Chapter 3 is "Chapter 3 – METHODOLOGY".
  - Sections: Heading2 (bold italic). Sub-subsections: bold body paragraphs, as with "Model Evaluation" at block 613.
  - Body: Arial 12 pt, double-spaced, justified, 0.5-inch first-line indent.
  - Page: Letter with 1.25-inch side margins, so the text width is 6.0 in.
- **L-3. Caption conventions.**
  - Figures are captioned BELOW the image, in style Heading4, centered: "**Figure N.** *Title*" (bold italic number, italic title).
  - The body currently has Figures 1–10 in Chapters 1–3. The appendices have Figures 11–45. The manuscript has no numbered tables.
  - **Numbering problem.** New Chapter 4 figures would collide with appendix Figures 11+.
  - **Options:**
    - (a) Continue at Figure 11 and renumber every appendix figure, about 35 edits plus the List of Figures.
    - (b) Use chapter-prefixed numbers in Chapter 4 only: Table 4.1, Figure 4.1.
    - (c) Follow APA 7: Chapter 4 continues at Figure 11, and appendix figures take letter prefixes (Figure B1…).
  - **My lean:** (b), to avoid touching appendices outside this task. Tables would be "Table 4.1", captioned ABOVE the table in the same Heading4 style. I am open to (c) if you think the panel would object to mixed numbering.
- **L-4. Table format.** Horizontal rules only, APA-like, with a header row. Body 10 pt, single-spaced inside tables. Notes go under each table, 10 pt: abbreviations, CI method, and the meaning of bold.
- **L-5. Figures.** Static 300-dpi PNGs, 6.0 in wide or less, reusing the package's palette. The palette is validated for color-vision deficiency, and each model has its own marker shape (SwinFusion++ circle, Swin-B square, Video Swin-B triangle), so the figures survive grayscale printing.

## Content positions

- **L-6. The RQ1 section covers BOTH in-distribution and cross-dataset results, as RQ1's wording requires.**
  - Holm families stay exactly as computed. The 18 transfer tests are reported under RQ1 even though the package calls that family "RQ6_architecture". In the manuscript I would call them "within-dataset architecture family (m = 8)" and "transfer architecture family (m = 18)", with no RQ prefix.
  - RQ6 later synthesizes these results with the external models and gives the Fix 1 verdict.
- **L-7. Proposed RQ1 order.**
  1. In-distribution, fixed recipe: metrics table, ΔAUC table, one figure.
  2. Cross-dataset, fixed recipe: AUC matrix, ΔAUC tests, the threshold-dependent metrics required by RQ1, one or two figures.
  3. The BO configured system and the optimization effect: a table and possibly a figure.
  4. A one-paragraph answer to RQ1.
  - The topology and capacity controls and the Tier-B ablations: I lean toward RQ4, where the package and the traceability file put them, with one cross-reference sentence in RQ1. The methodologist should rule on this.
- **L-8. Chapter 4 opening, about two paragraphs.**
  - Test-set sizes and clusters, and coverage (100%, no preprocessing failures; verify).
  - The three-seed mean-logit ensemble with frozen source-validation thresholds and temperatures.
  - The Option A disclosure sentence, verbatim.
  - The BO-trial deviation (12/12/8/8 vs the declared 12–20), stated once.
- **L-9. Presentation style** (Philippine convention): introduce the table or figure, state the 2–4 key numbers, then interpret ("This indicates…"). Keep it concise, with no paragraph that merely restates a table row by row.
- **L-10. Number formatting.**
  - AUC: 4 decimals in tables, 3 in text unless the difference needs 4.
  - ΔAUC: signed (+/−).
  - CIs: in brackets.
  - p-values: Holm-adjusted, 3 decimals, with "p < .001" style where applicable. Write p_Holm as "Holm-adjusted p".
  - Accuracy and similar metrics: percentages with 2 decimals, since one video is 0.36% of 280.
- **L-11. Claim discipline.**
  - "Improves" only where Holm-significant.
  - "Statistically indistinguishable / no detectable difference" elsewhere.
  - No causal claim about TLBG-HCA from the encoder comparison alone; the causal evidence is the controls under RQ4.
  - The mean transfer AUC is descriptive only.
- **L-12. Methodology edits.** All are tracked changes. Chapter 3 stays in future tense. Supplementary or post hoc analyses are labeled as such. The actual families are stated.

## Questions for the team

- **Q-L1:** Do threshold-dependent metrics under transfer get one compact table covering all nine directions and three models, or a figure?
- **Q-L2:** Should the within-dataset and transfer ΔAUC results be one combined forest plot with two panels, or separate figures?
- **Q-L3:** Should specificity and PR-AUC be shown even though RQ1 names only Accuracy, Precision, Recall, F1 and ROC-AUC?
