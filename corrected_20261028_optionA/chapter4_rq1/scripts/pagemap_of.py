import sys,re,subprocess
pdf=sys.argv[1]
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
pages=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout.split('\f')
blank=[i for i,p in enumerate(pages[:n],1) if len(re.sub(r'\s|\d','',p))==0]
few=[(i,re.sub(r'\s+',' ',p).strip()[:70]) for i,p in enumerate(pages[:n],1) if 0<len(re.sub(r'\s|\d','',p))<45 and i>6]
print('blank pages (text-wise):',blank); print('few-text pages:'); [print('  ',f) for f in few]
