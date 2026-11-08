# RQ2 expansion: the lead's merged plan (reply AGREE or OBJECT per item, then produce)

## Rules

1. **Complete-source rule (S A1).** When a comparison table is used, every row of it is recorded in J9. A row is left out of the chapter tables only by a category rule stated in J9, never because of its value:
   - (a) not a deepfake-video detector: generic image-forensics detectors (FF++ Table 4 steganalysis, Cozzolino, Bayar & Stamm, Rahmouni) and generated-image detectors (Patch-based, CNN-aug);
   - (b) not peer-reviewed (Comotion, arXiv-only; FaceNetLSTM, a poster);
   - (c) a misquoted value (DeepRhythm in STIL);
   - (d) a duplicate copy of a value already listed under its original source;
   - (e) not a within-dataset result: cross-dataset, cross-manipulation, cross-compression, distorted, or hidden test sets;
   - (f) one variant per model where a paper reports several aggregations. Xception is represented by XN-avg because frame-score averaging matches this study's mean-logit aggregation; XN-max goes to J9.
   - **Consequence:** M's exclusion of DSP-FWA as "near-chance padding" depends on its value, so it is **not allowed**. DSP-FWA enters Table 11 from Masi et al. (2020), Table 2. D-FWA's Celeb-DF-only value goes into Table 10's Celeb-DF column, and Celeb-DF accuracy is still not compared in the text.
2. **Tiers (S A2).**
   - Tier A: the FF++ DeepFakes subset at the same compression, or the DeeperForensics-1.0 standard (undistorted) set; video level; training and testing on the same dataset.
   - Tier B: pooled manipulations, unstated subset or unit, or frame or clip level.
   - Excluded (J9 only): category (e).
3. **DeeperForensics standard → standard values (Jiang et al., Table 5) become Tier A.** This study's construction is the standard set (unperturbed manipulated videos with their FF++ source originals). Our 96/201 validation/test pairs fit the 7:1:2 identity split, although identical lists cannot be verified; the note says so.
   - Consequences: I3D and Xception DFo 100.00 move from B to A, and C3D 98.50, TSN 99.25 and ResNet+LSTM 100.00 are added.
   - The RQ2 sentences "differs from the published benchmark settings" and "on different constructions" are narrowed to the distorted and hidden-set settings and to the SFormer and FTCN splits.
   - Methodologist: AGREE or OBJECT.
4. **Provenance (S A3).**
   - "As evaluated by X" marks a third-party run whose provenance is not stated (e.g. STIL's C3D and TEI). Use "re-implemented by X" when stated.
   - Each copied value is listed once, under its producer.
   - Where two sources disagree on the same model (Face X-ray: LipForensics vs TALL; Two-branch: Masi vs TALL; MesoNet: FF++ frame-level DF vs TALL pooled), each gets its own row and source letter, and they are never merged into a range.
   - Exception: XN-avg keeps its existing two-paper range in Table 10, as already agreed.
5. **No vote counts** ("higher than k of n"). Tier B values appear in the text only as ranges with the protocol named. Accuracy is compared only for Tier A balanced sets: FF++ DF C23/C40 and the DFo standard set. Celeb-DF accuracy is never compared. Both BO and fixed are always named.

## Model set (union of both memos under rule 1)

**Table 10 (Tier A).**
- Columns: FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics-1.0. Cells are "Acc …; AUC …" plus source letters.
- Rows grouped by family, SwinFusion++ BO and fixed first:
  - Xception (XN-avg); I3D; C3D; TEI;
  - CNN–LSTM (S-MIL "LSTM"); S-MIL-T; ADDNet-3D; STIL; SFormer;
  - TSN and ResNet+LSTM (DFo only); D-FWA (Celeb-DF only), if within-dataset and peer-reviewed. Methodologist: check D-FWA, and drop it if it fails rule 1(b) or (e).

**Table 11 (Tier B, new).**
- Columns: FF++ HQ (C23) Acc | AUC | FF++ LQ (C40) Acc | AUC | Setting | Source. DFo Tier-B values (FTCN's own split) go in the Setting column or the note.
- SwinFusion++ BO and fixed are the first rows, marked "DeepFakes subset only; not like-for-like".
- Rows:
  - all 18 rows of TALL Table 2, with Xception and TALL-Swin kept as TALL prints them;
  - the LipForensics Table 4 deepfake-detector rows (LipForensics, Face X-ray, CNN–GRU, plus any other deepfake detector in that table);
  - Masi Table 2 (Two-branch, DSP-FWA, plus any other row);
  - FF++ Table 4 frame-level DF-specific MesoNet and XceptionNet, if listed there;
  - FTCN (supplement).
- A model that appears in two sources gets two rows with its source letter.

**J9:** the master list, with every row from every table used, the reason codes 1(a)–(f), and an "In Table 10/11?" column.

## Chapters 1 and 3 (handled through the edit list; the methodologist drafts the final text)

- **Block 175 (C8):** M's NEW: «…with previously reported results for established frame-level, recurrent, 3D-convolutional, and spatio-temporal detectors, including Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer.»
- **Block 514 (C52):** a grouped list of EVERY model in Tables 10 and 11, plus CAST, TSFF-Net and the CNN–LSTM models (RQ3/RQ4).
- **Block 325 (C31):** append «, and the other previously reported detectors listed in Chapter 4».

## Production

- **Statistician:**
  - `team/rq2x/tables/T10.csv`, `T11.csv`, `J9.csv` (rebuilt master), each with a `_note.txt`;
  - `KEY_NUMBERS_RQ2X.md`, with every number the revised prose may cite: Tier A highest values per set (recomputed), Tier B ranges per column, and DFo standard-set ranges;
  - merge both values CSVs and the existing `team/rq2/tables/J9.csv`;
  - Table 10 note: ≤ 100 words with source letters; Table 11 note: ≤ 110.
- **Methodologist:**
  - `team/rq2x/refs_merged.txt`: every new reference, de-duplicated against the existing References (blocks 627–769) and against each other, in alphabetical order, plain style, each line prefixed by the existing entry it should follow;
  - `team/rq2x/ch13_edits.json`: the final OLD/NEW for C8, C52 and C31, written against the CURRENT accepted text (the C8, C52 and C31 NEW strings in `team/ch123/edits_agreed.json`);
  - verify the D-FWA, DSP-FWA and any added LipForensics/Masi rows from the original PDFs;
  - then check the statistician's T10/T11 against your verified values.
- **Lead:** revises the RQ2 prose (Tier A/B paragraphs, DFo sentences, C40 sentence in range form), then Round 3.
