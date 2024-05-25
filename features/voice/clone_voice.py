import os
import torch
from utils import TorchUtils

from features.voice import env_vars
from openvoice import se_extractor
from utils import AudioUtils


def _get_key(user_id: str) -> str:
    return user_id.replace('/', '_^')


def _clone_with_previous_voice(user_id: str, audio_path: str):
    AudioUtils.attach_wav(audio_path, f'resources/{user_id}/voice_rec.wav')
    (se, name) = se_extractor.get_se(f'resources/{user_id}/voice_rec.wav', env_vars.tone_color_converter,
                                     target_dir=f'resources/{user_id}',
                                     vad=False)
    os.remove(audio_path)
    return se, name


def _apply_previous_converter(user_id: str, audio_path: str):
    tgt_se = torch.load(f'resources/{user_id}/se.pth', map_location=env_vars.device)
    (src_se, name) = se_extractor.get_se(audio_path, env_vars.tone_color_converter, target_dir=f'resources/{user_id}', vad=False)
    ses = TorchUtils.stack_se(src_se, tgt_se)
    torch.save(ses, f'resources/{user_id}/se.pth')
    return ses, name


def _change_file_name(audio_path: str, target_path: str):
    os.rename(audio_path, target_path)


def clone_voice(user_id: str, audio_path: str):
    key = _get_key(user_id)
    # if resources/user_id/se.pth exists load that
    # else extract se from audio_path and save it to resources/user_id/se.pth
    if os.path.exists(f'resources/{user_id}/se.pth'):
        (se, name) = _apply_previous_converter(user_id, audio_path)
    else:
        (se, name) = se_extractor.get_se(audio_path, env_vars.tone_color_converter, target_dir=f'resources/{user_id}',
                                         vad=False)
        _change_file_name(audio_path, f'resources/{user_id}/voice_rec.wav')
    print(f"SE extracted from {name}")
    if os.path.exists(audio_path):
        os.remove(audio_path)
    return se, name
