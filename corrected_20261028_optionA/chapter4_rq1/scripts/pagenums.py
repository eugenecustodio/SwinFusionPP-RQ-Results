"""Page numbers for the TOC, List of Figures, List of Tables and front-matter list, read from a rendered PDF.

Usage: python pagenums.py <rendered.pdf> <accepted.docx> <out page_map.json>
The footer page number equals the physical page (one section, numbering starts at 1), front matter included.
"""
import html
import json
import re
import subprocess
import sys
import zipfile

pdf, docx, out = sys.argv[1:4]
n_pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
pages = {}
for p in range(1, n_pages + 1):
    t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', pdf, '-'], capture_output=True, text=True).stdout
    pages[p] = [re.sub(r'\s+', ' ', l.replace('\u2060', '')).strip() for l in t.split('\n')]

x = zipfile.ZipFile(docx).read('word/document.xml').decode()
body = x[x.index('<w:body>'):]
paras = [html.unescape(re.sub(r'<[^>]+>', '', p)) for p in re.findall(r'<w:p[ >].*?</w:p>', body, flags=re.S)]
i_lof = paras.index('LIST OF FIGURES')
i_lot = paras.index('LIST OF TABLES')
toc = [p for p in paras[:i_lof] if p.strip() and not p.lstrip().startswith(('TOC', 'TITLE', 'TABLE OF CONTENTS'))]
i_title_end = next(k for k, p in enumerate(toc) if p.startswith('Title Page'))
toc_entries = [re.sub(r'\s*[ivxlc\d]+$', '', p).strip() for p in toc[i_title_end + 4:]]  # after the four front-list lines

first_body = next(p for p in range(1, n_pages + 1) if any(l.startswith('Chapter 1 –') for l in pages[p]))


def find(pred, start):
    for p in range(start, n_pages + 1):
        if any(pred(l) for l in pages[p]):
            return p
    return None


result = {'toc': {}, 'fig': {}, 'tab': {}, 'front': {}}
cur = first_body
for title in toc_entries:
    key = title.split(':')[0].strip() if title.startswith('APPENDIX') else title.replace('Literatures', 'Literature')
    pg = find(lambda l, k=key: l == k or l.endswith('– ' + k) or l == k.upper(), cur)
    if pg is None:  # headings that wrap: match the first 40 characters
        pg = find(lambda l, k=key: l.startswith(k[:40]), cur)
    result['toc'][title] = pg
    cur = pg or cur
for lab in [p.split('. ')[0] + '.' for p in paras[i_lof:i_lot] if re.match(r'Figure [A-Z]?\d+\.', p)]:
    result['fig'][lab] = (find(lambda l, k=lab: l.startswith(k + ' '), first_body)
                          or find(lambda l, k=lab: (k + ' ') in l, first_body))  # side-by-side captions in tables
prev = None
for lab in result['fig']:  # a caption whose label the PDF text separates from it: use the previous figure's page
    if result['fig'][lab] is None:
        result['fig'][lab] = prev
    prev = result['fig'][lab]
for lab in [p.split('. ')[0] + '.' for p in paras[i_lot:i_lot + 40] if re.match(r'Table J?\d+\.', p)]:
    result['tab'][lab] = find(lambda l, k=lab: l.startswith(k + ' '), first_body)


result['front'] = {'Title Page': '1',
                   'Table of Contents': str(find(lambda l: l == 'TABLE OF CONTENTS', 1)),
                   'List of Figures': str(find(lambda l: l == 'LIST OF FIGURES', 1)),
                   'List of Tables': str(find(lambda l: l == 'LIST OF TABLES', 1))}
json.dump(result, open(out, 'w'), indent=1, ensure_ascii=False)
missing = [k for sec in ('toc', 'fig', 'tab') for k, v in result[sec].items() if v is None]
print(f'pages: {n_pages}; first body page {first_body}; toc {len(result["toc"])}, figures {len(result["fig"])}, '
      f'tables {len(result["tab"])}; missing: {missing}')
