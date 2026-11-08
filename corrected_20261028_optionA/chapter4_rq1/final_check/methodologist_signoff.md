# Final build sign-off: methodologist

**Verdict: OBJECTION, on format only.** No number is affected.

**LABELS: AGREE.**

I checked `render/final.pdf` (223 pages) and `render/final.docx`. I looked at page images, extracted page text, read the XML, and re-rendered the docx with the same LibreOffice build. The re-render matches `final.pdf`: same file size and same page count. I could not test in Word.

## Passed

- **Title page:** dated NOVEMBER 2026.
- **TOC:** every chapter, Heading 2, REFERENCES, APPENDICES and Appendix A–J page number matches the PDF.
- **List of Figures and List of Tables:** 81 of the 82 page numbers match. The exception is item 1 below.
- **Figure 1–10 callouts:** all present and readable in context. Each comes before its figure, except Figure 4, whose callout comes in the sentence right after it. That was expected, because the image sits directly under its heading.
- **Appendix H and I titles:** correct.
- **Table J9:**
  - It has 234 rows and 9 columns, and the header row repeats on each page.
  - Test set, metric, value and tier match `rq2x/tables/J9.csv` for all 234 rows.
  - The 64 † marks on values match the 64 "as extracted" rows.

## MUST-FIX

1. **List of Figures, Figure B7.** The page number 158 → 159. The caption is on page 159.

2. **Front-matter lines in the TOC.** They print "i, ii, iii, vi", but the footers print 1, 2, 4, 6.
   - "List of Figures iii" is wrong under either system, because it starts on page 4.
   - Change the four numbers to 1, 2, 4, 6, so they match what the reader sees.

3. **Page 177 is blank.**
   - After "12. Comments and/or Suggestions" (Appendix D), an empty paragraph and a page-break paragraph spill over from a full page 176.
   - Delete both and put `<w:pageBreakBefore/>` on the second "GOOGLE FORM" paragraph.

4. **Captions split across pages.**
   - Figure C6 leaves "Usability" at the top of page 173.
   - Figure D4 leaves its last three lines alone on page 180, which is otherwise empty.
   - Figure D5 leaves "Help/Documentation/Transparency" above the APPENDIX E heading on page 182.
   - In the Appendix C and D image tables, single-space the captions (`w:line="240"`) and set `<w:cantSplit/>` on the rows.
   - If a row still overflows, scale its images by about 5–10%.

5. **Figure 2.** The image is on page 62 and its caption sits alone on page 63. Scale the HIPO image by about 92% so the caption fits under it.

6. **Figure B7 caption (page 159).**
   - It prints as "Figure … B7." on either side of the floating image, because the image (`wrapSquare`) overlaps the caption paragraph.
   - Set that image to `<wp:wrapTopAndBottom/>`, then check the spacing from the empty paragraphs above the caption.

7. **Stray black vertical line on page 166,** to the right of Figure B27. The cell's `tcBorders` has no right border, so the table's black border shows. Add `<w:right w:color="ffffff" w:space="0" w:sz="8" w:val="single"/>`.

8. **APPENDICES and Appendix A headings (page 151).**
   - "APPENDICES", "APPENDIX A" and "GANTT CHART" are stranded under the last references, and the chart starts on page 152.
   - Put `<w:pageBreakBefore/>` on APPENDICES and remove its `w:ind w:left="720"`.
   - The headings and the chart should then share page 152, so only the APPENDICES and APPENDIX A entries in the TOC change (151 → 152). Check this in the re-render.

9. **Heading 1 alignment.**
   - The XML has `jc=center`, but LibreOffice drops it. In the ODT conversion these paragraphs carry no alignment, and the PDF places every Heading 1 at x = 90: Chapters 1–4, REFERENCES and APPENDICES.
   - Add `<w:jc w:val="center"/>` to the Heading1 style. All six Heading 1 paragraphs are meant to be centered, so the PDF and Word will then agree.

10. **Table J9, Setting column: stray ")" in 50 rows.**
    - "video; HQ), all four manipulations; all four FF++ manipulations (DF, F2F, FS, NT)" → "video; HQ; all four FF++ manipulations" (25 rows)
    - The same change for "LQ)" → "LQ;" (25 rows)
    - In every other row, "all four manipulations; all four FF++ manipulations" → "all four FF++ manipulations"
    - This also removes the undefined DF, F2F, FS and NT.

11. **Table J9, Source column: misleading "(†)" in 4 rows.**
    - "re-implemented (†)" → "re-implemented by Gu et al."
    - These are ADDNet-3D ×3 and TEI ×1. The † is Gu et al.'s own mark for re-implementation, carried over from the source.
    - The J9 note now defines † as "without re-checking against the original paper", but these four rows were verified against the PDF.

12. **Remove all 396 U+2060 word joiners** from "FF++" and "SwinFusion++". 129 of them are in prose.
    - They stop a text search for "SwinFusion++" from finding those instances, and they change the strings Turnitin and copy-paste see.
    - Word may also show them as boxes in fonts without that glyph. I could not test this.
    - As far as I know, Word does not break a line inside "++", so the protection is only needed for LibreOffice. If the PDF then breaks at "+ +" in a narrow table cell, widen that column.

## LABELS: AGREE

- Delete "; file label RQ1_architecture" and "; file label RQ6_architecture". They appear once each, on pages 117 and 120, and nowhere else in the PDF.
- The package README keeps the mapping (`corrected_20261028_optionA/README.md`, line 11).
- **The same reasoning applies to the amendment IDs on page 114, so delete them too:**
  - Table 2, two rows: "Primary family before scoring (A-16);" → "Primary family before scoring;"
  - Table 2: "Unchanged since before scoring (A-16, A-18)" → "Unchanged since before scoring"
  - Table 2 note: "recorded on October 2, 2026 (A-16):" → "recorded on October 2, 2026:"
  - These IDs are defined nowhere in the thesis.

## SHOULD

- **J9, DeeperForensics-1.0 Tier A rows from Jiang et al. Table 5.**
  - I3D and Xception show "video; unstated or other", while the C3D, ResNet+LSTM and TSN rows from the same table show the standard-set text. Use the standard-set text for all five.
  - Tidy that text too: "standard set, no distortions; standard set: 1,000 raw…" → "standard set, no distortions: 1,000 raw…".
- **J9, Value column.** The † wraps onto its own line ("99.67%" / "†"). Widen the column slightly or use a no-break space.
- **List of Tables and List of Figures.** Table 7, Table 10, Table J1 and Figure C8 leave only the dot leader and page number on a second line. This is acceptable. A right indent would wrap the titles earlier.

## For the lead to tell the user

- **Appendix I (AI report) has only its title; the page is otherwise empty.** We cannot produce a Turnitin report, so the user must supply it or the appendix must be removed.
- **All TOC, List of Figures and List of Tables page numbers come from a LibreOffice render.** Word may paginate differently, and all page-number checks here are against that render.
  - If the user submits from Word, the numbers need checking after opening it there.
  - Otherwise, submit the LibreOffice PDF.
- **Page numbers must be recomputed** after items 3, 4, 5 and 8.
