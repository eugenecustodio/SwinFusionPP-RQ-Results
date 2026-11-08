# Computational cost

Promised in the manuscript (Chapter 3, *Statistical Treatment of Data*): total and trainable parameters, operations per clip, peak memory where feasible, preprocessing/clip/video latency, throughput and checkpoint size.

| Measure | Swin-B | Video Swin-B | SwinFusion++ |
|---|---|---|---|
| Parameters | 86,744,249 | 87,640,009 | 180,885,009 |
| GFLOPs per 16-frame clip | 493.8 | 281.3 | 795.2 |
| TFLOPs per video (7 evaluation clips) | 3.46 | 1.97 | 5.57 |
| Training throughput, clips/s (Phase 38 smoke, microbatch 1) | 25.7 | 24.0 | 10.4 |
| Training throughput, clips/s (planning addendum) | 38.0 | 34.1 | 16.0 |
| Peak training GPU memory, GB | 4.12 | 4.63 | 9.24 |
| Cold single-clip inference, s (includes start-up overhead) | 0.035 | 0.022 | 0.051 |
| Training checkpoint, GB (weights + AdamW state) | 1.04 | 1.05 | 2.17 |
| Weights only (fp32), GB — derived | 0.35 | 0.35 | 0.72 |

## Sources and checks
- **Parameters and FLOPs** were counted with `../scripts/flops.py`. It runs the project's own model code (from the backup) with random weights, using the project's FLOP convention: FlopCounterMode, two FLOPs per multiply-add, matmul and convolution only, batch 1, 16×3×224×224.
  - **Check:** the Swin-B and Video Swin-B counts reproduce the stored values in `results/efficiency/standalone_operator_costs_v001.json` exactly.
  - **Check:** the SwinFusion++ parameter count (180,885,009) equals the count implied by its AdamW checkpoint size, as an independent confirmation.
- **Fusion overhead:** SwinFusion++ adds about 6.5 M parameters and about 20 GFLOPs per clip (2.5%) beyond the two backbones. Most of its cost is running both backbones.
- **Clips per video:** 7. Source: `00_Shared/protocol_and_decisions/evaluation_protocol_v020.json` (video aggregation "mean_of_seven_locked_clip_logits"). Checked 2026-10-30.
- **Throughput, memory and cold inference** were measured on an NVIDIA RTX 5090 in bf16 (2026-09-20; `results/efficiency/phase38_rtx5090_v001/` and `resource_cost_planning_addendum_v001.json`).
  - The two throughput measurements use different settings, so report both with their conditions, or only their ratio: SwinFusion++ trains at about 0.40–0.47× the speed of one backbone.
- **Not measured:** steady-state inference latency, preprocessing latency, whole-video latency and deployment-server throughput. The cold single-clip times include initialization overhead and are not a latency benchmark. State this as a limitation, or measure on the deployment server.
