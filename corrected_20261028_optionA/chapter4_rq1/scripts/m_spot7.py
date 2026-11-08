import pandas as pd, numpy as np
P='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/'
pt=pd.read_csv(P+'corrected_20261028_optionA/paired_tests_optionA.csv')
rc=pd.read_csv(P+'00_Shared/statistics_raw/paired_cluster_effects_rank_corrected.csv')
k=['model_a','model_b','training_dataset','test_dataset']
m=pt.merge(rc[k+['permutation_p_original_csv','bootstrap_two_sided_p']],on=k)
def holm(p):
    p=np.asarray(p); o=np.argsort(p); n=len(p); adj=np.empty(n); run=0
    for i,idx in enumerate(o):
        run=max(run,(n-i)*p[idx]); adj[idx]=min(1,run)
    return adj
m['holm_orig_perm']=m.groupby('family_optionA').permutation_p_original_csv.transform(holm)
m['holm_boot']=m.groupby('family_optionA').bootstrap_two_sided_p.transform(holm)
for f,g in m.groupby('family_optionA'):
    a=g.holm_optionA<.05; b=g.holm_orig_perm<.05; c=g.holm_boot<.05
    print(f,len(g),'rank sig',int(a.sum()),'orig-raw-perm sig',int(b.sum()),'changes',int((a!=b).sum()),'| bootstrap-p Holm sig',int(c.sum()),'changes vs rank',int((a!=c).sum()))
x=m[m.family_optionA.isin(['RQ1_architecture','RQ6_architecture'])&((m.holm_optionA<.05)!=(m.holm_orig_perm<.05))]
print(x[['family_optionA','model_b','training_dataset','test_dataset','auc_difference','permutation_p_original_csv','permutation_p_rank','holm_orig_perm','holm_optionA']].round(4).to_string())
y=m[m.family_optionA.isin(['RQ1_architecture','RQ6_architecture'])&((m.holm_optionA<.05)!=(m.holm_boot<.05))]
print(y[['family_optionA','model_b','training_dataset','test_dataset','auc_difference','bootstrap_two_sided_p','holm_boot','holm_optionA']].round(4).to_string())
