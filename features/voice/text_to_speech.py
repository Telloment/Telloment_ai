import os

import torch

from features.voice import env_vars
from features.voice import TTSModel


def text_to_speech(user_id: str, key: str, text: str):
    if not os.path.exists(env_vars.output_dir):
        os.makedirs(env_vars.output_dir, exist_ok=True)


    target_se = torch.load(f'processed/demo_speaker2_v2_{key}/se.pth', map_location=env_vars.device)

    # Convert the hash value to base64 and make file name possible
    src_path = f'{env_vars.output_dir}/tmp.wav'

    try:
        TTSModel.TTS_speecht5(text, src_path)

        save_path = f'{env_vars.output_dir}/output_v2_kr.wav'
        #save to save path
        # os.rename(src_path, save_path)
        # Run the tone color converter
        encode_message = "@MyShell"
        env_vars.tone_color_converter.convert(
            audio_src_path=src_path,
            src_se=env_vars.source_se,
            tgt_se=target_se,
            output_path=save_path,
            message=encode_message)
    finally:
        if os.path.exists(src_path):
            os.remove(src_path)
