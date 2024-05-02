from openvoice import se_extractor
from features.voice import env_vars


def clone_voice(user_id: str, audio_path: str):
    (se, name) = se_extractor.get_se(audio_path, env_vars.tone_color_converter, vad=False)
    return se, name
