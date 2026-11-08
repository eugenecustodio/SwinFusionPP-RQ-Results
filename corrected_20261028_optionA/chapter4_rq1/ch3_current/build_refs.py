import json, re, sys
cur = open(sys.argv[1]).read().split('\n# ORIGINAL CHAPTER 1-3')[0]
def demark(s):
    s = re.sub(r'\[([^\]]*)\]\(([^()]|\([^)]*\))*\)', lambda m: m.group(1), s)   # [text](url) -> text
    s = re.sub(r'<(https?://[^>]+)>', r'\1', s)
    s = s.replace('***', '').replace('**', '')
    s = re.sub(r'(?<![\w*])\*(?=\S)|(?<=\S)\*(?![\w*])', '', s)                   # single-* italics
    s = re.sub(r'\\([\[\]\(\)\*_#+\-.!<>|~])', r'\1', s)
    return s
L = cur.split('\n'); D = demark(cur)
def line(n): return demark(L[n-1])
Q = '\u2019'
R = {
 'Memon': "Memon, M. A., Ting, H., Cheah, J.-H., Ramayah, T., Chuah, F., & Cham, T. H. (2020). Sample size for survey research: Review and recommendations. Journal of Applied Structural Equation Modeling, 4(2), i\u2013xx. https://doi.org/10.47263/jasem.4(2)01",
 'Nielsen': f"Nielsen, J., & Landauer, T. K. (1993). A mathematical model of the finding of usability problems. In Proceedings of the INTERACT {Q}93 and CHI {Q}93 Conference on Human Factors in Computing Systems (pp. 206\u2013213). Association for Computing Machinery. https://doi.org/10.1145/169059.169166",
 'Pressman': f"Pressman, R. S., & Maxim, B. R. (2020). Software engineering: A practitioner{Q}s approach (9th ed.). McGraw-Hill Education.",
 'Roscoe': "Roscoe, J. T. (1975). Fundamental research statistics for the behavioral sciences (2nd ed.). Holt, Rinehart and Winston.",
}
out = {}
# bibliography inserts
out['INS_Memon']   = dict(find="Montserrat, D. M., Hao, H.", repl=R['Memon'] + "\nMontserrat, D. M., Hao, H.", regex=False)
out['INS_Nielsen'] = dict(find="Philippine Health Research Ethics Board. (2022).", repl=R['Nielsen'] + "\nPhilippine Health Research Ethics Board. (2022).", regex=False)
out['INS_Roscoe']  = dict(find="^R\u00f6ssler, A\\., Cozzolino", repl=R['Roscoe'] + "\nR\u00f6ssler, A., Cozzolino", regex=True)
out['INS_Pressman']= dict(find="^Republic Act No\\. 10173, ", repl=R['Pressman'] + "\nRepublic Act No. 10173, ", regex=True)
# removals from Chapter 3 (paragraph text + its newline)
out['DEL_Pressman'] = dict(find=line(251) + "\n", repl="", regex=False)
out['DEL_block']    = dict(find=line(315) + "\n" + line(316) + "\n" + line(317) + "\n", repl="", regex=False)
out['DEL_Nielsen']  = dict(find=line(349) + "\n", repl="", regex=False)
paras = D.split('\n')
for k, v in out.items():
    if v['regex']:
        c = sum(1 for p in paras if re.search(v['find'], p))
        c_any = len(re.findall(v['find'].lstrip('^'), D))
        print(f"{k:13s} regex paragraph-start matches={c} (anywhere={c_any})")
    else:
        print(f"{k:13s} plain matches={D.count(v['find'])} (without trailing newline: {D.count(v['find'].rstrip(chr(10)))})")
for k in ('DEL_Pressman','DEL_block','DEL_Nielsen'): print(k, repr(out[k]['find'][:90]), '...', repr(out[k]['find'][-60:]))
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
