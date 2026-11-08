"""Preview copy for LibreOffice only: <in.docx> <out.docx>. Never applied to the manuscript. Two LibreOffice habits
would make the preview differ from Word: it may split 'SwinFusion++' between the plus signs at a line end, so a word
joiner goes between them; and it shows Heading 4 paragraphs double-spaced even when single spacing is set on the
paragraph, so those paragraphs get a derived style that says the same thing."""
import re
import sys
import zipfile

STYLE = ('<w:style w:type="paragraph" w:styleId="Heading4Single"><w:name w:val="heading 4 single"/><w:basedOn w:val="Heading4"/>'
         '<w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr></w:style>')


def single(m):
    p = m.group(0)
    head, cut, rest = p.partition('</w:pPr>')
    if '<w:pStyle w:val="Heading4"/>' in head and 'w:line="240"' in head:
        head = head.replace('<w:pStyle w:val="Heading4"/>', '<w:pStyle w:val="Heading4Single"/>')
    return head + cut + rest


src, dst = sys.argv[1:3]
zi = zipfile.ZipFile(src)
zo = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for item in zi.infolist():
    data = zi.read(item.filename)
    if item.filename == 'word/document.xml':
        xml = data.decode('utf-8')
        xml = re.sub(r'(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)', lambda m: m.group(1) + m.group(2).replace('++', '+⁠+') + m.group(3), xml)
        xml = re.sub(r'<w:p[ >](?:(?!<w:p[ >]).)*?</w:p>', single, xml, flags=re.S)
        data = xml.encode('utf-8')
    elif item.filename == 'word/styles.xml':
        data = data.decode('utf-8').replace('</w:styles>', STYLE + '</w:styles>').encode('utf-8')
    zo.writestr(item, data)
zo.close()
