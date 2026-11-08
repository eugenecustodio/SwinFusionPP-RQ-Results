# KEY_NUMBERS_RQ2: printed strings the RQ2 prose may cite

**How to read this file.**
- `T9 rK` = row K of `team/rq2/tables/T9.csv` (1-based, header excluded, `__SPAN__` rows counted).
- SwinFusion++ values were recomputed from the raw predictions and asserted against `00_Shared/statistics_raw/three_seed_mean_logit_ensemble.csv`.
- Xception values come from `00_Shared/literature/preliminary_study_v020.csv` (preliminary manuscript, Table 7). Its test populations come from preliminary Table 2.
- Published values (section D) are from the methodologist's verification. Re-check them against T10 once it exists.
- All minus signs are U+2212.

## A. SwinFusion++, within datasets (T9)

| Test set | Configuration | ROC-AUC [95% CI] | Acc (%) | Row |
|---|---|---|---|---|
| FF++ C23 | BO-selected | 0.9964 [0.9886, 1.0000] | 98.21 | T9 r2 |
| FF++ C23 | fixed recipe | 0.9942 [0.9834, 0.9999] | 97.86 | T9 r3 |
| FF++ C40 | BO-selected | 0.9941 [0.9875, 0.9989] | 96.07 | T9 r6 |
| FF++ C40 | fixed recipe | 0.9878 [0.9772, 0.9965] | 94.64 | T9 r7 |
| Celeb-DF v2 | BO-selected | 0.9983 [0.9963, 1.0000] | 98.36 | T9 r10 |
| Celeb-DF v2 | fixed recipe | 0.9951 [0.9905, 0.9995] | 97.75 | T9 r11 |
| DeeperForensics-1.0 | BO-selected | 0.9954 [0.9874, 1.0000] | 98.51 | T9 r14 |
| DeeperForensics-1.0 | fixed recipe | 0.9974 [0.9921, 1.0000] | 98.76 | T9 r15 |

- **Ranges.** BO-selected: ROC-AUC 0.994–0.998 and accuracy 96.07–98.51% ("96.1–98.5%"). Fixed recipe: ROC-AUC 0.988–0.997 and accuracy 94.64–98.76% ("94.6–98.8%").
- **DeeperForensics-1.0:** both configurations made no false positives (Spec 100.00, T9 r14–r15).

## B. Preliminary-study Xception (T9)

| Test set | ROC-AUC | Acc (%) | F1 | Rec / Spec (%) | Test videos (fake) | Row |
|---|---|---|---|---|---|---|
| FF++ C23 | 0.7725 | 69.64 | 0.6886 | 67.14 / 72.14 | 280 (140) | T9 r4 |
| FF++ C40 | 0.8109 | 74.29 | 0.7429 | 74.29 / 74.29 | 280 (140) | T9 r8 |
| Celeb-DF v2 | 0.6480 | 84.17* | 0.9140* | 100.00 / 0.00 | 859 (723; 84.17%) | T9 r12 |
| DeeperForensics-1.0 | 0.9978 | 46.00† | 0.5821† | 41.05 / 100.00 | 2,385 (2,185; 91.61%), perturbation variants included | T9 r16 |

- **\* Celeb-DF:** every video was labeled fake (preliminary text: "predictions of fake for all 859 videos"), so accuracy equals the fake share.
- **† DeeperForensics:** no false positives, and 1,288 of 2,185 fake videos missed (preliminary text: "1,288 false negatives and no false positives").
- **Recall and specificity** are derived: each is the unique confusion matrix consistent with the reported accuracy and F1.
  - C23: TP 94, FP 39, TN 101, FN 46.
  - C40: TP 104, FP 36, TN 104, FN 36.
- **Preliminary training:** single seed 1701; at most 15 epochs, patience 4; 299 × 299 input; three 16-position anchors per video (preliminary §4.3–4.5 and Table 3).

**Descriptive ROC-AUC differences** (SwinFusion++ − Xception; not paired, no test):

| Test set | BO | Fixed | How to print |
|---|---|---|---|
| FF++ C23 | +0.2239 | +0.2217 | "about 0.22 higher", same test size and split rule |
| FF++ C40 | +0.1832 | +0.1769 | "0.18 higher" |
| Celeb-DF v2 | +0.3503 | +0.3471 | Different test populations: print side by side, not as a difference |
| DeeperForensics-1.0 | −0.0024 | −0.0004 | Different populations: "similar", no ranking |

## C. Prevalence facts for the accuracy rule

- **This study's test sets** (T9 span rows): Celeb-DF v2 86.20% fake (843 of 978), so an always-fake rule scores 86.20%. FF++ C23/C40 and DeeperForensics-1.0 are 50.00% fake.
- **The preliminary study's test sets:** Celeb-DF v2 84.17% fake; DeeperForensics-1.0 91.61% fake (an always-fake rule would score 91.61%).

## D. Previously reported values the text may cite

Source: the methodologist's verification. Tier in brackets.

**Accuracy, FF++ only, comparing the highest Tier-A value with SwinFusion++.**

| Test set | Highest Tier-A accuracy | BO gap | Fixed gap |
|---|---|---|---|
| FF++ C23 | 100.00 (Xception XN-avg, X. Li et al., 2020; STIL prints 98.93) | 98.21 → 1.79 points lower | 97.86 → 2.14 points lower |
| FF++ C40 | 98.21 (STIL, Gu et al., 2021) [A] | 96.07 → 2.14 points lower | 94.64 → **3.57 points lower** |

The "within about two points" wording therefore holds for the BO-selected configuration only. For the fixed recipe, give the gaps (2.14 and 3.57) or name the configuration.

**Lower reported accuracies:**
- I3D 92.86 (C23) and 91.07 (C40) [A];
- TALL-Swin 92.82 (C40) [B, all four manipulations].

**ROC-AUC on C40.** BO 0.9941 and fixed 0.9878 are both above:
- FTCN 0.983 [B];
- STIL 0.971 [A];
- TALL-Swin 0.946 [B].

The sentence holds for both configurations. Always add the "not like-for-like" clause.

**ROC-AUC on C23.** BO 0.9964 and fixed 0.9942 are close to:
- FTCN 0.998 [B]: 0.0016 and 0.0038 lower;
- TALL-Swin 0.999 [B]: 0.0026 and 0.0048 lower.

**DeeperForensics-1.0.**
- Reported values:
  - SFormer accuracy 99.67–100.00 [A, as extracted; original not re-verified];
  - I3D and Xception 100.00 for std → std [B];
  - FTCN AUC 1.000 [B].
- SwinFusion++: BO 98.51% / 0.9954, fixed 98.76% / 0.9974. Both are near the ceiling, on different constructions.

**Celeb-DF v2:** no accuracy comparison across studies (agreed plan, item 4).

**Do not cite:**
- the FTCN 0.999/0.981 and Xception 0.939 cross-manipulation values (M-A4a);
- the DeeperForensics hidden-set 77.00/79.25 (M-A4b);
- any frame-level value.

## E. Disclosure numbers

- **Celeb-DF v2 test set:** 978 videos, split by target identity. All 843 fake videos lie in 9 identity clusters (Table 1). The official list has 518 videos; that count is the methodologist's, so verify it in T10_note.
- **DeeperForensics-1.0 test set:** 402 videos, 201 of them unperturbed manipulated videos and 201 FF++ source originals.
- **Preliminary test sets:** Celeb-DF v2 859 videos; DeeperForensics-1.0 2,385 analyzed (91.61% fake, perturbation variants included).
- **Only one external model was run locally:** Xception, in the preliminary study.
