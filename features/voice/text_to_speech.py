import os

import torch
import hashlib
import base64

from features.voice import env_vars
from features.voice import TTSModel
from fastapi import File
from models.Emotions import Emotions

def _hash_numpy_array(key: str) -> str:
    # Convert the array to bytes
    array_bytes = key.encode('utf-8')
    # Calculate the hash of the array bytes
    hash_object = hashlib.sha256(array_bytes)
    hash_value = hash_object.digest()
    # Convert the hash value to base64
    base64_value = base64.b64encode(hash_value)
    return base64_value.decode('utf-8')[:16].replace('/', '_^')


def text_to_speech(user_id: str, text: str, emotion: str, strength: int) -> str:
    if not os.path.exists(env_vars.output_dir):
        os.makedirs(env_vars.output_dir, exist_ok=True)

    target_se = torch.load(f'resources/{user_id}/se.pth', map_location=env_vars.device)

    # Convert the hash value to base64 and make file name possible
    src_path = f'{env_vars.output_dir}/tmp.wav'
    # apply hash function to user_id && text
    h_value = _hash_numpy_array(f'{user_id}_{text}')
    save_path = f'{env_vars.output_dir}/output_v2_{h_value}.wav'
    print(f"save_path: {save_path}")
    emo = Emotions.from_description(emotion)
    TTSModel.tts(text, src_path, emo.clova_code, strength=strength)

    encode_message = "@MyShell"
    env_vars.tone_color_converter.convert(
        audio_src_path=src_path,
        src_se=env_vars.source_se,
        tgt_se=target_se,
        output_path=save_path,
        message=encode_message)

    print(f"Text to speech done")
    return save_path
