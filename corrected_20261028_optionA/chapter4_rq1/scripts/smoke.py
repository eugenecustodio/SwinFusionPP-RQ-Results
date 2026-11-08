import sys, zipfile, re
sys.path.insert(0, sys.argv[1])
import docx_ins as D
src, dst, png = sys.argv[2:5]
zin = zipfile.ZipFile(src)
ct = zin.read('[Content_Types].xml').decode()
print('png default' , 'Extension="png"' in ct)
doc = zin.read('word/document.xml').decode()
rels = zin.read('word/_rels/document.xml.rels').decode()
rels = rels.replace('</Relationships>', '<Relationship Id="rId9001" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/ch4_smoke.png"/></Relationships>')
xml = (D.heading1('Chapter 4 – RESULTS AND DISCUSSION') + D.heading2('Test section') + D.body('Body with **bold**, *italic*, p_{Holm} and ^{2}.') +
       D.caption('Table 4.1.', 'Smoke table', above=True) + D.table([['Model','AUC'],['SwinFusion++','0.9942'],['Swin-B','**0.9965**']],[3000,2000]) + D.note('*Note.* Test.') +
       D.image('rId9001', 5486400, 3086100, 'ch4_smoke.png') + D.caption('Figure 4.1.', 'Smoke figure'))
anchor = '<w:pStyle w:val="Heading1"/><w:spacing w:after="200" w:line="480" w:lineRule="auto"/><w:jc w:val="both"/><w:rPr/></w:pPr><w:bookmarkStart w:colFirst="0" w:colLast="0" w:name="_7b52zlp545kb"'
k = doc.index(anchor); k = doc.rindex('<w:p ', 0, k)
doc = doc[:k] + xml + doc[k:]
zout = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename == 'word/document.xml': data = doc.encode()
    if it.filename == 'word/_rels/document.xml.rels': data = rels.encode()
    zout.writestr(it, data)
zout.writestr('word/media/ch4_smoke.png', open(png,'rb').read())
zout.close(); print('written')
