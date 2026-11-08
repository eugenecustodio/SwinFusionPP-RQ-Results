# Statistician, Round 1: expanding the RQ2 comparison set

**Sources read in full, from the original PDFs** (downloaded to `rq2x/work/`, text extracted with pdftotext):
- Xu et al. (2023, TALL): CVF ICCV 2023 version and arXiv 2307.07494v3;
- Jiang et al. (2020, DeeperForensics-1.0): CVF CVPR 2020 version and arXiv 2001.03024v2.

In both papers, the two versions print identical values for every row I use. All 14 new references were matched on Crossref (`statistician_refs.txt`).

## A. Criteria

**AGREE with criteria 1–5, with three amendments that keep the expansion statistically honest.**

- **A1. Complete-source rule (against cherry-picking).** When a comparison table is used, **every row of it** goes into J9, and either all its rows enter the chapter table or a subset chosen by a rule stated in the text (e.g. "video-based models only"). The rule must not depend on whether a value favors SwinFusion++.
- **A2. Tier definitions for the expanded set.**

  | Tier | Definition |
  |---|---|
  | **A** | Same dataset; FF++ DeepFakes subset at the same compression, or the DeeperForensics-1.0 *standard (undistorted)* set; video-level unit; same dataset for training and testing; clean test set |
  | **B** | Same dataset, but the FF++ manipulations are pooled (all four), the subset or unit is unstated, or the unit is frame/clip |
  | **Excluded from chapter tables (J9 only)** | Cross-dataset, cross-manipulation, cross-compression, distorted test sets, and hidden test sets |

- **A3. Provenance labels.**
  - "As reported by …" marks values a paper cites from earlier work. TALL states: "results are directly cited from published papers if we follow the same setting."
  - "Reimplemented by …" marks values from the reporting paper's own run (TALL's ViViT*).
  - Identical copies are listed once. Differing values for the same model are shown as a range with both sources.

## B. Models proposed (from my two sources)

**B1. TALL, Table 2: "Intra-dataset evaluations… video-level Acc. (%) and AUC (%) on the FF++ dataset".**
- **The setting:** FF++ HQ (C23) and LQ (C40), **all four manipulations pooled**. §4.1 describes it as "1,000 real videos and 4,000 fake videos in four different manipulations". So every row is **Tier B**.
- **There is no within-dataset Celeb-DF table.** TALL's Table 3 is cross-dataset (trained on FF++) and belongs to RQ6.
- **The 18 rows** (C23 Acc / C23 AUC / C40 Acc / C40 AUC, as printed; AUC in percent; "–" = not reported):

| Model | C23 Acc | C23 AUC | C40 Acc | C40 AUC | Note |
|---|---|---|---|---|---|
| MesoNet | 83.10 | – | 70.47 | – | |
| Xception | 95.73 | 96.30 | 86.86 | 89.30 | Already in J9 |
| Face X-ray | – | 87.35 | – | 61.60 | |
| Two-branch | 96.43 | 98.70 | 86.34 | 86.59 | |
| Add-Net | 96.78 | 97.74 | 87.50 | 91.01 | |
| F3-Net | 97.52 | 98.10 | 90.43 | 90.43 | |
| FDFL | 96.69 | 99.30 | 89.00 | 92.40 | |
| Multi-Att | 97.60 | 99.29 | 88.69 | 90.40 | |
| RECCE | 97.06 | 99.32 | 91.03 | 95.02 | |
| LipForensics | 98.80 | 99.70 | 94.20 | 98.10 | |
| DFDT | 98.18 | 99.26 | 92.67 | 94.48 | |
| ADT | 92.05 | 96.30 | 81.48 | 82.52 | |
| ST-M2TR | – | 99.42 | – | 95.31 | |
| VTN | 98.47 | – | 94.02 | – | |
| VidTr | 97.42 | – | 92.12 | – | |
| ViViT* | 92.60 | – | 88.02 | – | Reimplemented by TALL |
| ISTVT | 99.00 | – | 96.15 | – | |
| TALL-Swin | 98.65 | 99.87 | 92.82 | 94.57 | Already in J9 |

**B2. Jiang et al. (2020), Table 5, column 2 (train std → test std), video-level binary accuracy.**

| Model | Accuracy | Status |
|---|---|---|
| C3D | 98.50 | New |
| TSN | 99.25 | New |
| I3D | 100.00 | Already in Table 10 |
| ResNet+LSTM | 100.00 | New; a baseline Jiang et al. built from ResNet and LSTM |
| XceptionNet | 100.00 | Already in Table 10 |

The std/sing, std/rand and swapped columns (distorted test sets) and Tables 4 and 6 (hidden test set) are excluded.

**B3. Proposed additions: 19 models.**
- 16 come from TALL Table 2 (all rows except Xception and TALL-Swin, which are already present) and 3 from DeeperForensics (C3D, TSN, ResNet+LSTM).
- That is above the brief's 8–15 target. I still recommend the **complete TALL table** under A1, because it is one coherent protocol for many models.
- If the lead wants fewer, the stated rule could be "video-based (temporal) models only": Two-branch, LipForensics, VTN, VidTr, ViViT, ISTVT and ST-M2TR, plus C3D, TSN and ResNet+LSTM, for 10 additions. The rest stay in J9.
- **Not proposed:** DeepfakeBench (Yan et al., 2023; already in References). Its within-FF++ results are frame-level (Tier B, unit differs), so they would add only J9 rows.

## C. Verification notes (exact locations)

- **TALL Table 2:** CVF ICCV 2023, printed page 22662. arXiv v3 Table 2 is identical; all 18 rows were compared programmatically.
- **TALL's dataset text:** §4.1, "consisting of 1,000 real videos and 4,000 fake videos in four different manipulations". The unit appears in the Table 2 caption: "video-level Acc. (%) and AUC (%)".
- **DeeperForensics Table 5:** CVF CVPR 2020, the page after printed page 2895 (2896). arXiv v2 is identical.
- **The DeeperForensics standard set (§4, "Dataset split"):** "1,000 raw manipulated videos … and 1,000 YouTube videos from FaceForensics++ as our standard set … split … 7:1:2 … 70, 10, and 20 identities".
- **Tier consequence: the DFo standard set should be Tier A.** It is the same construction as this study's (unperturbed manipulated videos with their FF++ source originals as the real class). Our validation and test sizes (96 and 201 pairs, i.e. 192 and 402 videos) fit the 7:1:2 identity split, although identical lists cannot be verified. I therefore propose that **I3D and Xception 100.00 on DFo change from (B) to (A)** in Table 10. The current RQ2 phrases "differs from the published benchmark settings" and "on different constructions of the dataset" should be narrowed to the distorted and hidden-set settings and to SFormer/FTCN's own splits. **Needs the methodologist's agreement.**
- **Per-row details:** `statistician_values.csv` has 63 rows, each with its source, provenance, tier, and verification string.

## D. Table layout

- **Table 10 (Tier A only).**
  - Models × {FF++ C23, FF++ C40, Celeb-DF v2, DeeperForensics-1.0}, with cells "Acc …; AUC …".
  - It contains the current Tier A values, the methodologist's new STIL/S-MIL Tier A rows, and the DeeperForensics standard-set rows (C3D, TSN, ResNet+LSTM, plus I3D and Xception moved to A).
  - SwinFusion++ BO and fixed are the reference rows.
- **Table 11 (Tier B), new.**
  - **Columns:** FF++ C23 Acc | C23 AUC | C40 Acc | C40 AUC | Source.
  - **Rows:** the TALL Table 2 rows (A1), FTCN (supplement) and any other Tier-B FF++ values.
  - **SwinFusion++ appears as a reference row** with the note "SwinFusion++: DeepFakes subset only; Tier B values pool all four manipulations, so no row is comparable like for like."
- **J9** stays the master list, with an "in Table 10/11?" column.
- **Comparison rules for the text.**
  1. Accuracy is compared only for Tier A on balanced test sets: FF++ DF C23/C40, and now the DFo standard set (both balanced).
  2. No Celeb-DF accuracy comparison.
  3. ROC-AUC statements stay per metric, per test set and per tier.
  4. **No vote counts** ("higher than 12 of 15 models"). Across non-matched protocols a count is a ranking in disguise.
  5. Tier B values appear only as ranges with the protocol named. For example: "on all four FF++ manipulations, the reported C40 ROC-AUC values ranged from 0.616 (Face X-ray) to 0.983 (FTCN); SwinFusion++ reached 0.9941 (fixed recipe 0.9878) on the DeepFakes subset only, so these are not like-for-like".
  6. The existing C40 sentence ("higher than FTCN, STIL, TALL-Swin") must be re-checked against the larger set. It still holds for both configurations: the highest Tier-B C40 AUC in TALL Table 2 is LipForensics 98.10 and FTCN's is 0.983. It should become the range form above.
  7. BO and fixed are both named (A7), and nothing is tested.
- **DeeperForensics-1.0 standard set, Tier A, balanced.**
  - Published accuracies: 98.50–100.00 (C3D, TSN, I3D, ResNet+LSTM, XceptionNet).
  - SwinFusion++: BO 98.51 and fixed 98.76. Both lie within that range.
  - Allowed: "within the reported range, near the ceiling". No ranking within it.

## E. Chapter 1 and 3 sentences that must change (final lists depend on the merged set)

- **Block 175 (C8 now):**
  - **OLD:** "…with previously reported results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer."
  - **NEW, option 1 (exact list):** "…with previously reported results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, SFormer, and the other detectors and video models evaluated in the same published comparison tables."
  - **NEW, option 2:** list every added model by name.
  - I prefer option 1 plus a full list in Chapter 3 block 514.
- **Block 514 (C52 now):**
  - **OLD:** "…Previously reported results will be given for the subset with values on the datasets of this study: Xception, I3D, STIL, FTCN, ISTVT, TALL-Swin, SFormer, CAST, TSFF-Net, and CNN–LSTM models."
  - **NEW:** the same sentence with the merged list. My additions: MesoNet, Face X-ray, F3-Net, FDFL, the multi-attentional detector, RECCE, LipForensics, M2TR, DFDT, ADT, Add-Net, VTN, VidTr, ViViT, two-branch recurrent network, C3D, TSN, and a ResNet+LSTM baseline (or the subset per B3).
  - Many of these names already appear in the block's comparator inventory (e.g. VTN, ViViT, VidTr, DFDT, F3-Net, Multi-attention, Two-Stream).
- **Block 616:** unchanged. It already says literature values keep their protocol and enter no paired test.

## Questions for the team

1. **Methodologist:** do you agree to move the DeeperForensics standard-set values to Tier A (C)? That also changes two current Table 10 cells and two RQ2 sentences.
2. **Lead:** the complete TALL table (19 additions) or the "temporal models only" rule (10 additions)? Either is defensible if the rule is stated. A hand-picked subset is not.
3. **Both:** do you agree to the new Table 11 (Tier B) with SwinFusion++ as a non-comparable reference row, and the "no vote counts" rule?
