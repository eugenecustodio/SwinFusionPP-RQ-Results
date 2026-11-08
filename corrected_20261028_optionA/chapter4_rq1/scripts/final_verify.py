# Independent check of the clean copy: every table against its source CSV, plus wording rules
import re,sys,zipfile,html,csv,os
S=sys.argv[1]; R=S+'/render'; T=S+'/ch4/team'
x=zipfile.ZipFile(R+'/final.docx').read('word/document.xml').decode()
body=x[x.index('<w:body>'):]
blocks=re.findall(r'<w:tbl>.*?</w:tbl>|<w:p[ >].*?</w:p>',body,flags=re.S)
plain=lambda s: html.unescape(re.sub(r'<[^>]+>','',s)).replace('⁠','').replace(' ',' ').strip()
txt=[plain(b) if not b.startswith('<w:tbl>') else '' for b in blocks]
caps={}
for i,bk in enumerate(blocks):
    if bk.startswith('<w:tbl>'):
        for k in range(i-1,max(0,i-4),-1):
            m=re.match(r'Table (J?\d+)',txt[k])
            if m: caps[m.group(1)]=bk; break
SRC={'1':'tables/T1','2':'tables/T2','3':'tables/T4','4':'tables/T5','5':'tables/T6','6':'tables/T7','7':'tables/T8','8':'tables/T9','9':'rq2/tables/T9','10':'rq2x/tables/T10','11':'rq2x/tables/T11',**{f'J{n}':f'tables/J{n}' for n in range(1,9)}}
norm=lambda s: re.sub(r'\s+',' ',s.replace('⁠','').replace(' ',' ').replace('**','')).strip()
bad=0
for tid,src in SRC.items():
    rows=list(csv.reader(open(f'{T}/{src}.csv',encoding='utf-8-sig')))
    pr=[[plain(c) for c in re.findall(r'<w:tc>.*?</w:tc>',r,flags=re.S)] for r in re.findall(r'<w:tr[ >].*?</w:tr>',caps[tid],flags=re.S)]
    csvc=[norm(c) for r in rows for c in r if norm(c) and norm(c)!='__SPAN__']
    docc=[norm(c) for r in pr for c in r if norm(c)]
    missing=[c for c in csvc if c not in docc and c not in ' '.join(docc)]
    extra=[c for c in docc if c not in csvc and c not in ' '.join(csvc)]
    print(f'Table {tid:>3}: csv cells {len(csvc):4d}, printed {len(docc):4d}, csv-not-printed {len(missing)}, printed-not-csv {len(extra)}', (missing[:3],extra[:3]) if missing or extra else '')
    bad+=len(missing)+len(extra)
print('total mismatches:',bad)
print('J9 rows:',len(re.findall(r'<w:tr[ >]',caps['J9']))-1)
st=next(i for i,t in enumerate(txt) if t=='Evaluation Setting')
en=next(i for i,t in enumerate(txt) if t=='REFERENCES' and i>st)
ch4=' '.join(plain(b) for b in blocks[st:en])
print('Chapter 4 words incl. tables:',len(ch4.split()))
for w in ['deviat','outperform','state of the art','state-of-the-art','equivalen','robust','superior',r'\btied\b']:
    hits=[ch4[max(0,m.start()-50):m.end()+30] for m in re.finditer(w,ch4,flags=re.I)]
    print(f'  {w}: {len(hits)}',hits[:3] if hits else '')
print('title date:',[t for t in txt[:40] if re.search(r'\b20\d\d\b',t)][:4])
print('Kuang ref present:',any(t.startswith('Kuang, L.') for t in txt),'| cited:',any('Kuang et al., 2022' in t for t in txt))
print('Esperanza cited:',any('Esperanza et al. (2025)' in t for t in txt),'| Laureta cited:',any('Laureta et al. (2025)' in t for t in txt))
for n in range(1,11):
    pat=f'Figure {n}\\b'
    print(f'  Figure {n} callout before its caption:',any(re.search(pat,t) and not re.match(pat,t) for t in txt if t), end=';')
print()
