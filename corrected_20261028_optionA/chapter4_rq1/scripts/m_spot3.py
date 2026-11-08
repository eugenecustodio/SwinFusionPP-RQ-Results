import pandas as pd, numpy as np
S='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/'
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_columns',40)
h=pd.read_csv(S+'heldout_seed_metrics_rq1_rq6.csv')
print(h.groupby(['subset','variant']).size())
print(h.groupby(['evidence_level','overlap_policy']).size())
print(h[['training_dataset','test_dataset']].drop_duplicates().sort_values(['training_dataset','test_dataset']).to_string())
# coverage per test set
c=h[(h.variant=='plain')&(h.subset=='full_test')].groupby(['test_dataset']).agg(n_manifest=('n_manifest_videos','unique'),n_analyzed=('n_analyzed','unique'),failed=('n_preprocessing_failed','unique'),cov=('coverage','unique'),analyzed_videos=('analyzed_videos','unique'))
print(c.to_string())
# strict subset
s=h[(h.subset!='full_test')&(h.variant=='plain')]
print(s.subset.unique())
cols=['family','optimization_regimen','seed_slot','training_dataset','test_dataset','subset','analyzed_videos','tp','tn','fp','fn','roc_auc','accuracy']
print(s[s.family.isin(['swin_b','video_swin_b','swinfusionpp'])][cols].sort_values(['training_dataset','test_dataset','family','optimization_regimen','seed_slot']).round(4).to_string())
