"""Figure 12: forest plot of the 26 principal paired ΔROC-AUCs (fixed recipe), from the statistician's tables/fig12_forest.csv.
Cross-checked against PKG paired_tests_optionA.csv. Style constants copied from make_figures_optionA.py."""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

TEAM = "/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/"
PKG = "/home/eugenecustodio/Desktop/Results/SwinFusionPP_RQ_Results_20261004/SwinFusionPP_RQ_Results/corrected_20261028_optionA/"
OUT = TEAM + "figures/fig12_forest.png"
SURFACE = "#ffffff"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#898781"; GRID = "#e1e0d9"; AXIS = "#c3c2b7"
MODELS = {"Swin-B": ("#eb6834", "s"), "Video Swin-B": ("#1baf7a", "^")}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
    "axes.labelcolor": INK2, "xtick.color": AXIS, "ytick.color": AXIS, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
    "grid.color": GRID, "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE, "legend.frameon": False,
    "savefig.dpi": 300, "axes.unicode_minus": True})
MINUS = "−"

rows = list(csv.DictReader(open(TEAM + "tables/fig12_forest.csv", encoding="utf-8")))
assert len(rows) == 26
# cross-check every row against the package
ref = {(r["model_b"].split("__")[0], r["training_dataset"], r["test_dataset"]): r
       for r in csv.DictReader(open(PKG + "paired_tests_optionA.csv"))
       if r["family_optionA"] in ("RQ1_architecture", "RQ6_architecture")}
CMP = {"Swin-B": "swin_b", "Video Swin-B": "video_swin_b"}
for r in rows:
    p = ref[(CMP[r["comparator"]], r["training"], r["test"])]
    for a, b in (("delta_auc", "auc_difference"), ("ci_low", "ci_low"), ("ci_high", "ci_high"), ("holm_p", "holm_optionA")):
        assert abs(float(r[a]) - float(p[b])) < 1e-12, (r, a)
    assert (r["holm_significant"] == "True") == (float(p["holm_optionA"]) < 0.05)
print("forest CSV matches paired_tests_optionA.csv for all 26 rows;",
      sum(r["holm_significant"] == "True" for r in rows), "significant")

ABBR = {"ffpp_c23": "C23", "ffpp_c40": "C40", "celeb_df_v2": "CDF", "deeperforensics_1_0": "DFo"}
def label(r):
    return ABBR[r["training"]] if r["panel"] == "within" else f"{ABBR[r['training']]} → {ABBR[r['test']]}"

panels = {"within": [], "transfer": []}
for r in sorted(rows, key=lambda r: int(r["order"])):
    key = label(r)
    if not panels[r["panel"]] or panels[r["panel"]][-1][0] != key:
        panels[r["panel"]].append((key, {}))
    panels[r["panel"]][-1][1][r["comparator"]] = r

fig = plt.figure(figsize=(6.0, 5.0))
gs = fig.add_gridspec(2, 1, height_ratios=[4, 9], hspace=0.42, left=0.13, right=0.98, top=0.90, bottom=0.08)
XL = {"within": (-0.0125, 0.0105), "transfer": (-0.105, 0.32)}
XT = {"within": np.arange(-0.012, 0.0101, 0.004), "transfer": np.arange(-0.1, 0.301, 0.1)}
DEC = {"within": 3, "transfer": 1}
TITLE = {"within": "(a) Within dataset (m = 8)", "transfer": "(b) Frozen transfer (m = 18)"}
OFF = {"Swin-B": -0.17, "Video Swin-B": 0.17}
for k, pan in enumerate(["within", "transfer"]):
    ax = fig.add_subplot(gs[k])
    groups = panels[pan]
    for i, (key, d) in enumerate(groups):
        for cmpname, r in d.items():
            c, mk = MODELS[cmpname]
            y = i + OFF[cmpname]
            lo, hi, v = float(r["ci_low"]), float(r["ci_high"]), float(r["delta_auc"])
            ax.plot([lo, hi], [y, y], color=c, lw=1.5, solid_capstyle="butt", zorder=2)
            sig = r["holm_significant"] == "True"
            ax.plot(v, y, marker=mk, ms=6, mfc=c if sig else SURFACE, mec=c, mew=1.3, ls="none", zorder=3)
    ax.axvline(0, color=INK2, lw=0.8, ls=(0, (4, 3)), zorder=1)
    if pan == "transfer":
        for b in (2.5, 5.5):
            ax.axhline(b, color=GRID, lw=0.8, zorder=0)
    ax.set_yticks(range(len(groups)), [g[0] for g in groups], fontsize=8)
    ax.set_ylim(len(groups) - 0.5, -0.5)
    ax.set_xlim(*XL[pan]); ax.set_xticks(XT[pan])
    ax.xaxis.set_major_formatter(plt.FuncFormatter(
        lambda v, _p, nd=DEC[pan]: (f"{v:+.{nd}f}" if abs(v) > 1e-12 else f"{0:.{nd}f}").replace("-", MINUS)))
    ax.tick_params(axis="both", labelsize=8, length=0, pad=3)
    ax.xaxis.grid(True); ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.set_title(TITLE[pan], loc="left", fontsize=8.5, fontweight="bold", color=INK, pad=4)
    ax.set_xlabel("ΔROC-AUC, SwinFusion++ minus comparator", fontsize=8)
handles = [Line2D([], [], color=MODELS["Swin-B"][0], marker="s", ms=6, lw=1.5, label="vs Swin-B"),
           Line2D([], [], color=MODELS["Video Swin-B"][0], marker="^", ms=6, lw=1.5, label="vs Video Swin-B"),
           Line2D([], [], color=INK2, marker="o", ms=6, mfc=INK2, ls="none", label="Holm p < 0.05"),
           Line2D([], [], color=INK2, marker="o", ms=6, mfc=SURFACE, ls="none", label="not significant")]
fig.legend(handles=handles, ncol=4, loc="upper left", bbox_to_anchor=(0.11, 0.995), fontsize=8,
           handletextpad=0.4, columnspacing=1.3)
fig.savefig(OUT, dpi=300)
print("wrote", OUT)
