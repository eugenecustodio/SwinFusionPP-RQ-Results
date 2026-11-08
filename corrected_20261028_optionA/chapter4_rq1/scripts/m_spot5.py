import pandas as pd, numpy as np
S='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/'
e=pd.read_csv(S+'three_seed_mean_logit_ensemble.csv')
e=e[(e.variant=='plain')&(e.optimization_regimen=='fixed_no_bo')&e.family.isin(['swin_b','video_swin_b','swinfusionpp'])].copy()
e['correct']=e.tp+e.tn; e['n_fake']=e.tp+e.fn; e['n_real']=e.tn+e.fp
w=e[e.training_dataset==e.test_dataset]
print(w.pivot(index='test_dataset',columns='family',values='correct'))
print(w.groupby('test_dataset')[['n_fake','n_real','clusters']].first())
t=e[e.training_dataset!=e.test_dataset]
for m in ['accuracy','f1','recall','precision','specificity','roc_auc']:
    p=t.pivot_table(index=['training_dataset','test_dataset'],columns='family',values=m)
    best=p.idxmax(axis=1); ties=(p.eq(p.max(axis=1),axis=0).sum(axis=1)>1)
    print(m,'best counts:',best.value_counts().to_dict(),'ties:',int(ties.sum()), 'SF best (incl ties):',int(p.eq(p.max(axis=1),axis=0)['swinfusionpp'].sum()))
nc=t[(t.training_dataset+t.test_dataset)!='ffpp_c23ffpp_c40']
print('transfer spec range',t.specificity.min().round(4),t.specificity.max().round(4),'recall range',t.recall.min().round(4),t.recall.max().round(4))
print('excluding C23->C40: recall max',nc.recall.max().round(4),'spec min',nc.specificity.min().round(4))
print('NaN precision cells (no fake predicted):'); print(t[t.precision.isna()][['family','training_dataset','test_dataset','tp','fp']])
print('precision with tp+fp<10:'); print(t[(t.tp+t.fp<10)&t.precision.notna()][['family','training_dataset','test_dataset','tp','fp','precision']])
