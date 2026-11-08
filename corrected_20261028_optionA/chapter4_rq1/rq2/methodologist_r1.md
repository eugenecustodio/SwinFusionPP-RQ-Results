# Methodologist R1: Chapter 4, RQ2

**Verification method.** I checked the published values against the original papers:
- arXiv/ar5iv for STIL, S-MIL and FTCN;
- the arXiv PDF for TALL (2307.07494);
- the CVF supplementary ZIP for FTCN;
- the preliminary-study PDF with pdftotext.

References were checked through the Crossref API. SFormer (Elsevier) could not be accessed.

## A. Positions

**M-A1. RQ2 has three separate kinds of evidence, and they are never mixed in one ranking.**
1. **SwinFusion++'s own held-out results.** The BO-selected configuration is shown with the fixed recipe alongside (Option A).
2. **The Xception baseline from the preliminary study** (Custodio et al., 2026). It uses an earlier pipeline and a single seed (1701). Its test populations are:
   - FF++: 280 + 280 test videos, the same size as ours (A-17);
   - Celeb-DF v2: 859 videos (723 fake), against our 978;
   - DeeperForensics-1.0: 2,385 analyzed of 2,412 (2,185 fake), against our 402 (201 fake).

   Only the FF++ cells are even close to like-for-like, and those differ too in pipeline, model and training.
3. **Previously reported results**, each with a comparability tier, its unit and its source.

There are no tests, intervals or p-values against (2) or (3).

**M-A2. Structure** (Philippine format: introduce, describe, interpret). The Heading2 is "Research Question 2: SwinFusion++ Compared With Established Baselines". Use the "With/From" Title Case adopted in RQ1.
1. **Opening paragraph.** Restate RQ2 and name the three kinds of evidence. Disclose:
   - that only Xception was run locally, in the earlier pipeline;
   - our Celeb-DF v2 test set (978 videos, identity-grouped) against the official 518-video list;
   - that our DeeperForensics-1.0 binary construction is not the official benchmark protocol.
2. **"SwinFusion++ and the Preliminary-Study Xception Baseline."** Table 9, then interpretation.
3. **"Comparison With Previously Reported Results."** Table 10 and Figure 14, then interpretation.
4. **"Answer to Research Question 2."** One paragraph.

**M-A3. ROC-AUC is the primary comparison metric; accuracy is secondary.**
- Published accuracies come from each paper's own operating point, usually not frozen on validation data, while ours are frozen on source validation.
- Precision, recall and F1 are not compared with published values; only SFormer reports them.
- In Table 9, F1 is shown only for the preliminary Xception, and its degenerate operating points are flagged.

**M-A4. Two package errors must not reach Chapter 4.** I flag them to the user; the package itself is not edited.
- **(a) FTCN cross-manipulation results tagged as within-dataset.** `RQ2/results/table2_published_AB.csv` rows 27, 28 and 45 tag these as Tier A within-dataset FF++ C23 results, but they are cross-manipulation:
  - FTCN 0.999 (FTCN Table 2) is leave-one-out: trained on F2F+FS+NT, tested on DF;
  - FTCN 0.981 (Table 8) is trained on F2F only;
  - Xception 0.939 (Table 2) uses the same leave-one-out protocol.

  The package's own `official_paper_results_v020.md` records them correctly as "unseen manipulation". The RQ2 write-up's "FTCN AUC 0.981–0.999" and the existing figure both repeat the error.
- **(b) DeeperForensics "Xception 77–100%, I3D 79–100%".** The 77.00 and 79.25 values are on the DeeperForensics hidden test set (Jiang et al., Table 4). The standard-to-standard values are 100.00 for both (Table 5).

## B. Tables and figures

**Table 9. SwinFusion++ and the Preliminary-Study Xception Baseline**
- **Layout:** one span row per test set, then 3 model rows.
- **Columns:** Model | Pipeline | Test videos (fake) | ROC-AUC | Acc (%) | F1.
- **Rows** (all numbers checked):

| Test set | Model | Test videos (fake) | ROC-AUC | Acc | F1 |
|---|---|---|---|---|---|
| FF++ C23 | SwinFusion++ (BO-selected) / (fixed recipe) | 280 (140) | 0.9964 / 0.9942 | 98.21 / 97.86 | 0.9822 / 0.9784 |
|  | Xception (preliminary study) | 280 (140) | 0.7725 | 69.64 | 0.6886 |
| FF++ C40 | SwinFusion++ BO / fixed | 280 (140) | 0.9941 / 0.9878 | 96.07 / 94.64 | 0.9617 / 0.9470 |
|  | Xception (prelim.) | 280 (140) | 0.8109 | 74.29 | 0.7429 |
| Celeb-DF v2 | SwinFusion++ BO / fixed | 978 (843) | 0.9983 / 0.9951 | 98.36 / 97.75 | 0.9904 / 0.9869 |
|  | Xception (prelim.) | 859 (723) | 0.6480 | 84.17* | 0.9140* |
| DeeperForensics-1.0 | SwinFusion++ BO / fixed | 402 (201) | 0.9954 / 0.9974 | 98.51 / 98.76 | 0.9848 / 0.9874 |
|  | Xception (prelim.) | 2,385 (2,185 approx.) | 0.9978 | 46.00† | 0.5821† |

- **Formatting:** one model per row in the final table; BO and fixed are combined above only to keep this memo short.
- **Note:**
  - *Xception called every Celeb-DF video fake, so its accuracy equals the fake share.
  - †At its threshold Xception missed 1,288 fake videos.
  - The preliminary study used an earlier pipeline (MTCNN cache, 3 anchors, fixed recipe, seed 1701).
  - Its Celeb-DF v2 and DeeperForensics-1.0 test populations differ from those of this study.
  - The SwinFusion++ values are three-seed ensembles.
- **Source:** the preliminary-study PDF, Table 7; `three_seed_mean_logit_ensemble.csv`.
- **The statistician should confirm** the analyzed-fake count for DeeperForensics-1.0.

**Table 10. Previously Reported Within-Dataset Results on the Benchmarks of This Study**
- **Layout:** rows = models; columns = FF++ C23 | FF++ C40 | Celeb-DF v2 | DeeperForensics-1.0.
- **Cells:** "Acc %; AUC", then the tier, then a superscript letter for the source. Use one value or a range, and only values verified in D.
- **Top rows:** SwinFusion++ (BO-selected) and SwinFusion++ (fixed recipe).

| Model | C23 | C40 | Celeb-DF v2 | DFo |
|---|---|---|---|---|
| Xception (XN-avg) | Acc 98.93–100.00 (A)ᵃᵇ | Acc 96.78–97.14 (A)ᵃᵇ | Acc 99.44 (A)ᵃᵇ | Acc 100.00, official std/std (B)ᶜ |
| Xception | Acc 95.73; AUC 0.963 (B, all four manipulations)ᵈ | Acc 86.86; AUC 0.893 (B)ᵈ | — | — |
| I3D | Acc 92.86 (A)ᵃᵇ | Acc 91.07 (A)ᵃᵇ | Acc 99.23 (A)ᵃᵇ | Acc 100.00, official std/std (B)ᶜ |
| STIL | Acc 99.64 (A)ᵃ | Acc 98.21; AUC 0.971 (A)ᵃ | Acc 99.78 (A)ᵃ | — |
| FTCN + TT | Acc 99.1; AUC 0.998 (B, subset unstated)ᵉ | AUC 0.983 (B)ᵉ | — | AUC 1.000 (B)ᵉ |
| TALL-Swin | Acc 98.65; AUC 0.999 (B, all four)ᵈ | Acc 92.82; AUC 0.946 (B)ᵈ | — | — |
| SFormer | Acc 98.5–99.9 (A)ᶠ | Acc 94.8–98.2 (A)ᶠ | Acc 95.0–99.1 (A)ᶠ | Acc 99.7–100 (A)ᶠ |

**Table 10 note.**
- **Tiers:**
  - A = same dataset, compression and DeepFakes subset, video-level;
  - B = same dataset, but the subset, unit or protocol differs or is not stated.
- **Every published value** comes from its paper's own split, frame sampling and operating point, so none was tested.
- **Celeb-DF v2:** the published results use their own splits; this study's 978-video identity-grouped test set is not the official 518-video list.
- **DeeperForensics-1.0:** the official protocol differs from this study's 402-video binary construction.
- **Sources:**
  - ᵃ Gu et al. (2021), Tables 1–3;
  - ᵇ Li, X. et al. (2020), Tables 1–2;
  - ᶜ Jiang et al. (2020), Table 5;
  - ᵈ Xu et al. (2023), Table 2;
  - ᵉ Zheng et al. (2021), supplementary Tables 1–2;
  - ᶠ Kingra et al. (2024), Tables 2–3.
- **The statistician decides** whether Celeb-DF A becomes "A (dataset only)".

**Figure 14 (remade, recommended).**
- **Layout:** ROC-AUC (top row) and accuracy (bottom row) × 4 datasets.
- **SwinFusion++ markers:** BO (filled circle) and fixed recipe (open circle), in SwinFusion++ blue.
- **Preliminary Xception:** purple diamond, with values below the axis range printed beside it.
- **Published values:** filled marker = Tier A, open = Tier B. Plot only the Table 10 values.
- **Style:** no embedded title or footer.
- **Why remake it:** the existing `figures/RQ2/fig1_vs_published.png` must not be used. It plots the cross-manipulation FTCN and Xception points as Tier A, the DeeperForensics hidden-set and distortion accuracies, and frame-level Xception points. It also has an embedded title and footer and omits the fixed recipe.
- **Timing:** I will draft it once Table 10 is agreed.

**Appendix J.**
- **New title:** "Supplementary Results for Research Questions 1 and 2".
- **J9:** the full list of Tier A/B published values considered, with paper, table, page, unit and subset. Include the excluded cross-manipulation and hidden-set values, each marked "not a within-dataset result", so nothing looks dropped.

## C. Claims allowed and forbidden

**Allowed** (descriptive, with the protocol caveat):
- **C-1.** "SwinFusion++ ranked videos much better than the preliminary-study Xception on FF++ C23 (ROC-AUC 0.996 BO-selected / 0.994 fixed recipe vs 0.773), C40 (0.994 / 0.988 vs 0.811), and Celeb-DF v2 (0.998 / 0.995 vs 0.648). On DeeperForensics-1.0 the values were similar (0.995 / 0.997 vs 0.998)."
  - Always attach: earlier pipeline, single seed, a different model and pretraining; the Celeb-DF v2 and DeeperForensics-1.0 test populations differ.
- **C-2.** "Xception's accuracy and F1 at its frozen threshold are not informative on Celeb-DF v2, where it labeled every video fake, or on DeeperForensics-1.0, where it missed 1,288 fake videos."
- **C-3.** "The highest previously reported within-dataset accuracies are 1.4–2.1 points above SwinFusion++'s at its frozen thresholds." Specifically:
  - C23: 100.0 vs 98.2;
  - C40: 98.2 vs 96.1;
  - Celeb-DF v2: 99.8 vs 98.4.

  Also say that several reported values are lower: I3D 92.9 and 91.1, TALL-Swin 92.8 on C40.
- **C-4.** "On C23, its ROC-AUC (0.996) is close to the values reported for FTCN (0.998) and TALL-Swin (0.999). On C40, its 0.994 is higher than the reported values for FTCN (0.983), STIL (0.971) and TALL-Swin (0.946)."
  - Always add: "these use pooled manipulations or unstated subsets, so the comparison is not like-for-like".
- **C-5.** "On DeeperForensics-1.0 every method is near the ceiling (reported 99.7–100% accuracy and AUC 1.000; SwinFusion++ 98.5% and 0.995), on different constructions."

**Answer to RQ2 (draft).**
> On the four benchmarks, BO-selected SwinFusion++ reached ROC-AUC 0.994–0.998 and accuracy 96.1–98.5% (fixed recipe: 0.988–0.997 and 94.6–98.8%). It ranked videos far better than the Xception baseline of the preliminary study on FF++ and Celeb-DF v2, and was similar to it on DeeperForensics-1.0. Its accuracy was within about two percentage points of the highest previously reported values. Those values come from different splits and protocols, so no ranking against them can be established.

**Forbidden:**
- "outperforms" or "beats" established baselines; "state-of-the-art"; "better than STIL/FTCN/TALL-Swin/SFormer";
- "the highest C40 ROC-AUC in the record". This is also false if Sabir et al. (RQ3 record, 0.996) is counted;
- "comparable" and "on par" (the RQ1 rule); use "close to" or "within about two points";
- "pre-registered" (the write-up's "pre-registered-style protocol"); use "thresholds frozen on source validation";
- "the clearest advantage over established CNN baselines appears on C40 and Celeb-DF". This generalizes from a single earlier-pipeline Xception;
- any p-value or interval against published values;
- calling Xception "reproduced" without "in the preliminary study (earlier pipeline)";
- using the FTCN Table 2/8 values, the DeeperForensics hidden-set values or frame-level values as within-dataset video-level results.

## D. Verification results

| Value(s) quoted | Source checked | Result |
|---|---|---|
| XN-avg DF: C23 0.9893, C40 0.9678; Celeb-DF 0.9944 | Gu et al. 2021 (STIL), Tables 1–2 (ar5iv) | ✓ (video-level; Celeb-DF has 5,639 fakes, so it is v2) |
| XN-avg DF: C23 1.0000, C40 0.9714; Celeb 0.9944 | Li, X. et al. 2020 (S-MIL), Tables 2 and 1 | ✓. STIL says it copies "from original papers" but prints 0.9893/0.9678, so the range form 98.93–100.00 / 96.78–97.14 is correct |
| I3D DF: 0.9286 / 0.9107; Celeb-DF 0.9923 | STIL Tables 1–2; S-MIL Tables 2/1 | ✓ (both papers agree) |
| STIL: 0.9964 / 0.9821; Celeb-DF 0.9978; FF++ DF AUC 0.9712 (trained on c40) | STIL Tables 1–3 | ✓ |
| FTCN + TT: FF++ HQ Acc 99.1 / AUC 99.8; LQ AUC 98.3; DFo → DFo AUC 100 | FTCN supplementary Tables 2 and 1 (CVF ZIP) | ✓. Tier B: the HQ setup "follows PE-LSTM/Two-branch" and the LQ setup "follows LipForensics", subset not stated |
| FTCN 99.9 / 98.1; Xception 93.9 (C23 "Tier A" in the package) | FTCN main paper, Tables 2 and 8 | ✗ Cross-manipulation; exclude (M-A4a) |
| TALL-Swin HQ 98.65 / 99.87, LQ 92.82 / 94.57; Xception 95.73 / 96.30, 86.86 / 89.30 | Xu et al. 2023, Table 2 (arXiv PDF) | ✓ (video-level, all four FF++ manipulations) |
| DFo I3D 100.00, Xception 100.00 (std → std); hidden set I3D 79.25, Xception 77.00 | Jiang et al. 2020, Tables 5 and 4 | ✓ (hidden set ≠ standard test set; M-A4b) |
| SFormer ranges | Kingra et al. 2024 | **Not verifiable** (paywalled). The package extraction cites Tables 2–3 (PDF pp. 8–9). Flag as "as extracted". The statistician or lead should check the PDF if the group has it |
| Preliminary-study Xception (4 cells) and test populations | Preliminary-study PDF, Table 7; text p. "859 Celeb-DF test videos", "2,385/2,412" | ✓ |

**References.**
- **Already in the list:**
  - Gu et al. (2021); Zheng et al. (2021); Xu et al. (2023); Kingra et al. (2024);
  - Jiang et al. (2020); Li, Y. et al. (2020) (Celeb-DF); Rössler et al. (2019);
  - Chollet (2017); Carreira & Zisserman (2017); Bandos et al. (2005) (DOI re-verified on Crossref).
- **Missing; add both:**
  - Li, X., Lang, Y., Chen, Y., Mao, X., He, Y., Wang, S., Xue, H., & Lu, Q. (2020). Sharp multiple instance learning for DeepFake video detection. In *Proceedings of the 28th ACM International Conference on Multimedia* (pp. 1864–1872). Association for Computing Machinery. https://doi.org/10.1145/3394171.3414034 (verified on Crossref)
  - Custodio, E. T., Degamo, M. K., Escueta, K. R. C., San Diego, D. A. E., & Sarmiento, M. J. F. (2026). *SwinFusion++: Face-aligned spatio-temporal Swin Transformer for deepfake detection* [Unpublished manuscript]. College of Computer Studies and Systems, University of the East–Manila. (The authors and title match the PDF.)
- **In-text citation note:** the APA in-text form for S-MIL is "X. Li et al., 2020", to distinguish it from Y. Li et al. (2020).

## E. Questions for the team

1. **Statistician:**
   - Should Celeb-DF published values stay Tier A or become "A (dataset only)" given the 978-vs-518 test sets?
   - Should Table 9 show the BO ensemble AUC CIs (as in RQ1), or point values only?
   - Please confirm the Xception DeeperForensics-1.0 analyzed-fake count (2,185 of 2,385).
2. **Lead:**
   - Accept the Table 9/10 split, the Appendix J retitle and J9 (the full value list, including the marked exclusions)?
   - Should Figure 14 be drafted now or after Table 10 is agreed? I recommend after.
3. **Lead:** flag M-A4 (the mislabeled FTCN and Xception rows) to the user, so the package and the LaTeX paper can be corrected; I have not edited either.
4. **Both:** do we agree that RQ2's answer gives no ranking claim at all against published models, only "within about two points"?
