# Consistency review of Chapters 1–3 against the results: brief (lead)

**The task, from the user:** "Since you know the Results, … double check Chapter 1 to Chapter 3, make sure there would be consistency." All three advisors must agree before anything is changed.

## Inputs (in `team/ch123/` unless stated)

- **`CH1_TO_CH3_blocks.txt`.** Chapters 1–3 (blocks 141–626) plus the front matter (0–140), as `[block] (style) text`.
  - This is the docx text before Chapter 4 was added. Chapters 1–3 have not changed since, except for two things:
    - the Fix 2 sentence already at block 521;
    - the new paragraph after block 617 (`CH3_AMENDMENTS_PARAGRAPH.txt`).
- **`CURRENT_CH4_AND_APPXJ.md`.** Chapter 4 and Appendix J as they now stand. The deviations table was removed at the user's request, and the tables are now numbered 1–8.
- **`figures/`.** The Chapter 1–3 images (Figure 1 Conceptual Framework, Figure 2 HIPO, Figure 3 Flowchart, equations) and `INDEX.txt`. You can read the PNGs.
- **Facts about what was actually done:**
  - `PKG/corrected_20261028_optionA/CHAPTER4_NOTES.md`, all sections. §4 covers the backup findings and §6 the web-app review.
  - `team/tables/T3.csv` (the removed deviations table) and `team/AGREED_PLAN.md`.
  - The package protocol files: `00_Shared/protocol_and_decisions/*`, `00_Shared/bayesian_optimisation/*`, and the RQ2–RQ4 write-ups in `PKG/corrected_20261028_optionA/RQ*/`.

## What to find

Find every statement in Chapters 1–3 that a panel would see as inconsistent, in any of four ways:
- **(a)** with the results or the pipeline that was actually run: datasets, preprocessing, models, controls, ablations, baselines, BO, hardware, evaluation, statistics, calibration, compute;
- **(b)** with Chapter 4 as written: terminology, family names, test sets, numbers;
- **(c)** within Chapters 1–3: terminology (e.g. "confidence score" vs the Chapter 3 rule that the term will not be used), duplicated paragraphs, contradictory numbers;
- **(d)** promises of things that were not done or do not exist. The user said: "We should not leave this promised if we do not have."

## Rules for proposed edits

1. **Format.** One item per issue: ID, block, severity (**MUST** or **SHOULD**), exact OLD text (a verbatim contiguous substring of that block's text), exact NEW text, a one-line reason, and the evidence file. Keep each edit minimal: change the smallest span that fixes the problem.
2. **Tense.** Keep the surrounding tense. Chapter 3 stays future tense; the switch to past tense is a separate, later formatting pass. Where future tense would misdescribe what happened, use a neutral formulation that is still true (e.g. "The final pipeline applies no low-light correction"). Propose a rule if you disagree.
3. **No deviation framing.** Do NOT add a deviations table, section or list anywhere. Do NOT add "deviated"/"than planned" wording. In Chapters 1–3, simply state what the study does or does not do.
   - Do NOT propose moving content into Appendix G (Revision List) or Chapter 5. List such ideas under "USER DECISION" instead.
4. **Do NOT change:**
   - the six RQ statements (blocks 163–168);
   - the "strong only if" criterion and Fix 2 (block 521);
   - the Option A framing.

   If an RQ statement itself is inconsistent, flag it under USER DECISION.
5. **Images cannot be edited.** If a figure contains text that contradicts the results (e.g. gamma in the conceptual framework), flag it under USER DECISION for the group to redraw.
6. **The web platform.**
   - The actual app differs from the Chapter 3 description in places (CHAPTER4_NOTES §6): "NN% sure", the sampling, a 3-clip fallback, deletion logging, and possibly the served model.
   - It is the group's choice whether to change the app or the text, so list these under USER DECISION. Do not edit them.
   - Exception: a manuscript statement that is wrong whatever the app does, e.g. gamma in the preprocessing description of the model pipeline.
7. **Facts only.** Every NEW text must be verifiable from the package or the notes; never invent. If you cannot verify a fact (e.g. whether training used cosine or Euclidean FaceNet distance), say so and mark the item VERIFY.

## Split, with overlap allowed

- **Methodologist:**
  - Chapter 1 (141–202): scope, limitations, significance, objectives;
  - Chapter 2 (203–316): claims, duplicates, the hypothesis wording if relevant;
  - the non-statistical parts of Chapter 3: framework, software framework, flowchart description, research design, data, preprocessing, models, controls, ablations, baselines, platform, instruments, data gathering.
- **Statistician:**
  - every quantitative or statistical statement in Chapters 1–3: hypotheses (blocks ~250–252), operational definitions with metrics or calibration, the evaluation protocol (≈495–522), BO (≈504), and Statistical Treatment (612–626);
  - consistency with the amendments paragraph and with Chapter 4's methods description;
  - a check of the RQ5 survey statistics for internal consistency only.

## Output

Write `team/ch123/<role>_r1.md` with these sections:
- A. MUST edits
- B. SHOULD edits
- C. VERIFY items
- D. USER DECISION items
- E. Notes for the other advisors

Keep the final reply under 150 words.
