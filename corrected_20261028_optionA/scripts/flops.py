"""Parameter and FLOP counts per 16-frame clip for SwinFusion++ and its two standalone backbones.

The project's model code is imported unchanged. Only the pretrained-weight checks are replaced, so
the models are built with random weights (FLOPs and parameter counts do not depend on weights):
  * load_pretrained -> torchvision constructor(weights=None), with the registered parameter count asserted
  * verify_checkpoint -> returns the digest already registered in the model config
  * validate_runtime / upstream-source hash -> skipped (CPU wheel instead of the CUDA build)
FLOP convention = the project's stored one (TorchDispatch FlopCounterMode, two FLOPs per multiply-add,
matmul and convolution only). The stored backbone FLOPs must be reproduced exactly before the
SwinFusion++ number is reported.

Usage: python flops.py <Thesis_Code_final_20261004 root> <out json>
"""
import json, sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / 'src'))
import torch, yaml
from torch.utils.flop_counter import FlopCounterMode
from torchvision.models import swin_b
from torchvision.models.video import swin3d_b
from swinfusionpp.models import checkpoints, stage_taps, standalone_swin, standalone_video_swin, full_model

STORED = {'spatial': (86744249, 493757562880), 'video': (87640009, 281332418560)}  # standalone_operator_costs_v001.json


def fake_verify(kind, root=ROOT):
    sha = yaml.safe_load((Path(root) / 'configs/models' / f'{kind}_backbone.yaml').read_text())['checkpoint_sha256']
    return None, {'sha256': sha, 'weight_enum': checkpoints.SPECS[kind].enum,
                  'provenance': {'torchvision_0_17_2_model_source.py': {'sha256': 'skipped'}}}


def fake_load(kind, root=ROOT):
    model = (swin_b if kind == 'swin_b' else swin3d_b)(weights=None)
    assert sum(p.numel() for p in model.parameters()) == checkpoints.SPECS[kind].parameters, kind
    return model


for module in (checkpoints, stage_taps, standalone_swin, standalone_video_swin, full_model):
    for name, value in (('verify_checkpoint', fake_verify), ('load_pretrained', fake_load),
                        ('validate_runtime', lambda: None), ('file_sha256', lambda path: 'skipped')):
        if hasattr(module, name):
            setattr(module, name, value)


def count(model):
    model.eval()
    params = sum(p.numel() for p in model.parameters())
    x = torch.randn(1, 16, 3, 224, 224)
    with torch.no_grad(), FlopCounterMode(display=False) as fc:
        out = model(x)
    assert tuple(out.shape) == (1, 1), out.shape
    return params, fc.get_total_flops()


torch.manual_seed(0)
result = {}
for key, build in (('spatial', lambda: standalone_swin.StandaloneSwinB(root=ROOT)),
                   ('video', lambda: standalone_video_swin.StandaloneVideoSwinB(root=ROOT))):
    params, flops = count(build())
    assert (params, flops) == STORED[key], (key, params, flops, STORED[key])
    result[key] = dict(parameters=params, clip_flops=flops)
    print(f'{key}: {params:,} parameters, {flops / 1e9:.2f} GFLOPs per clip  (matches stored value)')

params, flops = count(full_model.SwinFusionModel('full', root=ROOT))
result['swinfusionpp_full'] = dict(parameters=params, clip_flops=flops)
print(f'swinfusionpp_full: {params:,} parameters, {flops / 1e9:.2f} GFLOPs per clip')
result['convention'] = 'FlopCounterMode (torch 2.7.1 CPU, float32, batch 1, input 1x16x3x224x224); two FLOPs per multiply-add; matmul and convolution only'
json.dump(result, open(sys.argv[2], 'w'), indent=1)
