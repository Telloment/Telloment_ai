import os

import torch
import hashlib

from features.voice import env_vars
from features.voice import TTSModel
from fastapi import File


def text_to_speech(user_id: str, text: str) -> str:
    if not os.path.exists(env_vars.output_dir):
        os.makedirs(env_vars.output_dir, exist_ok=True)

    target_se = torch.load(f'resources/{user_id}/se.pth', map_location=env_vars.device)

    # Convert the hash value to base64 and make file name possible
    src_path = f'{env_vars.output_dir}/tmp.wav'
    # apply hash function to user_id && text
    h = hashlib.sha256()
    h.update(user_id.encode())
    h.update(text.encode())
    h_value = h.digest()
    h_value = h_value[:16].replace('/', '_^')
    save_path = f'{env_vars.output_dir}/output_v2_{h_value}.wav'
    print(f"save_path: {save_path}")
    TTSModel.tts(text, src_path)

    encode_message = "@MyShell"
    env_vars.tone_color_converter.convert(
        audio_src_path=src_path,
        src_se=env_vars.source_se,
        tgt_se=target_se,
        output_path=save_path,
        message=encode_message)

    print(f"Text to speech done")
    return save_path
