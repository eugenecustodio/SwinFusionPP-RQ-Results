"""Accepted-view export of build_out.docx to markdown for review (deletions dropped, insertions kept)."""
import re, sys, zipfile
x = zipfile.ZipFile(sys.argv[1]).read('word/document.xml').decode()
x = re.sub(r'<w:del [^>]*>.*?</w:del>', '', x, flags=re.S)
body = x[x.index('<w:body>'):]
out = []
for m in re.finditer(r'<w:tbl>.*?</w:tbl>|<w:p[ >].*?</w:p>', body, flags=re.S):
    b = m.group(0)
    if b.startswith('<w:tbl>'):
        ins = 'w:author="Claude"' in b
        rows = re.findall(r'<w:tr>.*?</w:tr>', b, flags=re.S)
        for k, r in enumerate(rows):
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<w:tc>.*?</w:tc>', r, flags=re.S)]
            out.append(('[NEW] ' if ins else '') + '| ' + ' | '.join(cells) + ' |')
            if k == 0 and ins:
                out.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
        continue
    st = re.search(r'<w:pStyle w:val="([^"]+)"', b)
    t = re.sub(r'<[^>]+>', '', b)
    new = 'w:author="Claude"' in b
    img = '[IMAGE] ' if '<w:drawing' in b else ''
    pre = {'Heading1': '# ', 'Heading2': '## ', 'Heading4': '#### '}.get(st.group(1) if st else '', '')
    out.append(('[NEW] ' if new else '') + pre + img + t)
open(sys.argv[2], 'w').write('\n'.join(out))
