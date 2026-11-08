"""Build tracked-insertion WordprocessingML (author "Claude") that matches the thesis house style.

Inline markup in text: **bold**, *italic*, ^{superscript}, _{subscript}.
Every run is wrapped in <w:ins>; every paragraph mark carries <w:ins/>, and every inserted
table row carries <w:trPr><w:ins/></w:trPr>, so the whole insertion can be accepted or rejected.
"""
import itertools
import re
from xml.sax.saxutils import escape

AUTHOR = 'Claude'
DATE = '2026-10-30T12:00:00Z'
_ids = itertools.count(910001)
_docpr = itertools.count(9101)


def _attrs():
    return f'w:id="{next(_ids)}" w:author="{AUTHOR}" w:date="{DATE}"'


def _rpr(bold=False, italic=False, size=24, vert=None):
    b = '<w:b w:val="1"/><w:bCs w:val="1"/>' if bold else ''
    i = '<w:i w:val="1"/><w:iCs w:val="1"/>' if italic else ''
    v = f'<w:vertAlign w:val="{vert}"/>' if vert else ''
    return f'<w:rPr>{b}{i}<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>{v}<w:rtl w:val="0"/></w:rPr>'


def runs(text, size=24, bold=False, italic=False):
    """Inline markup -> list of <w:r> (not yet wrapped)."""
    # keep '< 0.005' on one line (no-break space after '<')
    text = text.replace('< 0', '<\u00a00')
    out = []
    for tok in re.split(r'(\*\*.+?\*\*|\*[^*]+?\*|\^\{[^}]*\}|_\{[^}]*\})', text):
        if not tok:
            continue
        b, i, v = bold, italic, None
        if tok.startswith('**'):
            tok, b = tok[2:-2], True
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 1:
            tok, i = tok[1:-1], True
        elif tok.startswith('^{'):
            tok, v = tok[2:-1], 'superscript'
        elif tok.startswith('_{'):
            tok, v = tok[2:-1], 'subscript'
        out.append(f'<w:r>{_rpr(b, i, size, v)}<w:t xml:space="preserve">{escape(tok)}</w:t></w:r>')
    return out


def ins(run_xml):
    return f'<w:ins {_attrs()}>{"".join(run_xml)}</w:ins>'


def _p(ppr_inner, run_xml, size=24, page_break_after=False):
    mark = f'<w:rPr><w:ins {_attrs()}/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
    body = ins(run_xml) if run_xml else ''
    if page_break_after:
        body += ins(['<w:r><w:br w:type="page"/></w:r>'])
    return f'<w:p><w:pPr>{ppr_inner}{mark}</w:pPr>{body}</w:p>'


# ---- paragraph kinds (house style taken from blocks 317, 612, 613, 614, 245) ----
def heading1(text):
    return _p('<w:pStyle w:val="Heading1"/><w:spacing w:after="0" w:line="480" w:lineRule="auto"/><w:jc w:val="center"/>',
              runs(text))


def heading2(text):
    return _p('<w:pStyle w:val="Heading2"/><w:spacing w:before="200" w:line="480" w:lineRule="auto"/><w:ind w:left="0" w:firstLine="0"/>',
              runs(text))


def subhead(text):
    """Bold run-in subsection title, like 'Model Evaluation' (block 613)."""
    return _p('<w:keepNext w:val="1"/><w:spacing w:before="200" w:line="480" w:lineRule="auto"/><w:ind w:left="0" w:firstLine="0"/><w:jc w:val="both"/>',
              runs(text, bold=True))


def body(text, page_break_after=False):
    return _p('<w:spacing w:line="480" w:lineRule="auto"/><w:ind w:firstLine="720"/><w:jc w:val="both"/>',
              runs(text), page_break_after=page_break_after)


def bullet_like(text):
    """Indented paragraph (no numbering part needed)."""
    return _p('<w:spacing w:line="480" w:lineRule="auto"/><w:ind w:left="720" w:hanging="360"/><w:jc w:val="both"/>',
              runs(text))


def caption(label, title, above=False):
    """'Figure 4.1.' bold italic + title italic, centered, Heading4 (as block 245)."""
    after = '0' if above else '200'
    before = '240' if above else '0'
    r = runs(label + ' ', bold=True, italic=True) + runs(title, italic=True)
    return _p(f'<w:pStyle w:val="Heading4"/><w:keepNext w:val="{1 if above else 0}"/><w:spacing w:before="{before}" w:after="{after}" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>',
              r)


def note(text):
    return _p('<w:spacing w:before="60" w:after="240" w:line="240" w:lineRule="auto"/><w:ind w:left="0" w:firstLine="0"/><w:jc w:val="both"/>',
              runs(text, size=20), size=20)


def image(rid, cx_emu, cy_emu, name):
    n = next(_docpr)
    drawing = (
        f'<w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
        f'<wp:extent cx="{cx_emu}" cy="{cy_emu}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        f'<wp:docPr id="{n}" name="{escape(name)}"/>'
        f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
        f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        f'<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:nvPicPr><pic:cNvPr id="{n}" name="{escape(name)}"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx_emu}" cy="{cy_emu}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
        f'</wp:inline></w:drawing></w:r>')
    return _p('<w:keepNext w:val="1"/><w:spacing w:before="240" w:after="60" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>',
              [drawing])


def table(rows, widths_twips, header_rows=1, size=18, align=None, bold_cells=(), keep=None):
    """rows: list of lists of cell text (inline markup allowed). APA-style horizontal rules.
    align: per-column 'left'|'center'|'right'. bold_cells: set of (r, c) to bold."""
    total = sum(widths_twips)
    keep = len(rows) <= 16 if keep is None else keep
    kn = '<w:keepNext w:val="1"/>'
    align = align or (['left'] + ['center'] * (len(widths_twips) - 1))
    line = '<w:{0} w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
    tblpr = (f'<w:tblPr><w:tblW w:w="{total}" w:type="dxa"/><w:jc w:val="center"/>'
             f'<w:tblBorders>{line.format("top")}{line.format("bottom")}</w:tblBorders>'
             f'<w:tblLayout w:type="fixed"/>'
             f'<w:tblCellMar><w:top w:w="29" w:type="dxa"/><w:left w:w="72" w:type="dxa"/>'
             f'<w:bottom w:w="29" w:type="dxa"/><w:right w:w="72" w:type="dxa"/></w:tblCellMar>'
             f'<w:tblLook w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="1" w:noVBand="1"/></w:tblPr>')
    grid = '<w:tblGrid>' + ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths_twips) + '</w:tblGrid>'
    out = [f'<w:tbl>{tblpr}{grid}']
    for r_i, row in enumerate(rows):
        hdr = r_i < header_rows
        trpr = '<w:trPr><w:cantSplit/>' + ('<w:tblHeader/>' if hdr else '') + f'<w:ins {_attrs()}/></w:trPr>'
        if not hdr and row and row[0] == '__SPAN__':
            mark = f'<w:rPr><w:ins {_attrs()}/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
            para = (f'<w:p><w:pPr>{kn}<w:spacing w:before="40" w:after="0" w:line="240" w:lineRule="auto"/>'
                    f'<w:ind w:left="0" w:firstLine="0"/><w:jc w:val="left"/>{mark}</w:pPr>'
                    f'{ins(runs(str(row[1]), size=size, italic=True))}</w:p>')
            tcpr = f'<w:tcPr><w:tcW w:w="{total}" w:type="dxa"/><w:gridSpan w:val="{len(widths_twips)}"/><w:vAlign w:val="center"/></w:tcPr>'
            out.append(f'<w:tr>{trpr}<w:tc>{tcpr}{para}</w:tc></w:tr>')
            continue
        cells = []
        for c_i, (txt, w) in enumerate(zip(row, widths_twips)):
            borders = ''
            if r_i == header_rows - 1:
                borders = f'<w:tcBorders>{line.format("bottom")}</w:tcBorders>'
            tcpr = f'<w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{borders}<w:vAlign w:val="center"/></w:tcPr>'
            jc = align[c_i] if not hdr else ('left' if c_i == 0 else 'center')
            b = hdr or (r_i, c_i) in bold_cells
            mark = f'<w:rPr><w:ins {_attrs()}/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
            para = (f'<w:p><w:pPr>{kn if (keep or hdr) else ""}<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
                    f'<w:ind w:left="0" w:firstLine="0"/><w:jc w:val="{jc}"/>{mark}</w:pPr>'
                    f'{ins(runs(str(txt), size=size, bold=b)) if str(txt) else ""}</w:p>')
            cells.append(f'<w:tc>{tcpr}{para}</w:tc>')
        out.append(f'<w:tr>{trpr}{"".join(cells)}</w:tr>')
    out.append('</w:tbl>')
    return ''.join(out)


_RUN = re.compile(r'<w:r(?: [^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)?((?:(?!</w:r>).)*)</w:r>', re.S)
_T = re.compile(r'<w:t(?: [^>]*)?>([^<]*)</w:t>')


def _locate(par_xml, needle):
    """First run whose <w:t> contains `needle`: (run match, rPr, content-before-t, t text, content-after-t)."""
    for rm in _RUN.finditer(par_xml):
        content = rm.group(2)
        for tm in _T.finditer(content):
            if escape(needle) in tm.group(1):
                return rm, rm.group(1) or '', content[:tm.start()], tm.group(1), content[tm.end():]
    raise ValueError('text not found in a single <w:t>: ' + needle[:80])


def _split(par_xml, needle, old, new):
    rm, rpr, pre, txt, post = _locate(par_xml, needle)
    k = txt.index(escape(needle)) + (len(escape(needle)) if not old else 0)
    if old:
        k = txt.index(escape(old))
    before, after = txt[:k], txt[k + len(escape(old)):]
    t = lambda v: f'<w:t xml:space="preserve">{v}</w:t>' if v else ''
    parts = []
    if pre or before:
        parts.append(f'<w:r>{rpr}{pre}{t(before)}</w:r>')
    if old:
        parts.append(f'<w:del {_attrs()}><w:r>{rpr}<w:delText xml:space="preserve">{escape(old)}</w:delText></w:r></w:del>')
    if new:
        parts.append(f'<w:ins {_attrs()}><w:r>{rpr}<w:t xml:space="preserve">{escape(new)}</w:t></w:r></w:ins>')
    if after or post:
        parts.append(f'<w:r>{rpr}{t(after)}{post}</w:r>')
    return par_xml[:rm.start()] + ''.join(parts) + par_xml[rm.end():]


def replace_in_paragraph(par_xml, old, new):
    """Tracked replacement of `old` (inside one <w:t>) by `new`, keeping the run's rPr and other children."""
    return _split(par_xml, old, old, new)


def insert_text(par_xml, anchor, new):
    """Tracked insertion of `new` right after `anchor` (inside one <w:t>)."""
    return _split(par_xml, anchor, '', new)


def delete_paragraph(par):
    """Tracked deletion of a whole paragraph (runs and paragraph mark)."""
    runs = [m for m in re.finditer(r'<w:r(?: [^>]*)?>.*?</w:r>', par, flags=re.S)]
    for m in reversed(runs):
        r = re.sub(r'<w:t((?: [^>]*)?)>', r'<w:delText\1>', m.group(0)).replace('</w:t>', '</w:delText>')
        par = par[:m.start()] + f'<w:del {_attrs()}>{r}</w:del>' + par[m.end():]
    mark = f'<w:del {_attrs()}/>'
    head = par.split('</w:pPr>')[0]
    if '<w:pPr>' not in par:
        return re.sub(r'^(<w:p(?: [^>]*)?>)', r'\1<w:pPr><w:rPr>' + mark + '</w:rPr></w:pPr>', par)
    if '<w:rPr/>' in head:
        return par.replace('<w:rPr/>', '<w:rPr>' + mark + '</w:rPr>', 1)
    if re.search(r'<w:rPr>', head):
        return re.sub(r'(<w:pPr>(?:(?!</w:pPr>).)*?<w:rPr>)', r'\1' + mark, par, count=1, flags=re.S)
    return par.replace('</w:pPr>', '<w:rPr>' + mark + '</w:rPr></w:pPr>', 1)


# ---- tracked page-number and paragraph-format changes for existing paragraphs ----
_RUNX = re.compile(r'<w:r(?: [^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>|<w:rPr/>)?((?:(?!</w:r>).)*)</w:r>', re.S)


def set_trailing_number(par, new):
    """Replace the text after the last tab of a list entry (its page number) with `new`, as a tracked change."""
    dels = [(m.start(), m.end()) for m in re.finditer(r'<w:del (?:(?!/>)[^>])*>.*?</w:del>', par, flags=re.S)]
    runs = [m for m in _RUNX.finditer(par) if not any(a <= m.start() < b for a, b in dels)]
    tab_i = max((k for k, m in enumerate(runs) if '<w:tab/>' in m.group(2)), default=None)
    if tab_i is None:
        return par
    pieces = []  # (match, kind) from the end
    edits = []
    m = runs[tab_i]
    rpr = m.group(1) or ''
    content = m.group(2)
    k = content.rindex('<w:tab/>') + len('<w:tab/>')
    old_txt = ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', content[k:]))
    for mm in runs[tab_i + 1:]:
        if re.search(r'<w:(?:fldChar|instrText)', mm.group(2)):
            continue
        old_txt += ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', mm.group(2)))
    if old_txt.strip() == str(new):
        return par
    ins_run = f'<w:ins {_attrs()}><w:r>{rpr}<w:t xml:space="preserve">{escape(str(new))}</w:t></w:r></w:ins>'
    out = par
    # later runs first (offsets stay valid)
    last_piece_end = None
    for mm in reversed(runs[tab_i + 1:]):
        if re.search(r'<w:(?:fldChar|instrText)', mm.group(2)) or not re.search(r'<w:t[ >]', mm.group(2)):
            continue
        r = re.sub(r'<w:t((?: [^>]*)?)>', r'<w:delText\1>', mm.group(0)).replace('</w:t>', '</w:delText>')
        rep = f'<w:del {_attrs()}>{r}</w:del>'
        if last_piece_end is None:
            rep += ins_run
            last_piece_end = True
        out = out[:mm.start()] + rep + out[mm.end():]
    after = content[k:]
    head = f'<w:r>{rpr}{content[:k]}</w:r>'
    tail = ''
    if re.search(r'<w:t[ >]', after):
        tail = f'<w:del {_attrs()}><w:r>{rpr}' + re.sub(r'<w:t((?: [^>]*)?)>', r'<w:delText\1>', after).replace('</w:t>', '</w:delText>') + '</w:r></w:del>'
    if last_piece_end is None:
        tail += ins_run
    return out[:m.start()] + head + tail + out[m.end():]


def _ppr_inner(par):
    m = re.search(r'<w:pPr>(.*?)</w:pPr>', par, flags=re.S)
    return m.group(1) if m else ''


def change_ppr(par, transform):
    """Tracked paragraph-property change: transform(old pPr inner without rPr) -> new pPr inner."""
    inner = _ppr_inner(par)
    rpr = re.search(r'<w:rPr>.*?</w:rPr>|<w:rPr/>', inner, flags=re.S)
    rpr = rpr.group(0) if rpr else ''
    base = re.sub(r'<w:rPr>.*?</w:rPr>|<w:rPr/>', '', inner, flags=re.S)
    new_base = transform(base)
    if new_base == base:
        return par
    change = f'<w:pPrChange {_attrs()}><w:pPr>{base}</w:pPr></w:pPrChange>'
    new_ppr = f'<w:pPr>{new_base}{rpr}{change}</w:pPr>'
    if '<w:pPr>' in par:
        return re.sub(r'<w:pPr>.*?</w:pPr>', lambda _: new_ppr, par, count=1, flags=re.S)
    return re.sub(r'^(<w:p(?: [^>]*)?>)', lambda mm: mm.group(1) + new_ppr, par, count=1)


def to_normal(base):
    return re.sub(r'<w:pStyle w:val="[^"]+"/>', '', base)


def to_center(base):
    if '<w:jc ' in base:
        return re.sub(r'<w:jc w:val="[^"]+"/>', '<w:jc w:val="center"/>', base)
    # jc goes after spacing/ind and before textDirection/outlineLvl: insert before those or at the end
    m = re.search(r'<w:(?:textDirection|textAlignment|textboxTightWrap|outlineLvl|divId|cnfStyle)\b', base)
    return base[:m.start()] + '<w:jc w:val="center"/>' + base[m.start():] if m else base + '<w:jc w:val="center"/>'
