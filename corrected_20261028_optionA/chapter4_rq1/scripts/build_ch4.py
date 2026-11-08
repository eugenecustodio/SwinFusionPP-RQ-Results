"""Assemble Chapter 4 (opening + RQ1), the Chapter 3 statistics amendments, two references, the
appendix-figure relabeling and the supplementary appendix into the ONE thesis .docx as tracked changes.

Usage: python build_ch4.py <in.docx> <out.docx>
Content comes from ch4_content.py (same folder). Nothing is written next to the thesis file.
"""
import html
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import docx_ins as D          # noqa: E402
import ch4_content as C       # noqa: E402

src, dst = sys.argv[1:3]
zin = zipfile.ZipFile(src)
doc = zin.read('word/document.xml').decode('utf-8')
rels = zin.read('word/_rels/document.xml.rels').decode('utf-8')

head, body_start = doc[:doc.index('<w:body>') + len('<w:body>')], doc.index('<w:body>') + len('<w:body>')
body = doc[body_start:]
sect_at = body.rindex('<w:sectPr')
# Paragraphs and tables, numbered as in manuscript_text.txt. Wrapper markup between them (the TOC <w:sdt>)
# is kept verbatim as a prefix of the next block, so ''.join(blocks) reproduces the body exactly.
blocks, pos = [], 0
for m in re.finditer(r'<w:tbl>.*?</w:tbl>|<w:p[ >].*?</w:p>|<w:p/>', body[:sect_at], flags=re.S):
    blocks.append(body[pos:m.start()] + m.group(0))
    pos = m.end()
trailer = body[pos:sect_at]
assert ''.join(blocks) + trailer == body[:sect_at], 'block split does not cover the body exactly'
text = [re.sub(r'<[^>]+>', '', re.sub(r'^(?:(?!<w:p[ >]|<w:tbl>).)*', '', b, flags=re.S)) for b in blocks]


def find(pred, what):
    hits = [i for i, t in enumerate(text) if pred(t)]
    assert len(hits) == 1, (what, hits)
    return hits[0]


# ---- anchors (by content, not by position) ----
i_refs = find(lambda t: t == 'REFERENCES', 'REFERENCES heading')
i_ch3_last = i_refs - 1
assert text[i_ch3_last].startswith('Open‑ended comments are analyzed'), text[i_ch3_last][:60]
i_617 = find(lambda t: t.startswith('Calibration will use the previously frozen source-validation temperature'), 'block 617')
assert text[i_617 + 1] == 'End-User Survey', text[i_617 + 1]
i_lof = find(lambda t: t == 'LIST OF FIGURES', 'List of Figures')
i_appx = find(lambda t: t == 'APPENDICES', 'APPENDICES heading')
i_bach = find(lambda t: t.startswith('Bachlechner, T.'), 'Bachlechner ref')
i_ho = find(lambda t: t.startswith('Ho, J., Jain, A.'), 'Ho ref')
i_cubuk = find(lambda t: t.startswith('Cubuk, E. D.'), 'Cubuk ref')
i_li_y = find(lambda t: t.startswith('Li, Y., Chang, M.-C.'), 'first Li, Y. ref')

# ---- media and relationships ----
media = {}
for n, (name, path, cx, cy) in enumerate(C.IMAGES, start=9001):
    rid = f'rId{n}'
    assert f'Id="{rid}"' not in rels
    rels = rels.replace('</Relationships>',
                        f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{name}"/></Relationships>')
    media[name] = (rid, path, cx, cy)

# ---- edits to existing blocks ----
new = list(blocks)
new[i_617] = new[i_617] + C.amendments_paragraph()          # end of 'Model Evaluation', before 'End-User Survey'
assert text[i_bach + 1] == '' and text[i_ho + 1] == ''        # each entry is followed by an empty spacer
ref_slots = {}                                                  # block index -> [entry texts]; sorted below
ref_slots.setdefault(i_bach + 1, []).append(C.REFS['bandos'])   # Bachlechner < Bandos < Bartlett
ref_slots.setdefault(i_ho + 1, []).append(C.REFS['holm'])       # Ho < Holm < House Bill
if getattr(C, 'CITE_PRELIMINARY', False):
    assert text[i_cubuk + 1] == ''
    ref_slots.setdefault(i_cubuk + 1, []).append(C.REFS['custodio'])  # Cubuk < Custodio < D'Amico
    assert text[i_li_y - 1] == ''
    ref_slots.setdefault(i_li_y - 1, []).append(C.REFS['smil'])        # Li, X. < Li, Y.
for anchor, entry in C.extra_refs():            # extra references, each after the spacer of its anchor entry
    if anchor == 'START':
        ref_slots.setdefault(i_refs, []).append(entry)  # directly after the REFERENCES heading
        continue
    hits = [i for i, tx in enumerate(text) if i_refs < i < i_appx and html.unescape(tx).strip()[:60] == html.unescape(anchor)[:60]]
    assert len(hits) == 1, (anchor[:60], hits)
    assert text[hits[0] + 1] == '', anchor
    ref_slots.setdefault(hits[0] + 1, []).append(entry)
i_guera = find(lambda t: t.startswith('Güera, D.'), 'Güera ref')       # APA order: Guarnera < Güera < Guo
i_guarnera = find(lambda t: t.startswith('Guarnera, L.'), 'Guarnera ref')
assert text[i_guera + 1] == '' and text[i_guarnera + 1] == ''
ref_slots.setdefault(i_guarnera + 1, []).append(html.unescape(text[i_guera]).strip())
new[i_guera] = D.delete_paragraph(new[i_guera])
new[i_guera + 1] = D.delete_paragraph(new[i_guera + 1])
for slot, entries in ref_slots.items():
    for entry in sorted(entries, key=str.casefold):
        new[slot] = new[slot] + C.ref_paragraph(entry)
# front matter: List of Figures entries, List of Tables, front-matter list line
lof_rng = range(i_lof + 1, i_lof + 80)
i_fig10 = next(i for i in lof_rng if text[i].startswith('Figure 10. No. of Distributed Questionnaires'))
i_fig58 = next(i for i in lof_rng if text[i].startswith('Figure 58. CERC Result - Page 4'))
i_lof_break = next(i for i in range(i_fig58 + 1, i_fig58 + 10) if 'w:type="page"' in blocks[i])
i_front_lof = next(i for i in range(0, i_lof) if text[i].startswith('List of Figures'))
new[i_fig10] = new[i_fig10] + C.lof_after_fig10(blocks[i_fig10])
new[i_fig58] = new[i_fig58] + C.lof_after_last(blocks[i_fig58])
new[i_lof_break - 1] = new[i_lof_break - 1] + C.list_of_tables(blocks[i_lof], blocks[i_lof + 1], blocks[i_lof + 2], blocks[i_fig10])
new[i_front_lof] = new[i_front_lof] + C._num_entry(blocks[i_front_lof - 1], 'List of Tables', C._pg('front', 'List of Tables'))
new[i_ch3_last] = new[i_ch3_last] + C.chapter4(media)       # Chapter 4 between Chapter 3 and REFERENCES
for i in range(len(new)):
    in_scope = (i_lof < i < i_lof + 80) or (i > i_appx)
    new[i] = C.relabel_appendix_figures(new[i], i, text[i], in_scope)
# ---- formatting: empty headings -> Normal; REFERENCES/APPENDICES centered; appendix caption labels ----
for i, b in enumerate(blocks):
    if re.search(r'<w:pStyle w:val="Heading\d"/>', b) and not text[i].strip() and not b.startswith('<w:tbl>'):
        new[i] = D.change_ppr(new[i], D.to_normal)
new[i_refs] = D.change_ppr(new[i_refs], D.to_center)
new[i_appx] = D.change_ppr(new[i_appx], D.to_center)
LABEL_FMT = '<w:b w:val="1"/><w:bCs w:val="1"/><w:i w:val="1"/><w:iCs w:val="1"/>'


def _fmt_caption(par):
    acc = re.sub(r'<[^>]+>', '', re.sub(r'<w:del (?:(?!/>)[^>])*>.*?</w:del>', '', par, flags=re.S)).strip()
    if re.match(r'Figure [D-F]\d+\.', acc):
        par = D.change_ppr(par, D.to_center)
    if re.match(r'Figure [C-F]\d+\.', acc):
        def bold(m):
            inner = re.sub(r'<w:(?:b|bCs|i|iCs)(?: [^>]*)?/>', '', m.group(2) or '')
            lead = re.match(r'(?:<w:rStyle [^>]*/>|<w:rFonts [^>]*/>)*', inner).group(0)
            return f'{m.group(1)}<w:rPr>{lead}{LABEL_FMT}{inner[len(lead):]}</w:rPr><w:t xml:space="preserve">{m.group(3)}</w:t>'
        par = re.sub(r'(<w:ins [^>]*><w:r>)(?:<w:rPr>((?:(?!</w:rPr>).)*)</w:rPr>)?<w:t xml:space="preserve">(Figure [C-F]\d+(?:\.)?)</w:t>',
                     bold, par, count=1, flags=re.S)
    return par


for i in range(i_appx + 1, len(new)):
    new[i] = re.sub(r'<w:p[ >](?:(?!<w:p[ >]).)*?</w:p>', lambda m: _fmt_caption(m.group(0)), new[i], flags=re.S)

# ---- TOC, List of Figures and front-matter page numbers (from the render) ----
pm = C.page_map()
i_tocfield = next(i for i in range(0, i_lof) if 'TOC \\h' in text[i])
i_toc_stat = next(i for i in range(i_tocfield, i_lof) if text[i].startswith('Statistical Treatment of Data'))
i_toc_meth = next(i for i in range(i_tocfield, i_lof) if text[i].startswith('METHODOLOGY'))
i_toc_f = next(i for i in range(i_tocfield, i_lof) if text[i].startswith('APPENDIX F:'))
i_toc_g = next(i for i in range(i_tocfield, i_lof) if text[i].startswith('APPENDIX G:'))
lit = next(i for i in range(i_tocfield, i_lof) if text[i].startswith('Review of Related Literatures'))
new[lit] = D.replace_in_paragraph(new[lit], 'Review of Related Literatures', 'Review of Related Literature')
def num(sec, key):
    """Page number for a list entry; tolerates keys whose trailing number-like word was stripped."""
    d = (pm or {}).get(sec, {})
    if d.get(key):
        return str(d[key])
    near = [k for k in d if key.startswith(k) and len(k) >= 0.8 * len(key) and d[k]]
    return str(d[max(near, key=len)]) if near else ''
new[i_toc_stat] = new[i_toc_stat] + ''.join(
    C._num_entry(blocks[i_toc_meth if k == 0 else i_toc_stat], title, num('toc', title)) for k, title in enumerate(C.TOC_CH4))
new[i_toc_g] = new[i_toc_g] + ''.join(C._num_entry(blocks[i_toc_f], title, num('toc', title)) for title in C.TOC_APPX)
def _first_only(xml, fn):
    """Apply fn to the block's own paragraph only, not to entries appended after it."""
    first_par, cut, rest = xml.partition('</w:p>')
    return fn(first_par + cut) + rest


if pm:
    for i in range(0, i_tocfield):  # the front-matter lines sit above the TOC field
        title = re.sub(r'\s*[ivxlc\d]+$', '', html.unescape(text[i])).strip()
        if title in pm['front'] and title != 'List of Tables':
            new[i] = _first_only(new[i], lambda x, n=pm['front'][title]: D.set_trailing_number(x, n))
    for i in range(i_tocfield, i_lof):
        title = re.sub(r'\s*[ivxlc\d]+$', '', html.unescape(text[i])).strip().replace('Literatures', 'Literature')
        if title in pm['toc'] and pm['toc'][title]:
            new[i] = _first_only(new[i], lambda x, n=pm['toc'][title]: D.set_trailing_number(x, n))
        elif title in pm['front'] and title != 'List of Tables':
            new[i] = _first_only(new[i], lambda x, n=pm['front'][title]: D.set_trailing_number(x, n))
    last_label = None
    for i in range(i_lof + 1, i_lof + 80):
        m = re.match(r'Figure (\d+)\.', text[i])
        if m:
            n = int(m.group(1))
            last_label = f'Figure {C.RELABEL.get(n, n)}.'
        if last_label and '<w:tab/>' in blocks[i] and pm['fig'].get(last_label):
            new[i] = _first_only(new[i], lambda x, n=pm['fig'][last_label]: D.set_trailing_number(x, n))
# ---- the dotted right tab of the TOC and lists sat at 12000 twips, beyond the 8640-twip text width; move it ----
TAB_OLD, TAB_NEW = 'w:pos="12000"', 'w:pos="8640"'
for i in range(0, i_lof + 80):
    if TAB_OLD in blocks[i]:
        new[i] = D.change_ppr(new[i], lambda base: base.replace(TAB_OLD, TAB_NEW))
        # paragraphs inserted after this block (new entries copied from it) carry the old stop: fix them directly
        first_par, cut, rest = new[i].partition('</w:p>')
        new[i] = first_par + cut + rest.replace(TAB_OLD, TAB_NEW)
tail = C.appendix_supplement(media)                           # new last appendix, before sectPr

out_doc = head + ''.join(new) + trailer + tail + body[sect_at:]

zout = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename == 'word/document.xml':
        data = out_doc.encode('utf-8')
    elif it.filename == 'word/_rels/document.xml.rels':
        data = rels.encode('utf-8')
    zout.writestr(it, data)
for name, (rid, path, cx, cy) in media.items():
    zout.writestr(f'word/media/{name}', Path(path).read_bytes())
zout.close()
print('written', dst)
