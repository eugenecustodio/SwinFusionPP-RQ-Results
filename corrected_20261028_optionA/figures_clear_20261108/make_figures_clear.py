#!/usr/bin/env python3
"""Clear, print-ready redraws of every current SwinFusion++ results figure (2026-11-08).

Reads only CSV files inside this results package and writes PNGs next to this script.
Nothing outside this folder is changed. Every figure is 6.0 in wide or less at 300 dpi, so
text keeps its true size when placed at full thesis-page width (all text is 8 pt or larger).

Usage:  python make_figures_clear.py        (needs matplotlib, numpy, pandas)

Chart types are deliberately plain:
  * colour-coded number tables for train -> test results
  * horizontal bars for differences (right of 0 = SwinFusion++ higher)
  * horizontal bars for comparisons with large gaps
  * dots with 95% intervals, or dots against reported ranges, where bars from 0 would hide the values
  * simple line charts for ROC curves and calibration

RQ2 is drawn from the verified Tier A table (chapter4_rq1/rq2_expansion/tables/T10.csv), not from
RQ2/results/table2_published_AB.csv, which labels some cross-manipulation, ablation and
hidden-set values as within-dataset.
"""
import csv
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
OPTA = HERE.parent
PKG = OPTA.parent
STATS = PKG / "00_Shared" / "statistics_raw"
CH4 = OPTA / "chapter4_rq1" / "tables"
T10 = OPTA / "chapter4_rq1" / "rq2_expansion" / "tables" / "T10.csv"
CAL = OPTA / "calibration"
DPI = 300
W = 6.0

SURFACE, INK, INK2, MUTED, GRID, AXIS, EMPTY, BAND = ("#ffffff", "#0b0b0b", "#52514e", "#898781", "#e1e0d9",
                                                      "#c3c2b7", "#f0efec", "#f6f5f1")
BLUE, ORANGE, GREEN, PURPLE, RED = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7", "#e34948"
NS = "#c9c7bf"  # bars that are not statistically significant
MODELS = {"SwinFusion++": (BLUE, "o", "-"), "Swin-B": (ORANGE, "s", (0, (5, 2))),
          "Video Swin-B": (GREEN, "^", (0, (1.2, 1.4)))}
FAM = {"SwinFusion++": "swinfusionpp", "Swin-B": "swin_b", "Video Swin-B": "video_swin_b"}
SEQ = LinearSegmentedColormap.from_list("seq_blue", [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
    "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"])
DIV = LinearSegmentedColormap.from_list("div_red_blue", [
    "#a32d2c", "#e34948", "#f4b2ae", "#f0efec", "#9ec5f4", "#3987e5", "#184f95"])
AUC_NORM = Normalize(vmin=0.5, vmax=1.0, clip=True)

DS = ["ffpp_c23", "ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]
SHORT = {"ffpp_c23": "C23", "ffpp_c40": "C40", "celeb_df_v2": "CDF", "deeperforensics_1_0": "DFo"}
TWO = {"ffpp_c23": "FF++\nC23", "ffpp_c40": "FF++\nC40", "celeb_df_v2": "Celeb-\nDF v2",
       "deeperforensics_1_0": "Deeper-\nForensics"}
LONG = {"ffpp_c23": "FF++ C23 (HQ)", "ffpp_c40": "FF++ C40 (LQ)", "celeb_df_v2": "Celeb-DF v2",
        "deeperforensics_1_0": "DeeperForensics-1.0"}
ABBR = "C23 / C40 = FaceForensics++ high / low quality  ·  CDF = Celeb-DF v2  ·  DFo = DeeperForensics-1.0"
MINUS = "−"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8, "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
    "axes.labelcolor": INK2, "axes.labelsize": 8, "axes.titlesize": 8.5, "axes.titlecolor": INK,
    "axes.spines.top": False, "axes.spines.right": False, "xtick.color": AXIS, "ytick.color": AXIS,
    "xtick.labelcolor": INK2, "ytick.labelcolor": INK2, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "grid.color": GRID, "grid.linewidth": 0.6, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "legend.frameon": False, "legend.fontsize": 8, "axes.unicode_minus": True,
})


# ------------------------------------------------------------------ helpers
def rd(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


ENS = [r for r in rd(STATS / "three_seed_mean_logit_ensemble.csv") if r["variant"] == "plain"]
PAIRED = rd(OPTA / "paired_tests_optionA.csv")
TIER_B = rd(STATS / "tier_b_paired_effects.csv")
R_REG = {"fixed": "fixed_no_bo", "bo": "dataset_specific_bo"}


def ens(fam, reg, tr, te):
    for r in ENS:
        if (r["family"], r["optimization_regimen"], r["training_dataset"], r["test_dataset"]) == (fam, reg, tr, te):
            return r
    return None


def paired(family, a, b, tr, te):
    for r in PAIRED:
        if (r["family_optionA"], r["model_a"], r["model_b"], r["training_dataset"], r["test_dataset"]) == (family, a, b, tr, te):
            return r
    return None


def signed(v, nd):
    s = f"{v:+.{nd}f}"
    if float(s) == 0:
        s = f"{0:.{nd}f}"
    return s.replace("-", MINUS)


def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def best_text(rgb):
    """White or ink: whichever has the higher contrast against the fill."""
    L = 0.2126 * _lin(rgb[0]) + 0.7152 * _lin(rgb[1]) + 0.0722 * _lin(rgb[2])
    ink = 0.2126 * _lin(0x0b / 255) + 0.7152 * _lin(0x0b / 255) + 0.0722 * _lin(0x0b / 255)
    return SURFACE if 1.05 / (L + 0.05) >= (L + 0.05) / (ink + 0.05) else INK


def fig_in(w, h):
    return plt.figure(figsize=(w, h))


def ax_in(fig, l, b, w, h, **kw):
    fw, fh = fig.get_size_inches()
    return fig.add_axes([l / fw, b / fh, w / fw, h / fh], **kw)


def text_in(fig, x, y, s, **kw):
    fw, fh = fig.get_size_inches()
    kw.setdefault("color", INK2)
    kw.setdefault("fontsize", 8)
    fig.text(x / fw, y / fh, s, **kw)


def head(fig, title, sub=None, x=0.04):
    _, fh = fig.get_size_inches()
    text_in(fig, x, fh - 0.06, title, ha="left", va="top", fontsize=9.5, fontweight="bold", color=INK)
    if sub:
        text_in(fig, x, fh - 0.27, sub, ha="left", va="top")


def save(fig, *parts):
    out = HERE.joinpath(*parts)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    print("wrote", out.relative_to(HERE))


# ------------------------------------------------------------------ colour-coded number tables
def auc_matrix(model, reg="fixed"):
    M = np.full((4, 4), np.nan)
    for i, tr in enumerate(DS):
        for j, te in enumerate(DS):
            r = ens(FAM[model], R_REG[reg], tr, te)
            if r:
                M[i, j] = float(r["roc_auc"])
    return M


def matrix(ax, M, cmap, norm, fmt, ticks, ylabels=True, stars=None, fs=8, empty="—", xlab="Tested on", ylab="Trained on"):
    gap = 0.035
    for i in range(4):
        for j in range(4):
            v = M[i, j]
            if np.isnan(v):
                ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap, fc=EMPTY, ec="none"))
                ax.text(j + 0.5, i + 0.5, empty, ha="center", va="center", color=INK2, fontsize=fs)
                continue
            rgb = cmap(norm(v))
            ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap, fc=rgb, ec="none"))
            ax.text(j + 0.5, i + 0.5, fmt(v) + (stars[i, j] if stars is not None else ""), ha="center", va="center",
                    color=best_text(rgb), fontsize=fs, fontweight="bold" if i == j else "normal")
    ax.set_xlim(0, 4)
    ax.set_ylim(4, 0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks(np.arange(4) + 0.5, [ticks[d] for d in DS])
    ax.set_yticks(np.arange(4) + 0.5, [ticks[d] for d in DS] if ylabels else [])
    ax.tick_params(length=0, pad=2)
    ax.set_xlabel(xlab, labelpad=3)
    if ylabels:
        ax.set_ylabel(ylab, labelpad=3)


def cbar(fig, cax, cmap, norm, ticks, label, orient="horizontal", extend="neither", fmt=None):
    cb = fig.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), cax=cax, orientation=orient, ticks=ticks,
                      extend=extend, extendfrac=0.04)
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=0, labelsize=8, labelcolor=INK2, pad=2)
    if fmt:
        (cb.ax.xaxis if orient == "horizontal" else cb.ax.yaxis).set_major_formatter(FuncFormatter(fmt))
    cb.set_label(label, color=INK2, fontsize=8, labelpad=3)


def heat3(path, title=None, reg="fixed", names=None):
    pw = 1.7
    top = 0.26 + (0.3 if title else 0)
    H = top + pw + 0.5 + 0.11 + 0.38 + 0.4
    fig = fig_in(W, H)
    if title:
        head(fig, title)
    bot = H - top - pw
    for k, m in enumerate(["SwinFusion++", "Swin-B", "Video Swin-B"]):
        ax = ax_in(fig, 0.58 + k * (pw + 0.1), bot, pw, pw)
        matrix(ax, auc_matrix(m, reg if m == "SwinFusion++" else "fixed"), SEQ, AUC_NORM, lambda v: f"{v:.3f}", SHORT, ylabels=(k == 0))
        ax.set_title((names or {}).get(m, m), loc="left", fontweight="bold", pad=3)
    cax = ax_in(fig, 2.05, bot - 0.5 - 0.11, 2.4, 0.11)
    cbar(fig, cax, SEQ, AUC_NORM, np.arange(0.5, 1.01, 0.1), "ROC-AUC  (0.5 = random guessing, 1.0 = perfect)", extend="min",
         fmt=lambda v, _: f"{v:.1f}")
    text_in(fig, 0.04, 0.2, "Bold = same dataset for training and testing.   — = combination not tested.", va="bottom")
    text_in(fig, 0.04, 0.04, ABBR, va="bottom")
    save(fig, *path)


def heat1(path, model, reg, title):
    pw = 3.0
    H = 0.62 + pw + 0.55 + 0.58
    fig = fig_in(5.0, H)
    head(fig, title, "ROC-AUC when trained on one dataset (row) and tested on another (column).")
    bot = 0.58 + 0.55
    ax = ax_in(fig, 0.78, bot, pw, pw)
    matrix(ax, auc_matrix(model, reg), SEQ, AUC_NORM, lambda v: f"{v:.3f}", TWO, fs=9, empty="not tested")
    cax = ax_in(fig, 3.95, bot, 0.14, pw)
    cbar(fig, cax, SEQ, AUC_NORM, np.arange(0.5, 1.01, 0.1), "ROC-AUC  (0.5 = random guessing, 1.0 = perfect)", orient="vertical",
         extend="min", fmt=lambda v, _: f"{v:.1f}")
    key = "Bold = same dataset for training and testing. Darker = better."
    text_in(fig, 0.04, 0.22, key, va="bottom")
    text_in(fig, 0.04, 0.06, ("BO-selected = settings tuned for each dataset with Bayesian optimization."
                              if reg == "bo" else "Fixed recipe = same training settings on every dataset."), va="bottom")
    save(fig, *path)


def delta_heat(path, a, fams, title):
    pw = 2.5
    H = 0.62 + pw + 0.55 + 0.11 + 0.38 + 0.56
    fig = fig_in(W, H)
    head(fig, title, "Each cell = SwinFusion++ ROC-AUC minus the other model's ROC-AUC.")
    bot = H - 0.62 - pw
    lim = 0.26
    norm = Normalize(vmin=-lim, vmax=lim, clip=True)
    for k, (base, name) in enumerate(zip(["swin_b__fixed_no_bo", "video_swin_b__fixed_no_bo"], ["Swin-B", "Video Swin-B"])):
        M = np.full((4, 4), np.nan)
        S = np.full((4, 4), "", dtype=object)
        for i, tr in enumerate(DS):
            for j, te in enumerate(DS):
                r = paired(fams[0] if tr == te else fams[1], a, base, tr, te)
                if r:
                    M[i, j] = float(r["auc_difference"])
                    S[i, j] = "*" if float(r["holm_optionA"]) < 0.05 else ""
        ax = ax_in(fig, 0.74 + k * (pw + 0.14), bot, pw, pw)
        matrix(ax, M, DIV, norm, lambda v: signed(v, 3), TWO, ylabels=(k == 0), stars=S)
        ax.set_title(f"SwinFusion++ minus {name}", loc="left", fontweight="bold", pad=3)
    cax = ax_in(fig, 1.9, bot - 0.55 - 0.11, 2.9, 0.11)
    cbar(fig, cax, DIV, norm, [-0.2, -0.1, 0, 0.1, 0.2], "Difference in ROC-AUC  (blue = SwinFusion++ higher, red = other model higher)",
         fmt=lambda v, _: signed(v, 1))
    text_in(fig, 0.04, 0.2, "* = statistically significant after correcting for multiple comparisons (Holm p < 0.05).", va="bottom")
    text_in(fig, 0.04, 0.04, "Bold = same dataset for training and testing.", va="bottom")
    save(fig, *path)


# ------------------------------------------------------------------ dots with 95% intervals
def within_ci(path, reg, name, title):
    H = 3.5
    fig = fig_in(W, H)
    head(fig, title, "Higher is better. Vertical lines are 95% confidence intervals. The y-axis starts at 0.975.")
    ax = ax_in(fig, 0.62, 0.52, 5.3, 2.28)
    for m, o in zip(["SwinFusion++", "Swin-B", "Video Swin-B"], [-0.22, 0, 0.22]):
        c, mk, _ = MODELS[m]
        for i, d in enumerate(DS):
            r = ens(FAM[m], R_REG[reg] if m == "SwinFusion++" else "fixed_no_bo", d, d)
            ax.plot([i + o, i + o], [float(r["roc_auc_ci_low"]), float(r["roc_auc_ci_high"])], color=c, lw=1.8,
                    solid_capstyle="round", zorder=2)
            ax.plot(i + o, float(r["roc_auc"]), marker=mk, ms=7, color=c, mec=SURFACE, mew=1.2, ls="none", zorder=3)
    labels = []
    for d in DS:
        n = int(ens("swinfusionpp", "fixed_no_bo", d, d)["analyzed_videos"])
        labels.append(f"{LONG[d]}\n{n} test videos")
    ax.set_xticks(range(4), labels)
    ax.tick_params(axis="x", length=0, pad=4)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(-0.55, 3.55)
    ax.set_ylim(0.975, 1.0012)
    ax.set_yticks(np.arange(0.975, 1.0001, 0.005))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.3f}"))
    ax.set_ylabel("ROC-AUC")
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    handles = [Line2D([], [], color=MODELS[m][0], marker=MODELS[m][1], ms=7, mec=SURFACE, lw=1.8, label=(name if m == "SwinFusion++" else m))
               for m in ["SwinFusion++", "Swin-B", "Video Swin-B"]]
    fig.legend(handles=handles, ncol=3, loc="upper left", bbox_to_anchor=(0.62 / W, 1 - 0.46 / H), handletextpad=0.5,
               columnspacing=1.6, borderaxespad=0)
    save(fig, *path)


# ------------------------------------------------------------------ difference bars
def bar_color(p, d, against):
    if p >= 0.05:
        return NS
    return BLUE if d > 0 else against


def row_bars(ax, y, d, lo, hi, p, against, h=0.62):
    ax.barh(y, d, height=h, color=bar_color(p, d, against), edgecolor="none", zorder=2)
    ax.plot([lo, hi], [y, y], color=INK, lw=0.9, zorder=3, solid_capstyle="butt")


def fig12():
    rows = [r for r in rd(CH4 / "fig12_forest.csv")]
    assert len(rows) == 26
    H = 5.86
    fig = fig_in(W, H)
    handles = [Patch(fc=BLUE, label="SwinFusion++ significantly higher"), Patch(fc=NS, label="No significant difference"),
               Line2D([], [], color=INK, lw=0.9, label="95% interval")]
    fig.legend(handles=handles, ncol=3, loc="upper left", bbox_to_anchor=(0.04 / W, 1 - 0.04 / H), handlelength=1.2,
               handletextpad=0.5, columnspacing=1.5, borderaxespad=0)
    text_in(fig, 0.04, H - 0.28, "Bar = SwinFusion++ minus other model. Right of 0: SwinFusion++ higher; left of 0: other model higher.",
            va="top")
    panels = {"within": [], "transfer": []}
    for r in sorted(rows, key=lambda r: int(r["order"])):
        k = SHORT[r["training"]] if r["panel"] == "within" else f"{SHORT[r['training']]} → {SHORT[r['test']]}"
        if not panels[r["panel"]] or panels[r["panel"]][-1][0] != k:
            panels[r["panel"]].append((k, {}))
        panels[r["panel"]][-1][1][r["comparator"]] = r
    spec = {"within": dict(top=H - 0.82, title="(a) Trained and tested on the same dataset (note the much narrower scale)",
                           xl=(-0.0125, 0.0185), xt=[-0.01, 0, 0.01], nd=3, rowh=0.27, offs=0.0007),
            "transfer": dict(top=H - 0.82 - 1.08 - 0.82, title="(b) Trained on one dataset, tested on another (no retraining)",
                             xl=(-0.125, 0.43), xt=[-0.1, 0, 0.1, 0.2, 0.3], nd=1, rowh=0.27, offs=0.012)}
    left, pw, gap = 0.82, 2.44, 0.18
    for pan, s in spec.items():
        g = panels[pan]
        h = s["rowh"] * len(g)
        text_in(fig, 0.04, s["top"] + 0.26, s["title"], va="bottom", fontsize=8.5, fontweight="bold", color=INK)
        for k, cmpn in enumerate(["Swin-B", "Video Swin-B"]):
            ax = ax_in(fig, left + k * (pw + gap), s["top"] - h, pw, h)
            for i, (lab, d) in enumerate(g):
                if i % 2 == 0:
                    ax.axhspan(i - 0.5, i + 0.5, color=BAND, zorder=0, lw=0)
                r = d[cmpn]
                v, lo, hi, p = float(r["delta_auc"]), float(r["ci_low"]), float(r["ci_high"]), float(r["holm_p"])
                assert (r["holm_significant"] == "True") == (p < 0.05)
                row_bars(ax, i, v, lo, hi, p, MODELS[cmpn][0])
                ax.text(s["xl"][1], i, signed(v, 3), ha="right", va="center", fontsize=8, color=INK2, zorder=4)
            ax.axvline(0, color=INK2, lw=0.8, zorder=2.5)
            ax.set_xlim(*s["xl"])
            ax.set_ylim(len(g) - 0.5, -0.5)
            ax.set_xticks(s["xt"])
            ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _p, nd=s["nd"]: "0" if abs(v) < 1e-12 else signed(v, nd)))
            ax.tick_params(axis="both", length=0, pad=3)
            ax.xaxis.grid(True)
            ax.set_axisbelow(True)
            ax.spines["left"].set_visible(False)
            ax.set_yticks(range(len(g)), [x[0] for x in g] if k == 0 else [])
            ax.set_title(f"vs {cmpn}", loc="left", fontweight="bold", pad=3)
            ax.set_xlabel("Difference in ROC-AUC", labelpad=3)
    text_in(fig, 0.04, 0.04, ABBR, va="bottom")
    save(fig, "chapter4", "fig12_forest.png")


def effect_chart(path, title, sub, rows, xlabel, cue, keys, tick_nd, ticks, against=RED, label_w=1.9):
    n = len(rows)
    rh = 0.285
    top, bot = 0.62 + 0.36, 0.5 + 0.17 * len(keys) + 0.04
    H = top + rh * n + bot
    fig = fig_in(W, H)
    head(fig, title, sub)
    pw = 1.6
    table_x = label_w + pw + 0.1
    ax = ax_in(fig, label_w, bot, pw, rh * n)
    span = 0
    for y, r in enumerate(rows):
        if r[0] == "header":
            ax.text((0.04 - label_w) / pw, y, r[1], transform=ax.get_yaxis_transform(), ha="left", va="center", fontweight="bold",
                    color=INK, fontsize=8, clip_on=False, zorder=6, bbox=dict(fc=SURFACE, ec="none", pad=1.2))
            continue
        label, d, lo, hi, p = r
        span = max(span, abs(lo), abs(hi))
        row_bars(ax, y, d, lo, hi, p, against)
        ax.text(-0.06, y, label, transform=ax.get_yaxis_transform(), ha="right", va="center", color=INK2, fontsize=8, clip_on=False)
        sig = p < 0.05
        txt = f"{signed(d, 4)} [{signed(lo, 4)}, {signed(hi, 4)}]"
        ax.text((table_x - label_w) / pw, y, txt, transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=8,
                family="DejaVu Sans Mono", color=INK2, clip_on=False)
        ax.text((W - 0.04 - label_w) / pw, y, f"{p:.3f}", transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8,
                family="DejaVu Sans Mono", color=INK if sig else INK2, fontweight="bold" if sig else "normal", clip_on=False)
    lim = span * 1.18
    ax.set_xlim(-lim, lim)
    ax.set_ylim(n - 0.5, -0.5)
    ax.axvline(0, color=INK2, lw=0.8, zorder=2.5)
    ax.tick_params(axis="y", left=False, labelleft=False)
    ax.spines["left"].set_visible(False)
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", length=0, pad=3)
    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: "0" if abs(v) < 1e-12 else signed(v, tick_nd)))
    ax.set_xlabel(xlabel, labelpad=3)
    yc = H - top + 0.03
    text_in(fig, label_w, yc, cue[0], ha="left", va="bottom", fontsize=8)
    text_in(fig, label_w + pw, yc, cue[1], ha="right", va="bottom", fontsize=8)
    text_in(fig, table_x, yc, "Difference [95% CI]", va="bottom", fontweight="bold", color=INK)
    text_in(fig, W - 0.04, yc, "p (Holm)", va="bottom", ha="right", fontweight="bold", color=INK)
    for k, line in enumerate(keys):
        text_in(fig, 0.04, 0.04 + 0.17 * (len(keys) - 1 - k), line, va="bottom")
    save(fig, *path)


CTRL = {"capacity_control__fixed_no_bo": "vs capacity control", "topology_control__fixed_no_bo": "vs topology control"}
CTRL_KEYS = ["Capacity control: same size (±5% parameters), separate layers per stream, no attention between streams.",
             "Topology control: same stages, alignment and joint readout, with the exchange block removed.",
             "Blue: SwinFusion++ significantly higher. Red: control significantly higher. Gray: not significant."]


def rq4_controls():
    rows = []
    for b, lbl in CTRL.items():
        r = paired("RQ4_controls", "swinfusionpp__fixed_no_bo", b, "ffpp_c23", "ffpp_c23")
        rows.append((lbl, float(r["auc_difference"]), float(r["ci_low"]), float(r["ci_high"]), float(r["holm_optionA"])))
    effect_chart(("RQ4", "fig1_controls_forest.png"), "SwinFusion++ vs. matched control models on FF++ C23",
                 "Trained and tested on FF++ C23 (280 test videos), fixed recipe, three-seed ensembles.", rows,
                 "SwinFusion++ minus control", ("← control\n    higher", "SwinFusion++\nhigher →"), CTRL_KEYS, 3, [-0.005, 0, 0.005])


def rq4_transfer():
    rows = []
    n = {d: int(ens("swinfusionpp", "fixed_no_bo", d, d)["analyzed_videos"]) for d in DS}
    for te in ["ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]:
        rows.append(("header", f"{LONG[te]} ({n[te]} videos)"))
        for b, lbl in CTRL.items():
            r = paired("RQ4_controls_transfer", "swinfusionpp__fixed_no_bo", b, "ffpp_c23", te)
            rows.append((lbl, float(r["auc_difference"]), float(r["ci_low"]), float(r["ci_high"]), float(r["holm_optionA"])))
    effect_chart(("RQ4", "fig1b_controls_transfer_forest.png"), "SwinFusion++ vs. matched control models on other datasets",
                 "Trained on FF++ C23, tested on another dataset with no retraining; fixed recipe, three-seed ensembles.", rows,
                 "SwinFusion++ minus control", ("← control\n    higher", "SwinFusion++\nhigher →"), CTRL_KEYS, 2, [-0.05, 0, 0.05])


def rq4_tier_b():
    L = {"tierb_one_directional": "One-directional attention\n(S ← V only)", "tierb_no_gate": "No gates (all gates = 1)",
         "tierb_no_agreement": "No agreement features\n(|S−V|, S⊙V)", "tierb_stages_34_only": "Exchange in stages 3–4 only"}
    rows = [(L[r["model_a"]], float(r["auc_difference"]), float(r["ci_low"]), float(r["ci_high"]), float(r["holm_adjusted_p"])) for r in TIER_B]
    effect_chart(("RQ4", "fig2_tier_b_forest.png"), "Exploratory ablations: what happens when one part is changed",
                 "Change in ROC-AUC against the full SwinFusion++ on FF++ C23 (280 test videos).", rows,
                 "Variant minus full model", ("← variant\n    lower", "variant\nhigher →"),
                 ["S and V are the Swin-B and Video Swin-B streams. Gray = no significant difference.",
                  "One exploratory seed (260901), BO-selected C23 settings. p values are from the original raw-logit",
                  "permutation test (these ablations were not re-run with the rank-based correction)."], 3, [-0.002, 0, 0.002])


# ------------------------------------------------------------------ ROC curves
def roc_axes(ax, R, tr, te, zoom=None):
    g0 = R[(R.training == tr) & (R.test == te)]
    if zoom is None:
        ax.plot([0, 1], [0, 1], color=MUTED, lw=0.7, ls=(0, (3, 3)), zorder=1)
    lines = []
    for m, (col, mk, ls) in MODELS.items():
        g = g0[g0.model == m]
        c = g[g.point_type == "curve"].sort_values(["fpr", "tpr"])
        ax.plot(c.fpr, c.tpr, color=col, lw=1.3, ls=ls, zorder=2)
        op = g[g.point_type == "operating_point"].iloc[0]
        ax.plot(op.fpr, op.tpr, marker=mk, ms=5.5, mfc=col, mec=INK, mew=0.6, ls="none", zorder=4, clip_on=False)
        lines.append((m, float(g.auc.iloc[0])))
    if zoom:
        ax.set_xlim(*zoom[0])
        ax.set_ylim(*zoom[1])
    else:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, pad=2)
    return lines


def value_block(ax, header, rows, y0=0.03, dy=0.1, keyx=0.56):
    """A small key: coloured marker beside a number in ink (numbers never wear the series colour)."""
    t = ax.transAxes
    for k, (m, txt) in enumerate(rows):
        y = y0 + dy * (2 - k)
        ax.plot(keyx, y + 0.035, marker=MODELS[m][1], ms=4.8, mfc=MODELS[m][0], mec=SURFACE, mew=0.4, transform=t, clip_on=False, ls="none", zorder=6)
        ax.text(0.97, y, txt, transform=t, ha="right", va="bottom", fontsize=8, color=INK, zorder=6,
                bbox=dict(fc=SURFACE, ec="none", pad=0.6, alpha=0.75))
    ax.text(0.97, y0 + dy * 3, header, transform=t, ha="right", va="bottom", fontsize=8, color=INK2, fontweight="bold", zorder=6,
            bbox=dict(fc=SURFACE, ec="none", pad=0.6, alpha=0.75))


LEG = [Line2D([], [], color=c, ls=ls, lw=1.5, marker=mk, ms=5.5, mec=INK, mew=0.6, label=m) for m, (c, mk, ls) in MODELS.items()]


def roc_check():
    R = pd.read_csv(CH4 / "roc_points.csv")
    E = pd.DataFrame(ENS)
    E = E[E.optimization_regimen == "fixed_no_bo"]
    n = 0
    for (tr, te, m), g in R.groupby(["training", "test", "model"]):
        e = E[(E.family == FAM[m]) & (E.training_dataset == tr) & (E.test_dataset == te)].iloc[0]
        c = g[g.point_type == "curve"].sort_values(["fpr", "tpr"])
        assert abs(np.trapezoid(c.tpr.values, c.fpr.values) - float(e.roc_auc)) < 1e-9, (tr, te, m)
        op = g[g.point_type == "operating_point"].iloc[0]
        fp, tn = float(e.fp), float(e.tn)
        assert abs(op.fpr - fp / (fp + tn)) < 1e-12 and abs(op.tpr - float(e.recall)) < 1e-12
        n += 1
    print(f"ROC check: {n} model-cells match the ensemble CSV")
    return R


def fig13(R):
    SRC = ["ffpp_c23", "celeb_df_v2", "deeperforensics_1_0"]
    TGT = {"ffpp_c23": ["ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"], "celeb_df_v2": ["ffpp_c23", "ffpp_c40", "deeperforensics_1_0"],
           "deeperforensics_1_0": ["ffpp_c23", "ffpp_c40", "celeb_df_v2"]}
    H, pw = 7.16, 1.62
    fig = fig_in(W, H)
    fig.legend(handles=LEG, ncol=3, loc="upper left", bbox_to_anchor=(0.54 / W, 1 - 0.03 / H), handlelength=2.6, handletextpad=0.5,
               columnspacing=1.6, borderaxespad=0)
    text_in(fig, 0.54, H - 0.3, "Panel title = trained on → tested on. Curves closer to the top-left corner are better.", va="top")
    text_in(fig, 0.54, H - 0.46, "Dashed line = random guessing. Markers = each model's decision point at its fixed threshold.", va="top")
    tops = [H - 0.92, H - 0.92 - 2.0, H - 0.92 - 4.0]
    for i, s in enumerate(SRC):
        for j, t in enumerate(TGT[s]):
            ax = ax_in(fig, 0.54 + j * (pw + 0.2), tops[i] - pw, pw, pw)
            lines = roc_axes(ax, R, s, t)
            ax.set_title(f"{SHORT[s]} → {SHORT[t]}", loc="left", fontweight="bold", pad=3)
            ax.set_xticks([0, 0.5, 1], ["0", "0.5", "1"] if i == 2 else [])
            ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"] if j == 0 else [])
            value_block(ax, "AUC", [(m, f"{a:.3f}") for m, a in lines])
            if i == 0 and j == 0:
                ax.text(0.5, 0.43, "random guessing", rotation=45, rotation_mode="anchor", ha="center", va="center", fontsize=8, color=INK2,
                        transform=ax.transData)
    text_in(fig, 0.54 + (3 * pw + 0.4) / 2, 0.25, "False positive rate (share of real videos wrongly flagged)", ha="center", va="bottom")
    text_in(fig, 0.1, tops[1] - pw / 2, "True positive rate (share of fakes caught)", rotation=90, ha="center", va="center")
    text_in(fig, 0.04, 0.03, ABBR, va="bottom")
    save(fig, "chapter4", "fig13_transfer_roc.png")


def figJ1(R):
    Z = ((0, 0.2), (0.8, 1.0))
    H, pw = 2.3, 1.18
    fig = fig_in(W, H)
    fig.legend(handles=LEG, ncol=3, loc="upper left", bbox_to_anchor=(0.52 / W, 1 - 0.03 / H), handlelength=2.6, handletextpad=0.5,
               columnspacing=1.6, borderaxespad=0)
    text_in(fig, 0.52, H - 0.3, "Zoomed in: only the top-left corner of each ROC plot is shown. Markers are decision points.", va="top")
    for j, d in enumerate(DS):
        ax = ax_in(fig, 0.52 + j * (pw + 0.2), 0.42, pw, pw)
        lines = roc_axes(ax, R, d, d, zoom=Z)
        ax.set_title(SHORT[d], loc="left", fontweight="bold", pad=3)
        ax.set_xticks([0, 0.1, 0.2], ["0", "0.1", "0.2"])
        ax.set_yticks([0.8, 0.9, 1.0], ["0.8", "0.9", "1.0"] if j == 0 else [])
        value_block(ax, "AUC", [(m, f"{a:.3f}") for m, a in lines], y0=0.04, dy=0.125, keyx=0.5)
    text_in(fig, 0.52 + (4 * pw + 0.6) / 2, 0.04, "False positive rate (share of real videos wrongly flagged)", ha="center", va="bottom")
    text_in(fig, 0.1, 0.42 + pw / 2, "True positive rate", rotation=90, ha="center", va="center")
    save(fig, "chapter4", "figJ1_within_roc.png")


# ------------------------------------------------------------------ RQ2 / RQ3 comparisons
def parse_t10():
    rows = list(csv.reader(open(T10, encoding="utf-8")))
    columns = dict(zip(rows[0][1:], DS))
    assert len(columns) == 4
    out = {}
    for r in rows[1:]:
        if r[0] == "__SPAN__":
            continue
        d = {}
        for c, ds in zip(r[1:], DS):
            m = re.search(r"Acc ([\d.]+)(?:–([\d.]+))?", c)
            if m:
                d[ds] = [float(m.group(1))] + ([float(m.group(2))] if m.group(2) else [])
        out[r[0]] = d
    return out


def rq2():
    t = parse_t10()
    sf = {"SwinFusion++ (BO-selected)": "dataset_specific_bo", "SwinFusion++ (fixed recipe)": "fixed_no_bo"}
    for name, reg in sf.items():
        for ds in DS:
            assert abs(t[name][ds][0] - 100 * float(ens("swinfusionpp", reg, ds, ds)["accuracy"])) < 0.006, (name, ds)
    prior = [k for k in t if k not in sf]
    counts = {ds: sum(len(t[k].get(ds, [])) for k in prior) for ds in DS}
    assert counts == {"ffpp_c23": 11, "ffpp_c40": 11, "celeb_df_v2": 10, "deeperforensics_1_0": 7}, counts
    print("RQ2 check: Table 10 parsed; value counts match the verified key numbers; our accuracies match the ensemble CSV")
    repro = {d: float(r["accuracy"]) * 100 for d, r in
             ((next(k for k, v in LONG.items() if v == r["test_condition"]), r) for r in rd(PKG / "RQ2" / "results" / "table1b_preliminary_baselines.csv"))}
    assert (round(repro["celeb_df_v2"], 2), round(repro["deeperforensics_1_0"], 2)) == (84.17, 46.0)
    names = list(sf) + ["Xception (preliminary study)"] + prior
    n = len(names)
    rh, left, pw, gap = 0.215, 1.86, 0.96, 0.06
    top, bot = 0.72, 1.12
    H = top + n * rh + bot
    fig = fig_in(W, H)
    head(fig, "SwinFusion++ accuracy compared with previously reported results",
         "Right is better. Blue = this study. Gray = values reported by other papers (Tier A).")
    titles = {"ffpp_c23": "FF++ C23", "ffpp_c40": "FF++ C40", "celeb_df_v2": "Celeb-DF v2", "deeperforensics_1_0": "DeeperForensics"}
    lo, hi = 88, 100.8
    for b, ds in enumerate(DS):
        ax = ax_in(fig, left + b * (pw + gap), bot, pw, n * rh)
        a, c = t[names[0]][ds][0], t[names[1]][ds][0]
        ax.axvspan(min(a, c), max(a, c), color=BLUE, alpha=0.16, lw=0, zorder=0)
        for y, nm in enumerate(names):
            ax.axhline(y, color=GRID, lw=0.6, zorder=0)
            if nm in sf:
                v = t[nm][ds][0]
                filled = nm.endswith("(BO-selected)")
                ax.plot(v, y, "o", ms=6, mfc=BLUE if filled else SURFACE, mec=BLUE, mew=1.3, ls="none", zorder=4)
                ax.text(v - 0.8, y, f"{v:.1f}", ha="right", va="center", fontsize=8, color=INK, zorder=5,
                        bbox=dict(fc=SURFACE, ec="none", pad=0.4, alpha=0.8))
            elif nm.startswith("Xception (prelim"):
                mark = {"celeb_df_v2": "*", "deeperforensics_1_0": "†"}.get(ds, "")
                ax.text(lo + 0.3, y, f"◂ {repro[ds]:.1f}{mark}", ha="left", va="center", fontsize=8, color=PURPLE, zorder=5)
            else:
                vs = t[nm].get(ds)
                if not vs:
                    continue
                if len(vs) == 2:
                    ax.plot(vs, [y, y], color=INK2, lw=1.4, zorder=2)
                ax.plot(vs, [y] * len(vs), "o", ms=4.8, color=INK2, mec=SURFACE, mew=0.6, ls="none", zorder=3)
        ax.set_xlim(lo, hi)
        ax.set_ylim(n - 0.5, -0.5)
        ax.set_xticks([90, 95, 100])
        ax.xaxis.grid(True)
        ax.set_axisbelow(True)
        ax.spines["left"].set_visible(False)
        ax.tick_params(length=0, pad=3)
        ax.set_yticks(range(n), names if b == 0 else [])
        ax.set_title(titles[ds], loc="left", fontweight="bold", fontsize=8, pad=3)
        ax.set_xlabel("Accuracy (%)", labelpad=2)
    keys = ["Other papers use their own splits, frame sampling and thresholds: context only, not head-to-head tests.",
            "Celeb-DF test sets differ in fake share (86.2% here). Lines join a model's lowest and highest values.",
            "◂ = off the axis. Xception (preliminary study): earlier pipeline, one seed. * Labeled every video fake.",
            "† No false positives, but 1,288 of 2,185 fakes missed. Blank = not reported."]
    for k, line in enumerate(keys):
        text_in(fig, 0.04, 0.04 + 0.17 * (3 - k), line, va="bottom")
    save(fig, "RQ2", "fig1_vs_published.png")


def rq3():
    rdir = PKG / "RQ3" / "results"
    pub = [r for r in rd(rdir / "table2_published_AB.csv") if r["subset"] == "deepfakes"]
    rep = {r["test_condition"]: r for r in rd(rdir / "table1b_preliminary_baselines.csv")}
    best = lambda metric, test: max(float(r["value"]) for r in pub if r["metric_std"] == metric and test(r["model"]))
    is_single = lambda m: ("frame-1" in m) or ("1 frame" in m)
    is_final = lambda m: "proposed/best" in m
    sab_final = {"roc_auc": best("roc_auc", is_final), "accuracy": best("accuracy", is_final)}
    sab_single = {"roc_auc": best("roc_auc", is_single), "accuracy": best("accuracy", is_single)}
    assert (sab_final["roc_auc"], sab_final["accuracy"], sab_single["roc_auc"], sab_single["accuracy"]) == (0.9959, 0.969, 0.9949, 0.964)
    rows = ["SwinFusion++ (BO-selected)", "SwinFusion++ (fixed recipe)", "CNN–LSTM (preliminary study)",
            "Sabir et al. 2019: CNN + GRU", "Sabir et al. 2019: single frame"]
    colors = [BLUE, BLUE, PURPLE, INK2, INK2]
    H, pw, left = 4.5, 1.96, 1.92
    fig = fig_in(W, H)
    head(fig, "SwinFusion++ compared with CNN–recurrent models on FF++ DeepFakes", "Longer bars are better. All axes start at 0.")
    tops = [H - 0.8, H - 0.8 - 1.5]
    h = 1.08
    for a, (metric, label) in enumerate([("roc_auc", "ROC-AUC"), ("accuracy", "Accuracy (%)")]):
        for b, ds in enumerate(["ffpp_c23", "ffpp_c40"]):
            ax = ax_in(fig, left + b * (pw + 0.12), tops[a] - h, pw, h)
            scale = 100 if metric == "accuracy" else 1
            vals = [float(ens("swinfusionpp", "dataset_specific_bo", ds, ds)[metric]), float(ens("swinfusionpp", "fixed_no_bo", ds, ds)[metric]),
                    float(rep[LONG[ds]][metric]), sab_final[metric] if ds == "ffpp_c40" else None, sab_single[metric] if ds == "ffpp_c40" else None]
            for y, (v, c) in enumerate(zip(vals, colors)):
                if v is None:
                    ax.text(0.02 * scale, y, "not reported", va="center", ha="left", fontsize=8, color=INK2)
                    continue
                ax.barh(y, v * scale, height=0.62, color=c, edgecolor="none", alpha=0.45 if y == 1 else 1, zorder=2)
                ax.text(v * scale + 0.02 * scale, y, f"{v * scale:.1f}" if metric == "accuracy" else f"{v:.3f}", va="center", ha="left", fontsize=8, color=INK, zorder=3)
            ax.set_xlim(0, 1.2 * scale)
            ax.set_xticks([0, 0.5 * scale, 1.0 * scale])
            ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _, m=metric: f"{v:.0f}" if m == "accuracy" else ("0" if v == 0 else ("1" if v == 1 else f"{v:.1f}"))))
            ax.set_ylim(len(rows) - 0.5, -0.5)
            ax.xaxis.grid(True)
            ax.set_axisbelow(True)
            ax.spines["left"].set_visible(False)
            ax.tick_params(length=0, pad=3)
            ax.set_yticks(range(len(rows)), rows if b == 0 else [])
            if a == 0:
                ax.set_title(LONG[ds], loc="left", fontweight="bold", pad=3)
            ax.set_xlabel(label, labelpad=2)
    keys = ["Sabir et al.: C40 only, GRUs rather than LSTMs, evaluation unit unstated (Tier B, context only).",
            "CNN–LSTM: preliminary study, earlier pipeline, one seed. In that study SwinFusion++ scored significantly",
            "higher on 280 shared C40 videos (ΔAUC +0.185, Holm p = 0.0004); those runs are not the bars shown."]
    for k, line in enumerate(keys):
        text_in(fig, 0.04, 0.04 + 0.17 * (2 - k), line, va="bottom")
    save(fig, "RQ3", "fig1_vs_published.png")


# ------------------------------------------------------------------ calibration lines
def rel_panel(ax, b, ece, tr, te, y0=0.03, dy=0.1, keyx=0.56):
    ax.plot([0, 1], [0, 1], color=MUTED, lw=0.8, ls=(0, (3, 3)), zorder=1)
    rows = []
    for m, (col, mk, ls) in MODELS.items():
        d = b[(b.training == tr) & (b.test == te) & (b.family == FAM[m]) & (b.regimen == "fixed_no_bo") & (b.n >= 5)].sort_values("bin")
        ax.plot(d.mean_predicted_fake_probability, d.observed_fake_fraction, color=col, lw=1.3, ls=ls, marker=mk, ms=3.8, mec=SURFACE, mew=0.3, zorder=2, clip_on=False)
        e = ece[(ece.training == tr) & (ece.test == te) & (ece.family == FAM[m]) & (ece.regimen == "fixed_no_bo")].iloc[0]
        rows.append((m, f"{e.ece15_calibrated:.3f}"))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, pad=2)
    value_block(ax, "ECE", rows, y0=y0, dy=dy, keyx=keyx)


def reliability():
    b = pd.read_csv(CAL / "reliability_bins.csv")
    ece = pd.read_csv(CAL / "calibration_ensembles.csv")
    fx = b[(b.regimen == "fixed_no_bo") & (b.n > 0)]
    small = 100 * fx[fx.n < 5].n.sum() / fx.n.sum()
    print(f"Reliability: bins with fewer than 5 videos hold {small:.1f}% of videos")
    legend = [Line2D([], [], color=c, ls=ls, lw=1.5, marker=mk, ms=4.5, mec=SURFACE, label=m) for m, (c, mk, ls) in MODELS.items()]
    notes = ["Dashed line = predictions match reality. ECE = average gap between the two (lower is better).",
             "Above the line, the model underestimates how likely a video is to be fake.",
             "Bins with fewer than 5 videos are not drawn; a model with only one bin left appears as a single point."]
    # within
    H, pw = 2.92, 1.18
    fig = fig_in(W, H)
    head(fig, "Calibration on the training dataset (fixed recipe, three-seed ensembles)")
    fig.legend(handles=legend, ncol=3, loc="upper left", bbox_to_anchor=(0.52 / W, 1 - 0.28 / H), handlelength=2.6, handletextpad=0.5, columnspacing=1.6, borderaxespad=0)
    for j, d in enumerate(DS):
        ax = ax_in(fig, 0.52 + j * (pw + 0.2), 0.94, pw, pw)
        rel_panel(ax, b, ece, d, d, y0=0.03, dy=0.125, keyx=0.5)
        ax.set_title(SHORT[d], loc="left", fontweight="bold", pad=3)
        ax.set_xticks([0, 0.5, 1], ["0", "0.5", "1"])
        ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"] if j == 0 else [])
    text_in(fig, 0.52 + (4 * pw + 0.6) / 2, 0.56, "Predicted probability of fake", ha="center", va="bottom")
    text_in(fig, 0.1, 0.94 + pw / 2, "Actual share of fakes", rotation=90, ha="center", va="center")
    for k, line in enumerate(notes):
        text_in(fig, 0.04, 0.04 + 0.16 * (2 - k), line, va="bottom")
    save(fig, "calibration", "fig_reliability_within.png")
    # transfer
    SRC = ["ffpp_c23", "celeb_df_v2", "deeperforensics_1_0"]
    TGT = {"ffpp_c23": ["ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"], "celeb_df_v2": ["ffpp_c23", "ffpp_c40", "deeperforensics_1_0"],
           "deeperforensics_1_0": ["ffpp_c23", "ffpp_c40", "celeb_df_v2"]}
    H, pw = 7.56, 1.62
    fig = fig_in(W, H)
    head(fig, "Calibration on other datasets (fixed recipe, three-seed ensembles)", "Panel title = trained on → tested on.")
    fig.legend(handles=legend, ncol=3, loc="upper left", bbox_to_anchor=(0.54 / W, 1 - 0.48 / H), handlelength=2.6, handletextpad=0.5, columnspacing=1.6, borderaxespad=0)
    tops = [H - 0.96, H - 0.96 - 2.0, H - 0.96 - 4.0]
    for i, s in enumerate(SRC):
        for j, t in enumerate(TGT[s]):
            ax = ax_in(fig, 0.54 + j * (pw + 0.2), tops[i] - pw, pw, pw)
            rel_panel(ax, b, ece, s, t)
            ax.set_title(f"{SHORT[s]} → {SHORT[t]}", loc="left", fontweight="bold", pad=3)
            ax.set_xticks([0, 0.5, 1], ["0", "0.5", "1"] if i == 2 else [])
            ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"] if j == 0 else [])
    text_in(fig, 0.54 + (3 * pw + 0.4) / 2, 0.56, "Predicted probability of fake", ha="center", va="bottom")
    text_in(fig, 0.1, tops[1] - pw / 2, "Actual share of fakes", rotation=90, ha="center", va="center")
    for k, line in enumerate(notes):
        text_in(fig, 0.04, 0.04 + 0.16 * (2 - k), line, va="bottom")
    save(fig, "calibration", "fig_reliability_transfer.png")


# ------------------------------------------------------------------ main
if __name__ == "__main__":
    R = roc_check()
    # Chapter 4 (drop-in replacements, same file names)
    heat3(("chapter4", "fig11_transfer_heatmap.png"))
    fig12()
    fig13(R)
    figJ1(R)
    # RQ1 / RQ6, principal comparison (fixed recipe)
    within_ci(("RQ1", "fig1_within_ci.png"), "fixed", "SwinFusion++", "Same-dataset ROC-AUC: SwinFusion++ (fixed recipe) and both encoders")
    heat3(("RQ1", "fig2_transfer_all_models.png"), "ROC-AUC by training and test dataset (fixed recipe, three-seed ensembles)")
    heat1(("RQ1", "fig2_transfer_swinfusionpp.png"), "SwinFusion++", "fixed", "SwinFusion++ (fixed recipe)")
    heat1(("RQ1", "fig2_transfer_swin_b.png"), "Swin-B", "fixed", "Swin-B (fixed recipe)")
    heat1(("RQ1", "fig2_transfer_video_swin_b.png"), "Video Swin-B", "fixed", "Video Swin-B (fixed recipe)")
    heat1(("RQ6", "fig1_matrix_swinfusionpp.png"), "SwinFusion++", "fixed", "SwinFusion++ (fixed recipe)")
    delta_heat(("RQ6", "fig1b_delta_vs_baselines.png"), "swinfusionpp__fixed_no_bo", ("RQ1_architecture", "RQ6_architecture"),
               "SwinFusion++ (fixed recipe) compared with each encoder")
    # Configured system (BO-selected SwinFusion++)
    within_ci(("RQ1", "fig1b_within_ci_configured_system.png"), "bo", "SwinFusion++ (BO-selected)", "Same-dataset ROC-AUC: SwinFusion++ (BO-selected) and both encoders")
    heat1(("RQ1", "fig2b_transfer_swinfusionpp_bo.png"), "SwinFusion++", "bo", "SwinFusion++ (BO-selected)")
    delta_heat(("RQ6", "fig1c_delta_vs_baselines_configured_system.png"), "swinfusionpp__dataset_specific_bo",
               ("RQ1_configured_system", "RQ6_configured_system"), "SwinFusion++ (BO-selected) compared with each encoder")
    # RQ2, RQ3, RQ4, calibration
    rq2()
    rq3()
    rq4_controls()
    rq4_transfer()
    rq4_tier_b()
    reliability()
