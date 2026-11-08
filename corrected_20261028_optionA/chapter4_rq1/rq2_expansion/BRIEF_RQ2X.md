# Brief: expanding the RQ2 comparison models (lead). Same team, same rule: all three advisors must agree.

**What the user asked:** "If it possible to further expand No. 2 Models, like you can add other models to compare to SwinFusion++."

**Hard limit:** nothing can be retrained. There is no GPU, the datasets are not here, and the backup access was revoked. So the expansion uses **previously reported results only**, verified against the original papers, with tiers, exactly as in the current RQ2.

## Current RQ2 (in the docx)

- **Table 9:** SwinFusion++ vs the preliminary-study Xception.
- **Table 10:** a matrix of 6 models (Xception, I3D, STIL, FTCN+TT, TALL-Swin, SFormer) × 4 benchmarks.
- **Table J9:** every value considered.
- **Files:** `team/rq2/` (RQ2_AGREED_PLAN.md, the tables, KEY_NUMBERS_RQ2.md and RQ2_FINAL_PROSE.md).
- **Rules in force:** the tiers; ROC-AUC first; accuracy compared on balanced FF++ only; no Celeb-DF accuracy comparison; no tests; no ranking; and the BO and fixed configurations both named.

## Selection criteria for added models (the lead proposes; agree or amend)

1. Peer-reviewed, and open access, so the values can be checked on arXiv, CVF or the publisher.
2. Reports **within-dataset** results on at least one of FF++ DeepFakes C23 or C40, Celeb-DF v2, or DeeperForensics-1.0.
   - Video-level results are Tier A when the subset and compression match.
   - FF++ all-manipulation or frame-level results are Tier B.
   - Cross-dataset or cross-manipulation results are excluded here; they belong to RQ6.
3. Third-party evaluations are allowed, reported as "as evaluated by …", for example the video models in the STIL and S-MIL tables. Cite both the model's original paper and the evaluating paper.
4. Relevance: established CNN, recurrent, video or transformer detectors and video backbones. No padding. The target is the models with verified values, roughly 8–15 additions.
5. Each added model needs an APA reference verified on Crossref (or the publisher), unless the manuscript already has it. Check blocks 627–769 of `.../ch4/manuscript_text.txt`.

## Source split (each advisor extracts AND verifies from the original PDF/HTML)

- **Methodologist:**
  - Gu et al. (2021, STIL), Tables 1–2: every model row on FF++ DF C23/C40 and Celeb-DF v2, e.g. TSN, TSM, TEI, V4D, S-MIL, S-MIL-T and others.
  - X. Li et al. (2020, S-MIL), Tables 1–2.
  - Zhao et al. (2023, ISTVT; already in References).
  - Rössler et al. (2019, FaceForensics++) per-manipulation results. These are likely frame-level (Tier B); confirm.
  - Haliassos et al. (2021, LipForensics), if it reports within-dataset FF++ results.
- **Statistician:**
  - Xu et al. (2023, TALL), Table 2 and any Celeb-DF within table: every model row, e.g. MesoNet, Face X-ray, F3-Net, M2TR, LipForensics and others, with unit and subset.
  - Jiang et al. (2020, DeeperForensics), Table 5 (standard→standard): C3D, TSN, ResNet+LSTM and others.
  - The comparability rules for the expanded set.
- **Both:** list any other open-access comparison table you know that fits criterion 2, but verify it before proposing it.

## Output (per advisor)

1. `team/rq2x/<role>_r1.md`:
   - A. criteria (agree or amend);
   - B. the models proposed, with the evidence;
   - C. verification notes (the PDF location of each value);
   - D. table layout proposal, e.g. Table 10 split into Tier A and Tier B tables, or one long matrix;
   - E. the Chapter 1 and 3 sentences that must change. Block 175 C8 lists the RQ2 baselines, and block 514 (C52) lists the reported subset.
2. `team/rq2x/<role>_values.csv`, with columns: Test set, Model, Metric, Value (as printed), Unit, Subset, Source (paper, table), Evaluated by, Tier, Verified (yes/no + how), Notes.
3. `team/rq2x/<role>_refs.txt`: APA entries for every model or paper not yet in References, each verified, in the plain style of the existing reference list.

Final reply: under 150 words.
