import pandas as pd
S='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/'
T='/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/stats_out/'
e=pd.read_csv(S+'three_seed_mean_logit_ensemble.csv')
e=e[(e.variant=='plain')&(e.optimization_regimen=='fixed_no_bo')&e.family.isin(['swin_b','video_swin_b','swinfusionpp'])].copy()
e['calls']=e.tp+e.fp
t=e[e.training_dataset!=e.test_dataset]
p=t.pivot_table(index=['training_dataset','test_dataset'],columns='family',values='calls')
p['fewest']=p.idxmin(axis=1); p['tie']=p[['swin_b','swinfusionpp','video_swin_b']].eq(p[['swin_b','swinfusionpp','video_swin_b']].min(axis=1),axis=0).sum(axis=1)
print(p)
for m in ['precision','specificity']:
    q=t.pivot_table(index=['training_dataset','test_dataset'],columns='family',values=m)
    print(m,'SF++ highest or tied:',int(q.eq(q.max(axis=1),axis=0)['swinfusionpp'].sum()),'of',len(q))
w=e[e.training_dataset==e.test_dataset][['family','test_dataset','pr_auc']]
print(w.pivot(index='test_dataset',columns='family',values='pr_auc').round(4))
print(t.pivot_table(index=['training_dataset','test_dataset'],columns='family',values='pr_auc').round(4))
j=pd.read_csv(T+'statistician_jackknife_vs_bootstrap.csv'); print(j.columns.tolist()); print(j.head(3).to_string())
pd.set_option('display.width',200)
print(p[['swin_b','swinfusionpp','video_swin_b','fewest','tie']].to_string())
j['cdf']=j.test=='celeb_df_v2'
print(j.groupby('cdf').ratio_jack_over_boot.agg(['min','max','mean','count']).round(2))
print(j.groupby(['cdf',j.family.str.contains('architecture')]).ratio_jack_over_boot.agg(['min','max','mean','count']).round(2))
