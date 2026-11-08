# Final check, round 3: methodologist

Checked: `FULL_ACCEPTED_TEXT_v2.txt` and the XML of `render/thesis_final_accepted.docx`.
Script: `team/scripts/m_fmt_v2.py`, a re-run of m_fmt_audit, m_fmt_cites and m_fmt_initials with the new block boundaries:

| Part | Block |
|---|---|
| List of Figures | 76 |
| List of Tables | 146 |
| Chapter 1 | 170 |
| References | 745 |
| Appendices | 934 |
| Appendix J | 1168 |

## Verified

**Numbering and lists**
- **Caption numbering:** every sequence is complete, with no duplicates (Tables 1–11 and J1–J9; Figures 1–13, B1–B27, C1–C8, D1–D6, E1–E3, F1–F4 and J1).
- **List of Figures:** 62 entries, in order, none missing. Figures 11–13 follow Figure 10, and J1 follows F4.
- **List of Tables:** 20 entries, in order, with every title matching its caption.

**Front-matter layout (XML)**
- The List of Tables page has the same layout as the List of Figures:
  - a page-break paragraph before it;
  - a centered, bold, 12 pt "LIST OF TABLES" heading;
  - the same "TITLE … PAGE" header line;
  - entries with one tab and a right-aligned dot leader at 12000;
  - a page break before Chapter 1.
- The new "List of Tables" line in the front-matter list matches the formatting of the lines above it.

**Citations and references**
- Every in-text citation has a reference. The only exception is de Lima et al. (2020), which is correct because it is cited in the "as cited in" form.
- The only references never cited are Esperanza (2025) and Laureta (2025). These are a user decision (item S10).
- No ambiguous surname is cited without initials.
- The specific fixes are in place: Thakre 2026, Kuang removed, Nielsen corrected, and Akiba, Bergstra, Cubuk and Holm now cited.

**Abbreviations and wording**
- ROC-AUC, BO, TPE, PR-AUC, BCE, ECE and MTCNN are each defined at first use.
- There are no broken compounds, no "Video-Swin-B", no "Celeb-DF (v2)" and no "Literatures".
- Chapter 4 and Appendix J contain no hyphen-minus before a number, no bare "points" and no forbidden word. The one "collapsed" is in the Table J8 note's phrase "collapsed generalization score", which is technical usage.

**Applied edits**
- The E2 and E4 MUST amendments are applied: "SwinFusion++ was statistically indistinguishable from both encoders".
- E11 and E14 use the range wording; Table J9 is not used as a yardstick.
- E14 includes the S6(v) sentence.
- P5, P12, G2 and G5–G8 are applied.

**Table and note fixes**
- J9: H. Zhang ×4, the "as cited in" forms (2 + 3), Rössler, "PDF p. N", and "pp. 9–10".
- Curly quotes in the notes, and the column-abbreviation sentences.

**Required disclosures, unchanged**
- The Option A sentence and the rank-correction sentence are verbatim.
- The "strong only if" block (now block 544) is present.

## MUST-FIX (small leftovers)

1. **Block 641 (Amendments after Test Scoring): straight apostrophes.**
   - "each model's video scores" → "each model’s video scores"
   - "McNemar's test" → "McNemar’s test"
2. **List of Figures, block 126: entry does not match its caption (block 1064).**
   - "Figure C8. User Evaluation Survey - Security, Comments and/or Suggestions" → "Figure C8. User Evaluation Survey - Security & Comments and/or Suggestions"
3. **Block 175: stray leading space.**
   - " To address this gap, this study proposes" → "To address this gap, this study proposes"

## Still for the user in Word (from round 1, part (v); no lead action)

- Restyle the empty heading paragraphs (blocks 267, 384 and 634, Heading 2; block 1011, Heading 4) as Normal.
- Update the TOC, using "Update page numbers only" and then adding the new entries by hand.
- Add page numbers to all new List of Figures, List of Tables and TOC entries. The extra page shifts every later page by one.
- Change the "MARCH 2026" date on the title page.
- Fill Appendix I, which is still empty.
- Add callouts in the text for Figures 1–10.
- Decide on Esperanza (2025) and Laureta (2025): cite them or delete them.
