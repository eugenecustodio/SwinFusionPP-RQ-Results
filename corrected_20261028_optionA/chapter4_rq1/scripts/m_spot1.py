import pandas as pd, numpy as np, sys
S='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/'
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_columns',40)
e=pd.read_csv(S+'three_seed_mean_logit_ensemble.csv')
print(e.groupby(['variant','family','optimization_regimen']).size())
print(sorted(e.training_dataset.unique()), sorted(e.test_dataset.unique()))
f=e[(e.variant=='plain')&(e.family.isin(['swin_b','video_swin_b','swinfusionpp']))]
cols=['family','optimization_regimen','training_dataset','test_dataset','roc_auc','roc_auc_ci_low','roc_auc_ci_high','accuracy','precision','recall','specificity','f1','tp','tn','fp','fn','analyzed_videos','seed_auc_mean','seed_auc_sd','clusters']
print(f[cols].sort_values(['training_dataset','test_dataset','family','optimization_regimen']).round(4).to_string())
# mean transfer AUC fixed
t=f[(f.training_dataset!=f.test_dataset)]
print(t.groupby(['family','optimization_regimen']).roc_auc.agg(['mean','median','count','min']).round(4))
