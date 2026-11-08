#!/usr/bin/env python3
"""OPTION A (2026-10-28) copy of figures_recreated/make_figures.py. The fixed-recipe SwinFusion++ is the
principal model in the RQ1/RQ6 figures; the BO-selected configuration appears only in separately named
configured-system figures. Paired p-values come from ../paired_tests_optionA.csv (Option A Holm families).
Run from anywhere:  python corrected_20261028_optionA/figures/make_figures_optionA.py

Recreate the RQ figures from the CSV files in this results package.

Usage:  python make_figures.py
Needs:  matplotlib, numpy

Reads only CSVs inside the package (00_Shared/statistics_raw and RQx/results)
and writes PNGs to figures_recreated/<RQ>/, using the same file names as the
originals so each one is a drop-in replacement. Nothing outside this folder
is modified.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter
from matplotlib.transforms import blended_transform_factory

HERE = Path(__file__).resolve().parent
PKG = HERE.parent.parent  # package root (SwinFusionPP_RQ_Results)
OPTA = HERE.parent  # corrected_20261028_optionA
STATS = PKG / "00_Shared" / "statistics_raw"
SHOW_TITLES = True  # set False if the thesis captions carry the titles
DPI = 300

# ---------------------------------------------------------------- palette
SURFACE = "#ffffff"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
EMPTY = "#f0efec"

# Colour follows the model in every figure (validated all-pairs, light mode).
MODELS = {
    "SwinFusion++": ("#2a78d6", "o"),
    "SwinFusion++ (BO-selected)": ("#2a78d6", "o"),  # same entity, same colour; never drawn with the fixed one
    "Swin-B": ("#eb6834", "s"),
    "Video Swin-B": ("#1baf7a", "^"),
}
SFPP = MODELS["SwinFusion++"][0]
REPRO = "#4a3aa7"   # baselines reproduced in the preliminary study
PUB = INK2          # published values (de-emphasised)

SEQ = LinearSegmentedColormap.from_list("seq_blue", [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
    "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"])
DIV = LinearSegmentedColormap.from_list("div_red_blue", [
    "#a32d2c", "#e34948", "#f4b2ae", "#f0efec", "#9ec5f4", "#3987e5", "#184f95"])

DS = ["ffpp_c23", "ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]
DS_LABEL = {
    "ffpp_c23": "FF++ C23 (HQ)",
    "ffpp_c40": "FF++ C40 (LQ)",
    "celeb_df_v2": "Celeb-DF v2",
    "deeperforensics_1_0": "DeeperForensics-1.0",
}
DS_SHORT = {
    "ffpp_c23": "FF++\nC23",
    "ffpp_c40": "FF++\nC40",
    "celeb_df_v2": "Celeb-\nDF v2",
    "deeperforensics_1_0": "Deeper-\nForensics",
}
LABEL2DS = {v: k for k, v in DS_LABEL.items()}
MINUS = "−"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "axes.edgecolor": AXIS,
    "axes.linewidth": 0.8,
    "axes.labelcolor": INK2,
    "axes.titlecolor": INK,
    "axes.titlesize": 9.5,
    "axes.titlelocation": "left",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.color": AXIS,
    "ytick.color": AXIS,
    "xtick.labelcolor": INK2,
    "ytick.labelcolor": INK2,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "grid.linestyle": "-",
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "legend.frameon": False,
    "legend.fontsize": 8,
    "savefig.dpi": DPI,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "axes.unicode_minus": True,
})


# ---------------------------------------------------------------- data
def read(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


ENS = read(STATS / "three_seed_mean_logit_ensemble.csv")
# Option A families with Holm-adjusted rank-based cluster permutation p-values.
PAIRED = [dict(r, family_rq=r["family_optionA"], holm_adjusted_p=r["holm_optionA"])
          for r in read(OPTA / "paired_tests_optionA.csv")]
P_TEST = "rank-based cluster permutation test"
TIER_B = read(STATS / "tier_b_paired_effects.csv")

FAMILY = {
    "SwinFusion++": ("swinfusionpp", "fixed_no_bo"),  # Option A: principal model = fixed recipe
    "SwinFusion++ (BO-selected)": ("swinfusionpp", "dataset_specific_bo"),
    "SwinFusion++ (fixed recipe)": ("swinfusionpp", "fixed_no_bo"),
    "Swin-B": ("swin_b", "fixed_no_bo"),
    "Video Swin-B": ("video_swin_b", "fixed_no_bo"),
}


def ens(model, train, test, variant="plain"):
    fam, reg = FAMILY[model]
    for r in ENS:
        if (r["family"], r["optimization_regimen"], r["training_dataset"],
                r["test_dataset"], r["variant"]) == (fam, reg, train, test, variant):
            return r
    return None


def paired(family, model_a, model_b, train, test):
    for r in PAIRED:
        if (r["family_rq"], r["model_a"], r["model_b"], r["training_dataset"],
                r["test_dataset"]) == (family, model_a, model_b, train, test):
            return r
    return None


def n_test(ds):
    return int(ens("SwinFusion++", ds, ds)["analyzed_videos"])


def fmt_p(p):
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def signed(v, nd):
    s = f"{v:+.{nd}f}"
    if float(s) == 0:
        s = f"{0:.{nd}f}"
    return s.replace("-", MINUS)


def text_on(rgb):
    """Ink or white, whichever reads better on a filled cell."""
    r, g, b = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb[:3]]
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return SURFACE if lum < 0.36 else INK


def fig_title(fig, text, H):
    if SHOW_TITLES:
        fig.text(0.0, 1 - 0.06 / H, text, ha="left", va="top", fontsize=9.5, fontweight="bold", color=INK)


def save(fig, rq, name):
    out = HERE / rq
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / name)
    plt.close(fig)
    print("wrote", (out / name).relative_to(PKG))


# ---------------------------------------------------------------- RQ1 fig1
def rq1_within(sf="SwinFusion++", fname="fig1_within_ci.png",
               heading="RQ1 · Within-dataset ROC-AUC, fixed recipe (principal comparison), 95% cluster-bootstrap CIs"):
    fig, ax = plt.subplots(figsize=(6.6, 3.5))
    order = [sf, "Swin-B", "Video Swin-B"]
    offsets = [-0.22, 0.0, 0.22]
    for m, o in zip(order, offsets):
        c, mk = MODELS[m]
        for i, d in enumerate(DS):
            r = ens(m, d, d)
            v, lo, hi = float(r["roc_auc"]), float(r["roc_auc_ci_low"]), float(r["roc_auc_ci_high"])
            ax.plot([i + o, i + o], [lo, hi], color=c, lw=1.8, solid_capstyle="round", zorder=2)
            ax.plot(i + o, v, marker=mk, ms=7, color=c, mec=SURFACE, mew=1.3, zorder=3,
                    label=m if i == 0 else None, ls="none")
    ax.set_xticks(range(len(DS)), [f"{DS_LABEL[d]}\nn = {n_test(d)} videos" for d in DS])
    ax.tick_params(axis="x", length=0, pad=6)
    ax.set_xlim(-0.6, len(DS) - 0.4)
    ax.set_ylim(0.975, 1.0012)
    ax.set_yticks(np.arange(0.975, 1.0001, 0.005))
    ax.set_ylabel("Video-level ROC-AUC")
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    ax.legend(ncol=3, loc="lower left", bbox_to_anchor=(0, 1.0), handletextpad=0.3,
              columnspacing=1.4, borderaxespad=0.2)
    if SHOW_TITLES:
        ax.set_title(heading,
                     loc="left", fontweight="bold", pad=26)
    save(fig, "RQ1", fname)


# ---------------------------------------------------------------- heatmaps
AUC_NORM = Normalize(vmin=0.5, vmax=1.0, clip=True)


def draw_matrix(ax, values, cmap, norm, fmt, ylabels=True, stars=None, fs=7.5, tick_fs=7.5):
    gap = 0.03
    for i in range(4):
        for j in range(4):
            v = values[i, j]
            if np.isnan(v):
                ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap,
                                       facecolor=EMPTY, edgecolor="none"))
                ax.text(j + 0.5, i + 0.5, "not run", ha="center", va="center", color=MUTED, fontsize=fs - 1)
                continue
            rgb = cmap(norm(v))
            ax.add_patch(Rectangle((j + gap, i + gap), 1 - 2 * gap, 1 - 2 * gap,
                                   facecolor=rgb, edgecolor="none"))
            label = fmt(v) + (stars[i, j] if stars is not None else "")
            ax.text(j + 0.5, i + 0.5, label, ha="center", va="center", color=text_on(rgb),
                    fontsize=fs, fontweight="bold" if i == j else "normal")
    ax.set_xlim(0, 4)
    ax.set_ylim(4, 0)
    ax.set_aspect("equal")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks(np.arange(4) + 0.5, [DS_SHORT[d] for d in DS], fontsize=tick_fs)
    ax.set_yticks(np.arange(4) + 0.5, [DS_SHORT[d] for d in DS] if ylabels else [], fontsize=tick_fs)
    ax.tick_params(length=0)
    ax.set_xlabel("Test dataset")
    if ylabels:
        ax.set_ylabel("Training dataset")


def auc_matrix(model):
    M = np.full((4, 4), np.nan)
    for i, tr in enumerate(DS):
        for j, te in enumerate(DS):
            r = ens(model, tr, te)
            if r:
                M[i, j] = float(r["roc_auc"])
    return M


def colorbar(fig, axes, cmap, norm, ticks, label, fmt=None, **kw):
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    cb = fig.colorbar(sm, ax=axes, ticks=ticks, **kw)
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=0, labelsize=7, labelcolor=INK2)
    if fmt:
        cb.ax.yaxis.set_major_formatter(FuncFormatter(fmt))
    cb.set_label(label, color=INK2, fontsize=7.5)
    return cb


FOOT_MATRIX = ("Bold diagonal = in-distribution test; off-diagonal = frozen transfer (source weights and "
               "thresholds unchanged).\nFF++ C40 was not used as a transfer source. Values below 0.5 "
               "share the lightest colour.")


def heatmap_single(model, rq, name, heading):
    fig, ax = plt.subplots(figsize=(4.4, 4.0))
    draw_matrix(ax, auc_matrix(model), SEQ, AUC_NORM, lambda v: f"{v:.3f}")
    colorbar(fig, ax, SEQ, AUC_NORM, np.arange(0.5, 1.01, 0.1), "ROC-AUC (0.5 = chance)",
             fraction=0.046, pad=0.04)
    if SHOW_TITLES:
        ax.set_title(heading, loc="left", fontweight="bold", pad=10)
    fig.text(0.02, -0.04, FOOT_MATRIX, fontsize=6.5, color=MUTED, va="top")
    save(fig, rq, name)


def heatmap_all():
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 3.0), gridspec_kw=dict(wspace=0.08))
    for k, (ax, m) in enumerate(zip(axes, ["SwinFusion++", "Swin-B", "Video Swin-B"])):
        draw_matrix(ax, auc_matrix(m), SEQ, AUC_NORM, lambda v: f"{v:.3f}", ylabels=(k == 0),
                    fs=7, tick_fs=6.8)
        sub = "BO-selected" if "BO" in m else "fixed recipe"
        ax.set_title(f"{m}\n", loc="left", fontsize=8.5, fontweight="bold", pad=4)
        ax.text(0, 1.035, sub, transform=ax.transAxes, fontsize=7, color=INK2, va="bottom")
    colorbar(fig, list(axes), SEQ, AUC_NORM, np.arange(0.5, 1.01, 0.1), "ROC-AUC (0.5 = chance)",
             fraction=0.018, pad=0.02)
    if SHOW_TITLES:
        fig.suptitle("RQ1 · Directional ROC-AUC, fixed recipe (principal comparison), three-seed ensembles", x=0.08, ha="left",
                     fontsize=9.5, fontweight="bold", color=INK, y=1.0)
    fig.text(0.08, 0.0, FOOT_MATRIX, fontsize=6.5, color=MUTED, va="top")
    save(fig, "RQ1", "fig2_transfer_all_models.png")


def delta_heatmaps(model_a="swinfusionpp__fixed_no_bo", fams=("RQ1_architecture", "RQ6_architecture"),
                   fname="fig1b_delta_vs_baselines.png", who="SwinFusion++ (fixed recipe)",
                   what="principal comparison, fixed recipe vs fixed recipe"):
    """SwinFusion++ minus each baseline, within (diagonal) and transfer (off-diagonal), Option A families."""
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.5))
    lim = 0.17
    norm = Normalize(vmin=-lim, vmax=lim, clip=True)
    for k, (ax, base, bname) in enumerate(zip(
            axes, ["swin_b__fixed_no_bo", "video_swin_b__fixed_no_bo"], ["Swin-B", "Video Swin-B"])):
        M = np.full((4, 4), np.nan)
        S = np.full((4, 4), "", dtype=object)
        for i, tr in enumerate(DS):
            for j, te in enumerate(DS):
                fam = fams[0] if tr == te else fams[1]
                r = paired(fam, model_a, base, tr, te)
                if r:
                    M[i, j] = float(r["auc_difference"])
                    S[i, j] = "*" if float(r["holm_adjusted_p"]) < 0.05 else ""
        draw_matrix(ax, M, DIV, norm, lambda v: signed(v, 3), ylabels=(k == 0), stars=S)
        ax.set_title(f"SwinFusion++ {MINUS} {bname}", loc="left", fontsize=8.5, fontweight="bold", pad=6)
    colorbar(fig, list(axes), DIV, norm, [-0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15],
             "ΔROC-AUC  (blue = SwinFusion++ better)", fmt=lambda v, _: signed(v, 2),
             fraction=0.03, pad=0.03)
    if SHOW_TITLES:
        fig.suptitle(f"RQ6 · Paired ΔROC-AUC of {who} against each baseline", x=0.02, ha="left",
                     fontsize=9.5, fontweight="bold", color=INK, y=1.02)
    fig.text(0.02, -0.02,
             f"* p_Holm < 0.05: {P_TEST}, Holm within {fams[0]} (diagonal) or {fams[1]} (transfer); {what}.\n"
             "Bold diagonal = in-distribution. FF++ C40 was not used as a transfer source.",
             fontsize=6.5, color=MUTED, va="top")
    save(fig, "RQ6", fname)


# ---------------------------------------------------------------- published dot plots
def norm_model(name):
    for key, out in [("Xception", "Xception"), ("FTCN", "FTCN"), ("I3D", "I3D"), ("STIL", "STIL"),
                     ("TALL", "TALL-Swin"), ("SFormer", "SFormer")]:
        if name.startswith(key):
            return out
    return name


METRIC_FMT = {"roc_auc": lambda v: f"{v:.3f}", "accuracy": lambda v: f"{v * 100:.1f}%"}
OFFSCALE_FMT = {"roc_auc": lambda v: f"{v:.4f}", "accuracy": lambda v: f"{v * 100:.1f}%"}
METRIC_TICK = {"roc_auc": lambda v, _: f"{v:.2f}", "accuracy": lambda v, _: f"{v * 100:.0f}%"}


def dotplot(rq, fname, heading, datasets, rows, ours, repro, published, xlims, ticks,
            notes=None, label_max=(), footnote="", panel_w=1.6):
    """rows: list of (row_key, label). ours[ds] = dict(roc_auc, ci_low, ci_high, accuracy).
    repro[(row_key, ds)] = dict(roc_auc, accuracy). published: list of (row_key, ds, metric, value, tier).
    Values below the axis minimum are drawn as a ◄ at the edge with their value printed."""
    notes = notes or {}
    metrics = [("roc_auc", "ROC-AUC"), ("accuracy", "Accuracy")]
    nr, nc = len(metrics), len(datasets)
    row_h, left_in, right_in, top_in, bottom_in, gap_h, gap_w = 0.27, 1.85, 0.25, 0.95, 1.05, 0.62, 0.16
    panel_h = row_h * len(rows) + 0.2
    W = left_in + nc * panel_w + (nc - 1) * gap_w + right_in
    H = top_in + nr * panel_h + (nr - 1) * gap_h + bottom_in
    fig, axes = plt.subplots(nr, nc, figsize=(W, H), squeeze=False, sharey=True)
    fig.subplots_adjust(left=left_in / W, right=1 - right_in / W, top=1 - top_in / H, bottom=bottom_in / H,
                        wspace=gap_w / panel_w, hspace=gap_h / panel_h)
    ypos = {key: i for i, (key, _) in enumerate(rows)}

    def put(ax, metric, x, y, note=None, label_above=False, **style):
        lo, hi = ax.get_xlim()
        fmt = METRIC_FMT[metric]
        if x < lo:
            edge = lo + 0.012 * (hi - lo)
            ax.plot(edge, y, marker="<", ms=5.5, color=style.get("mec") if style.get("mfc") == SURFACE
                    else style.get("color", PUB), ls="none", clip_on=False, zorder=4)
            txt = OFFSCALE_FMT[metric](x) + (f"  ({note})" if note else "")
            ax.text(edge + 0.03 * (hi - lo), y, txt, fontsize=6.3, color=INK2, va="center", ha="left")
            return
        ax.plot(x, y, ls="none", zorder=4, **style)
        if note:
            ax.annotate(note, (x, y), xytext=(0, 5), textcoords="offset points", fontsize=6.0,
                        color=MUTED, ha="center", va="bottom")
        if label_above:
            ax.annotate(fmt(x), (x, y), xytext=(0, 4.5), textcoords="offset points", fontsize=6.3,
                        color=INK2, ha="center", va="bottom")

    for a, (metric, mlabel) in enumerate(metrics):
        for b, ds in enumerate(datasets):
            ax = axes[a, b]
            ax.set_xlim(*xlims[metric])
            ax.set_xticks(ticks[metric])
            ax.xaxis.set_major_formatter(FuncFormatter(METRIC_TICK[metric]))
            ax.set_ylim(len(rows) - 0.5, -0.75)
            for y in range(len(rows)):
                ax.axhline(y, color=GRID, lw=0.6, zorder=0)
            ax.xaxis.grid(True)
            ax.set_axisbelow(True)
            ax.spines["left"].set_visible(False)
            ax.tick_params(axis="y", length=0)
            ax.tick_params(axis="x", labelsize=7)
            # ours
            o = ours.get(ds)
            if o and o.get(metric) is not None:
                v, y = o[metric], ypos["ours"]
                ax.axvline(v, color=SFPP, lw=0.8, alpha=0.3, zorder=1)
                if metric == "roc_auc":
                    ax.plot([o["ci_low"], o["ci_high"]], [y, y], color=SFPP, lw=1.8,
                            solid_capstyle="round", zorder=3)
                put(ax, metric, v, y, label_above=True, marker="o", ms=6.5, color=SFPP, mec=SURFACE, mew=1.2)
            # reproduced
            for (key, rds), vals in repro.items():
                if rds == ds and vals.get(metric) is not None:
                    put(ax, metric, vals[metric], ypos[key], note=notes.get((metric, ds, key)),
                        marker="D", ms=5.5, color=REPRO, mec=SURFACE, mew=1.0)
            # published
            best = {}
            for key, pds, pm, val, tier in published:
                if pds != ds or pm != metric:
                    continue
                y = ypos[key] + (-0.13 if tier == "A" else 0.13)
                if tier == "A":
                    put(ax, metric, val, y, marker="o", ms=4.8, color=PUB, mec=SURFACE, mew=0.8)
                else:
                    put(ax, metric, val, y, marker="o", ms=4.5, mfc=SURFACE, mec=PUB, mew=1.0)
                if key in label_max:
                    hi_v, lo_v, _ = best.get(key, (-1, 2, 0))
                    best[key] = (max(hi_v, val), min(lo_v, val), ypos[key])
            for key, (hi_v, lo_v, y) in best.items():
                ax.annotate(f"best {METRIC_FMT[metric](hi_v)}", (lo_v, y), xytext=(-7, 0),
                            textcoords="offset points", fontsize=6.3, color=INK2, ha="right", va="center")
            for (nm, nds, nkey), (txt, dx, dy) in notes.get("free", {}).items():
                if nm == metric and nds == ds:
                    x0 = repro[(nkey, ds)][metric]
                    ax.annotate(txt, (x0, ypos[nkey]), xytext=(dx, dy), textcoords="offset points",
                                fontsize=6.0, color=MUTED, ha="left", va="center")
            if a == 0:
                ax.set_title(DS_LABEL[ds], loc="left", fontsize=8.5, fontweight="bold", pad=4)
            ax.set_xlabel(mlabel, fontsize=8)
        axes[a, 0].set_yticks(range(len(rows)), [lbl for _, lbl in rows])
    handles = [
        Line2D([], [], marker="o", ls="-", lw=1.8, color=SFPP, mec=SURFACE, ms=6.5,
               label="SwinFusion++ (ours, BO-selected; line = 95% CI)"),
        Line2D([], [], marker="D", ls="none", color=REPRO, mec=SURFACE, ms=5.5,
               label="Reproduced in preliminary study"),
        Line2D([], [], marker="o", ls="none", color=PUB, mec=SURFACE, ms=4.8, label="Published, Tier A"),
        Line2D([], [], marker="o", ls="none", mfc=SURFACE, mec=PUB, ms=4.5, label="Published, Tier B"),
    ]
    fig_title(fig, heading, H)
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1 - 0.30 / H), ncol=2,
               fontsize=7.5, handletextpad=0.4, columnspacing=1.6, borderaxespad=0)
    if footnote:
        fig.text(0.0, 0.08 / H, footnote, fontsize=6.5, color=MUTED, va="bottom")
    save(fig, rq, fname)


def rq2_published():
    rdir = PKG / "RQ2" / "results"
    ours = {LABEL2DS[r["dataset"]]: {k: float(r[k]) for k in ("roc_auc", "ci_low", "ci_high", "accuracy")}
            for r in read(rdir / "table1_ours.csv")}
    repro = {("xception_repro", LABEL2DS[r["test_condition"]]):
             {"roc_auc": float(r["roc_auc"]), "accuracy": float(r["accuracy"])}
             for r in read(rdir / "table1b_preliminary_baselines.csv")}
    published = []
    for r in read(OPTA / "RQ2" / "results" / "table2_published_AB.csv"):
        if r.get("optionA_20261028_note"):  # six SFormer cross-compression cells, not within-dataset
            continue
        if r["train_condition"] != r["test_condition"] or r["metric_std"] not in ("roc_auc", "accuracy"):
            continue
        published.append((norm_model(r["model"]), r["test_condition"], r["metric_std"], float(r["value"]), r["tier"]))
    rows = [("ours", "SwinFusion++ (ours, BO-selected)"), ("xception_repro", "Xception (reproduced)"),
            ("Xception", "Xception"), ("I3D", "I3D"), ("STIL", "STIL"), ("FTCN", "FTCN"),
            ("TALL-Swin", "TALL-Swin"), ("SFormer", "SFormer")]
    notes = {("accuracy", "celeb_df_v2", "xception_repro"): "predicts every video fake",
             ("accuracy", "deeperforensics_1_0", "xception_repro"): "threshold failure"}
    dotplot("RQ2", "fig1_vs_published.png",
            "RQ2 · SwinFusion++ against reproduced and published baselines (within-dataset)",
            DS, rows, ours, repro, published,
            xlims={"roc_auc": (0.88, 1.003), "accuracy": (0.75, 1.005)},
            ticks={"roc_auc": [0.90, 0.95, 1.00], "accuracy": [0.8, 0.9, 1.0]}, notes=notes,
            footnote=("◄ = value below the axis range, printed beside the marker. Published values are context "
                      "under each paper's own protocol (Tier A: same dataset and\ncompression, video level, "
                      "DeepFakes subset; Tier B: same dataset, unit or subset differs or is unstated). Empty rows "
                      "= not reported.\nSource: RQ2/results/table1_ours.csv, table1b_preliminary_baselines.csv, "
                      "table2_published_AB.csv (Option A copy; SFormer cross-compression cells excluded)."))


def rq3_published():
    rdir = PKG / "RQ3" / "results"
    ours = {LABEL2DS[r["dataset"]]: {k: float(r[k]) for k in ("roc_auc", "ci_low", "ci_high", "accuracy")}
            for r in read(rdir / "table1_ours.csv")}
    repro = {("cnnlstm_repro", LABEL2DS[r["test_condition"]]):
             {"roc_auc": float(r["roc_auc"]), "accuracy": float(r["accuracy"])}
             for r in read(rdir / "table1b_preliminary_baselines.csv")}
    published = []
    for r in read(rdir / "table2_published_AB.csv"):
        # Sabir et al. report DeepFakes, Face2Face and FaceSwap; keep the DeepFakes subset only.
        if r["subset"] != "deepfakes" or r["metric_std"] not in ("roc_auc", "accuracy"):
            continue
        single = ("frame-1" in r["model"]) or ("1 frame" in r["model"])
        key = "sabir_single" if single else "sabir_recurrent"
        published.append((key, r["test_condition"], r["metric_std"], float(r["value"]), r["tier"]))
    rows = [("ours", "SwinFusion++ (ours, BO-selected)"), ("cnnlstm_repro", "CNN–LSTM (reproduced)"),
            ("sabir_recurrent", "Sabir et al. 2019,\n5-frame CNN+GRU"),
            ("sabir_single", "Sabir et al. 2019,\nsingle frame")]
    notes = {"free": {("roc_auc", "ffpp_c40", "cnnlstm_repro"):
                      ("prelim. paired test vs SwinFusion++:\nΔAUC +0.185, p_Holm = 0.0004", 9, 0)}}
    dotplot("RQ3", "fig1_vs_published.png",
            "RQ3 · SwinFusion++ against CNN–recurrent models on FF++ DeepFakes",
            ["ffpp_c23", "ffpp_c40"], rows, ours, repro, published,
            xlims={"roc_auc": (0.75, 1.005), "accuracy": (0.65, 1.01)},
            ticks={"roc_auc": [0.8, 0.9, 1.0], "accuracy": [0.7, 0.8, 0.9, 1.0]}, notes=notes,
            label_max=("sabir_recurrent", "sabir_single"), panel_w=2.3,
            footnote=("Sabir et al. report C40 only; their Face2Face/FaceSwap results are excluded. All Sabir "
                      "values are Tier B (evaluation unit\nunstated) and use GRUs, not LSTMs; 'best' labels give the "
                      "highest value per row. Source: RQ3/results/table1_ours.csv,\ntable1b_preliminary_baselines.csv, "
                      "table2_published_AB.csv (subset = deepfakes)."))


# ---------------------------------------------------------------- forest plots
def forest(rows, rq, fname, heading, left_lbl, right_lbl, axis_lbl, footnote=""):
    """rows: list of either ('header', text) or (label, d, lo, hi, p)."""
    n = len(rows)
    top_in, bottom_in = 0.42, 0.85
    H = 0.30 * n + top_in + bottom_in
    W = 7.2
    fig = plt.figure(figsize=(W, H))
    gs = fig.add_gridspec(1, 3, width_ratios=[2.6, 2.2, 2.4], wspace=0.03, left=0.0, right=1.0,
                          top=1 - top_in / H, bottom=bottom_in / H)
    axl = fig.add_subplot(gs[0])
    ax = fig.add_subplot(gs[1], sharey=axl)
    axr = fig.add_subplot(gs[2], sharey=axl)
    for side in (axl, axr):
        side.axis("off")
    tl = blended_transform_factory(axl.transAxes, axl.transData)
    tr = blended_transform_factory(axr.transAxes, axr.transData)
    tp = blended_transform_factory(ax.transAxes, ax.transData)
    span = 0
    for y, r in enumerate(rows):
        if r[0] == "header":
            axl.text(0.98, y + 0.12, r[1], transform=tl, ha="right", va="center", fontsize=8,
                     fontweight="bold", color=INK)
            continue
        label, d, lo, hi, p = r
        span = max(span, abs(lo), abs(hi))
        ax.plot([lo, hi], [y, y], color=SFPP, lw=1.8, solid_capstyle="round", zorder=2)
        ax.plot(d, y, "o", ms=6.5, color=SFPP, mec=SURFACE, mew=1.2, zorder=3)
        axl.text(0.98, y, label, transform=tl, ha="right", va="center", fontsize=8, color=INK2)
        axr.text(0.04, y, f"{signed(d, 4)} [{signed(lo, 4)}, {signed(hi, 4)}]", transform=tr, ha="left",
                 va="center", fontsize=7, color=INK2, family="DejaVu Sans Mono")
        axr.text(0.78, y, fmt_p(p), transform=tr, ha="left", va="center", fontsize=7, color=INK2,
                 family="DejaVu Sans Mono")
    lim = span * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(n - 0.5, -0.95)
    ax.axvline(0, color=MUTED, lw=0.9, zorder=1)
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", left=False, labelleft=False)
    ax.spines["left"].set_visible(False)
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda v, _: "0" if abs(v) < 1e-12 else (signed(v, 3) if abs(v) >= 0.01 else signed(v, 4))))
    ax.locator_params(axis="x", nbins=5)
    ax.tick_params(axis="x", labelsize=7)
    ax.set_xlabel(axis_lbl, fontsize=8)
    halo = dict(facecolor=SURFACE, edgecolor="none", pad=1.0)
    ax.text(0.01, -0.75, f"← {left_lbl}", transform=tp, ha="left", va="center", fontsize=6.5, color=MUTED,
            bbox=halo, zorder=5)
    ax.text(0.99, -0.75, f"{right_lbl} →", transform=tp, ha="right", va="center", fontsize=6.5, color=MUTED,
            bbox=halo, zorder=5)
    axr.text(0.04, -0.75, "ΔAUC [95% CI]", transform=tr, ha="left", va="center", fontsize=7.5,
             color=INK, fontweight="bold")
    axr.text(0.78, -0.75, "p (Holm)", transform=tr, ha="left", va="center", fontsize=7.5,
             color=INK, fontweight="bold")
    fig_title(fig, heading, H)
    if footnote:
        fig.text(0.0, 0.06 / H, footnote, fontsize=6.5, color=MUTED, va="bottom")
    save(fig, rq, fname)


CTRL = {"capacity_control__fixed_no_bo": "vs capacity control",
        "topology_control__fixed_no_bo": "vs topology control"}
CTRL_NOTE = ("Capacity control: same parameter count (±5%), per-stream layers, no cross-stream attention. "
             "Topology control: same stages,\nalignment and joint readout, exchange block removed. Three-seed "
             "ensembles, fixed recipe, FF++ C23 training. ")


def rq4_controls():
    rows = []
    for b, lbl in CTRL.items():
        r = paired("RQ4_controls", "swinfusionpp__fixed_no_bo", b, "ffpp_c23", "ffpp_c23")
        rows.append((lbl, float(r["auc_difference"]), float(r["ci_low"]), float(r["ci_high"]),
                     float(r["holm_adjusted_p"])))
    forest(rows, "RQ4", "fig1_controls_forest.png",
           "RQ4 · SwinFusion++ (fixed recipe) minus matched control, FF++ C23 test (n = 280)",
           "control better", "SwinFusion++ better", "ΔROC-AUC (95% cluster-bootstrap CI)",
           footnote=CTRL_NOTE + "\np = " + P_TEST + ", Holm within RQ4_controls.")


def rq4_controls_transfer():
    rows = []
    for te in ["ffpp_c40", "celeb_df_v2", "deeperforensics_1_0"]:
        rows.append(("header", f"C23 → {DS_LABEL[te]}  (n = {n_test(te)})"))
        for b, lbl in CTRL.items():
            r = paired("RQ4_controls_transfer", "swinfusionpp__fixed_no_bo", b, "ffpp_c23", te)
            rows.append((lbl, float(r["auc_difference"]), float(r["ci_low"]), float(r["ci_high"]),
                         float(r["holm_adjusted_p"])))
    forest(rows, "RQ4", "fig1b_controls_transfer_forest.png",
           "RQ4 · SwinFusion++ (fixed recipe) minus matched control, frozen transfer from FF++ C23",
           "control better", "SwinFusion++ better", "ΔROC-AUC (95% cluster-bootstrap CI)",
           footnote=CTRL_NOTE + "\np = " + P_TEST + ", Holm within RQ4_controls_transfer.")


TIER_B_LABEL = {
    "tierb_one_directional": "One-directional attention (S ← V)",
    "tierb_no_gate": "No gates (all gates = 1)",
    "tierb_no_agreement": "No agreement features (|S−V|, S⊙V)",
    "tierb_stages_34_only": "Exchange in stages 3–4 only",
}


def rq4_tier_b():
    rows = []
    for r in TIER_B:
        rows.append((TIER_B_LABEL[r["model_a"]], float(r["auc_difference"]), float(r["ci_low"]),
                     float(r["ci_high"]), float(r["holm_adjusted_p"])))
    forest(rows, "RQ4", "fig2_tier_b_forest.png",
           "RQ4 · Tier B ablations: variant minus full SwinFusion++, FF++ C23 test (n = 280)",
           "full model better", "variant better", "ΔROC-AUC (95% cluster-bootstrap CI)",
           footnote="Single exploratory seed (260901) with the BO-selected C23 settings; the full model uses the "
                    "same seed.\nSign is variant − full (the control plots use SwinFusion++ − control). "
                    "p = original raw-logit cluster permutation test (Tier B was not re-run), Holm within the Tier B family.")


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    # Principal architecture comparison (fixed recipe for all three models)
    rq1_within()
    heatmap_single("SwinFusion++", "RQ1", "fig2_transfer_swinfusionpp.png",
                   "RQ1 · SwinFusion++ (fixed recipe), directional ROC-AUC")
    heatmap_single("Swin-B", "RQ1", "fig2_transfer_swin_b.png", "RQ1 · Swin-B (fixed recipe), directional ROC-AUC")
    heatmap_single("Video Swin-B", "RQ1", "fig2_transfer_video_swin_b.png",
                   "RQ1 · Video Swin-B (fixed recipe), directional ROC-AUC")
    heatmap_all()
    heatmap_single("SwinFusion++", "RQ6", "fig1_matrix_swinfusionpp.png",
                   "RQ6 · SwinFusion++ (fixed recipe) train → test ROC-AUC")
    delta_heatmaps()
    # Configured system (BO-selected SwinFusion++ vs fixed-recipe baselines)
    rq1_within("SwinFusion++ (BO-selected)", "fig1b_within_ci_configured_system.png",
               "RQ1 · Within-dataset ROC-AUC, configured system (BO-selected SwinFusion++), 95% CIs")
    heatmap_single("SwinFusion++ (BO-selected)", "RQ1", "fig2b_transfer_swinfusionpp_bo.png",
                   "RQ1 · SwinFusion++ (BO-selected, configured system), directional ROC-AUC")
    delta_heatmaps("swinfusionpp__dataset_specific_bo", ("RQ1_configured_system", "RQ6_configured_system"),
                   "fig1c_delta_vs_baselines_configured_system.png", "SwinFusion++ (BO-selected)",
                   "configured system, BO-selected vs fixed-recipe baselines")
    # External comparisons (BO-selected configuration, per Chapter 3) and RQ4 (unchanged families)
    rq2_published()
    rq3_published()
    rq4_controls()
    rq4_controls_transfer()
    rq4_tier_b()
