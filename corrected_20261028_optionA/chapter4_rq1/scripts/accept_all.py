"""Accepted-changes copy of a .docx without LibreOffice: drop <w:del> content, unwrap <w:ins>, remove paragraphs
whose mark was deleted and whose text is gone. Usage: python accept_all.py in.docx out.docx"""
import re, sys, zipfile
src, dst = sys.argv[1:3]
z = zipfile.ZipFile(src)
x = z.read('word/document.xml').decode('utf-8')
x = re.sub(r'<w:del (?:(?!/>)[^>])*>.*?</w:del>', '', x, flags=re.S)   # deleted runs (incl. math runs); not the self-closing marks
x = re.sub(r'<w:ins (?:(?!/>)[^>])*>(.*?)</w:ins>', r'\1', x, flags=re.S)  # unwrap inserted runs
x = re.sub(r'<w:ins [^>]*/>', '', x)                                     # inserted-mark / row markers
def drop(m):
    p = m.group(0)
    if re.search(r'<w:rPr>(?:(?!</w:rPr>).)*<w:del [^>]*/>', p, flags=re.S):
        if not re.sub(r'<[^>]+>', '', p).strip() and '<w:drawing' not in p:
            return ''
        p = re.sub(r'<w:del [^>]*/>', '', p)
    return p
x = re.sub(r'<w:p[ >](?:(?!<w:p[ >]).)*?</w:p>', drop, x, flags=re.S)
x = re.sub(r'<w:del [^>]*/>', '', x)
x = re.sub(r'<w:(pPrChange|rPrChange|trPrChange|tcPrChange)\b[^>]*>.*?</w:\1>', '', x, flags=re.S)   # accept format changes too
x = re.sub(r'<m:oMath>\s*(<w:r(?: [^>]*)?>\s*</w:r>)?\s*</m:oMath>', '', x)
out = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for it in z.infolist():
    out.writestr(it, x.encode('utf-8') if it.filename == 'word/document.xml' else z.read(it.filename))
out.close()
print('tracked markup left:', len(re.findall(r'<w:(?:ins|del) ', x)))
