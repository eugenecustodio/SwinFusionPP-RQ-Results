# Final check of RQ1 and RQ2, positive framing, and whole-paper format (lead). All three advisors must agree.

**The user's request:** "Please re-double check RQ1 and RQ2 results. At the end of the day, we want to shed a positive light on SwinFusion++. Make sure also the format is good through all the paper."

## How we read "positive light" (binding for the team)

1. **Make the chapter as favorable as the evidence honestly allows.**
   - Lead with SwinFusion++'s genuine strengths.
   - Keep each caveat once, short, and placed after the finding rather than before it.
   - Remove duplicated or over-long negative sentences.
   - Prefer neutral or positive phrasings that are equally true. For example, "performed at the same near-ceiling level" in place of "did not measurably improve", as long as it is not "equivalent".
2. **Do not:**
   - add claims the evidence does not support;
   - drop required disclosures (Option A, the rank-correction sentence, the Celeb-DF caveat, the threshold-transfer result, the BO caveats);
   - use forbidden words ("outperforms", "robust", "state of the art", "significantly" without a test, "equivalent", vote counts against published models);
   - break the existing claim rules (AGREED_PLAN.md, RQ2_AGREED_PLAN.md, RQ2X_AGREED_PLAN.md).

   An overclaim is the easiest thing for a panel to attack, so honesty protects the user.
3. **Strengths that are true and may be stated more prominently** (verify each):
   - all fixed-recipe AUCs are ≥ 0.9878 within datasets;
   - under transfer, significantly higher ROC-AUC than Swin-B in 7/9 directions and than Video Swin-B in 3/9, and never significantly lower;
   - the highest point AUC among the three matched models in 5 of 9 transfer directions. This is a count within our own matched models, not a count against published models; the statistician must rule;
   - the C23→DFo case, where temporal models held while Swin-B collapsed;
   - BO-selected: the highest point AUCs within C40 (0.9941) and Celeb-DF (0.9983) among all our models (descriptive);
   - RQ2: far above the preliminary Xception on FF++/CDF; C40 AUC above every reported value (Tier A STIL 0.9712; Tier B ≤ 0.983); DFo within the 98.50–100.00 ceiling range; FF++ accuracy within about 2 points of the best reported (BO); thresholds frozen on source validation, unlike most published operating points, which are not stated (factual, and allowed if worded neutrally).

## Inputs

- **Current document, accepted view, block-numbered:** `team/final_check/FULL_ACCEPTED_TEXT.txt` (1,178 blocks; `<TR>` = table row).
- **Accepted .docx copy for XML/style checks:** `.../scratchpad/render/thesis_current_accepted.docx`. Unzip it into your own work folder.
- **The current prose sources:** `tools/ch4_content.py` (opening and RQ1) and `tools/rq2_content.py`.
- **Table CSVs:** `team/tables` (RQ1), `team/rq2/tables` (T9), `team/rq2x/tables` (T10, T11, J9).
- **The Chapter 1–3 edit list:** `team/ch123/edits_agreed.json`.
- **The package:** as before.

## Roles

**Statistician**
- (a) **Re-verify every number in Chapter 4 (opening, RQ1, RQ2), Tables 1–11, Tables J1–J9 and Figures 11–13/J1.** Check them as they appear in FULL_ACCEPTED_TEXT.txt, against the package and the raw predictions. Recompute independently where possible, not just against our own CSVs. Report every mismatch.
- (b) **The positive-framing edit list for RQ1 and RQ2:** exact current sentence → proposed sentence, with the evidence. It covers the RQ1 subsections and answer and the RQ2 answer.
- (c) **Rule on the "5 of 9 highest point AUC" statement** and on any other proposed strength statement.

**Methodologist**
- (a) **A format audit of the WHOLE paper,** front matter to appendices. Check:
  - headings and their styles;
  - chapter heading format;
  - figure and table caption format and numbering sequences;
  - every in-text "Table N"/"Figure N" reference resolving to an existing item;
  - the List of Figures (missing entries for Figures 11–13 and J1);
  - the need for a List of Tables (Tables 1–11, J1–J9);
  - the TOC (a field; note what the user must update);
  - the title page and date;
  - abbreviations defined at first use (FF++, BO, ROC-AUC, PR-AUC, TLBG-HCA, ECE …);
  - consistent naming (FF++ C23 vs C23/HQ; Video Swin-B vs Video Swin Transformer; DeeperForensics-1.0; Celeb-DF v2);
  - number formatting (decimals, % and percentage points, en dash in ranges, U+2212 minus);
  - American spelling;
  - citation ↔ reference consistency, both directions: every in-text citation has a reference and every reference is cited, with author and year matching;
  - APA reference formatting consistency;
  - leftover blank or duplicate paragraphs, stray characters and typos.
- (b) **The examiner's view of the statistician's framing list.**

**Output format (both).**
- Write `team/final_check/<role>_r1.md` with items marked MUST/SHOULD.
- Each edit gives its location (block number, or source file and table) and exact OLD → NEW text.
- Group the edits by where they will be applied:
  - (i) Chapter 1–3 text (via the edit list);
  - (ii) Chapter 4/Appendix J prose (via the content files);
  - (iii) table CSVs and notes;
  - (iv) front matter (LoF/LoT entries);
  - (v) items the user must do in Word (e.g. update fields and page numbers, redraw figures).

Final reply: under 150 words.
