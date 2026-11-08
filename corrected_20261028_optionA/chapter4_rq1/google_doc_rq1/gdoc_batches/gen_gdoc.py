"""Generate Google Docs batchUpdate requests that put Chapter 4 RQ1 and Appendix J into the CURRENT DRAFT tab.

Usage: python gen_gdoc.py <read_doc.json> <rq1_text.py> <tables_dir> <out_dir> [--only A,B,C,J] [--subset]
All positions come from the read_doc JSON (a trimmed copy of the thesis doc). Anchors are found by text.
Every unit is inserted at a fixed anchor index X in reverse document order, so each unit's positions are
known relative to X. Operations run from the highest anchor to the lowest.
"""
import csv, importlib.util, json, re, sys
from pathlib import Path

TAB = 't.l5c18frq5wuo'
doc = json.load(open(sys.argv[1]))
if 'content' in doc: doc = doc['content']
spec = importlib.util.spec_from_file_location('rq1', sys.argv[2]); T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
TBL = Path(sys.argv[3]); OUT = Path(sys.argv[4]); OUT.mkdir(parents=True, exist_ok=True)
ONLY = set(sys.argv[sys.argv.index('--only') + 1].split(',')) if '--only' in sys.argv else {'A', 'B', 'C', 'J'}
SUBSET = '--subset' in sys.argv

tab = [t for t in doc['tabs'] if t['tabProperties']['tabId'] == TAB][0]
body = tab['documentTab']['body']['content']
s = json.dumps(tab)
assert 'suggestedInsertionIds' not in s and 'suggestedDeletionIds' not in s, 'tab has pending suggestions'


def u16(t): return len(t.encode('utf-16-le')) // 2


def ptext(el): return ''.join(e.get('textRun', {}).get('content', '') for e in el['paragraph']['elements'])


paras = [el for el in body if 'paragraph' in el]


def find_para(prefix, after=0, exact=False):
    for el in paras:
        if el['startIndex'] >= after:
            t = ptext(el).rstrip('\n').strip()
            if (t == prefix) if exact else t.startswith(prefix):
                return el
    raise SystemExit(f'anchor not found: {prefix!r}')


def nxt(el):
    i = body.index(el); n = body[i + 1]; assert 'paragraph' in n, 'expected paragraph after anchor'; return n


H_A = find_para('RQ1: SwinFusion++ Compared with')
L_A = nxt(H_A); assert ptext(L_A).startswith('Lorem ipsum')
H_B = nxt(L_A); assert ptext(H_B).strip() == 'Within-Dataset Performance'
L_B = nxt(H_B); assert ptext(L_B).startswith('Lorem ipsum')
PH1 = nxt(L_B); assert ptext(PH1).strip() == '[THEN TABLES, IF MERON, ETO FORMAT]'
PH2 = nxt(PH1); assert ptext(PH2).strip() == 'Table X. Lorem ipsum dolor sit amet.'
H_C = nxt(PH2); assert ptext(H_C).strip() == 'Discussion of RQ1'
L_C = nxt(H_C); assert ptext(L_C).strip().startswith('Lorem ipsum')
RQ2 = nxt(L_C); assert ptext(RQ2).strip().startswith('[THEN RQ2')
APX_I = find_para('APPENDIX I', exact=True)
H_J = nxt(APX_I); assert ptext(H_J).strip() == 'Turnitin Results - AI Report'
assert body.index(H_J) == len(body) - 1, 'Appendix I title is not the last paragraph of the tab'
for el in (H_A, L_A, H_B, L_B, PH1, PH2, H_C, L_C, H_J):
    assert all('textRun' in e for e in el['paragraph']['elements']), 'non-text element in anchor paragraph'

loc = lambda i: {'index': i, 'tabId': TAB}
rng = lambda a, b: {'startIndex': a, 'endIndex': b, 'tabId': TAB}
PT = lambda v: {'magnitude': v, 'unit': 'PT'}
TEXT_FIELDS = 'bold,italic,underline,backgroundColor,fontSize'
PARA_FIELDS = 'namedStyleType,alignment,lineSpacing,indentFirstLine,spaceAbove,spaceBelow,keepWithNext'


def pstyle(a, b, named='NORMAL_TEXT', align='JUSTIFIED', line=200, first=0, above=0, below=0, kwn=False, pbb=None):
    st = {'namedStyleType': named, 'alignment': align, 'lineSpacing': line, 'indentFirstLine': PT(first),
          'spaceAbove': PT(above), 'spaceBelow': PT(below), 'keepWithNext': kwn}
    f = PARA_FIELDS
    if pbb is not None:
        st['pageBreakBefore'] = pbb; f += ',pageBreakBefore'
    return {'updateParagraphStyle': {'range': rng(a, b), 'paragraphStyle': st, 'fields': f}}


def tstyle(a, b, size=12, bold=None, italic=None):
    st = {}
    if size: st['fontSize'] = PT(size)
    if bold is not None: st['bold'] = bold
    if italic is not None: st['italic'] = italic
    return {'updateTextStyle': {'range': rng(a, b), 'textStyle': st, 'fields': TEXT_FIELDS}}


def flag(a, b, **kw):
    return {'updateTextStyle': {'range': rng(a, b), 'textStyle': kw, 'fields': ','.join(kw)}}


def strip_italics(t):
    out, spans, pos = [], [], 0
    for part in re.split(r'(\*[^*]+\*)', t):
        if not part: continue
        if part.startswith('*') and part.endswith('*') and len(part) > 2:
            inner = part[1:-1]; spans.append((pos, pos + u16(inner))); out.append(inner); pos += u16(inner)
        else:
            out.append(part); pos += u16(part)
    return ''.join(out), spans


# ---------- units: each returns requests that insert it at X (the newline of the paragraph before it) ----------
def u_body(X, text, kind='p'):
    t, ital = strip_italics(text); n = u16(t)
    r = [{'insertText': {'location': loc(X), 'text': '\n' + t}}]
    a, b = X + 1, X + 2 + n
    # text styles never span the paragraph's final newline, which may be an original (non-suggested) character;
    # that newline is styled by a separate request so each style suggestion covers one kind of text only
    if kind == 'p':
        r += [pstyle(a, b, first=36), tstyle(a, b - 1), tstyle(b - 1, b)]
    elif kind == 'sub':
        r += [pstyle(a, b, kwn=True), tstyle(a, b - 1, bold=True), tstyle(b - 1, b, bold=True)]
    elif kind == 'apxhead':
        r += [pstyle(a, b, named='HEADING_4', align='CENTER', line=115, below=10, pbb=True), tstyle(a, b - 1, size=None), tstyle(b - 1, b, size=None)]
    elif kind == 'apxtitle':
        r += [pstyle(a, b, align='CENTER', line=115, below=10), tstyle(a, b - 1, bold=True), tstyle(b - 1, b, bold=True)]
    for s0, s1 in ital:
        r.append(flag(a + s0, a + s1, italic=True))
    return r


def note_text(src):
    f = TBL / f'{src}_note.txt'
    if not f.exists(): return None
    t = f.read_text(encoding='utf-8').strip()
    return t if t.startswith('Note.') else 'Note. ' + t


def cap_and_note(E, label, title, note, fig=False):
    """Insert caption (+ note) into the empty paragraph at E (just before its newline)."""
    cap = f'{label} {title}'
    txt = cap + ('\n' + note if note else '')
    r = [{'insertText': {'location': loc(E), 'text': txt}}]
    c0, c1 = E, E + u16(cap) + 1
    if fig:
        r += [pstyle(c0, c1, named='HEADING_4', align='CENTER', line=200, below=10), tstyle(c0, c1, size=None, bold=False, italic=True),
              flag(c0, c0 + u16(label), bold=True)]
    else:
        r += [pstyle(c0, c1, align='CENTER', line=200, above=10, below=10), tstyle(c0, c1, italic=True),
              flag(c0, c0 + u16(label), bold=True)]
    if note:
        n0, n1 = c1, c1 + u16(note) + 1
        r += [pstyle(n0, n1, line=100, below=12), tstyle(n0, n1 - 1, size=10), tstyle(n1 - 1, n1, size=10), flag(n0, n0 + u16('Note.'), italic=True)]
    return r


def u_table(X, label, src, title):
    rows = list(csv.reader(open(TBL / f'{src}.csv', encoding='utf-8')))
    C = len(rows[0]); R = len(rows)
    grid, spans = [], []
    for ri, v in enumerate(rows):
        if v and v[0] == '__SPAN__':
            spans.append(ri); grid.append([v[1]] + [''] * (C - 1))
        else:
            v = v + [''] * (C - len(v)); assert len(v) == C, (src, ri); grid.append(v)
    size = 8 if C >= 9 else 9
    W = 2 * C + 1
    cell = lambda r_, c_: X + 4 + r_ * W + 2 * c_
    E = X + 3 + R * W
    tstart = X + 1
    r = [{'insertTable': {'rows': R, 'columns': C, 'location': loc(X)}}]
    for ri in spans:  # merge while the cells are empty
        r.append({'mergeTableCells': {'tableRange': {'tableCellLocation': {'tableStartLocation': loc(tstart), 'rowIndex': ri, 'columnIndex': 0}, 'rowSpan': 1, 'columnSpan': C}}})
    r += cap_and_note(E, f'Table {label}.', title, note_text(src))
    for ri in range(R - 1, -1, -1):
        for ci in range(C - 1, -1, -1):
            t = grid[ri][ci]
            if t: r.append({'insertText': {'location': loc(cell(ri, ci)), 'text': t}})
    # positions after filling
    lens = [sum(u16(x) for x in row) for row in grid]
    rowstart = [X + 2 + ri * W + sum(lens[:ri]) for ri in range(R)]
    tend = rowstart[-1] + W + lens[-1]  # index of the table end marker
    r.append(pstyle(X + 4, tend, align='START', line=100))
    r.append(tstyle(X + 4, tend, size=size))
    r.append({'updateParagraphStyle': {'range': rng(rowstart[0] + 2, rowstart[0] + W + lens[0]), 'paragraphStyle': {'alignment': 'CENTER'}, 'fields': 'alignment'}})
    for ri in spans:
        r.append(flag(rowstart[ri] + 2, rowstart[ri] + W + lens[ri], italic=True))
    r.append({'pinTableHeaderRows': {'tableStartLocation': loc(tstart), 'pinnedHeaderRowsCount': 1}})
    r.append({'updateTableRowStyle': {'tableStartLocation': loc(tstart), 'rowIndices': list(range(R)), 'tableRowStyle': {'preventOverflow': True}, 'fields': 'preventOverflow'}})
    return r


def u_fig(X, label, fname, title, note):
    ph = f'[Insert figure here: {fname}]'
    note = note.strip(); note = note if note.startswith('Note.') else 'Note. ' + note
    r = [{'insertText': {'location': loc(X), 'text': '\n' + ph}}]
    a, b = X + 1, X + 2 + u16(ph)
    r += [pstyle(a, b, align='CENTER', line=100, kwn=True), tstyle(a, b - 1, bold=True), flag(a, b - 1, backgroundColor={'color': {'rgbColor': {'red': 1, 'green': 1, 'blue': 0}}})]
    # the paragraph after the placeholder: insert a new empty paragraph for caption+note at its end
    r2 = [{'insertText': {'location': loc(b - 1), 'text': '\n'}}]  # splits: placeholder | empty paragraph (at b)
    r2 += cap_and_note(b, label, title, note, fig=True)
    return r + r2


def units_for(blocks):
    us = []
    for b in blocks:
        if b[0] == 'p': us.append(('p', lambda X, b=b: u_body(X, b[1])))
        elif b[0] == 'sub': us.append(('sub', lambda X, b=b: u_body(X, b[1], 'sub')))
        elif b[0] == 'table': us.append(('table ' + b[1], lambda X, b=b: u_table(X, b[1], b[2], b[3])))
        elif b[0] == 'fig': us.append(('fig ' + b[1], lambda X, b=b: u_fig(X, 'Figure X.', b[1], b[2], b[3])))
        else: raise SystemExit(b[0])
    return us


B = T.BLOCKS
iW = next(i for i, b in enumerate(B) if b[0] == 'sub' and b[1] == 'Within-Dataset Performance')
iD = next(i for i, b in enumerate(B) if b[0] == 'sub' and b[1] == 'Discussion of RQ1')
segA, segB, segC = B[:iW], B[iW + 1:iD], B[iD + 1:]
segJ_units = [('apxhead', lambda X: u_body(X, 'APPENDIX J', 'apxhead')),
              ('apxtitle', lambda X: u_body(X, 'SUPPLEMENTARY RESULTS FOR RESEARCH QUESTION 1', 'apxtitle')),
              ('p', lambda X: u_body(X, T.APPX_J_INTRO))]
J_TABLES = T.J_TABLES
if SUBSET:  # small validation run: a few blocks per segment
    segA = [b for b in segA[:5]]
    segB = [b for b in segB if b[0] == 'table' and b[2] == 'T4'] + [b for b in segB if b[0] == 'fig'][:1] + [b for b in segB if b[0] == 'sub'][:1]
    segC = segC[:1]
    J_TABLES = [j for j in J_TABLES if j[0] == 'J6']
segJ_units += [('table ' + tid, lambda X, tid=tid, ti=ti: u_table(X, tid, tid, ti)) for tid, ti in J_TABLES]
segJ_units.append(('fig J1', lambda X: u_fig(X, 'Figure J1.', *T.FIG_J1)))

ops = []  # (label, requests)


def add_segment(name, X, units):
    for lab, fn in reversed(units):
        ops.append((f'{name}:{lab}', fn(X)))


def delete(name, a, b):
    ops.append((f'del {name}', [{'deleteContentRange': {'range': rng(a, b)}}]))


endm1 = lambda el: el['endIndex'] - 1
if 'J' in ONLY: add_segment('J', endm1(H_J), segJ_units)
if 'C' in ONLY:
    delete('lorem C', L_C['startIndex'], L_C['endIndex'])
    add_segment('C', endm1(H_C), units_for(segC))
if 'B' in ONLY:
    delete('placeholders', PH1['startIndex'], PH2['endIndex'])
    delete('lorem B', L_B['startIndex'], L_B['endIndex'])
    add_segment('B', endm1(H_B), units_for(segB))
if 'A' in ONLY:
    delete('lorem A', L_A['startIndex'], L_A['endIndex'])
    add_segment('A', endm1(H_A), units_for(segA))

# chunking at unit boundaries
LIMIT = int(sys.argv[sys.argv.index('--chunk') + 1]) if '--chunk' in sys.argv else 45000
chunks, cur, curlen = [], [], 0
for lab, reqs in ops:
    sz = len(json.dumps(reqs, ensure_ascii=False))
    if cur and curlen + sz > LIMIT:
        chunks.append(cur); cur, curlen = [], 0
    cur.append((lab, reqs)); curlen += sz
if cur: chunks.append(cur)
for f in OUT.glob('chunk_*.json'): f.unlink()
manifest = []
for k, ch in enumerate(chunks, 1):
    reqs = [q for _, rs in ch for q in rs]
    p = OUT / f'chunk_{k:02d}.json'
    p.write_text('[\n' + ',\n'.join(json.dumps(q, ensure_ascii=False, separators=(',', ':')) for q in reqs) + '\n]\n', encoding='utf-8')
    manifest.append({'chunk': p.name, 'requests': len(reqs), 'bytes': p.stat().st_size, 'units': [l for l, _ in ch]})
json.dump({'revisionId': doc.get('revisionId'), 'chunks': manifest}, open(OUT / 'manifest.json', 'w'), indent=1, ensure_ascii=False)
tot = sum(m['bytes'] for m in manifest)
print(f'{len(ops)} ops, {sum(m["requests"] for m in manifest)} requests, {len(manifest)} chunks, {tot} bytes')
for m in manifest: print(m['chunk'], m['requests'], m['bytes'], m['units'][0], '...', m['units'][-1])
