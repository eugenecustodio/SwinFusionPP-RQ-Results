# Chapter 4 RQ1 for the Google Doc (CURRENT DRAFT tab), 2026-11-07

**Paste sources:** these are not manuscript copies; delete them after pasting.
- `RQ1_paste_into_CURRENT_DRAFT.docx`: paste over the template block between the "RQ1: SwinFusion++ Compared with…" heading and "[THEN RQ2, RQ3, RQ4 WITH THE SAME FORMATS]". It contains Tables VI–XII and 3 figures captioned "Figure X".
- `AppendixJ_paste_into_CURRENT_DRAFT.docx`: paste after Appendix I. It contains Tables J1–J8 and Figure J1.

**Sources:** the text is in `rq1_text.py` and the builder in `build_docx.py`. Tables come from ../tables/*.csv and figures from ../figures/*.png.

**Agreement:** lead, statistician and methodologist, in two review rounds.
- The statistician's fixes covered tuning wording, the seed average, "combining two encoders", Li 2020 reporting AUC, the "motivated" wording plus Zheng 2021, the primary measure, BO tuning wording, and the platform sentence.
- The methodologist's fixes covered the flip-TTA wording, the 0.011 bound, the literature sentence, the threshold sentence and the platform sentence.
- Both independently caught a false "most target scores fell below" sentence. It was replaced with a version verified in all 27 T7 cells.
