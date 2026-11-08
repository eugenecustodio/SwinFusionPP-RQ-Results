import sys, pandas as pd, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
b = pd.read_csv(sys.argv[1]); out = sys.argv[2]
INK, INK2, MUTED, GRID = '#0b0b0b', '#52514e', '#898781', '#e1e0d9'
M = [('swinfusionpp', 'SwinFusion++', '#2a78d6', 'o'), ('swin_b', 'Swin-B', '#eb6834', 's'), ('video_swin_b', 'Video Swin-B', '#1baf7a', '^')]
LAB = {'ffpp_c23': 'C23', 'ffpp_c40': 'C40', 'celeb_df_v2': 'Celeb-DF', 'deeperforensics_1_0': 'DFo'}
import numpy as np
cells = [('ffpp_c23', 'ffpp_c23'), ('ffpp_c40', 'ffpp_c40'), ('celeb_df_v2', 'celeb_df_v2'), ('deeperforensics_1_0', 'deeperforensics_1_0'),
         ('ffpp_c23', 'ffpp_c40'), ('ffpp_c23', 'celeb_df_v2'), ('ffpp_c23', 'deeperforensics_1_0'), ('celeb_df_v2', 'ffpp_c23')]
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.edgecolor': '#c3c2b7', 'axes.labelcolor': INK2,
                     'xtick.color': '#c3c2b7', 'ytick.color': '#c3c2b7', 'xtick.labelcolor': INK2, 'ytick.labelcolor': INK2,
                     'axes.spines.top': False, 'axes.spines.right': False, 'savefig.dpi': 300, 'savefig.bbox': 'tight'})
fig, axes = plt.subplots(2, 4, figsize=(7.6, 4.6), sharex=True, sharey=True)
fig.subplots_adjust(top=0.84, wspace=0.12, hspace=0.32)
for ax, (tr, te) in zip(axes.flat, cells):
    ax.plot([0, 1], [0, 1], color=MUTED, lw=0.8, ls='--', zorder=1)
    for fam, name, col, mk in M:
        d = b[(b.training == tr) & (b.test == te) & (b.family == fam) & (b.regimen == 'fixed_no_bo') & (b.n > 0)]
        ax.scatter(d.mean_predicted_fake_probability, d.observed_fake_fraction, s=4 + 5 * np.sqrt(d.n), color=col, marker=mk,
                   edgecolors='white', linewidths=0.6, alpha=0.85, label=name, zorder=2)
    ax.set_title(('Within ' + LAB[te]) if tr == te else f'{LAB[tr]} → {LAB[te]}', fontsize=7.5, color=INK, loc='left')
    ax.set_xticks([0, 0.5, 1], ['0', '0.5', '1']); ax.set_yticks([0, 0.5, 1], ['0', '0.5', '1'])
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.02, 1.02); ax.grid(True, color=GRID, lw=0.5); ax.set_axisbelow(True); ax.set_aspect('equal')
for ax in axes[1]: ax.set_xlabel('Predicted P(fake)')
for ax in axes[:, 0]: ax.set_ylabel('Observed fake fraction')
h, l = axes[0, 0].get_legend_handles_labels()
fig.legend(h, l, loc='upper left', bbox_to_anchor=(0.0, 0.935), ncol=3, fontsize=7, frameon=False, markerscale=0.6)
fig.text(0.0, 1.0, 'Reliability of the fixed-recipe three-seed ensembles (frozen source-validation temperature, 15 bins)', fontsize=9, fontweight='bold', color=INK)
fig.text(0.0, 0.955, 'Top: within-dataset.  Bottom: frozen transfer.  Dashed line = perfect calibration.  Marker area grows with the number of videos in the bin.', fontsize=7, color=INK2)
fig.savefig(out); print('wrote', out)
