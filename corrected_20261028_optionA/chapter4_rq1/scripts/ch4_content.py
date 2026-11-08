"""Chapter 4 (opening + RQ1), Chapter 3 amendment, references, appendix relabeling and Appendix J.

Prose lives here; every number in it must appear in team/tables/KEY_NUMBERS.md (checked by check_numbers.py).
Tables are read from team/tables/<ID>.csv (+ <ID>_note.txt); figures from team/figures/.
"""
import csv
import re
import struct
from pathlib import Path

import docx_ins as D
from xml.sax.saxutils import escape as _esc

TEAM = Path(__file__).resolve().parents[1] / 'team'
TAB, FIG = TEAM / 'tables', TEAM / 'figures'
TEXT_W_EMU = 5486400          # 6.0 in
TEXT_W_TW = 8640


def _png_size(path):
    with open(path, 'rb') as f:
        head = f.read(24)
    return struct.unpack('>II', head[16:24])


def _img(name):
    w, h = _png_size(FIG / name)
    return (f'ch4_{name}', str(FIG / name), TEXT_W_EMU, int(TEXT_W_EMU * h / w))


FIGS = {'11': 'fig11_transfer_heatmap.png', '12': 'fig12_forest.png', '13': 'fig13_transfer_roc.png',
        'J1': 'figJ1_within_roc.png'}
IMAGES = [_img(v) for v in FIGS.values()]


def _captions():
    """captions.md: '## Figure 11. Title' followed by a 'Note. …' line."""
    out, cur = {}, None
    for line in (FIG / 'captions.md').read_text().splitlines():
        m = re.match(r'#+\s*Figure\s+(\S+?)\.\s+(.+?)\s*$', line.strip())
        if m:
            cur = m.group(1)
            out[cur] = {'title': m.group(2)}
        elif cur and line.strip().startswith('Note.'):
            out[cur]['note'] = line.strip().removeprefix('Note.').strip()
    return out


def _read_table(tid):
    if tid.startswith('RQ2X/'):
        base, name = TEAM / 'rq2x' / 'tables', tid[5:]
    elif tid.startswith('RQ2/'):
        base, name = TEAM / 'rq2' / 'tables', tid[4:]
    else:
        base, name = TAB, tid
    with open(base / f'{name}.csv', newline='') as f:
        rows = [r for r in csv.reader(f)]
    note = (base / f'{name}_note.txt').read_text().strip() if (base / f'{name}_note.txt').exists() else ''
    return rows, note


def _widths(rows, size, total=TEXT_W_TW):
    """Column widths in twips: every column at least as wide as its longest word (so no word is broken),
    remaining space shared in proportion to how much more each column would like. Returns (widths, fits)."""
    n = len(rows[0])
    cw = size * 10 * 0.56           # average character width in twips (size is in half-points)
    pad = 170
    body = [r for r in rows if not (r and r[0] == '__SPAN__')]
    minw, prefw = [0] * n, [0] * n
    for k, r in enumerate(body):
        f = 1.12 if k == 0 else 1.0  # header row is bold
        for c in range(n):
            cell = str(r[c]) if c < len(r) else ''
            cell = cell.replace('< 0', '<~0')  # printed with a no-break space, so it is one word
            longest = max((len(w) for w in re.split(r' +|(?<=[-/–])', cell) if w), default=1)  # breaks after - / –
            minw[c] = max(minw[c], longest * cw * f + pad)
            prefw[c] = max(prefw[c], min(len(cell), 34) * cw * f + pad)
    if sum(minw) > total:
        return [int(total * m / sum(minw)) for m in minw], False
    extra = total - sum(minw)
    want = [max(p - m, 0) for p, m in zip(prefw, minw)]
    tot = sum(want) or 1
    w = [int(m + extra * x / tot) for m, x in zip(minw, want)]
    w[w.index(max(w))] += total - sum(w)
    return w, True


def table_block(tid, title, src=None):
    rows, note = _read_table(src or (tid if tid.startswith('J') else f'T{tid}'))
    if tid == 'J9':
        rows, note = _slim_j9(rows, note)
    size = 18 if len(rows[0]) <= 7 else 16
    widths, fits = _widths(rows, size)
    while not fits and size > 13:
        size -= 1
        widths, fits = _widths(rows, size)
    xml = D.caption(f'Table {tid}.', title, above=True)
    xml += D.table(rows, widths, size=size)
    if note:
        xml += D.note('*Note.* ' + note.removeprefix('Note.').strip())
    return xml


STD_SET = 'standard set, no distortions: 1,000 raw manipulated videos + 1,000 FF++ YouTube originals; 7:1:2 split by swapped identity'


def _slim_j9(rows, note):
    """Table J9 has 12 columns in its CSV; print 9: unit and subset merged into Setting, the evaluating
    paper folded into Source, and unverified values marked with a dagger instead of a Verification column."""
    h = rows[0]
    ci = {k: i for i, k in enumerate(h)}
    def col(name):
        return next(i for k, i in ci.items() if k.startswith(name))
    t, m, me, v, u, sub, src, ev, tier, inn, why, ver = (col('Test set'), col('Model'), col('Metric'), col('Value'),
        col('Unit'), col('Subset'), col('Source'), col('Evaluated'), col('Tier'), col('In Table'), col('Reason'),
        col('Verif'))
    out = [['Test set', 'Model', 'Metric', 'Value', 'Setting', 'Source', 'Tier', 'In table?', 'Reason if not']]
    for r in rows[1:]:
        if r and r[0] == '__SPAN__':
            out.append(r); continue
        # 'HQ),' / 'LQ),' are parsing leftovers in the record; the compression is already in the Test set column
        subset = re.sub(r'^[HL]Q\), ', '', r[sub]).replace('all four manipulations; all four FF++', 'all four FF++')
        subset = subset.replace(' (DF, F2F, FS, NT)', '').replace('no distortions; standard set:', 'no distortions:')
        subset = 'DeepFakes' if subset == 'deepfakes' else subset
        if r[tier] == 'A' and r[src].startswith('Jiang et al. (2020), Table 5') and subset == 'unstated or other':
            subset = STD_SET  # same column of the same table as the C3D, TSN and ResNet+LSTM rows
        setting = '; '.join(x for x in (r[u], subset) if x and x not in ('—', ''))
        # the source's own '(†)' (re-implemented) would clash with the † printed in the Value column
        ev_txt = r[ev].replace('re-implemented (†)', 're-implemented by Gu et al.').strip()
        cite = re.match(r'[^()]*\(\d{4}\)', ev_txt)
        if cite and cite.group(0).split(' (')[0] in r[src]:
            ev_txt = ev_txt[cite.end():].lstrip(' ,;')
            if ev_txt.startswith('(') and ev_txt.endswith(')'):
                ev_txt = ev_txt[1:-1]
        source = r[src] + (f'; {ev_txt}' if ev_txt else '')
        value = r[v] + ('' if r[ver].lower().startswith(('yes', 'verified')) else '\u00a0†')
        test = r[t]
        for a, b in (('FF++ C23', 'C23'), ('FF++ C40', 'C40'), ('Celeb-DF v2', 'CDF'), ('DeeperForensics-1.0', 'DFo'),
                     ('all four manipulations', 'all four')):
            test = test.replace(a, b)
        out.append([test, r[m], r[me], value, setting, source, r[tier], r[inn], r[why]])
    return out, note.rstrip() + ' C23/C40 = FaceForensics++ DeepFakes at C23/C40; CDF = Celeb-DF v2; DFo = DeeperForensics-1.0. † = taken from the study’s literature record without re-checking against the original paper.'


def figure_block(fid, media):
    cap = _captions()[fid]
    name = f'ch4_{FIGS[fid]}'
    rid, _, cx, cy = media[name]
    xml = D.image(rid, cx, cy, name) + D.caption(f'Figure {fid}.', cap['title'])
    if cap.get('note'):
        xml += D.note('*Note.* ' + cap['note'])
    return xml


B = D.body
CITE_PRELIMINARY = True   # user decision 2026-10-31: cite the preliminary study as an unpublished manuscript

# ----------------------------------------------------------------------------------------------
# Chapter 4
# ----------------------------------------------------------------------------------------------
OPTION_A = ('Results are reported according to the analysis plan in Chapter 3. An interim decision to present the '
            'BO-selected configuration as primary was reverted to the approved plan; all comparisons under both '
            'regimens are reported.')


def chapter4(media):
    x = []
    x.append(D.heading1('Chapter 4 – PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA'))
    x.append(B('This chapter presents, analyzes, and interprets the results of the experiments described in Chapter 3. '
               'It begins with the evaluation setting shared by all model comparisons and then addresses the research '
               'questions in turn. Each table and figure is introduced, its main values are stated, and their meaning '
               'for the research question is then interpreted.'))

    # ---- Evaluation setting ----
    x.append(D.heading2('Evaluation Setting'))
    x.append(B('All model results in this chapter come from held-out test videos that were not used for training, model '
               'selection, threshold selection, or calibration. Swin-B, Video Swin-B, and SwinFusion++ were each trained '
               'with the same predefined non-BO recipe on each of the four within-dataset conditions (FaceForensics++ [FF++] DeepFakes at compression C23 and C40, Celeb-DF v2, and DeeperForensics-1.0), using three recorded seeds (260901, 260902, and 260903). SwinFusion++ was also trained with the training parameters '
               'selected by its condition-specific Bayesian optimization (BO) study. Each test video produced one '
               'prediction: the logits of its seven locked 16-frame clips of aligned 224 × 224 face crops, sampled at '
               '2 frames per second, were averaged into one video logit. The three seeds of each model were combined '
               'into a three-seed ensemble by averaging their video logits.'))
    x.append(B('The operating threshold, chosen to maximize Youden’s J, and the calibration temperature were fitted on '
               'source-validation videos only and frozen before any test video was scored. Under cross-dataset '
               'transfer, the source-trained ensemble, threshold, and temperature were applied unchanged to the target '
               'dataset, and no target label was used for any decision. All results use the plain inference variant; '
               'the predeclared horizontal-flip variant is reported in Appendix J, Table J4.'))
    x.append(B(OPTION_A + ' The statistical amendments made after test scoring, including the rank-based form of the '
               'permutation test and the regrouping of the comparison families, are described in Chapter 3 under Amendments after Test Scoring, and the original and corrected tests are '
               'compared in Appendix J, Table J5. The rank correction removed one significant difference favoring SwinFusion++ '
               '(within DeeperForensics-1.0, against Video Swin-B) and added two (Celeb-DF v2 → FF++ C23 and '
               'DeeperForensics-1.0 → Celeb-DF v2, both against Swin-B).'))
    x.append(B('Table 1 summarizes the four test sets, their dependence structure, and their coverage.'))
    x.append(table_block('1', 'Test Sets, Dependence Structure, and Coverage'))
    x.append(B('All test videos were analyzed. Coverage was 100%, and no video ended in a preprocessing failure or an '
               'insufficient-evidence state, so no result in this chapter depends on how failed videos would have been '
               'counted. The test sets differ in their dependence structure. The FaceForensics++ test sets each contain '
               '70 source clusters of four videos, and DeeperForensics-1.0 contains 201 real–fake source pairs. '
               'Celeb-DF v2 contains 978 videos, but all 843 of its fake videos lie in nine target-identity clusters, '
               'so its fake class rests on nine independent clusters and its intervals are approximate. Because the '
               'clusters are keyed by target identity, whether the identity of the swapped-in source face was also '
               'held out could not be verified from the archived records.'))
    x.append(B((TAB / 'opening_integrity.txt').read_text().split('\nSources:')[0].strip()))
    x.append(B('Table 2 maps each analysis to its comparison family and to the section in which it is reported. Holm '
               'adjustment was applied within each family.'))
    x.append(table_block('2', 'Analyses, Comparison Families, and Where They Are Reported'))
    x.append(B('Two rules apply to every comparison in this chapter. First, ROC-AUC differences are paired: both models '
               'are evaluated on the same videos, and each bootstrap draw or permutation is applied to both. Intervals '
               'are 95% percentile intervals from 5,000 stratified cluster-bootstrap draws and are not adjusted for '
               'multiplicity, so the decision for each comparison is the Holm-adjusted p-value of the rank-based '
               'cluster permutation test; Holm-adjusted p-values below 0.005, which include the smallest attainable '
               'values, are written as < 0.005. Second, the inference is conditional on the trained ensembles: it describes how the evaluated '
               'models perform on new test videos, not how a retrained model would perform. Threshold-independent '
               'results (ROC-AUC and PR-AUC) and threshold-dependent results (accuracy, precision, recall, '
               'specificity, and F1-score) are reported separately, and differences in threshold-dependent metrics '
               'are given only as supplementary paired intervals, without tests.'))

    # ---- RQ1 ----
    x.append(D.heading2('Research Question 1: SwinFusion++ Compared With the Standalone Encoders'))
    x.append(B('RQ1 asked: *To what extent does SwinFusion++ improve video-level deepfake detection performance compared '
               'with standalone Swin Transformer and standalone Video Swin Transformer under in-distribution and '
               'cross-dataset evaluation, in terms of Accuracy, Precision, Recall, F1-Score, and ROC-AUC?* The principal '
               'evidence is the fixed-recipe comparison, in which all three models were trained with the identical '
               'recipe. The BO-selected SwinFusion++ is reported afterward as a configured system with unequal '
               'optimization effort.'))

    x.append(D.subhead('In-Distribution Performance Under the Fixed Recipe'))
    x.append(B('Table 3 presents the within-dataset results of the three fixed-recipe models.'))
    x.append(table_block('3', src='T4', title='Within-Dataset Performance of the Fixed-Recipe Models'))
    x.append(B('All three models reached ROC-AUC between 0.9878 and 0.9974 on every test set. SwinFusion++ had the '
               'highest point estimate of the three on DeeperForensics-1.0 (0.9974) and was within 0.0037 of the highest '
               'on the other three test sets (FF++ C23 0.9942, C40 0.9878, Celeb-DF v2 0.9951). In accuracy, it '
               'classified the most videos correctly of the three on DeeperForensics-1.0 (397 of 402, compared with 393 '
               'for Swin-B and 390 for Video Swin-B) and the second most on Celeb-DF v2 (956 of 978, compared with 933 '
               'and 961). On the FaceForensics++ test sets, the three models differed by at most three of 280 videos: '
               'SwinFusion++ matched Swin-B on C23 (97.86%) and C40 (94.64%), and Video Swin-B classified three more '
               'videos correctly on each. All three models therefore operated near the ceiling of the metric on every '
               'test set (ROC curves in Appendix J, Figure J1).'))
    x.append(B('Table 4 presents the paired ROC-AUC differences between SwinFusion++ and each encoder.'))
    x.append(table_block('4', src='T5', title='Paired ROC-AUC Differences Within Datasets, Fixed Recipe'))
    x.append(B('No ROC-AUC difference between SwinFusion++ and either encoder was detectable (all Holm-adjusted p = '
               '1.000; raw p from 0.198 to 0.925), and every paired 95% interval lay between −0.011 and +0.009 AUC, '
               'which is incompatible with a large difference in either direction. SwinFusion++ had the lower point '
               'estimate in six of the eight comparisons. The ceiling left little room to detect a gain: in seven of the '
               'eight comparisons, even the largest gain still possible was smaller than the difference the test could '
               'detect with 80% power (Appendix J, Table J6), so these results do not establish equivalence. In the '
               'supplementary paired intervals for threshold-dependent metrics (Table J2), SwinFusion++ had higher '
               'accuracy than Swin-B on Celeb-DF v2 (+2.35 percentage points [+0.08, +5.10]; approximate, nine '
               'fake-class clusters) and than Video Swin-B on DeeperForensics-1.0 (+1.74 percentage points [+0.50, '
               '+3.23]). Because the corresponding ROC-AUC differences were not detectable, these gains are best read as '
               'differences in where the frozen thresholds fell rather than as better separation of real and fake '
               'videos. Within each benchmark, SwinFusion++ was therefore statistically indistinguishable from both '
               'encoders in ROC-AUC, and all three models operated near the ceiling of the metric.'))

    x.append(D.subhead('Frozen Cross-Dataset Transfer Under the Fixed Recipe'))
    x.append(B('Figure 11 shows the ROC-AUC of each fixed-recipe model for every combination of training and test '
               'dataset, Table 5 gives the paired differences for the nine transfer directions, and Figure 12 shows '
               'all 26 paired differences of the fixed-recipe comparison together.'))
    x.append(figure_block('11', media))
    x.append(table_block('5', src='T6', title='Paired ROC-AUC Differences Under Frozen Transfer, Fixed Recipe'))
    x.append(figure_block('12', media))
    x.append(B('Under frozen transfer, SwinFusion++ had a significantly higher ROC-AUC than Swin-B in seven of the nine '
               'directions, by +0.049 to +0.258 (Holm-adjusted p from < 0.005 to 0.018), and than Video Swin-B in three, '
               'Celeb-DF v2 → FF++ C40 (+0.0754), Celeb-DF v2 → DeeperForensics-1.0 (+0.0630), and DeeperForensics-1.0 → '
               'FF++ C40 (+0.0840), all with Holm-adjusted p < 0.005. In these three directions, it was significantly '
               'better than both encoders and had the highest ROC-AUC of the three models. SwinFusion++ was '
               'significantly lower than an encoder in none of the 18 comparisons. This is not evidence of '
               'non-inferiority: the five negative point estimates were not significant, but the widest interval reached '
               '−0.092 (DeeperForensics-1.0 → Celeb-DF v2, against Video Swin-B). SwinFusion++ also had the highest '
               'point estimate in FF++ C23 → C40 and DeeperForensics-1.0 → FF++ C23 (Figure 11), but its lead over the '
               'runner-up, Video Swin-B, was not significant in either direction (+0.0014; and +0.0451 [+0.0077, '
               '+0.0816], Holm-adjusted p = 0.152, shown with an open marker in Figure 12).'))
    x.append(B('The advantage was clearest when the models were trained on Celeb-DF v2 or DeeperForensics-1.0: from '
               'these sources, SwinFusion++ was significantly better than Swin-B in all six directions and than Video '
               'Swin-B in three. From FF++ C23, SwinFusion++ was statistically indistinguishable from both encoders on '
               'FF++ C40 and Celeb-DF v2, and the one significant difference was the largest of all 18: on '
               'DeeperForensics-1.0, Swin-B’s ROC-AUC fell to 0.5678 [0.5250, 0.6105], while the two models with a '
               'temporal stream kept 0.8261 (SwinFusion++, +0.258 over Swin-B) and 0.8421 (Video Swin-B). The same ordering '
               'appeared on the 60-video subset that shares no source lineage with the FF++ C23 training or validation data (seed means: '
               'Swin-B 0.5322, SwinFusion++ 0.7356, Video Swin-B 0.7874; no interval; Appendix J, Table J3). This pattern '
               'is consistent with temporal evidence transferring better than frame appearance in this direction. '
               'Swin-B and Video Swin-B also differ in pretraining and input handling, however, so the comparison does '
               'not isolate the cause.'))
    x.append(B('The significant differences were stable across seeds and analysis choices. Nine of the ten had the same '
               'sign in all nine pairings of individual seeds, and the tenth (Celeb-DF v2 → FF++ C40 against Video '
               'Swin-B) in eight of nine; all ten remained significant under the family grouping recorded before scoring '
               'and under one pooled family, and no DeeperForensics-1.0-target decision changed with 175 lineage '
               'clusters (Appendix J, Table J7). Two limits apply. Transfer lowered ROC-AUC for every model, to between '
               '0.459 and 0.976, and from DeeperForensics-1.0 to Celeb-DF v2 all three models were near chance (0.4593 '
               'to 0.6001). The three significant differences from DeeperForensics-1.0 to FF++ C23 and C40 could not be '
               'checked meaningfully on a lineage-free subset, because only 20 such test videos exist (Table 1; per-seed '
               'values in Table J3). Under matched training, SwinFusion++ therefore ranked target videos significantly '
               'better than Swin-B in seven of the nine transfer directions and than Video Swin-B in three. Whether '
               'these differences can be attributed to TLBG-HCA, rather than to the combination of two encoders, is '
               'examined under RQ4 with the topology and capacity-matched controls.'))

    x.append(D.subhead('Threshold-Dependent Metrics Under Transfer'))
    x.append(B('RQ1 also concerns accuracy, precision, recall, and F1-score. Table 6 gives these metrics at the frozen '
               'source thresholds, and Figure 13 shows where each frozen threshold fell on the target ROC curve.'))
    x.append(table_block('6', src='T7', title='Threshold-Dependent Metrics Under Frozen Transfer, Fixed Recipe'))
    x.append(figure_block('13', media))
    x.append(B('At the frozen source thresholds, every model became conservative on the target data. Specificity stayed '
               'between 91.11% and 100.00%, while recall was below 64% in every direction except FF++ C23 → C40 '
               '(79.29% to 87.14%). From the Celeb-DF v2 and DeeperForensics-1.0 sources, no model flagged more than 60 test videos '
               'as fake, so accuracy in those directions mainly reflects the share of real videos. From '
               'DeeperForensics-1.0 to Celeb-DF v2, where 86.20% of the test videos are fake, accuracy was only 13.80% to '
               '15.24%, close to the 13.80% obtained by calling every video real.'))
    x.append(B('SwinFusion++ did not have the highest accuracy, recall, or F1-score in any of the nine directions (point '
               'estimates; several margins were one or two videos). From FF++ C23, its high precision and specificity reflect that it made the fewest positive calls of the three models (114, 458, and 8 on C40, Celeb-DF v2, and DeeperForensics-1.0); from the other two sources, Swin-B made the fewest or tied for the fewest. From FF++ C23 to Celeb-DF v2, for example, it raised only six false '
               'alarms among 135 real videos (specificity 95.56%) but detected 53.62% of the fake videos, and its '
               'accuracy (59.41%) was lower than that of Swin-B (67.48%) and Video Swin-B (66.46%), although the three '
               'ROC-AUC values did not differ detectably. In the supplementary paired intervals (Table J2), its '
               'transfer accuracy was lower than an encoder’s in 6 of 18 comparisons (both encoders from FF++ C23 to '
               'C40 and to Celeb-DF v2; Video Swin-B from FF++ C23 to DeeperForensics-1.0 and from Celeb-DF v2 to C23) '
               'and higher in 2 (Swin-B from Celeb-DF v2 to C23 and to DeeperForensics-1.0).'))
    x.append(B('Figure 13 illustrates the split between ROC-AUC and accuracy. Outside FF++ C23 → C40, where ROC-AUC stayed near or above 0.8, the curves show that the ranking of fake above real videos was largely retained, but the frozen operating point sat in the low-recall part of the curve. Moving it would require target labels, which the '
               'frozen-transfer design excludes. Where ROC-AUC was near 0.5, as from DeeperForensics-1.0 to '
               'Celeb-DF v2, the ranking itself was close to chance, so the problem was not only the threshold. For all three models, the frozen screening label on an unseen dataset is therefore much less '
               'informative than the ranking results suggest.'))

    x.append(D.subhead('Configured System and Optimization Effect'))
    x.append(B('Table 7 compares the BO-selected SwinFusion++ with the fixed-recipe encoders, and Table 8 compares it '
               'with the fixed-recipe SwinFusion++. Because only SwinFusion++ received a hyperparameter search, Table 7 '
               'measures configured-system performance with unequal optimization effort and is not evidence about the '
               'architecture itself.'))
    x.append(table_block('7', src='T8', title='BO-Selected SwinFusion++ Compared With the Fixed-Recipe Encoders'))
    x.append(B('Within datasets, the BO-selected configuration had the highest point estimates of any model evaluated on '
               'FF++ C40 (0.9941) and Celeb-DF v2 (0.9983), but none of its eight differences from the encoders was '
               'significant, so these leads are descriptive. Under transfer, it was significantly better than Swin-B in '
               'six of the nine directions and, from FF++ C23 to C40, significantly better than both encoders (+0.0123 '
               'and +0.0116). It was significantly worse than Video Swin-B from FF++ C23 to DeeperForensics-1.0 '
               '(−0.1105) and from Celeb-DF v2 to FF++ C23 (−0.0390).'))
    x.append(table_block('8', src='T9', title='Optimization Effect: BO-Selected Minus Fixed-Recipe SwinFusion++'))
    x.append(B('Table 8 shows the source of this pattern. The BO-selected parameters significantly raised ROC-AUC within '
               'FF++ C40 (+0.0063) and Celeb-DF v2 (+0.0031) and from FF++ C23 to C40 (+0.0102), but they significantly '
               'lowered it in five transfer directions, by 0.041 to 0.104. The Celeb-DF v2 gain was significant in its own family '
               '(Holm-adjusted p = 0.021) but not when the families were pooled as recorded before scoring (p = 0.077). '
               'The pattern is consistent with the BO objective, source-validation ROC-AUC, fitting each training '
               'source more tightly at the expense of transfer. Two limitations apply: the searches used 12, 12, 8, and 8 trials, which limits how fully each search space was explored, and the objective was close to saturation, with best validation ROC-AUC between 0.9977 and 0.9994. The BO-selected configurations also differed from the fixed recipe in several training parameters at once, so the effect cannot be attributed to any single parameter.'))

    x.append(D.subhead('Answer to Research Question 1'))
    x.append(B('In distribution, under the principal fixed-recipe comparison, SwinFusion++ performed at the same '
               'near-ceiling level as standalone Swin-B and Video Swin-B. All three models reached ROC-AUC of 0.988 to '
               '0.997, no paired ROC-AUC difference was detectable, and each paired interval lay between −0.011 and '
               '+0.009 AUC; at this ceiling, little room remained for a detectable improvement. The threshold-dependent '
               'metrics were similarly close: accuracy differed by at most three videos on FaceForensics++, and '
               'precision and recall differed from those of either encoder by at most 2.0 and 3.1 percentage points. The '
               'only supplementary accuracy and F1-score intervals that excluded zero favored SwinFusion++ (Celeb-DF v2 '
               'against Swin-B; DeeperForensics-1.0 against Video Swin-B); because the ROC-AUC differences there were '
               'not detectable, these gains are best read as threshold placement rather than better ranking.'))
    x.append(B('Under frozen cross-dataset evaluation, SwinFusion++ had significantly higher ROC-AUC than Swin-B in '
               'seven of the nine directions (by +0.049 to +0.258) and than Video Swin-B in three (by +0.063 to +0.084), '
               'and in those three it was significantly better than both encoders. It was not significantly lower than '
               'either encoder in any direction, although the widest interval reached −0.092, and nine of the ten '
               'significant differences had the same sign in every pairing of individual seeds. The advantage came '
               'mainly from the Celeb-DF v2 and DeeperForensics-1.0 sources; from FF++ C23, the one detectable '
               'difference was also the largest, +0.258 against Swin-B on DeeperForensics-1.0. At the frozen source '
               'thresholds, however, SwinFusion++ did not have the highest transfer accuracy, recall, or F1-score in any '
               'direction (point estimates; several margins were one or two videos), and in the supplementary paired '
               'intervals its transfer accuracy was lower than an encoder’s in 6 of 18 comparisons and higher in 2 '
               '(Table J2).'))
    x.append(B('The improvement that RQ1 asks about is therefore present in ranking performance under frozen '
               'transfer, in seven of nine directions against Swin-B and in three of nine against Video Swin-B. Within '
               'datasets, where all three models were near the ceiling, no improvement was detectable, and under transfer '
               'the ranking advantage did not carry over to threshold-dependent performance at the frozen source '
               'operating points. Relative to the fixed recipe, the BO-selected configuration '
               'significantly raised ROC-AUC within FF++ C40 and Celeb-DF v2 (the latter depending on the family '
               'grouping) and from FF++ C23 to C40, but significantly lowered it in five other transfer directions, '
               'consistent with tighter fitting to each training source. Whether the transfer differences are due to '
               'TLBG-HCA is examined under RQ4, and the verdict against the Chapter 3 criterion for a strong model is '
               'given under RQ6.'))
    x.append(rq2_section(media))
    x.append(D._p('', ['<w:r><w:br w:type="page"/></w:r>']))
    return ''.join(x)


def rq2_section(media):
    """Research Question 2 (filled in after the advisors agree)."""
    try:
        import rq2_content
    except ImportError:
        return ''
    return rq2_content.section(media, table_block, figure_block, B)


# ----------------------------------------------------------------------------------------------
# Chapter 3 amendment (after block 617), references
# ----------------------------------------------------------------------------------------------
def amendments_paragraph():
    t = (TAB / 'D2_final.txt').read_text().strip()
    t = re.sub(r'^\**Amendments after [Tt]est [Ss]coring\.?\**\s*', '', t)
    return B('**Amendments after Test Scoring.** ' + t)


REFS = {
    'bandos': ('Bandos, A. I., Rockette, H. E., & Gur, D. (2005). A permutation test sensitive to differences in areas '
               'for comparing ROC curves from a paired design. Statistics in Medicine, 24(18), 2873–2893. '
               'https://doi.org/10.1002/sim.2149'),
    'custodio': ('Custodio, E. T., Degamo, M. K., Escueta, K. R. C., San Diego, D. A. E., & Sarmiento, M. J. F. (2026). '
                 'SwinFusion++: Face-aligned spatio-temporal Swin Transformer for deepfake detection [Unpublished '
                 'manuscript]. College of Computer Studies and Systems, University of the East–Manila.'),
    'smil': ('Li, X., Lang, Y., Chen, Y., Mao, X., He, Y., Wang, S., Xue, H., & Lu, Q. (2020). Sharp multiple instance '
             'learning for DeepFake video detection. In Proceedings of the 28th ACM International Conference on '
             'Multimedia (pp. 1864–1872). Association for Computing Machinery. https://doi.org/10.1145/3394171.3414034'),
    'holm': ('Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of '
             'Statistics, 6(2), 65–70.'),
}


def ref_paragraph(key_or_text):
    ppr = '<w:spacing w:line="240" w:lineRule="auto"/><w:ind w:left="720" w:hanging="720"/><w:jc w:val="both"/>'
    text = REFS.get(key_or_text, key_or_text)
    return D._p(ppr, D.runs(text)) + D._p(ppr, [])


def extra_refs():
    """[(anchor_entry_or_START, entry_text)] from team/rq2x/refs_merged.txt ('AFTER: …' then 'NEW: …')."""
    f = TEAM / 'rq2x' / 'refs_merged.txt'
    out, anchor = [], None
    if f.exists():
        for line in f.read_text().splitlines():
            if line.startswith('AFTER:'):
                anchor = line[len('AFTER:'):].strip()
            elif line.startswith('NEW:') and anchor is not None:
                out.append(('START' if anchor.startswith('(start') else anchor, line[len('NEW:'):].strip()))
                anchor = None
    return out


# ----------------------------------------------------------------------------------------------
# Appendix figure relabeling (APA 7 appendix-letter numbering)
# ----------------------------------------------------------------------------------------------
APPX = [('B', 11, 37), ('C', 38, 45), ('D', 46, 51), ('E', 52, 54), ('F', 55, 58)]
RELABEL = {n: f'{L}{n - lo + 1}' for L, lo, hi in APPX for n in range(lo, hi + 1)}


def relabel_appendix_figures(xml, i, text, in_scope):
    if not in_scope:
        return xml
    for m in sorted(set(int(k) for k in re.findall(r'Figure (\d+)\.', text)), reverse=True):
        if m in RELABEL:
            while f'Figure {m}.' in re.sub(r'<w:delText[^>]*>.*?</w:delText>', '', xml):
                xml = D.replace_in_paragraph(xml, f'Figure {m}.', f'Figure {RELABEL[m]}.')
    # One caption (Figure 41) is typed across three runs: 'Figure 4' + '1' + '. '.
    split = re.compile(r'<w:r(?: [^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)<w:t xml:space="preserve">Figure 4</w:t></w:r>'
                       r'<w:r(?: [^>]*)?><w:rPr>(?:(?!</w:rPr>).)*</w:rPr><w:t xml:space="preserve">1</w:t></w:r>', re.S)
    mm = split.search(xml)
    if mm:
        rpr = mm.group(1)
        xml = (xml[:mm.start()]
               + f'<w:del {D._attrs()}><w:r>{rpr}<w:delText xml:space="preserve">Figure 41</w:delText></w:r></w:del>'
               + f'<w:ins {D._attrs()}><w:r>{rpr}<w:t xml:space="preserve">Figure {RELABEL[41]}</w:t></w:r></w:ins>'
               + xml[mm.end():])
    return xml


# ----------------------------------------------------------------------------------------------
# Appendix J
# ----------------------------------------------------------------------------------------------
J_TABLES = [
    ('J1', 'Per-Seed ROC-AUC for Every Model, Regimen, and Test Condition'),
    ('J2', 'Supplementary Paired Differences in Threshold-Dependent Metrics, Fixed Recipe'),
    ('J3', 'ROC-AUC on the Strict Lineage-Free Subsets, by Seed'),
    ('J4', 'Plain and Horizontal-Flip ROC-AUC for All Models'),
    ('J5', 'Original Raw-Logit and Corrected Rank-Based Permutation Tests'),
    ('J6', 'Within-Dataset Sensitivity: Detectable Difference and Available Headroom'),
    ('J7', 'Robustness of the Ten Significant Architecture Differences'),
    ('J8', 'Transfer ROC-AUC With 95% Intervals for All Models'),
    ('J9', 'Previously Reported Values Considered for Research Question 2'),
]


def appendix_supplement(media):
    x = [D._p('', ['<w:r><w:br w:type="page"/></w:r>'])]
    x.append(D._p('<w:pStyle w:val="Heading4"/><w:spacing w:after="200" w:line="276" w:lineRule="auto"/>',
                  D.runs('APPENDIX J')))
    x.append(D._p('<w:spacing w:after="200" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/>',
                  D.runs('SUPPLEMENTARY RESULTS FOR RESEARCH QUESTIONS 1 AND 2', bold=True)))
    x.append(B('This appendix reports the per-seed results, the supplementary analyses listed in Chapter 3 under '
               'Amendments after Test Scoring, and the predeclared horizontal-flip variant for RQ1 (Tables J1 to J8 and Figure J1), '
               'and the full list of previously reported values considered for RQ2 (Table J9). None of these analyses '
               'was used to decide a hypothesis.'))
    for tid, title in J_TABLES:
        x.append(table_block(tid, title, src='RQ2X/J9' if tid == 'J9' else None))
    x.append(figure_block('J1', media))
    return ''.join(x)


# ----------------------------------------------------------------------------------------------
# Front matter: List of Figures entries, List of Tables, front-matter list line
# ----------------------------------------------------------------------------------------------
def _like(template_block, text, with_tab=False):
    """Tracked paragraph that copies the paragraph properties of an existing block; plain runs."""
    ppr = re.search(r'<w:pPr>(.*?)</w:pPr>', template_block, flags=re.S).group(1)
    ppr = re.sub(r'<w:rPr>.*?</w:rPr>|<w:rPr/>', '', ppr, flags=re.S)
    m = re.search(r'<w:r(?: [^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)', template_block, flags=re.S)
    rpr = m.group(1) if m else '<w:rPr><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>'
    run = f'<w:r>{rpr}<w:t xml:space="preserve">{D.escape(text)}</w:t>' + ('<w:tab/>' if with_tab else '') + '</w:r>'
    return D._p(ppr, [run] if text else [])


LOF_CH4 = [('Figure 11.', '11'), ('Figure 12.', '12'), ('Figure 13.', '13')]
LOT = [('1', 'Test Sets, Dependence Structure, and Coverage'),
       ('2', 'Analyses, Comparison Families, and Where They Are Reported'),
       ('3', 'Within-Dataset Performance of the Fixed-Recipe Models'),
       ('4', 'Paired ROC-AUC Differences Within Datasets, Fixed Recipe'),
       ('5', 'Paired ROC-AUC Differences Under Frozen Transfer, Fixed Recipe'),
       ('6', 'Threshold-Dependent Metrics Under Frozen Transfer, Fixed Recipe'),
       ('7', 'BO-Selected SwinFusion++ Compared With the Fixed-Recipe Encoders'),
       ('8', 'Optimization Effect: BO-Selected Minus Fixed-Recipe SwinFusion++'),
       ('9', 'SwinFusion++ and the Preliminary-Study Xception Baseline'),
       ('10', 'Previously Reported Tier A Results on the Benchmarks of This Study'),
       ('11', 'Previously Reported Tier B Results on FaceForensics++')] + [(tid, title) for tid, title in J_TABLES]


def _pg(sec, key):
    pm = page_map()
    return (pm or {}).get(sec, {}).get(key) or ''


def lof_after_fig10(entry_block):
    caps = _captions()
    return ''.join(_num_entry(entry_block, f'Figure {n}. {caps[n]["title"]}', _pg('fig', f'Figure {n}.'))
                   for _, n in LOF_CH4)


def lof_after_last(entry_block):
    return _num_entry(entry_block, f'Figure J1. {_captions()["J1"]["title"]}', _pg('fig', 'Figure J1.'))


def list_of_tables(heading_block, blank_block, title_row_block, entry_block):
    x = [D._p('', ['<w:r><w:br w:type="page"/></w:r>'])]
    x.append(_like(heading_block, 'LIST OF TABLES'))
    x.append(_like(blank_block, ''))
    x.append(_like(title_row_block, re.sub(r'<[^>]+>', '', title_row_block).replace('&amp;', '&')))  # same text as the List of Figures header
    for tid, title in LOT:
        x.append(_num_entry(entry_block, f'Table {tid}. {title}', _pg('tab', f'Table {tid}.')))
    return ''.join(x)


# ----------------------------------------------------------------------------------------------
# Page numbers (from pagenums.py) and new TOC lines
# ----------------------------------------------------------------------------------------------
PAGE_MAP = TEAM / 'final_check' / 'page_map.json'


def page_map():
    import json
    return json.loads(PAGE_MAP.read_text()) if PAGE_MAP.exists() else None


def _num_entry(template_block, text, num):
    """A list entry like the template: text, tab, page number (or nothing yet)."""
    ppr = re.search(r'<w:pPr>(.*?)</w:pPr>', template_block, flags=re.S).group(1)
    ppr = re.sub(r'<w:rPr>.*?</w:rPr>|<w:rPr/>', '', ppr, flags=re.S)
    m = re.search(r'<w:r(?: [^>]*)?>(<w:rPr>(?:(?!</w:rPr>).)*</w:rPr>)', template_block, flags=re.S)
    rpr = m.group(1) if m else ''
    run = (f'<w:r>{rpr}<w:t xml:space="preserve">{D.escape(text)}</w:t><w:tab/>'
           + (f'<w:t xml:space="preserve">{num}</w:t>' if num else '') + '</w:r>')
    return D._p(ppr, [run])


TOC_CH4 = ['PRESENTATION, ANALYSIS, AND INTERPRETATION OF DATA', 'Evaluation Setting',
           'Research Question 1: SwinFusion++ Compared With the Standalone Encoders',
           'Research Question 2: SwinFusion++ Compared With Established Baselines']
TOC_APPX = ['APPENDIX H: TURNITIN RESULTS – SIMILARITY REPORT', 'APPENDIX I: TURNITIN RESULTS – AI REPORT',
            'APPENDIX J: SUPPLEMENTARY RESULTS FOR RESEARCH QUESTIONS 1 AND 2']
