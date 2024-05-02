import torch

from openvoice.api import ToneColorConverter

ckpt_converter = 'OpenVoice/checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'
source_se = torch.load(f'OpenVoice/checkpoints_v2/base_speakers/ses/KR.pth', map_location=device)
tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')