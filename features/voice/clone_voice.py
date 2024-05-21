import base64
import hashlib
import os

from openvoice import se_extractor
from features.voice import env_vars

from openvoice.se_extractor import hash_numpy_array
from openvoice.api import ToneColorConverter


def _get_key(user_id: str) -> str:
    return user_id.replace('/', '_^')


def clone_voice(user_id: str, audio_path: str):
    key = _get_key(user_id)
    # if resources/user_id/se.pth exists load that
    # else extract se from audio_path and save it to resources/user_id/se.pth
    if os.path.exists(f'resources/{user_id}/se.pth'):
        converter = ToneColorConverter(f'{env_vars.ckpt_converter}/config.json', device=env_vars.device)
        converter.load_ckpt(f'resources/{user_id}/se.pth')
        (se, name) = se_extractor.get_se(audio_path, converter, target_dir=f'resources/{user_id}', vad=False)
    else:
        (se, name) = se_extractor.get_se(audio_path, env_vars.tone_color_converter, target_dir=f'resources/{user_id}', vad=False)
    print(f"SE extracted from {name}")
    return se, name
