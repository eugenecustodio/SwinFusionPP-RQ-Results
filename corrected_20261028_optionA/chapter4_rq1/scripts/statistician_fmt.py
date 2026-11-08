"""Shared labels, formatting and data assembly for the production tables (statistician)."""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/scripts')
from statistician_common import *

TAB = SCR + '/ch4/team/tables'
MINUS = '−'
ARROW = '→'
SHORT = {'ffpp_c23': 'C23', 'ffpp_c40': 'C40', 'celeb_df_v2': 'CDF', 'deeperforensics_1_0': 'DFo'}
LONG = {'ffpp_c23': 'FF++ C23', 'ffpp_c40': 'FF++ C40', 'celeb_df_v2': 'Celeb-DF v2', 'deeperforensics_1_0': 'DeeperForensics-1.0'}
WITHIN = [(d, d) for d in DS]
TRANSFER = [('ffpp_c23', 'ffpp_c40'), ('ffpp_c23', 'celeb_df_v2'), ('ffpp_c23', 'deeperforensics_1_0'),
            ('celeb_df_v2', 'ffpp_c23'), ('celeb_df_v2', 'ffpp_c40'), ('celeb_df_v2', 'deeperforensics_1_0'),
            ('deeperforensics_1_0', 'ffpp_c23'), ('deeperforensics_1_0', 'ffpp_c40'), ('deeperforensics_1_0', 'celeb_df_v2')]
CELLS = WITHIN + TRANSFER
MODELS = {'SF++F': ('swinfusionpp', 'fixed_no_bo'), 'SwinB': ('swin_b', 'fixed_no_bo'),
          'VSB': ('video_swin_b', 'fixed_no_bo'), 'SF++BO': ('swinfusionpp', 'dataset_specific_bo')}
MLABEL = {'SF++F': 'SwinFusion++', 'SwinB': 'Swin-B', 'VSB': 'Video Swin-B', 'SF++BO': 'SwinFusion++ (BO)'}
PKGKEY = {'SF++F': 'swinfusionpp__fixed_no_bo', 'SwinB': 'swin_b__fixed_no_bo', 'VSB': 'video_swin_b__fixed_no_bo',
          'SF++BO': 'swinfusionpp__dataset_specific_bo'}
KEY2M = {v: k for k, v in PKGKEY.items()}
FAMNAME = {'RQ1_architecture': 'Architecture, within (m = 8)', 'RQ6_architecture': 'Architecture, transfer (m = 18)',
           'RQ1_configured_system': 'Configured system, within (m = 8)', 'RQ6_configured_system': 'Configured system, transfer (m = 18)',
           'RQ1_optimization_effect': 'Optimization effect, within (m = 4)', 'RQ6_optimization_effect': 'Optimization effect, transfer (m = 9)'}
FAMM = {'RQ1_architecture': 8, 'RQ6_architecture': 18, 'RQ1_configured_system': 8, 'RQ6_configured_system': 18,
        'RQ1_optimization_effect': 4, 'RQ6_optimization_effect': 9}


def cond(src, tgt):
    return f'{SHORT[src]} {ARROW} {SHORT[tgt]}'


def m_(s):
    return s.replace('-', MINUS)


def num(x, d=4):
    return m_(f'{x:.{d}f}')


def sgn(x, d=4):
    s = f'{x:+.{d}f}'
    if float(s) == 0:
        s = f'{0:.{d}f}'
    return m_(s)


def ci(lo, hi, d=4, signed=True):
    f = sgn if signed else num
    return f'[{f(lo, d)}, {f(hi, d)}]'


def pct(x):
    return num(100 * x, 2)


def p_raw(p):
    return '< 0.001' if p < 0.001 else f'{p:.3f}'


def p_holm(h, m):
    """Holm p: family floor (m/5001) written '< 0.005' when the floor is below 0.005; else 3 decimals."""
    floor = m / (B + 1)
    if abs(h - floor) < 1e-12 and floor < 0.005:
        return '< 0.005'
    return f'{h:.3f}'


def load_all():
    data = {}
    for src, tgt in CELLS:
        for mk, (fam, reg) in MODELS.items():
            df, thr, T, st = load_cell(fam, reg, src, tgt)
            df['pred'] = (df.z.values >= thr).astype(int)
            data[(mk, src, tgt)] = dict(df=df, thr=thr, T=T, seedthr=st)
    return data


def paired_tests():
    pt = pd.read_csv(PKG + '/corrected_20261028_optionA/paired_tests_optionA.csv')
    pt = pt[pt.family_optionA.isin(FAMM)].copy()
    pt['ma'] = pt.model_a.map(KEY2M); pt['mb'] = pt.model_b.map(KEY2M)
    return pt


def get_test(pt, a, b, src, tgt):
    r = pt[(pt.ma == a) & (pt.mb == b) & (pt.training_dataset == src) & (pt.test_dataset == tgt)]
    assert len(r) == 1, (a, b, src, tgt)
    return r.iloc[0]
