import json,re,sys
raw=open(sys.argv[1]).read()
d=re.sub(r'<comment_(start|end)[^>]*>','',raw)
d=re.sub(r'\[([^\]]*)\]\(([^()]|\([^)]*\))*\)', lambda m: m.group(1), d)
d=re.sub(r'<(https?://[^>]+)>', r'\1', d)
d=d.replace('***','').replace('**',''); d=re.sub(r'\*+','',d); d=re.sub(r'\\([\[\]\(\)\*_#+\-.!<>|~])', r'\1', d)
L=d.split('\n')
def refline(prefix): 
    m=[l for l in L if l.startswith(prefix)]; assert len(m)==1, prefix; return m[0]
Q='\u2019'
E=[]
E.append(('CRON',f'Internal consistency reliability was assessed using Cronbach{Q}s alpha for each dimension to determine whether the items within a dimension behaved coherently. The weighted means were interpreted using the following scale:',
          'The weighted mean of each item and dimension, computed as the sum of each scale value multiplied by its frequency and divided by the total number of responses (Pimentel, 2019, p. 186), was rounded to two decimal places and interpreted using the equal-width intervals for 5-point scales of Pimentel (2019, p. 188), with the labels of the end-user response scale:',1))
E.append(('EXPINTRO','before the dimension mean was computed. The weighted means were interpreted using the following scale:',
          'before the dimension mean was computed. The weighted means were interpreted using the same intervals (Pimentel, 2019, p. 188), with the labels of the expert response scale:',1))
for o,n in [('4.21 \u2013 5.00','4.20 \u2013 5.00'),('3.41 \u2013 4.20','3.40 \u2013 4.19'),('2.61 \u2013 3.40','2.60 \u2013 3.39'),('1.81 \u2013 2.60','1.80 \u2013 2.59'),('1.00 \u2013 1.80','1.00 \u2013 1.79')]:
    E.append(('BAND '+o,o,n,2))
E.append(('TAB5','Table IV.','Table V.',1))
E.append(('TAB4','Table III. Interpretation Scale for the End-User Survey','Table IV. Interpretation Scale for the End-User Survey',1))
E.append(('EMAIL','namely their organizational or institutional email address','namely their email address (organizational, institutional, or personal)',1))
for p in ['Esperanza, J., Marquez','Joshi, A., Kale','Laureta, M. P.','Norman, G. (2010)']:
    E.append(('DEL '+p, refline(p)+'\n','',1))
ok=True
for i,o,n,exp in E:
    c=d.count(o); ok&=(c==exp); print(f'{i:28s} count={c} expected={exp}')
# band replacements must not create text matched by later band finds
print('ALL OK' if ok else 'PROBLEM')
json.dump([{"replaceAllText":{"containsText":{"text":o,"matchCase":True},"replaceText":n,"tabsCriteria":{"tabIds":["t.l5c18frq5wuo"]}}} for _,o,n,_ in E],open(sys.argv[2],'w'),ensure_ascii=True)
for i,o,n,exp in E:
    if i.startswith('DEL'): print(repr(o[-60:]))
