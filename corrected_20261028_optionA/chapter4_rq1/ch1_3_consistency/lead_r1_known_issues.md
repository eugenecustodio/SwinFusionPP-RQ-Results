# Lead: issues already known from earlier work (check each one and write the edits)

1. **Gamma correction is described as applied**, but the final pipeline disabled it (D-08). Places to check:
   - block 246 (Conceptual Framework inputs);
   - block 269 (operational definition: "Any low-light transformation … evaluated as an ablation");
   - block 334 (Software Framework preprocessing layer);
   - blocks 442–444 (clip-consistent photometric handling and the gamma formula);
   - block 563 (Data Gathering: "gamma correction γ=2 for dark frames");
   - block 175 (gamma-policy ablation);
   - Figure 1 (image) may also show it.
2. **Ablations promised under RQ1 scope (block 175):**
   - The gamma-policy and augmentation-policy ablations were not run.
   - The component ablations ran as single seed, BO regimen, C23 only.
   - The controls ran on C23 only.
3. **BO trial budget "12, 16, or 20" (blocks 174 and 504):** the actual counts were 12/12/8/8 (completed 8/8/5/8).
4. **Baselines (blocks 148, 175, 326, 368):** Xception, I3D, STIL, FTCN, TALL-Swin and SFormer, the two CNN–LSTMs, CAST and TSFF-Net.
   - The registry gives every external model as LITERATURE_ONLY or NOT_REPORTED.
   - The CNN–LSTM and Xception numbers come from the preliminary study (a different pipeline).
   - Check how the RQ2–RQ4 write-ups present them, and whether the Chapter 1/3 wording ("will reproduce", "verified established-baseline core") is still true.
5. **Transfer directions:** block 520 implies every source; FF++ C40 was not used as a source.
6. **DeeperForensics perturbation strata (blocks 173 and 614):** not evaluated.
7. **Hardware (block 498):** H100/A100 is stated; the work ran on an RTX 5090.
8. **Compute (block 617):** promises preprocessing, clip and complete-video latency and throughput. Latency was not properly measured; only cold single-clip timings exist.
9. **The "confidence score" term:**
   - Chapter 1 (block 198: "label + confidence + metadata") and Chapter 2 (block 235: "Real or Fake label with confidence") use it.
   - Block 316 says the term will not be used.
   - The appendix figure description (Results Interface) says "deepfake probability score".
10. **FaceNet distance:** blocks 441 and 563 say Euclidean; the web-app review says the shared preprocessing uses cosine distance (max 0.55). VERIFY from the package.
11. **Frame sampling:** 2 fps and seven locked 16-frame clips per video (evaluation_protocol_v020.json). Check every Chapter 1–3 mention of the clip count and sampling (e.g. the HIPO/flowchart text).
12. **Duplicated paragraphs in Chapter 2:** blocks 213 and 218 look like near-duplicates. Check for others.
13. **Leftover "undersampling" text** somewhere in Chapters 1–3 (noted earlier). Find it and check it against the actual sampler (class → group → video → clip).
14. **The title-page date:** check it.
15. **Hypothesis (blocks 250–252):** its wording must match how Chapter 4/RQ6 will decide it (Holm families, ROC-AUC). Do not change the hypothesis itself; flag it if needed.
16. **Metadata shortcut audit (block 433):** it was done. Its D-43 stratified reporting was not, so check whether Chapter 3 promises it.
17. **Normalization:** ImageNet mean/std for both backbones. Chapter 3 says "checkpoint-specific normalization", which is still true; just confirm.
18. **Tables 1–8 in Chapter 4 now use the family names** ("within-dataset architecture family", etc.). Check that Chapter 3 block 615 is consistent ("Holm adjustment will be the default…").
