"""Build paste-source .docx files for the Google Doc (CURRENT DRAFT): RQ1 section and Appendix J.
Usage: python build_docx.py <rq1_text.py> <tables_dir> <figures_dir> <out_dir>"""
import csv, importlib.util, re, sys
from pathlib import Path
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

spec = importlib.util.spec_from_file_location('rq1', sys.argv[1]); T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
TAB, FIG, OUT = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]); OUT.mkdir(parents=True, exist_ok=True)
FONT = 'Arial'


def new_doc():
    d = Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    for side in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
        setattr(sec, side, Inches(1.0))
    st = d.styles['Normal']; st.font.name = FONT; st.font.size = Pt(12)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
    pf = st.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 2.0
    return d


def runs(p, text, size=None, bold=False, italic=False):
    for k, part in enumerate(re.split(r'(\*[^*]+\*)', text)):
        if not part:
            continue
        it = part.startswith('*') and part.endswith('*')
        r = p.add_run(part[1:-1] if it else part)
        r.bold = bold; r.italic = italic or it; r.font.name = FONT
        if size: r.font.size = Pt(size)
    return p


def body(d, text):
    p = d.add_paragraph(); f = p.paragraph_format
    f.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; f.first_line_indent = Inches(0.5)
    return runs(p, text)


def sub(d, text, center=False):
    p = d.add_paragraph(); p.paragraph_format.keep_with_next = True
    if center: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return runs(p, text, bold=True)


def caption(d, label, title):
    p = d.add_paragraph(); f = p.paragraph_format
    f.alignment = WD_ALIGN_PARAGRAPH.CENTER; f.line_spacing = 1.0; f.space_before = Pt(6); f.space_after = Pt(4)
    r = p.add_run(label + ' '); r.bold = True; r.italic = True; r.font.name = FONT
    r = p.add_run(title); r.italic = True; r.font.name = FONT
    return p


def note(d, text):
    text = text.strip()
    if text.startswith('Note.'):
        text = text[len('Note.'):].strip()
    p = d.add_paragraph(); f = p.paragraph_format
    f.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; f.line_spacing = 1.0; f.space_after = Pt(12)
    r = p.add_run('Note. '); r.italic = True; r.font.name = FONT; r.font.size = Pt(10)
    runs(p, text, size=10)
    return p


def set_repeat_header(row):
    trPr = row._tr.get_or_add_trPr(); el = OxmlElement('w:tblHeader'); el.set(qn('w:val'), 'true'); trPr.append(el)


def cant_split(row):
    trPr = row._tr.get_or_add_trPr(); trPr.append(OxmlElement('w:cantSplit'))


def table(d, label, src, title):
    rows = list(csv.reader(open(TAB / f'{src}.csv', encoding='utf-8')))
    header, data = rows[0], rows[1:]
    ncol = len(header)
    size = 8 if ncol >= 9 else 9
    t = d.add_table(rows=0, cols=ncol); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    def fill(row, vals, bold=False, italic=False, span=False):
        cells = row.cells
        if span:
            c = cells[0].merge(cells[-1]); vals = [vals[1]]; cells = [c]
        for k, (c, v) in enumerate(zip(cells, vals)):
            c.text = ''
            p = c.paragraphs[0]; pf = p.paragraph_format; pf.line_spacing = 1.0; pf.first_line_indent = Inches(0)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if (k == 0 or span) else WD_ALIGN_PARAGRAPH.CENTER
            runs(p, v, size=size, bold=bold, italic=italic)
    hr = t.add_row(); fill(hr, header, bold=True); set_repeat_header(hr); cant_split(hr)
    for v in data:
        r = t.add_row(); cant_split(r)
        if v and v[0] == '__SPAN__':
            fill(r, v, italic=True, span=True)
        else:
            fill(r, v + [''] * (ncol - len(v)))
    caption(d, f'Table {label}.', title)
    nf = TAB / f'{src}_note.txt'
    if nf.exists():
        note(d, nf.read_text(encoding='utf-8'))


def figure(d, label, fname, title, ntext):
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(str(FIG / fname), width=Inches(6.0))
    caption(d, label, title)
    note(d, ntext)


# ---------------- RQ1 section ----------------
d = new_doc()
for b in T.BLOCKS:
    kind = b[0]
    if kind == 'p':
        body(d, b[1])
    elif kind == 'sub':
        sub(d, b[1])
    elif kind == 'table':
        table(d, b[1], b[2], b[3])
    elif kind == 'fig':
        figure(d, 'Figure X.', b[1], b[2], b[3])
d.save(OUT / 'RQ1_paste_into_CURRENT_DRAFT.docx')

# ---------------- Appendix J ----------------
a = new_doc()
sub(a, 'APPENDIX J', center=True)
sub(a, 'SUPPLEMENTARY RESULTS FOR RESEARCH QUESTION 1', center=True)
body(a, T.APPX_J_INTRO)
for tid, title in T.J_TABLES:
    table(a, tid, tid, title)
figure(a, 'Figure J1.', *T.FIG_J1)
a.save(OUT / 'AppendixJ_paste_into_CURRENT_DRAFT.docx')

# plain-text export for review
with open(OUT / 'RQ1_text_for_review.txt', 'w', encoding='utf-8') as f:
    for b in T.BLOCKS:
        if b[0] == 'p': f.write(b[1] + '\n\n')
        elif b[0] == 'sub': f.write('## ' + b[1] + '\n\n')
        elif b[0] == 'table': f.write(f'[Table {b[1]}. {b[3]}  (source {b[2]}.csv)]\n\n')
        elif b[0] == 'fig': f.write(f'[Figure X. {b[2]}  ({b[1]})]\n\n')
print('built', sorted(p.name for p in OUT.iterdir()))
