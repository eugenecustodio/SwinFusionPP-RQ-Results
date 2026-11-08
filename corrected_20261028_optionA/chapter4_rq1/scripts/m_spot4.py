import pandas as pd, numpy as np
S='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/'
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_columns',40)
h=pd.read_csv(S+'heldout_seed_metrics_rq1_rq6.csv')
h=h[(h.variant=='plain')&(h.subset=='full_test')&(h.optimization_regimen=='fixed_no_bo')&h.family.isin(['swin_b','video_swin_b','swinfusionpp'])]
p=h.pivot_table(index=['training_dataset','test_dataset'],columns=['family','seed_slot'],values='roc_auc').round(4)
print(p.to_string())
# seed overlap: min SF++ seed vs max baseline seed
for (tr,te),g in h.groupby(['training_dataset','test_dataset']):
    sf=g[g.family=='swinfusionpp'].roc_auc; sb=g[g.family=='swin_b'].roc_auc; vs=g[g.family=='video_swin_b'].roc_auc
    print(f'{tr:>20}->{te:<20} SF[{sf.min():.4f},{sf.max():.4f}] SB[{sb.min():.4f},{sb.max():.4f}] VSB[{vs.min():.4f},{vs.max():.4f}]  SF>allSB:{sf.min()>sb.max()} SF>allVSB:{sf.min()>vs.max()} SF<allVSB:{sf.max()<vs.min()}')
# strict subset seed means
s=pd.read_csv(S+'heldout_seed_metrics_rq1_rq6.csv')
s=s[(s.variant=='plain')&(s.subset=='strict_overlap_free')&(s.optimization_regimen=='fixed_no_bo')&s.family.isin(['swin_b','video_swin_b','swinfusionpp'])]
s=s[s.analyzed_videos<s.groupby(['training_dataset','test_dataset']).analyzed_videos.transform('max')+1]
q=s.groupby(['training_dataset','test_dataset','family']).agg(n=('analyzed_videos','first'),auc_mean=('roc_auc','mean'),auc_sd=('roc_auc','std'),auc_min=('roc_auc','min'),auc_max=('roc_auc','max')).round(4)
print(q[q.n<300].to_string())
# TTA vs plain ensembles all models
e=pd.read_csv(S+'three_seed_mean_logit_ensemble.csv')
e=e[e.family.isin(['swin_b','video_swin_b','swinfusionpp'])]
w=e.pivot_table(index=['training_dataset','test_dataset'],columns=['family','optimization_regimen','variant'],values='roc_auc').round(4)
print(w.to_string())
