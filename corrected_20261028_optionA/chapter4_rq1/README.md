# Chapter 4 opening + RQ1 — production files (2026-10-30)

Chapter 4 (opening and RQ1), a Chapter 3 "Amendments after Test Scoring" paragraph, two references (Bandos et al., 2005; Holm, 1979), APA appendix-letter figure numbering (B1–F4), and Appendix J were inserted into the ONE thesis .docx as tracked changes by "Claude". Written by a three-advisor team (lead, statistician, methodologist), which agreed every item over three rounds.

| Folder | Contents |
|---|---|
| `tables/` | One verified CSV per table (T1–T9, J1–J8; T3 = deviations table, NOT used in the manuscript since 2026-10-30, and files T4–T9 print as Tables 3–8) plus `<ID>_note.txt`; `KEY_NUMBERS.md` (source of every number in the prose); `D2_final.txt` (the Chapter 3 amendment); `opening_integrity.txt` |
| `figures/` | Figures 11, 12, 13, J1 (300 dpi, 6 in) and `captions.md` |
| `scripts/` | `ch4_content.py` (all prose), `build_ch4.py` (assembles into the .docx), `docx_ins.py` (tracked-change XML), `check_numbers.py`, `export_review.py`; the statistician's and methodologist's table/figure scripts |
| `stats_out/` | Supplementary analyses (threshold Δ intervals, MDD, seed sign agreement, Holm partitions, DFo global clusters, Celeb-DF leave-one-identity-out, jackknife/bootstrap, rank-correction impact, bootstrap-p decision check) |
| `advisory_team/` | Round 1–3 memos, `AGREED_PLAN.md`, `round3_resolution.md`, `FINAL_DRAFT.md` (accepted view) |

The scripts expect the scratchpad layout of the session that produced them (`.../scratchpad/ch4/{tools,team}` and the raw predictions under `.../scratchpad/b2dl/`); adjust the paths to rerun.
