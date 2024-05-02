import os

import torch
from melo.api import TTS

from features.voice import env_vars


def text_to_speech(key: str, text: str, language: str = 'KR'):
    target_se = torch.load(f'../OpenVoice/checkpoints_v2/base_speakers/ses/{key}.pth', map_location=device)
    speed = 1.0
    model = TTS(language=language, device=env_vars.device)
    speaker_ids = model.hps.data.spk2id
    # Convert the hash value to base64 and make file name possible
    src_path = f'{env_vars.output_dir}/tmp.wav'
    speaker_key = 'KR'
    speaker_id = speaker_ids[speaker_key]

    try:
        speaker_key = speaker_key.lower().replace('_', '-')

        model.tts_to_file(text, speaker_id, src_path, speed=speed)
        save_path = f'{env_vars.output_dir}/output_v2_{speaker_key}.wav'

        # Run the tone color converter
        encode_message = "@MyShell"
        env_vars.tone_color_converter.convert(
            audio_src_path=src_path,
            src_se=env_vars.source_se,
            tgt_se=target_se,
            output_path=save_path,
            message=encode_message)
    finally:
        os.remove(src_path)
