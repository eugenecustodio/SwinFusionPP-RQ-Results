"""Figure 13 (3x3 transfer ROC curves) and Figure J1 (1x4 within-dataset ROC curves, zoomed), fixed-recipe
three-seed ensembles, from the statistician's tables/roc_points.csv. Self-checks: curve AUC (trapezoid) and the
operating point (FPR = FP/(FP+TN), TPR = recall) against 00_Shared/statistics_raw/three_seed_mean_logit_ensemble.csv."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from matplotlib.lines import Line2D

TEAM = "/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/"
STATS = "/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/"
SURFACE = "#ffffff"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#898781"; GRID = "#e1e0d9"; AXIS = "#c3c2b7"
MODELS = {"SwinFusion++": ("#2a78d6", "o", "-"), "Swin-B": ("#eb6834", "s", (0, (5, 2))), "Video Swin-B": ("#1baf7a", "^", (0, (1.2, 1.4)))}
FAM = {"SwinFusion++": "swinfusionpp", "Swin-B": "swin_b", "Video Swin-B": "video_swin_b"}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
    "axes.labelcolor": INK2, "xtick.color": AXIS, "ytick.color": AXIS, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
    "grid.color": GRID, "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE, "legend.frameon": False,
    "savefig.dpi": 300, "axes.unicode_minus": True})
ABBR = {"ffpp_c23": "C23", "ffpp_c40": "C40", "celeb_df_v2": "CDF", "deeperforensics_1_0": "DFo"}

R = pd.read_csv(TEAM + "tables/roc_points.csv")
E = pd.read_csv(STATS + "three_seed_mean_logit_ensemble.csv")
E = E[(E.variant == "plain") & (E.optimization_regimen == "fixed_no_bo")]
nchk = 0
for (tr, te, m), g in R.groupby(["training", "test", "model"]):
    e = E[(E.family == FAM[m]) & (E.training_dataset == tr) & (E.test_dataset == te)].iloc[0]
    c = g[g.point_type == "curve"].sort_values(["fpr", "tpr"])
    a = np.trapezoid(c.tpr.values, c.fpr.values)
    assert abs(a - e.roc_auc) < 1e-9 and abs(g.auc.iloc[0] - e.roc_auc) < 1e-12, (tr, te, m, a, e.roc_auc)
    op = g[g.point_type == "operating_point"].iloc[0]
    assert abs(op.fpr - e.fp / (e.fp + e.tn)) < 1e-12 and abs(op.tpr - e.recall) < 1e-12, (tr, te, m)
    nchk += 1
print(f"{nchk} model-cells checked: curve AUCs and operating points match the ensemble CSV")

def draw(ax, tr, te, zoom=None, auc_loc="lower right"):
    g0 = R[(R.training == tr) & (R.test == te)]
    if zoom is None:
        ax.plot([0, 1], [0, 1], color=MUTED, lw=0.7, ls=(0, (3, 3)), zorder=1)
    lines = []
    for m, (col, mk, ls) in MODELS.items():
        g = g0[g0.model == m]; c = g[g.point_type == "curve"].sort_values(["fpr", "tpr"])
        ax.plot(c.fpr, c.tpr, color=col, lw=1.3, ls=ls, zorder=2, drawstyle="default")
        op = g[g.point_type == "operating_point"].iloc[0]
        ax.plot(op.fpr, op.tpr, marker=mk, ms=5.5, mfc=col, mec=INK, mew=0.7, ls="none", zorder=4, clip_on=False)
        lines.append((m, g.auc.iloc[0], col))
    if zoom:
        ax.set_xlim(*zoom[0]); ax.set_ylim(*zoom[1])
    else:
        ax.set_xlim(0, 1); ax.set_ylim(0, 1.0)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True); ax.set_axisbelow(True)
    ax.tick_params(labelsize=7.5, length=0, pad=2)
    # AUCs in model color, lower-right
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    for k, (m, a, col) in enumerate(lines):
        ax.text(x1 - 0.03 * (x1 - x0), y0 + (0.05 + 0.105 * (2 - k)) * (y1 - y0), f"{a:.3f}", color=col,
                fontsize=8, ha="right", va="bottom", fontweight="bold")

legend_handles = [Line2D([], [], color=c, ls=ls, lw=1.5, marker=mk, ms=5.5, mec=INK, mew=0.7, label=m)
                  for m, (c, mk, ls) in MODELS.items()]

# ---------- Figure 13: 3 x 3 transfer grid
SRC = ["ffpp_c23", "celeb_df_v2", "deeperforensics_1_0"]
TGT = {"ffpp_c23": ["ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"],
       "celeb_df_v2": ["ffpp_c23", "ffpp_c40", "deeperforensics_1_0"],
       "deeperforensics_1_0": ["ffpp_c23", "ffpp_c40", "celeb_df_v2"]}
fig, axes = plt.subplots(3, 3, figsize=(6.0, 6.55), gridspec_kw=dict(wspace=0.12, hspace=0.32,
                         left=0.095, right=0.99, top=0.915, bottom=0.075))
for i, s in enumerate(SRC):
    for j, t in enumerate(TGT[s]):
        ax = axes[i, j]; draw(ax, s, t)
        ax.set_title(f"{ABBR[s]} → {ABBR[t]}", loc="left", fontsize=8.5, fontweight="bold", color=INK, pad=3)
        ax.set_xticks([0, 0.5, 1], ["0", "0.5", "1"] if i == 2 else [])
        ax.set_yticks([0, 0.5, 1], ["", "0.5", "1"] if j == 0 else [])
fig.supxlabel("False positive rate (1 − specificity)", fontsize=8, color=INK2, y=0.012)
fig.supylabel("True positive rate (recall)", fontsize=8, color=INK2, x=0.01)
fig.legend(handles=legend_handles, ncol=3, loc="upper left", bbox_to_anchor=(0.085, 0.995), fontsize=8,
           handletextpad=0.5, columnspacing=1.6, handlelength=2.6)
fig.savefig(TEAM + "figures/fig13_transfer_roc.png", dpi=300); plt.close(fig)
print("wrote fig13")

# ---------- Figure J1: 1 x 4 within-dataset (zoomed)
DS = ["ffpp_c23", "ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]
Z = ((0, 0.2), (0.8, 1.0))
fig, axes = plt.subplots(1, 4, figsize=(6.0, 2.05), gridspec_kw=dict(wspace=0.16, left=0.085, right=0.975, top=0.80, bottom=0.17))
for j, d in enumerate(DS):
    ax = axes[j]; draw(ax, d, d, zoom=Z)
    ax.set_title(ABBR[d], loc="left", fontsize=8.5, fontweight="bold", color=INK, pad=3)
    ax.set_xticks([0, 0.1, 0.2], ["", "0.1", "0.2"])
    ax.set_yticks([0.8, 0.9, 1.0], ["0.8", "0.9", "1.0"] if j == 0 else [])
fig.supxlabel("False positive rate (1 − specificity)", fontsize=8, color=INK2, y=0.0)
fig.supylabel("True positive rate", fontsize=8, color=INK2, x=0.005)
fig.legend(handles=legend_handles, ncol=3, loc="upper left", bbox_to_anchor=(0.075, 1.0), fontsize=8,
           handletextpad=0.5, columnspacing=1.6, handlelength=2.6)
fig.savefig(TEAM + "figures/figJ1_within_roc.png", dpi=300); plt.close(fig)
print("wrote figJ1")
