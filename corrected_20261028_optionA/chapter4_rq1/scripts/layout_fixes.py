"""Layout fixes that run after the text edits. Usage: python layout_fixes.py in.docx out.docx
Paragraph, row and cell changes are tracked. Word cannot track image size, image wrap or style definitions, so those
three are direct changes: Figure 2 and the rows in SCALE (size), Figure B7 (wrap), Heading 1 (centered, as its six
paragraphs already are)."""
import html
import itertools
import re
import sys
import zipfile

import docx_ins as D

D._ids = itertools.count(990001)
# caption label -> factor for the image in the same table cell; both images of a row keep the same size
SCALE = {'Figure C6.': 0.92, 'Figure C7.': 0.92, 'Figure D3.': 0.88, 'Figure D4.': 0.88, 'Figure D5.': 0.88, 'Figure D6.': 0.88}
scaled = set()

PAR = re.compile(r'<w:p[ >](?:(?!<w:p[ >]).)*?</w:p>', re.S)


def vis(xml):
    xml = re.sub(r'<w:del (?:(?!/>)[^>])*>.*?</w:del>', '', xml, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', xml)).strip()


def add_ppr(base, tag):
    """Insert after pStyle/keepNext/keepLines, which is where these elements belong in schema order."""
    m = re.match(r'(<w:pStyle [^>]*/>)?(<w:keepNext[^>]*/>)?(<w:keepLines[^>]*/>)?', base)
    return base[:m.end()] + tag + base[m.end():]


def retrack(par, transform):
    """change_ppr, but a paragraph already holding a format change keeps that one as its 'before' state."""
    m = re.search(r'(<w:pPr>)(.*?)(<w:pPrChange\b.*?</w:pPrChange></w:pPr>)', par, flags=re.S)
    if m:
        return par[:m.start(2)] + transform(m.group(2)) + par[m.end(2):]
    return D.change_ppr(par, transform)


def remove(par):
    """Tracked deletion, except a paragraph this build itself inserted: that one simply never existed."""
    return '' if '<w:ins ' in par.split('</w:pPr>')[0] else D.delete_paragraph(par)


def scale(xml, f):
    def one(m):
        return f'{m.group(1)}cx="{round(int(m.group(2)) * f)}" cy="{round(int(m.group(3)) * f)}"/>'
    return re.sub(r'(<(?:wp:extent|a:ext) )cx="(\d+)" cy="(\d+)"/>', one, xml)


src, dst = sys.argv[1:3]
zi = zipfile.ZipFile(src)
x = zi.read('word/document.xml').decode('utf-8')
pars = list(PAR.finditer(x))
txt = [vis(m.group(0)) for m in pars]
new = {}


def at(pred, nth=0):
    hits = [i for i, t in enumerate(txt) if pred(t)]
    assert len(hits) > nth, 'not found'
    return hits[nth]


get = lambda i: new.get(i, pars[i].group(0))

# Figure 2: the image and caption fall on different pages
i = at(lambda t: t == 'Figure 2. HIPO Chart')
assert '<w:drawing' in get(i - 1) and '<wp:inline' in get(i - 1)
new[i - 1] = retrack(scale(get(i - 1), 0.92), lambda b: add_ppr(b, '<w:keepNext/>'))

# APPENDICES starts a page, so its heading stays with the Gantt chart, and its stray indent goes
i = at(lambda t: t == 'APPENDICES')
assert 'w:val="Heading1"' in get(i)
new[i] = retrack(get(i), lambda b: add_ppr(b.replace('<w:ind w:left="720"/>', ''), '<w:pageBreakBefore/>'))

# An empty paragraph holding only a page break makes a blank page whenever the page before it is exactly full,
# so the break moves onto the paragraph it introduces; empty paragraphs right before that break go as well
moved = 0
for k in range(1, len(pars) - 1):
    if txt[k] or 'w:type="page"' not in get(k) or '<w:drawing' in get(k):
        continue
    if not txt[k + 1] or x[pars[k].end():pars[k + 1].start()].strip():  # next is empty, or not a sibling paragraph
        continue
    new[k] = remove(get(k))
    new[k + 1] = retrack(get(k + 1), lambda b: add_ppr(b, '<w:pageBreakBefore/>'))
    moved += 1
    e = k - 1
    while not txt[e] and '<w:drawing' not in get(e) and 'w:type="page"' not in get(e) and not x[pars[e].end():pars[e + 1].start()].strip():
        new[e] = remove(get(e))
        e -= 1
print('page breaks moved:', moved)

# Appendix E starts its own page, so its heading stays with the letter
i = at(lambda t: t == 'APPENDIX E')
new[i] = retrack(get(i), lambda b: add_ppr(b, '<w:pageBreakBefore/>'))

# Figure B7: the floating image overlapped its caption; six empty paragraphs were holding the caption down
i = at(lambda t: t.startswith('Figure B7.'), nth=1)  # 0 is its List of Figures entry
a = i - 7
assert '<wp:wrapSquare' in get(a) and all(not txt[k] and '<w:drawing' not in get(k) for k in range(a + 1, i))
new[a] = re.sub(r'<wp:wrapSquare [^>]*/>', '<wp:wrapTopAndBottom distT="114300" distB="114300"/>', get(a))
for k in range(a + 1, i):
    new[k] = remove(get(k))

out, pos = [], 0
for k, m in enumerate(pars):
    out += [x[pos:m.start()], get(k)]
    pos = m.end()
x = ''.join(out) + x[pos:]


def fix_table(m):
    t = m.group(0)
    if not re.search(r'Figure [CD]\d+\.', vis(t)):
        return t
    def row(rm):
        inner = rm.group(1)
        if '<w:cantSplit w:val="0"/>' not in inner:
            return rm.group(0)
        return ('<w:trPr>' + inner.replace('<w:cantSplit w:val="0"/>', '<w:cantSplit/>')
                + f'<w:trPrChange {D._attrs()}><w:trPr>{inner}</w:trPr></w:trPrChange></w:trPr>')
    return re.sub(r'<w:trPr>(.*?)</w:trPr>', row, t, flags=re.S)


# Appendix C and D image rows: an image and its caption stay on one page
x = re.sub(r'<w:tbl>.*?</w:tbl>', fix_table, x, flags=re.S)


def fix_cell(m):
    c = m.group(0)
    t = vis(c)
    if t.startswith('Figure B27.'):  # no right border on this cell, so the table's black one showed
        pr = re.search(r'<w:tcPr>(.*?)</w:tcPr>', c, flags=re.S)
        inner = pr.group(1)
        assert '<w:right ' not in re.search(r'<w:tcBorders>.*?</w:tcBorders>', inner, flags=re.S).group(0)
        changed = inner.replace('</w:tcBorders>', '<w:right w:color="ffffff" w:space="0" w:sz="8" w:val="single"/></w:tcBorders>')
        c = c[:pr.start()] + f'<w:tcPr>{changed}<w:tcPrChange {D._attrs()}><w:tcPr>{inner}</w:tcPr></w:tcPrChange></w:tcPr>' + c[pr.end():]
    for label, f in SCALE.items():
        if t.startswith(label):
            c = scale(c, f)
            scaled.add(label)
    return c


x = re.sub(r'<w:tc>(?:(?!<w:tc>).)*?</w:tc>', fix_cell, x, flags=re.S)

assert scaled == set(SCALE), set(SCALE) - scaled
st = zi.read('word/styles.xml').decode('utf-8')
hm = re.search(r'<w:style [^>]*w:styleId="Heading1".*?</w:style>', st, flags=re.S)
h = hm.group(0)
assert '<w:jc ' not in h
h2 = h.replace('<w:spacing w:after="160" w:lineRule="auto"/></w:pPr>', '<w:spacing w:after="160" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>')
assert h2 != h
st = st[:hm.start()] + h2 + st[hm.end():]

zo = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for item in zi.infolist():
    data = zi.read(item.filename)
    if item.filename == 'word/document.xml':
        data = x.encode('utf-8')
    elif item.filename == 'word/styles.xml':
        data = st.encode('utf-8')
    zo.writestr(item, data)
zo.close()
print('layout fixes applied')
