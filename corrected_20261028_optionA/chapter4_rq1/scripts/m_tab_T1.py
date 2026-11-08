"""Build T1 (test sets and coverage) from the package; asserts every value it prints."""
import json, pandas as pd, numpy as np
P='/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/'
OUT='/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/tables/'
RAW='/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/b2dl/Thesis_Code_final_20261004/results/raw_predictions_v020/'
h=pd.read_csv(P+'00_Shared/statistics_raw/heldout_seed_metrics_rq1_rq6.csv')
prot=json.load(open(P+'00_Shared/protocol_and_decisions/evaluation_protocol_v020.json'))
lin={r['condition']:r for r in prot['required_disclosures'][1]['rows'] if r['role']=='primary'}
LINKEY={'ffpp_c23':'ffpp_deepfakes_hq','ffpp_c40':'ffpp_deepfakes_lq','celeb_df_v2':'celeb_df_v2','deeperforensics_1_0':'deeperforensics_1_0'}
NAME={'ffpp_c23':'FF++ C23 (HQ)','ffpp_c40':'FF++ C40 (LQ)','celeb_df_v2':'Celeb-DF v2','deeperforensics_1_0':'DeeperForensics-1.0'}
full=h[h.subset=='full_test']; strict=h[(h.subset=='strict_overlap_free')&(h.variant=='plain')]
rows=[]
for ds in ['ffpp_c23','ffpp_c40','celeb_df_v2','deeperforensics_1_0']:
    f=full[full.test_dataset==ds]
    n=f.n_manifest_videos.unique(); a=f.n_analyzed.unique(); fl=f.n_preprocessing_failed.unique(); cv=f.coverage.unique()
    assert len(n)==len(a)==len(fl)==len(cv)==1, ds
    n=int(n[0]); assert int(a[0])==n and float(fl[0])==0 and float(cv[0])==1.0
    w=f[(f.training_dataset==ds)&(f.variant=='plain')].iloc[0]
    fake=int(w.tp+w.fn); real=int(w.tn+w.fp); assert fake+real==n
    # clusters from raw predictions
    x=pd.read_parquet(RAW+f'{ds}_to_{ds}/principal_swin_b_{ds}_fixed_no_bo_s1_v002.video_predictions.parquet')
    assert len(x)==n and (x.analysis_status=='analyzed').all()
    g=x.groupby('dependency_cluster').label.sum(); ncl=len(g); nfc=int((g>0).sum())
    L=lin[LINKEY[ds]]; assert L['test_videos']==n
    ov=L['with_cross_condition_lineage_or_unknown']
    s=strict[strict.test_dataset==ds].groupby('training_dataset').analyzed_videos.unique()
    parts=[]
    for src in ['ffpp_c23','celeb_df_v2','deeperforensics_1_0']:
        if src in s.index and src!=ds:
            v=s[src]; assert len(v)==1; parts.append(f"from {NAME[src]}: {int(v[0])}")
    clus=f"{ncl}" if nfc==ncl or ds!='celeb_df_v2' else f"{ncl} (all fakes in {nfc})"
    rows.append({'Test set':NAME[ds],'Videos (fake / real)':f"{n} ({fake} / {real})",'Clusters':clus,
                 'Coverage':'100.0%','Preprocessing failures':'0',
                 'Test videos sharing lineage with another condition':f"{ov} ({100*ov/n:.1f}%)",
                 'Strict lineage-free subset, by transfer source':'; '.join(parts) if parts else '—'})
    print(ds,n,fake,real,ncl,nfc,ov,parts)
pd.DataFrame(rows).to_csv(OUT+'T1.csv',index=False)
# source-validation coverage
op=pd.read_csv(P+'00_Shared/statistics_raw/source_validation_operating_points_v020.csv')
print(op[op.kind=='single_seed'].groupby('condition')[['n_validation_videos','n_analyzed']].agg(['min','max']))
