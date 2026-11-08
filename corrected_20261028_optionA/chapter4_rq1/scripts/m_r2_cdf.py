import pandas as pd, glob
R='/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/b2dl/Thesis_Code_final_20261004/results/raw_predictions_v020/'
f=sorted(glob.glob(R+'celeb_df_v2_to_celeb_df_v2/principal_swin_b_*fixed_no_bo_s1*.parquet'))[0]
x=pd.read_parquet(f)
print(x.columns.tolist()); print(x.head(5).to_string())
g=x.groupby('dependency_cluster').agg(n=('label','size'),fake=('label','sum'),src=('source_group','nunique'),glob=('global_cluster','nunique'))
print(g.sort_values('n',ascending=False).head(12).to_string()); print('clusters',len(g),'with fakes',(g.fake>0).sum())
print(x.dependency_cluster.head(3).tolist(), x.source_group.head(3).tolist(), x.global_cluster.head(3).tolist())
# CDF->other directions: do train/val identities appear? Not available. Check C23->CDF cluster ids same?
y=pd.read_parquet(sorted(glob.glob(R+'ffpp_c23_to_celeb_df_v2/principal_swin_b_*s1*.parquet'))[0])
print('same cluster ids in C23->CDF:', set(y.dependency_cluster)==set(x.dependency_cluster))
