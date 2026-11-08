"""Figure 11: train->test ROC-AUC matrices for the three fixed-recipe models (three-seed ensembles, plain variant).
Style constants copied from PKG/corrected_20261028_optionA/figures/make_figures_optionA.py (not imported; package untouched)."""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.patches import Rectangle

STATS = "/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/00_Shared/statistics_raw/"
OUT = "/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/figures/fig11_transfer_heatmap.png"
# ---- style constants (copied) ----
SURFACE = "#ffffff"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#898781"; GRID = "#e1e0d9"; AXIS = "#c3c2b7"; EMPTY = "#f0efec"
SEQ = LinearSegmentedColormap.from_list("seq_blue", [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
    "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"])
DS = ["ffpp_c23", "ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]
DS_SHORT = {"ffpp_c23": "C23", "ffpp_c40": "C40", "celeb_df_v2": "CDF", "deeperforensics_1_0": "DFo"}  # defined in the caption
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
    "axes.labelcolor": INK2, "xtick.color": AXIS, "ytick.color": AXIS, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE, "legend.frameon": False,
    "savefig.dpi": 300, "axes.unicode_minus": True})
AUC_NORM = Normalize(vmin=0.5, vmax=1.0, clip=True)

def text_on(rgb):
    r, g, b = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb[:3]]
    return SURFACE if 0.2126 * r + 0.7152 * g + 0.0722 * b < 0.36 else INK

rows = [r for r in csv.DictReader(open(STATS + "three_seed_mean_logit_ensemble.csv")) if r["variant"] == "plain"]
def matrix(fam):
    M = np.full((4, 4), np.nan)
    for r in rows:
        if r["family"] == fam and r["optimization_regimen"] == "fixed_no_bo":
            M[DS.index(r["training_dataset"]), DS.index(r["test_dataset"])] = float(r["roc_auc"])
    return M

MODELS = [("SwinFusion++", "swinfusionpp"), ("Swin-B", "swin_b"), ("Video Swin-B", "video_swin_b")]
mats = {lab: matrix(f) for lab, f in MODELS}
# self-check against values verified in Round 1 (m_spot1.py)
assert abs(mats["SwinFusion++"][0, 3] - 0.8261) < 5e-5 and abs(mats["Swin-B"][0, 3] - 0.5678) < 5e-5
assert abs(mats["Video Swin-B"][3, 2] - 0.6001) < 5e-5 and abs(mats["Swin-B"][3, 2] - 0.4593) < 5e-5
assert np.isnan(mats["SwinFusion++"][1, 0]) and np.sum(~np.isnan(mats["Swin-B"])) == 13

fig = plt.figure(figsize=(6.0, 2.75))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 0.05], hspace=0.42, wspace=0.10, left=0.075, right=0.99, top=0.93, bottom=0.14)
gap = 0.035
for k, (lab, _) in enumerate(MODELS):
    ax = fig.add_subplot(gs[0, k]); M = mats[lab]
    for i in range(4):
        for j in range(4):
            v = M[i, j]
            if np.isnan(v):
                ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap, facecolor=EMPTY, edgecolor="none"))
                ax.text(j + 0.5, i + 0.5, "—", ha="center", va="center", color=MUTED, fontsize=8)
                continue
            rgb = SEQ(AUC_NORM(v))
            ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap, facecolor=rgb, edgecolor="none"))
            ax.text(j + 0.5, i + 0.5, f"{v:.3f}", ha="center", va="center", color=text_on(rgb), fontsize=8,
                    fontweight="bold" if i == j else "normal")
    ax.set_xlim(0, 4); ax.set_ylim(4, 0); ax.set_aspect("equal")
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_xticks(np.arange(4) + 0.5, [DS_SHORT[d] for d in DS], fontsize=8)
    ax.set_yticks(np.arange(4) + 0.5, [DS_SHORT[d] for d in DS] if k == 0 else [], fontsize=8)
    ax.tick_params(length=0, pad=2)
    ax.set_xlabel("Test dataset", fontsize=8)
    if k == 0: ax.set_ylabel("Training dataset", fontsize=8)
    ax.set_title(lab, loc="left", fontsize=8.5, fontweight="bold", color=INK, pad=4)
cax = fig.add_subplot(gs[1, :])
pos = cax.get_position(); cax.set_position([pos.x0 + pos.width * 0.25, pos.y0, pos.width * 0.5, pos.height])
sm = plt.cm.ScalarMappable(cmap=SEQ, norm=AUC_NORM)
cb = fig.colorbar(sm, cax=cax, orientation="horizontal", ticks=np.arange(0.5, 1.01, 0.1))
cb.outline.set_visible(False); cb.ax.tick_params(length=0, labelsize=7.5, labelcolor=INK2)
cb.ax.set_xticklabels(["≤ 0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
cb.set_label("Video-level ROC-AUC", color=INK2, fontsize=8, labelpad=2)
fig.savefig(OUT, dpi=300)
print("wrote", OUT)
