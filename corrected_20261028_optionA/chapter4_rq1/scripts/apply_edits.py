"""Apply agreed text edits to Chapters 1–3 (and the front matter) of the thesis .docx as tracked changes.

Usage: python apply_edits.py <in.docx> <edits.json> <out.docx>
edits.json: [{"id": "E1", "old": "exact text", "new": "replacement text"}, ...]
Each `old` must occur exactly once in the accepted text of the paragraphs before the Chapter 4 heading
(deleted text is ignored; earlier tracked insertions count as text). An edit may span several runs of
one paragraph. new == "" deletes; the paragraph and its formatting are kept.
"""
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import itertools  # noqa: E402
import docx_ins as D  # noqa: E402
D._ids = itertools.count(950001)  # above every id used by the Chapter 4 insertion

src, edits_path, dst = sys.argv[1:4]
edits = json.loads(Path(edits_path).read_text())
zin = zipfile.ZipFile(src)
doc = zin.read('word/document.xml').decode('utf-8')

RUN = re.compile(r'<w:r(?: [^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)?((?:(?!</w:r>).)*)</w:r>', re.S)
DEL = re.compile(r'<w:del [^>]*>.*?</w:del>', re.S)


def unesc(s):
    return s.replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&amp;', '&')


def live_runs(par):
    """(start, end, rpr, content) for runs outside <w:del>, with their visible text."""
    dels = [(m.start(), m.end()) for m in DEL.finditer(par)]
    out = []
    for m in RUN.finditer(par):
        if any(a <= m.start() < b for a, b in dels):
            continue
        out.append(m)
    return out


def run_text(m):
    return ''.join(unesc(t) for t in re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', m.group(2)))


def para_text(par):
    t = ''.join(run_text(m) for m in live_runs(par))
    return t + ''.join(unesc(x) for x in re.findall(r'<m:t(?: [^>]*)?>([^<]*)</m:t>', par))


def tracked_replace(par, old, new):
    runs = live_runs(par)
    texts = [run_text(m) for m in runs]
    full = ''.join(texts)
    assert full.count(old) == 1, (full.count(old), old[:60])
    a = full.index(old)
    b = a + len(old)
    pieces, pos, first_rpr, inserted = [], 0, None, False
    out = par
    # rebuild from the last run backwards so earlier offsets stay valid
    plan = []
    for m, t in zip(runs, texts):
        s, e = pos, pos + len(t)
        pos = e
        if e <= a or s >= b or not t:
            continue
        plan.append((m, t, max(a, s) - s, min(b, e) - s, s))
    assert plan, 'no run overlaps the edit'
    for k, (m, t, i, j, s) in enumerate(reversed(plan)):
        rpr = m.group(1) or ''
        content = m.group(2)
        if re.sub(r'<w:t(?: [^>]*)?>[^<]*</w:t>', '', content).strip():
            # run holds other children (tab, break, drawing): only allow when untouched part is plain text
            assert not re.search(r'<w:(?:tab|br|drawing|fldChar|instrText)', content), 'edit crosses a non-text run'
        before, mid, after = t[:i], t[i:j], t[j:]
        seg = ''
        if before:
            seg += f'<w:r>{rpr}<w:t xml:space="preserve">{escape(before)}</w:t></w:r>'
        if mid:
            seg += f'<w:del {D._attrs()}><w:r>{rpr}<w:delText xml:space="preserve">{escape(mid)}</w:delText></w:r></w:del>'
        if k == 0 and new:  # the last overlapping run gets the insertion after its deleted part
            seg += f'<w:ins {D._attrs()}><w:r>{rpr}<w:t xml:space="preserve">{escape(new)}</w:t></w:r></w:ins>'
        if after:
            seg += f'<w:r>{rpr}<w:t xml:space="preserve">{escape(after)}</w:t></w:r>'
        out = out[:m.start()] + seg + out[m.end():]
    return out


body_start = doc.index('<w:body>') + len('<w:body>')
blocks = list(re.finditer(r'<w:tbl>.*?</w:tbl>|<w:p[ >].*?</w:p>', doc[body_start:], flags=re.S))
ch4 = next(i for i, m in enumerate(blocks) if para_text(m.group(0)).startswith('Chapter 4 – PRESENTATION'))
scope = blocks          # edits located by context may target any paragraph; others only those before Chapter 4
pre = set(range(ch4))
new_xml = {i: m.group(0) for i, m in enumerate(scope)}
report = []
def delete_paragraph(par):
    """Tracked deletion of a whole paragraph: every live run (w:r or m:r) goes into <w:del>, and so does the mark."""
    dels = [(m.start(), m.end()) for m in DEL.finditer(par)]
    runs = [m for m in re.finditer(r'<(w|m):r(?: [^>]*)?>.*?</\1:r>', par, flags=re.S)
            if not any(a <= m.start() < b for a, b in dels)]
    for m in reversed(runs):
        r = m.group(0)
        if m.group(1) == 'w':
            r = re.sub(r'<w:t((?: [^>]*)?)>', r'<w:delText\1>', r).replace('</w:t>', '</w:delText>')
        par = par[:m.start()] + f'<w:del {D._attrs()}>{r}</w:del>' + par[m.end():]
    mark = f'<w:del {D._attrs()}/>'
    if '<w:pPr>' not in par:
        par = re.sub(r'^(<w:p(?: [^>]*)?>)', r'\1<w:pPr><w:rPr>' + mark + '</w:rPr></w:pPr>', par)
    elif re.search(r'<w:pPr>(?:(?!</w:pPr>).)*<w:rPr>', par, flags=re.S):
        par = re.sub(r'(<w:pPr>(?:(?!</w:pPr>).)*?<w:rPr>)', r'\1' + mark, par, count=1, flags=re.S)
    elif '<w:rPr/>' in par.split('</w:pPr>')[0]:
        par = par.replace('<w:rPr/>', '<w:rPr>' + mark + '</w:rPr>', 1)
    else:
        par = par.replace('</w:pPr>', '<w:rPr>' + mark + '</w:rPr></w:pPr>', 1)
    return par


ctx_index = {}
for e in edits:
    if e.get('op') == 'delete_paragraph':
        hits = [i for i in new_xml if i in pre and not scope[i].group(0).startswith('<w:tbl>')
                and para_text(new_xml[i]).strip().startswith(e['match'])]
        if len(hits) != 1:
            report.append(f"{e['id']}: FAILED, paragraph match found {len(hits)} times")
            continue
        new_xml[hits[0]] = delete_paragraph(new_xml[hits[0]])
        report.append(f"{e['id']}: paragraph deleted (block {hits[0]})")
        continue
    if e.get('ctx'):  # locate the paragraph by its full accepted text, then require `old` once inside it
        hits = ctx_index.get(e['ctx']) or [i for i in new_xml if not scope[i].group(0).startswith('<w:tbl>')
                                           and para_text(new_xml[i]).strip() == e['ctx'].strip()]
        if len(hits) != 1:  # paragraphs with images: the exported context also holds drawing offsets
            hits = [i for i in new_xml if not scope[i].group(0).startswith('<w:tbl>')
                    and para_text(new_xml[i]).count(e['old']) == 1 and para_text(new_xml[i]).strip()
                    and para_text(new_xml[i]).strip() in e['ctx']]
        ctx_index[e['ctx']] = hits  # later edits of the same paragraph reuse the location
        if len(hits) != 1 or para_text(new_xml[hits[0]]).count(e['old']) != 1:
            report.append(f"{e['id']}: FAILED, context paragraphs {len(hits)}")
            continue
        new_xml[hits[0]] = tracked_replace(new_xml[hits[0]], e['old'], e['new'])
        report.append(f"{e['id']}: applied in block {hits[0]} (by context)")
        continue
    hits = [i for i in new_xml if i in pre and para_text(new_xml[i]).count(e['old']) == 1]
    total = sum(para_text(new_xml[i]).count(e['old']) for i in new_xml if i in pre)
    if total != 1:
        report.append(f"{e['id']}: FAILED, old text found {total} times")
        continue
    i = hits[0]
    if scope[i].group(0).startswith('<w:tbl>'):
        report.append(f"{e['id']}: FAILED, text is inside a table (handle by hand)")
        continue
    try:
        new_xml[i] = tracked_replace(new_xml[i], e['old'], e['new'])
        report.append(f"{e['id']}: applied in block {i}")
    except AssertionError as err:
        try:  # old text inside one <w:t> of a run that also holds a tab or break: keep the other children
            new_xml[i] = D.replace_in_paragraph(new_xml[i], e['old'], e['new'])
            report.append(f"{e['id']}: applied in block {i} (single-text-node path)")
        except ValueError:
            report.append(f"{e['id']}: FAILED, {err}")

out = doc[:body_start]
pos = 0
body = doc[body_start:]
for i, m in enumerate(scope):
    out += body[pos:m.start()] + new_xml[i]
    pos = m.end()
out += body[pos:]
zout = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename == 'word/document.xml':
        data = out.encode('utf-8')
    zout.writestr(it, data)
zout.close()
print('\n'.join(report))
