import pandas as pd
T='/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/stats_out/'
d=pd.read_csv(T+'statistician_threshold_metrics.csv')
print(d.kind.unique(), d.model.unique(), d.versus.unique(), d.metric.unique())
x=d[(d.kind!='per_model')&(d.model=='SF++F')&(d.training!=d.test)]
for m in ['accuracy','f1','recall','precision']:
    y=x[x.metric==m]
    lo=y[(y.ci_high<0)]; hi=y[(y.ci_low>0)]
    print(m,'n',len(y),'lower',len(lo),'higher',len(hi))
    print('  lower:',[(r.training,r.test,r.versus,round(r.estimate,3)) for r in lo.itertuples()])
    print('  higher:',[(r.training,r.test,r.versus,round(r.estimate,3)) for r in hi.itertuples()])
w=d[(d.kind!='per_model')&(d.model=='SF++F')&(d.training==d.test)]
for m in ['accuracy','f1']:
    y=w[w.metric==m]; print('within',m,[(r.test,r.versus,round(r.estimate,3),round(r.ci_low,3),round(r.ci_high,3)) for r in y.itertuples() if r.ci_low>0 or r.ci_high<0])
