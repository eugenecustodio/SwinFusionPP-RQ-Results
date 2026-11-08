import pandas as pd
P='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/'
pt=pd.read_csv(P+'corrected_20261028_optionA/paired_tests_optionA.csv')
a=pt[pt.family_optionA=='RQ6_architecture']
print('negative transfer point estimates:',(a.auc_difference<0).sum(), a[a.auc_difference<0][['model_b','training_dataset','test_dataset','auc_difference']].round(4).to_string())
w=pt[pt.family_optionA=='RQ1_architecture']; print('within negatives',(w.auc_difference<0).sum(),'max upper CI',w.ci_high.max().round(4),'min lower',w.ci_low.min().round(4))
# decisions identical across groupings for architecture families
for f in ['RQ1_architecture','RQ6_architecture','RQ1_configured_system','RQ6_configured_system','RQ1_optimization_effect','RQ6_optimization_effect','RQ4_controls','RQ4_controls_transfer']:
    g=pt[pt.family_optionA==f]
    print(f, 'sig optionA',int((g.holm_optionA<.05).sum()),'prev',int((g.holm_previous_family<.05).sum()),'pooled',int((g.holm_sensitivity_pooled<.05).sum()),
          'decision changes vs prev',int(((g.holm_optionA<.05)!=(g.holm_previous_family<.05)).sum()),'vs pooled',int(((g.holm_optionA<.05)!=(g.holm_sensitivity_pooled<.05)).sum()))
e=pd.read_csv(P+'00_Shared/statistics_raw/three_seed_mean_logit_ensemble.csv')
x=e[(e.variant=='plain')&(e.training_dataset=='ffpp_c23')&(e.test_dataset=='celeb_df_v2')][['family','optimization_regimen','pr_auc']]
print(x.round(4).to_string())
op=pd.read_csv(P+'00_Shared/statistics_raw/source_validation_operating_points_v020.csv')
print(op.kind.value_counts().to_dict(), op.tie_rule.unique(), op.displayed_value.unique())
print(op[op.kind=='three_seed_ensemble'][['run_id','n_validation_videos','n_analyzed','youden_j','threshold_logit','temperature']].head(8).to_string())
print(op.groupby('condition')[['n_validation_videos','n_analyzed']].agg(['min','max']))
