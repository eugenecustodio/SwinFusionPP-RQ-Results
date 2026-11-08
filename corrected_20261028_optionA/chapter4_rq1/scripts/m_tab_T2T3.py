"""Write T2 (analyses/families/sections) and T3 (deviations) as printed strings, plus notes for T1-T3."""
import csv
D='/tmp/claude-1000/-home-eugenecustodio-Desktop-Results-SwinFusionPP-RQ-Results-20261004/ab6b7cb5-192a-4488-bb74-326f7040dde1/scratchpad/ch4/team/tables/'
def w(name, header, rows):
    with open(D+name,'w',newline='',encoding='utf-8') as fh:
        c=csv.writer(fh); c.writerow(header); c.writerows(rows)
SAME='Regrouped after scoring; same decisions under the pre-scoring and pooled groupings'
w('T2.csv',['Analysis','Models (regimen)','Family (m)','Grouping status','Section'],[
 ['Within-dataset architecture comparison','SwinFusion++, Swin-B, Video Swin-B (all fixed recipe)','Within-dataset architecture family (8) [RQ1_architecture]',SAME,'4.1.1'],
 ['Frozen-transfer architecture comparison','SwinFusion++, Swin-B, Video Swin-B (all fixed recipe)','Frozen-transfer architecture family (18) [RQ6_architecture]',SAME,'4.1.2; cited in RQ6'],
 ['Threshold-dependent transfer metrics','SwinFusion++, Swin-B, Video Swin-B (all fixed recipe)','None (descriptive; supplementary paired intervals in Appendix J)','Not applicable','4.1.3'],
 ['Configured system, within datasets','BO-selected SwinFusion++ vs fixed-recipe Swin-B and Video Swin-B','Configured-system family, within (8) [RQ1_configured_system]','Primary family before scoring (A-16); relabeled after scoring; same decisions','4.1.4'],
 ['Configured system, frozen transfer','BO-selected SwinFusion++ vs fixed-recipe Swin-B and Video Swin-B','Configured-system family, transfer (18) [RQ6_configured_system]','Primary family before scoring (A-16); relabeled after scoring; same decisions','4.1.4'],
 ['Optimization effect, within datasets','BO-selected minus fixed-recipe SwinFusion++','Optimization-effect family, within (4) [RQ1_optimization_effect]','Separated after scoring; one decision depends on grouping (Celeb-DF v2: p_Holm 0.021 vs 0.077)','4.1.4'],
 ['Optimization effect, frozen transfer','BO-selected minus fixed-recipe SwinFusion++','Optimization-effect family, transfer (9) [RQ6_optimization_effect]',SAME,'4.1.4'],
 ['Matched controls','Fixed-recipe SwinFusion++ vs topology and capacity controls (FF++ C23 training)','Controls families (2 within; 6 transfer) [RQ4_controls, RQ4_controls_transfer]','Unchanged since before scoring (A-16, A-18)','RQ4'],
 ['Component ablations (Tier B)','One-change variants of BO-selected SwinFusion++, one seed, FF++ C23','None (descriptive)','Not applicable','RQ4'],
 ['Calibration and computational cost','All internal models','None (descriptive)','Not applicable','Section after RQ6'],
])
w('T3.csv',['Planned (Chapter 3)','What was done','Reason / source','Consequence for interpretation'],[
 ['12, 16, or 20 BO trials per study, chosen by a resource pilot (blocks 175, 504)','12 trials for FF++ C23 and C40; 8 for Celeb-DF v2 and DeeperForensics-1.0 (8, 8, 5, and 8 completed)','Four-day deadline (A-12); bo_summary.csv','Smaller search for Celeb-DF v2 and DeeperForensics-1.0; affects only the configured-system and optimization-effect results'],
 ['Clip-level gamma correction (γ = 2) for dark clips (blocks 334, 442–444, 563)','No low-light correction in the final pipeline, for any model','D-08 (approved disabled)','Identical for all models; results describe a pipeline without low-light correction'],
 ['Gamma-policy and augmentation-policy (RandAugment) ablations (blocks 175, 444)','Not run','Four-day deadline (A-12; Phases 158–159 skipped)','No evidence on either policy'],
 ['Exact tensor-preserving component ablations (blocks 175, 238)','Four variants, one seed, BO-selected FF++ C23 configuration, FF++ C23 test only','A-11, A-12, A-14','Descriptive only (block 615); reported in RQ4'],
 ['Topology and capacity-matched controls (blocks 159, 175; all four datasets reserved in A-03)','FF++ C23 training only, with frozen transfer from C23','A-03 withdrawn by A-12; A-18','Cannot address the transfer results from Celeb-DF v2 and DeeperForensics-1.0 sources'],
 ['Each source tested on the remaining datasets (block 520)','9 directions from FF++ C23, Celeb-DF v2, and DeeperForensics-1.0; FF++ C40 not used as a source','Optional extension not run (A-07; rq_traceability.yaml)','9 of 12 possible directions are reported'],
 ['DeeperForensics-1.0 perturbation variants as robustness strata (blocks 173, 614)','Not evaluated; only the unperturbed primary test set (402 videos) was scored','evaluation_protocol_v020.json lists 2,010 robustness videos; no results in heldout_seed_metrics_rq1_rq6.csv','No evidence on robustness to perturbations'],
 ['BF16 training on H100 or A100 (block 498)','NVIDIA RTX 5090','A-08; compute/COMPUTE_COST.md','None for accuracy metrics; compute figures refer to the RTX 5090'],
 ['Metadata-shortcut audit for DeeperForensics-1.0 (block 238); D-43 requires results stratified by source metadata','Audit run and passed after the input change; stratified results not produced','D-43; CHAPTER4_NOTES.md §4','Stability across metadata strata is not shown'],
])
notes={
'T1_note.txt':"Note. Videos are the frozen test manifests; coverage and preprocessing failures were identical for every model, seed, and direction. Clusters are the resampling units. Celeb-DF v2 was split by target identity; all 843 fake videos lie in 9 identity clusters, so its intervals are approximate, and whether the swapped-in source identity was also held out could not be verified. Lineage counts follow the evaluation protocol. Strict subsets exclude target videos whose lineage appears in the source's training or validation data. Source-validation coverage: 279/280 (FF++), 977/977, 192/192.",
'T2_note.txt':"Note. Bracketed names are the labels in paired_tests_optionA.csv. Every family applies Holm correction to rank-based cluster permutation p-values. The pre-scoring grouping is the one recorded on 2 October 2026 (A-16): the BO-selected comparisons formed the primary families, and the fixed-recipe comparisons were pooled with the optimization effect (12 within, 27 transfer). The pooled grouping combines all 26 architecture comparisons in one family.",
'T3_note.txt':"Note. Block numbers refer to Chapters 1 and 3 of this manuscript. Decision IDs (A-xx, D-xx) refer to the project's decision log. Statistical amendments made after test scoring are described in Chapter 3 under Amendments after Test Scoring, not in this table. None of the deviations changed a test set, threshold, or temperature.",
}
for k,v in notes.items():
    open(D+k,'w',encoding='utf-8').write(v+'\n'); print(k,len(v.split()))
