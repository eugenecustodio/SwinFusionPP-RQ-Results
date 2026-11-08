"""Chapter 4, Research Question 2 (agreed plan: team/rq2/RQ2_AGREED_PLAN.md). Tables 9–10 from team/rq2/tables/."""
import docx_ins as D


def section(media, table_block, figure_block, B):
    x = []
    x.append(D.heading2('Research Question 2: SwinFusion++ Compared With Established Baselines'))
    x.append(B('RQ2 asked: *What is the performance of SwinFusion++ relative to established baselines when evaluated '
               'on the Deepfake subset of FaceForensics++ (HQ/LQ), Celeb-DF datasets and DeeperForensics-1.0?* Three '
               'kinds of evidence are kept separate. The first is the held-out performance of SwinFusion++; following '
               'the analysis plan, the BO-selected configuration is reported with the fixed-recipe result alongside. '
               'The second is the Xception baseline that the authors trained in their preliminary study (Custodio et '
               'al., 2026), the only established baseline that this group has run on these datasets; it used an '
               'earlier pipeline, a single seed, and partly different test populations. The third consists of previously reported results for established frame-level, recurrent, 3D-convolutional, and spatio-temporal detectors, taken from the comparison tables of X. Li et al. (2020), Gu et al. (2021), Jiang et al. (2020), Masi et al. (2020), Haliassos et al. (2021), and Xu et al. (2023) and from Rössler et al. (2019), Zheng et al. (2021), and Kingra et al. (2024). Every row of each table used is recorded in Appendix J, Table J9, and rows were left out of the chapter tables only by a stated category, never because of their values. No baseline was retrained in the present study, so none of these comparisons is paired and '
               'none is tested; they are descriptive.'))
    x.append(B('Two features of this study’s test sets further limit comparison with published values. The Celeb-DF v2 '
               'test set contains 978 videos split by target identity rather than the official 518-video test list, '
               'and the DeeperForensics-1.0 test set is this study’s construction of unperturbed manipulated videos and their FaceForensics++ source originals, which corresponds to the benchmark’s standard (undistorted) setting, although identical test lists cannot be verified; the benchmark’s distorted and hidden test settings are not comparable. Published results also come from their own splits, frame sampling, face crops, and '
               'operating points.'))
    x.append(B('The models and their original papers are as follows: frame-level detectors Xception (Chollet, 2017), MesoNet '
               '(Afchar et al., 2018), the face-warping detectors D-FWA and DSP-FWA (Y. Li & Lyu, 2018), Face X-ray (L. Li '
               'et al., 2020), F3-Net (Qian et al., 2020), FDFL (J. Li et al., 2021), the multi-attentional detector (H. '
               'Zhao et al., 2021), RECCE (Cao et al., 2022), and Add-Net (Zi et al., 2020); recurrent models, namely a CNN–LSTM baseline (Hochreiter & Schmidhuber, 1997), a ResNet+LSTM baseline (He et al., 2016), a CNN–GRU (Sabir et al., 2019), and the two-branch recurrent network '
               '(Masi et al., 2020); 3D-convolutional and video-recognition models C3D (Tran et al., 2015), I3D '
               '(Carreira & Zisserman, 2017), TSN (L. Wang et al., 2016), TEI (Liu et al., 2020), and ADDNet-3D (Zi et al., 2020); and '
               'spatio-temporal detectors and video transformers S-MIL-T (X. Li et al., 2020), STIL (Gu et al., 2021), '
               'FTCN (Zheng et al., 2021), LipForensics (Haliassos et al., 2021), DFDT (Khormali & Yuan, 2022), ADT (P. '
               'Wang et al., 2022), M2TR (J. Wang et al., 2022), VTN (Neimark et al., 2021), VidTr (Y. Zhang et al., '
               '2021), ViViT (Arnab et al., 2021), ISTVT (C. Zhao et al., 2023), TALL-Swin (Xu et al., 2023), and '
               'SFormer (Kingra et al., 2024). DeepRhythm (Qi et al., 2020) is listed in Table J9 only, because the value '
               'quoted for it by Gu et al. (2021) does not match its original paper.'))

    x.append(D.subhead('SwinFusion++ and the Preliminary-Study Xception Baseline'))
    x.append(B('Table 9 places SwinFusion++ beside the Xception baseline of the preliminary study.'))
    x.append(table_block('9', src='RQ2/T9', title='SwinFusion++ and the Preliminary-Study Xception Baseline'))
    x.append(B('On FaceForensics++, where both studies used test sets of 280 videos (140 fake) drawn under the same '
               'source-pair split rule, SwinFusion++ reached ROC-AUC 0.9964 on C23 and 0.9941 on C40 (fixed recipe '
               '0.9942 and 0.9878), against 0.7725 and 0.8109 for Xception. Its accuracy was 98.21% and 96.07% (fixed '
               'recipe 97.86% and 94.64%), against 69.64% and 74.29%. On Celeb-DF v2, SwinFusion++ reached ROC-AUC '
               '0.9983 (fixed recipe 0.9951) on its 978-video test set, while Xception reached 0.6480 on its 859-video '
               'test set and labeled every video fake, so its 84.17% accuracy equals the share of fake videos. On '
               'DeeperForensics-1.0, both ranked videos almost perfectly (SwinFusion++ 0.9954, fixed recipe 0.9974; '
               'Xception 0.9978), but on very different populations: Xception’s test set held 2,385 videos, 91.61% of '
               'them fake and including perturbed variants, and at its threshold it missed 1,288 fake videos '
               '(accuracy 46.00%).'))
    x.append(B('SwinFusion++ therefore ranked videos far better than the preliminary-study Xception on FaceForensics++ '
               'C23 and C40 and much better on Celeb-DF v2, although on a different test population; on '
               'DeeperForensics-1.0 the two were similar. The two models differ in pipeline, training budget, '
               'pretraining, capacity, and number of seeds, so the comparison shows that SwinFusion++ exceeds this particular baseline on FaceForensics++ and Celeb-DF v2, not that the architecture alone accounts for the gap.'))

    x.append(D.subhead('Comparison With Previously Reported Results'))
    x.append(B('Table 10 lists the previously reported Tier A results, which use the same dataset, manipulation subset, '
               'compression, and video-level unit as this study, and Table 11 lists the Tier B results, which pool all '
               'four FaceForensics++ manipulations, leave the subset unstated, or score frames. Table J9 gives the full '
               'list of values considered and the reason for each exclusion.'))
    x.append(table_block('10', src='RQ2X/T10', title='Previously Reported Tier A Results on the Benchmarks of This Study'))
    x.append(table_block('11', src='RQ2X/T11', title='Previously Reported Tier B Results on FaceForensics++'))
    x.append(B('In ROC-AUC, the only Tier A value is STIL’s 0.9712 on C40, below the 0.9941 of the BO-selected '
               'SwinFusion++ (fixed recipe 0.9878). The Tier B ROC-AUC values ranged from 0.5749 (DSP-FWA) to 0.9987 '
               '(TALL-Swin) on C23 and from 0.6160 (Face X-ray, as reported by Xu et al., 2023) to 0.983 (FTCN) on C40, '
               'while SwinFusion++ reached 0.9964 and 0.9941 (fixed recipe 0.9942 and 0.9878) on the DeepFakes subset '
               'alone; because the Tier B values pool manipulations or leave the subset unstated, they are not '
               'like-for-like.'))
    x.append(B('Accuracy is compared only for the Tier A values on balanced test sets: the two FaceForensics++ sets and '
               'the DeeperForensics-1.0 standard set. On FF++ C23, the reported accuracies ranged from 92.14% (ADDNet-3D) '
               'to 100.00% (Xception with frame-score averaging, as reported by X. Li et al., 2020), and on C40 from '
               '89.29% (C3D) to 98.21% (STIL). The BO-selected SwinFusion++ reached 98.21% and 96.07%, 1.79 and 2.14 '
               'percentage points below the highest values; the fixed recipe was 2.14 and 3.57 points below. On the '
               'DeeperForensics-1.0 standard set, the reported accuracies ranged from 98.50% (C3D) to 100.00%, and '
               'SwinFusion++ (98.51%; fixed recipe 98.76%) lay within that range, near the ceiling. Celeb-DF v2 '
               'accuracies are not compared: this study’s test set is 86.20% fake, so calling every video fake would '
               'already score 86.20%, and the published test sets have other or unstated class balances.'))
    x.append(B('Under their own protocols, the published within-dataset results and those of SwinFusion++ therefore lie in the same high range on FaceForensics++ and near the ceiling on DeeperForensics-1.0; Celeb-DF v2 accuracies cannot be compared. Because no test videos, splits, or operating points are '
               'shared, the data support neither a claim that SwinFusion++ outperforms these established models nor '
               'the reverse.'))

    x.append(D.subhead('Answer to Research Question 2'))
    x.append(B('On the FaceForensics++ DeepFakes C23 and C40 subsets, Celeb-DF v2, and the DeeperForensics-1.0 '
               'construction, the BO-selected SwinFusion++ reached ROC-AUC of 0.9941 to 0.9983 and accuracy of 96.07% '
               'to 98.51% (fixed recipe 0.9878 to 0.9974 and 94.64% to 98.76%). It ranked videos far better than the '
               'Xception baseline of the preliminary study on FaceForensics++ and Celeb-DF v2 and similarly on '
               'DeeperForensics-1.0, a comparison limited by the different pipeline and, for the last two datasets, '
               'by different test populations. Against previously reported results for a wider set of established detectors, its FaceForensics++ ROC-AUC lay within the reported range on C23 and above it on C40, although almost all of these values are Tier B and not like-for-like; its accuracy on the balanced FaceForensics++ test sets was 1.79 to 2.14 percentage points below the highest Tier A values (fixed recipe 2.14 to 3.57); and on the DeeperForensics-1.0 standard set its accuracy lay within the reported range, near the ceiling. Because those results come from other splits and protocols, they place SwinFusion++ among the listed methods on FaceForensics++ but cannot rank it against them.'))
    return ''.join(x)
