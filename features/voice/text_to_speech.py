import os

import torch

from features.voice import env_vars
from features.voice import TTSModel
from fastapi import File


def text_to_speech(user_id: str, text: str) -> File:
    if not os.path.exists(env_vars.output_dir):
        os.makedirs(env_vars.output_dir, exist_ok=True)

    target_se = torch.load(f'resources/{user_id}/se.pth', map_location=env_vars.device)

    # Convert the hash value to base64 and make file name possible
    src_path = f'{env_vars.output_dir}/tmp.wav'
    save_path = f'{env_vars.output_dir}/output_v2_kr.wav'

    TTSModel.tts(text, src_path)

    encode_message = "@MyShell"
    env_vars.tone_color_converter.convert(
        audio_src_path=src_path,
        src_se=env_vars.source_se,
        tgt_se=target_se,
        output_path=save_path,
        message=encode_message)

    f: File = open(save_path, 'rb')
    return f
