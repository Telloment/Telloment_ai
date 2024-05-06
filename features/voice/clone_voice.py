import base64
import hashlib

from openvoice import se_extractor
from features.voice import env_vars

from openvoice.se_extractor import hash_numpy_array


def get_key(user_id: str) -> str:
    hsh = hashlib.sha256(user_id.encode()).digest()
    b64 = base64.b64encode(hsh)
    return b64.decode('utf-8')[:16].replace('/', '_^')


def clone_voice(user_id: str, key: str, audio_path: str):
    (se, name) = se_extractor.get_se(audio_path, env_vars.tone_color_converter, key, vad=False)
    return se, name
