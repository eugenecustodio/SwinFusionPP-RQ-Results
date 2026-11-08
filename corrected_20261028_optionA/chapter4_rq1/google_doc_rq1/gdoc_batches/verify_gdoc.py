"""Verify inserted RQ1/Appendix J content in a read_doc JSON against the CSV tables and expected styles."""
import csv, json, sys
from pathlib import Path
d = json.load(open(sys.argv[1])); TBL = Path(sys.argv[2]); TAB = 't.l5c18frq5wuo'
tab = [t for t in d['tabs'] if t['tabProperties']['tabId'] == TAB][0]['documentTab']
body = tab['body']['content']
def eff_ts(tr):
    st = dict(tr.get('textStyle', {}))
    for sid, ch in tr.get('suggestedTextStyleChanges', {}).items():
        st2 = ch['textStyle']; state = ch.get('textStyleSuggestionState', {})
        for k, v in state.items():
            if v and k.endswith('Suggested'):
                key = k[:-len('Suggested')]
                if key in st2: st[key] = st2[key]
                else: st.pop(key, None)
    return st
def eff_ps(p):
    st = dict(p.get('paragraphStyle', {}))
    for sid, ch in p.get('suggestedParagraphStyleChanges', {}).items():
        st2 = ch['paragraphStyle']; state = ch.get('paragraphStyleSuggestionState', {})
        for k, v in state.items():
            if v and k.endswith('Suggested'):
                key = k[:-len('Suggested')]
                if key in st2: st[key] = st2[key]
                else: st.pop(key, None)
    return st
def ptext(p, live=True):
    return ''.join(e['textRun']['content'] for e in p['elements'] if 'textRun' in e and not (live and e['textRun'].get('suggestedDeletionIds')))
def short(st):
    o = {}
    for k in ('namedStyleType', 'alignment', 'lineSpacing', 'pageBreakBefore', 'keepWithNext'):
        if k in st: o[k] = st[k]
    for k in ('indentFirstLine', 'spaceAbove', 'spaceBelow'):
        if k in st: o[k] = st[k].get('magnitude', 0)
    return o
def tshort(st):
    o = {k: st[k] for k in ('bold', 'italic') if k in st}
    if 'fontSize' in st: o['sz'] = st['fontSize'].get('magnitude')
    if 'backgroundColor' in st and st['backgroundColor'].get('color'): o['bg'] = 1
    return o
mode = sys.argv[3] if len(sys.argv) > 3 else 'paras'
inserted = [el for el in body if 'paragraph' in el and any(e.get('textRun', {}).get('suggestedInsertionIds') for e in el['paragraph']['elements'])]
tables = [el for el in body if 'table' in el and el['table'].get('suggestedInsertionIds')]
if mode == 'paras':
    for el in inserted:
        p = el['paragraph']; runs = [(e['textRun']['content'][:18], tshort(eff_ts(e['textRun']))) for e in p['elements'] if 'textRun' in e]
        print(el['startIndex'], repr(ptext(p)[:45]), short(eff_ps(p)), runs[:3])
# tables: compare cells to CSVs by caption that follows
idx = {id(el): i for i, el in enumerate(body)}
bad = 0
for el in tables:
    i = idx[id(el)]; cap = ptext(body[i + 1]['paragraph']); lab = cap.split('.')[0].replace('Table ', '')
    src = {'VI': 'T1', 'VII': 'T4', 'VIII': 'T5', 'IX': 'T6', 'X': 'T7', 'XI': 'T8', 'XII': 'T9'}.get(lab, lab)
    rows = list(csv.reader(open(TBL / f'{src}.csv', encoding='utf-8')))
    t = el['table']; ok = (t['rows'] == len(rows) and t['columns'] == len(rows[0]))
    for ri, (row, exp) in enumerate(zip(t['tableRows'], rows)):
        cells = row['tableCells']
        if exp[0] == '__SPAN__':
            got = [''.join(ptext(c['paragraph']) for c in cells[0]['content'])]
            want = [exp[1] + '\n']
            span = cells[0].get('tableCellStyle', {}).get('columnSpan')
            if span != len(rows[0]): ok = False; print('  span not merged', lab, ri, span)
            if len(cells[0]['content']) != 1: ok = False; print('  merged head has', len(cells[0]['content']), 'paragraphs', lab, ri)
        else:
            got = [''.join(ptext(c['paragraph']) for c in cl['content']) for cl in cells]
            want = [x + '\n' for x in exp] + ['\n'] * (len(cells) - len(exp))
        if got != want: ok = False; print('  MISMATCH', lab, ri, got[:4], want[:4])
    # style sample: header cell and a body cell
    def cst(r, c):
        p = t['tableRows'][r]['tableCells'][c]['content'][0]['paragraph']; tr = [e for e in p['elements'] if 'textRun' in e][0]['textRun']
        return short(eff_ps(p)), tshort(eff_ts(tr))
    print(f"Table {lab} ({src}) {t['rows']}x{t['columns']} cells_ok={ok} header={cst(0,0)} body={cst(len(rows)-1, 1)} pinned={t['tableRows'][0].get('tableRowStyle',{}).get('tableHeader')}")
    bad += not ok
print('tables with problems:', bad, 'of', len(tables))
