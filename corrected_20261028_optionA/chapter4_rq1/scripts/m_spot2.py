import pandas as pd, numpy as np
P='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/'
S=P+'00_Shared/statistics_raw/'
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_columns',40)
pt=pd.read_csv(P+'corrected_20261028_optionA/paired_tests_optionA.csv')
rc=pd.read_csv(S+'paired_cluster_effects_rank_corrected.csv')
for fam in ['RQ1_architecture','RQ6_architecture','RQ1_optimization_effect','RQ6_optimization_effect','RQ1_configured_system','RQ6_configured_system']:
    g=pt[pt.family_optionA==fam].copy()
    g['ci_excl0']=(g.ci_low>0)|(g.ci_high<0)
    g['sig']=g.holm_optionA<0.05
    print('==',fam,len(g))
    print(g[['model_a','model_b','training_dataset','test_dataset','auc_difference','ci_low','ci_high','permutation_p_rank','holm_optionA','holm_previous_family','holm_sensitivity_pooled','ci_excl0','sig','clusters','videos']].round(4).to_string())
# cross-check auc_difference vs ensemble
e=pd.read_csv(S+'three_seed_mean_logit_ensemble.csv'); e=e[e.variant=='plain']
e['key']=e.family+'__'+e.optimization_regimen
m=pt.merge(e[['key','training_dataset','test_dataset','roc_auc']].rename(columns={'key':'model_a','roc_auc':'auc_a'}),on=['model_a','training_dataset','test_dataset'],how='left')
m=m.merge(e[['key','training_dataset','test_dataset','roc_auc']].rename(columns={'key':'model_b','roc_auc':'auc_b'}),on=['model_a' if False else 'model_b','training_dataset','test_dataset'],how='left')
m['chk']=m.auc_a-m.auc_b-m.auc_difference
print('max |ensemble diff - stored delta|:',m.chk.abs().max(), 'n missing',m.chk.isna().sum())
# rank-corrected vs optionA perm p
k=['model_a','model_b','training_dataset','test_dataset']
mm=pt.merge(rc[k+['permutation_p_rank','auc_difference','ci_low','ci_high']],on=k,suffixes=('','_rc'))
print('rows matched',len(mm),'max dp',(mm.permutation_p_rank-mm.permutation_p_rank_rc).abs().max(),'max dd',(mm.auc_difference-mm.auc_difference_rc).abs().max(),'max dci',(mm.ci_low-mm.ci_low_rc).abs().max())
# recompute Holm per family
def holm(p):
    p=np.asarray(p); o=np.argsort(p); m=len(p); adj=np.empty(m); run=0
    for i,idx in enumerate(o):
        run=max(run,(m-i)*p[idx]); adj[idx]=min(1,run)
    return adj
pt['holm_re']=pt.groupby('family_optionA').permutation_p_rank.transform(holm)
print('max holm recompute diff',(pt.holm_re-pt.holm_optionA).abs().max())
# discordances CI vs Holm
d=pt[((pt.ci_low>0)|(pt.ci_high<0))!=(pt.holm_optionA<0.05)]
print('CI-excludes-0 vs Holm<0.05 discordant:'); print(d[['family_optionA','model_a','model_b','training_dataset','test_dataset','auc_difference','ci_low','ci_high','permutation_p_rank','holm_optionA']].round(4).to_string())
