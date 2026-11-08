import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *
ens = pd.read_csv(ST + '/three_seed_mean_logit_ensemble.csv'); ens = ens[ens.variant == 'plain']
df, thr, T, _ = load_cell('swinfusionpp', 'fixed_no_bo', 'celeb_df_v2', 'celeb_df_v2')
y = df.label.values.astype(int); z = df.z.values; cl = df.dependency_cluster.values
uniq = np.array(sorted(set(cl.tolist()))); idx = {c: np.flatnonzero(cl == c) for c in uniq}
print('stored', 0.9905061174010277, 0.9994564360988719)
def run(pickfn, name):
    rng = np.random.default_rng(SEED); out = []
    for b in range(B):
        ii = pickfn(rng)
        yy = y[ii]
        if yy.min() == yy.max(): continue
        out.append(auc(yy, z[ii]))
    print(name, len(out), np.quantile(out, [0.025, 0.975]))
hasf = np.array([y[idx[c]].max() == 1 for c in uniq])
G1 = [np.flatnonzero(~hasf), np.flatnonzero(hasf)]
run(lambda rng: np.concatenate([idx[uniq[p]] for g in G1 for p in g[rng.integers(0, len(g), len(g))]]), 'strata real-only first')
# per-class cluster resampling
pc = {}
for c in (0, 1):
    m = y == c
    cc = np.array(sorted(set(cl[m].tolist())))
    pc[c] = (cc, {k: np.flatnonzero(m & (cl == k)) for k in cc})
for order in [(0, 1), (1, 0)]:
    run(lambda rng: np.concatenate([pc[c][1][pc[c][0][p]] for c in order for p in rng.integers(0, len(pc[c][0]), len(pc[c][0]))]), f'per-class clusters order {order}')
    run(lambda rng: np.concatenate([pc[c][1][pc[c][0][p]] for c in order for p in rng.choice(len(pc[c][0]), len(pc[c][0]))]), f'per-class choice order {order}')
# cluster labels as strata by majority?
maj = np.array([y[idx[c]].mean() >= 0.5 for c in uniq])
for o in [(False, True), (True, False)]:
    G = [np.flatnonzero(maj == v) for v in o]
    run(lambda rng: np.concatenate([idx[uniq[p]] for g in G for p in g[rng.integers(0, len(g), len(g))]]), f'majority strata {o}')
# sorted by str of cluster? uniq with pandas unique order
uq2 = pd.unique(cl)
idx2 = {c: np.flatnonzero(cl == c) for c in uq2}
run(lambda rng: np.concatenate([idx2[uq2[p]] for p in rng.integers(0, len(uq2), len(uq2))]), 'appearance order plain')
