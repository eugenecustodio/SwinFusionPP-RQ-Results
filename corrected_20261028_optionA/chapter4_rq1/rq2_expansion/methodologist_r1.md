# Methodologist R1: expanding the RQ2 comparison set

**Sources.** I read each value from the original arXiv PDF with pdftotext:
- STIL (2109.01860), S-MIL (2008.04585), LipForensics (2012.07657), Two-branch (2008.03412) and FaceForensics++ (1901.08971);
- DeepRhythm (2006.07634), as a check of STIL's copied values.

**Checking.** Each value in `methodologist_values.csv` was checked by script against the source text with an anchor string (`team/scripts/m_rq2x_values.py`). References were checked on Crossref, or on the CVF page for Sabir et al.

## A. Criteria

**Agree with criteria 1–5, with three amendments:**
1. **One evaluation protocol per Tier-A source.** S-MIL's and STIL's DeepFakes-column values come from one shared protocol (20 frames per video at test, dlib/MTCNN crops, video-level accuracy). Say so in the note: these values are mutually comparable, but not comparable with ours.
2. **List each copied value once, under the paper that produced it.** STIL repeats S-MIL's LSTM and S-MIL-T values verbatim. A "directly from original papers" claim in a comparison table is not proof (see the DeepRhythm finding in C).
3. **Exclude non-peer-reviewed sources and posters**, even when a comparison table quotes them.

## B. Models proposed (my sources), with evidence

| # | Model (original paper) | Values | Tier | Evaluated by |
|---|---|---|---|---|
| 1 | **C3D** (Tran et al., 2015) | DF accuracy: C23 0.9286, C40 0.8929 | A | Gu et al. (2021) |
| 2 | **TEI / TEINet** (Liu et al., 2020) | C23 0.9786, C40 0.9500; Celeb-DF 0.9912 | A | Gu et al. (2021); the Celeb-DF value is re-implemented |
| 3 | **CNN–LSTM ("LSTM")** (Hochreiter & Schmidhuber, 1997, as the recurrent unit) | C23 0.9964, C40 0.9643; Celeb-DF 0.9573 | A | X. Li et al. (2020) |
| 4 | **S-MIL-T** (X. Li et al., 2020; S-MIL k = 1 in a note) | C23 0.9964, C40 0.9714; Celeb-DF 0.9884 | A | original |
| 5 | **ADDNet-3D** (Zi et al., 2020) | C23 0.9214, C40 0.9036; Celeb-DF 0.9516 | A | Gu et al. (2021), re-implemented |
| 6 | **LipForensics** (Haliassos et al., 2021) | HQ accuracy 98.8 / AUC 99.7; LQ 94.2 / 98.1 | B (all four manipulations) | original |
| 7 | **Face X-ray** (L. Li et al., 2020) | HQ 78.4 / 97.8; LQ 34.2 / 77.3 | B | Haliassos et al. (2021) |
| 8 | **CNN–GRU** (Sabir et al., 2019) | HQ 97.0 / 99.3; LQ 90.1 / 92.2 | B | Haliassos et al. (2021) |
| 9 | **Two-branch** (Masi et al., 2020) | AUC: HQ 99.12, LQ 91.10 (700 test videos) | B | original |
| 10 | **MesoNet** (Afchar et al., 2018) | DF-specific accuracy: C23 95.26, C40 89.52 | B (frame-level, 100 images per video) | Rössler et al. (2019) |

**ISTVT is not verifiable.** The paper is IEEE TIFS, behind a paywall, and not on arXiv. The statistician's source (Xu et al., 2023, Table 2) prints ISTVT HQ 99.00 and LQ 96.15 (all four manipulations). I propose including it, marked "as reported by Xu et al. (2023); original not re-verified", the same treatment as SFormer.

**Excluded from my sources (list them in J9 with the reason):**
- **DeepRhythm** (Qi et al., 2020): see C-1.
- **Comotion-35/70:** arXiv-only (CoRR 2008.04848).
- **FaceNetLSTM:** a CCS 2019 poster.
- **XN-max:** a variant of Xception.
- **D-FWA:** only a Celeb-DF value, and Celeb-DF accuracies are not compared.
- **DSP-FWA:** FF++ AUC 57.5 / 62.3 (Masi Table 2). It is a near-chance baseline, so including it would only pad the table.
- **Steganalysis, Cozzolino, Bayar & Stamm, Rahmouni** (FF++ Table 4): generic image-forensics detectors evaluated at frame level.
- **Patch-based and CNN-aug** (LipForensics Table 4): detectors of generated images, not deepfake-video detectors.

## C. Verification notes

**Locations:**
- STIL: Table 1 (PDF p.5; the DF column for c23/c40) and Table 2 (p.5; Celeb-DF has 5,639 fakes, so it is v2).
- S-MIL: Table 2 (p.7; the video-level accuracy block for c23/c40) and Table 1 (p.7; Celeb).
- LipForensics: Table 4 (p.7; separate models per quality; FF++ all four manipulations; video level).
- Two-branch: Table 2 (p.11; video level, 700 samples, four manipulations).
- FaceForensics++: Table 4 (p.13; manipulation-specific detectors). Accuracies are computed on 100 images per video (Appendix D), so they are frame-level.

**Findings:**
- **C-1. STIL misquotes DeepRhythm.**
  - STIL prints DeepRhythm C23 DF 0.9870. DeepRhythm's own Table 2 gives DF 1.0 (trained on DF) or 0.997 (trained on all), and 0.987 is its DFD value.
  - DeepRhythm also uses its own 8:1:1 split, with the real videos augmented by flipping and the compression level unstated.
  - Exclude it. This also shows why STIL's "results of other methods are directly from their original papers" needs checking.
- **C-2. Unclear provenance of STIL's FF++ values.** STIL's C3D and TEI FF++ values have no re-implementation mark, but neither original paper evaluates deepfakes. Label them "as evaluated by Gu et al. (2021); provenance not stated".
- **C-3. S-MIL's accuracy definition.** S-MIL §4.3 defines accuracy as the mean of the fake and real accuracies for its partial-attack experiments, and its Celeb column sits in that table. This is one more reason not to compare Celeb-DF accuracies.
- **C-4. Face X-ray values disagree between sources.**
  - LipForensics evaluates Face X-ray at LQ accuracy 34.2% (AUC 77.3); TALL prints 61.60 AUC.
  - The two sources disagree, and both are third-party runs.
  - Show the source letter on every Face X-ray cell, and never merge values from both sources into one range.
- **C-5. Two-branch quotes agree.** Two-branch's AUCs (99.12/91.10) match the quotes in LipForensics and the FTCN supplement (99.1/91.1).

## D. Table layout

**Split Table 10 into two tables**, each led by the SwinFusion++ BO and fixed-recipe rows. Rows are grouped by family: frame-level CNN; recurrent; 3D/video CNN; spatio-temporal detector; transformer.
- **Table 10. Tier A: DeepFakes subset, video level.**
  - Columns: FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics-1.0.
  - Accuracy only, plus STIL's C40 AUC.
  - **Rows:** Xception, I3D, C3D, TEI, CNN–LSTM, S-MIL-T, ADDNet-3D and STIL, plus SFormer and the statistician's Tier-A rows, if any.
  - **Note:** "values from X. Li et al. (2020) and Gu et al. (2021) share one evaluation protocol".
- **Table 11. Tier B: pooled manipulations, frame level, or other constructions.**
  - Columns: FF++ HQ | FF++ LQ | DeeperForensics-1.0, with cells "Acc …; AUC …".
  - **Rows:** MesoNet, Face X-ray, CNN–GRU, Two-branch, LipForensics, FTCN, TALL-Swin and ISTVT, plus the statistician's TALL Table 2 rows and the DeeperForensics Table 5 rows.
- **Appendix J9:** extended with every added and excluded value.
- **Prose rules stay as they are:**
  - accuracy is compared on Tier A FF++ only;
  - the "highest Tier A" statement must be recomputed. C23 Tier A now includes CNN–LSTM 99.64 and S-MIL-T 99.64, both below XN-avg 100.00; C40 Tier A includes S-MIL-T 97.14, below STIL 98.21. The stated highest values therefore do not change;
  - no ranking.

## E. Chapter 1 and 3 sentences that must change

These are drafts; the final model list follows the agreed set.
- **Block 175 (C8).**
  - OLD: «with previously reported results for Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer.»
  - NEW: «with previously reported results for established frame-level, recurrent, 3D-convolutional, and spatio-temporal detectors, including Xception, I3D, STIL, FTCN with its Temporal Transformer component, TALL-Swin, and SFormer.»
- **Block 514 (C52), the list after "for the subset with values on the datasets of this study:".** Replace it with the agreed list, grouped. Draft: «frame-level detectors (Xception, MesoNet, Face X-ray), recurrent and 3D-convolutional video models (CNN–LSTM and CNN–GRU models, C3D, I3D, TEI), and spatio-temporal detectors (S-MIL, ADDNet-3D, STIL, FTCN, LipForensics, Two-branch, ISTVT, TALL-Swin, SFormer, CAST, and TSFF-Net).»
- **Block 325 (C31).** Append "and the other previously reported detectors listed in Chapter 4" after "TSFF-Net". This keeps the "will not be retrained" sentence complete.
- **RQ3 note.** The CNN–LSTM (S-MIL) and CNN–GRU (Sabir via LipForensics) rows are recurrent models, so they are relevant to RQ3, which uses CNN–LSTM comparators. The lead decides whether RQ3 refers back to them; Sabir et al. (2019) is needed in References either way.

**References:** `methodologist_refs.txt` has 7 new entries, all verified (Afchar, Hochreiter, L. Li, Liu, Sabir, Tran, Zi). The following are already in References: Gu, X. Li (added for RQ2), Haliassos, Masi, Rössler, Carreira, Chollet, Zhao (ISTVT) and Xu.

**In-text forms:** "L. Li et al., 2020" (Face X-ray), alongside "X. Li et al., 2020" (S-MIL) and "Y. Li et al., 2020" (Celeb-DF).
