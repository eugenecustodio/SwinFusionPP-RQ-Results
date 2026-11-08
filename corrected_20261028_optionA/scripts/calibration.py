"""Calibration of the three-seed mean-logit ensembles (manuscript Ch. 3, Statistical Treatment of Data).

Probability = sigmoid(mean seed video logit / T), where T is the frozen source-validation ensemble
temperature from 00_Shared/statistics_raw/source_validation_operating_points_v020.csv. Brier score and
ECE with 15 equal-width bins on the fake-class probability (the binning declared in the preliminary study).

Self-checks (the run aborts if any fails):
  * every seed file's stored calibrated_probability equals sigmoid(video_logit / T_seed);
  * every ensemble ROC-AUC equals the package value in three_seed_mean_logit_ensemble.csv.

Usage: python calibration.py <raw_predictions_v020 dir> <package root> <out dir>
Writes calibration_ensembles.csv and reliability_bins.csv to <out dir>.
"""
import glob, os, sys
import numpy as np, pandas as pd

RAW, PKG, OUT = sys.argv[1:4]
ST = os.path.join(PKG, '00_Shared', 'statistics_raw')
BINS = 15
op = pd.read_csv(os.path.join(ST, 'source_validation_operating_points_v020.csv'))
ens_ref = pd.read_csv(os.path.join(ST, 'three_seed_mean_logit_ensemble.csv'))
ens_ref = ens_ref[ens_ref.variant == 'plain']
sig = lambda z: 1 / (1 + np.exp(-z))


def auc(y, s):
    r = pd.Series(s).rank().values
    n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def bin_table(y, p):
    idx = np.minimum((p * BINS).astype(int), BINS - 1)
    out = []
    for b in range(BINS):
        m = idx == b
        out.append((b, int(m.sum()), float(p[m].mean()) if m.any() else np.nan, float(y[m].mean()) if m.any() else np.nan))
    return out


def ece(y, p):
    return sum(n / len(y) * abs(acc - conf) for _, n, conf, acc in bin_table(y, p) if n)


rows, bins_rows, seed_checks = [], [], 0
for d in sorted(glob.glob(os.path.join(RAW, '*_to_*'))):
    src, tgt = os.path.basename(d).split('_to_')
    cells = ens_ref[(ens_ref.training_dataset == src) & (ens_ref.test_dataset == tgt)]
    for (fam, reg), g in cells.groupby(['family', 'optimization_regimen']):
        files = sorted(glob.glob(os.path.join(d, f'principal_{fam}_{src}_{reg}_s[123]_v002.video_predictions.parquet')))
        assert len(files) == 3, (d, fam, reg, files)
        seeds = []
        for k, f in enumerate(files, 1):
            x = pd.read_parquet(f, columns=['video_id', 'label', 'video_logit', 'calibrated_probability', 'analysis_status'])
            assert (x.analysis_status == 'analyzed').all(), f
            t = op[(op.kind == 'single_seed') & (op.family == fam) & (op.optimization_regimen == reg)
                   & (op.condition == src) & (op.seed_slot == k)].temperature
            assert len(t) == 1, (fam, reg, src, k)
            assert np.allclose(sig(x.video_logit / float(t.iloc[0])), x.calibrated_probability, atol=1e-6), f
            seed_checks += 1
            seeds.append(x.set_index('video_id'))
        ids = seeds[0].index
        assert all(set(s.index) == set(ids) for s in seeds)
        y = seeds[0].loc[ids, 'label'].values.astype(int)
        z = np.mean([s.loc[ids, 'video_logit'].values for s in seeds], axis=0)
        T = op[(op.kind == 'three_seed_ensemble') & (op.family == fam) & (op.optimization_regimen == reg)
               & (op.condition == src) & (~op.run_id.str.endswith('__tta'))].temperature
        assert len(T) == 1, (fam, reg, src)
        T = float(T.iloc[0])
        a = auc(y, z)
        assert abs(a - float(g.roc_auc.iloc[0])) < 1e-9, ('AUC mismatch', src, tgt, fam, reg)
        pc, pu = sig(z / T), sig(z)
        rows.append(dict(training=src, test=tgt, family=fam, regimen=reg, n_videos=len(y), fake_prevalence=y.mean(),
                         ensemble_temperature=T, roc_auc=a,
                         brier_calibrated=np.mean((pc - y) ** 2), brier_uncalibrated=np.mean((pu - y) ** 2),
                         ece15_calibrated=ece(y, pc), ece15_uncalibrated=ece(y, pu),
                         brier_constant_prevalence=y.mean() * (1 - y.mean())))
        for b, n, conf, acc in bin_table(y, pc):
            bins_rows.append(dict(training=src, test=tgt, family=fam, regimen=reg, bin=b, n=n,
                                  mean_predicted_fake_probability=conf, observed_fake_fraction=acc))

os.makedirs(OUT, exist_ok=True)
pd.DataFrame(rows).to_csv(os.path.join(OUT, 'calibration_ensembles.csv'), index=False)
pd.DataFrame(bins_rows).to_csv(os.path.join(OUT, 'reliability_bins.csv'), index=False)
print(f'cells: {len(rows)} | seed files checked: {seed_checks} | all ensemble AUCs reproduced exactly')
