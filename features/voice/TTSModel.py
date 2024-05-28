import requests
from features.voice import env_vars
import os
from init_vars import configs

url = 'https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts'


def tts(text: str, filename: str, emotion: int, strength: int):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-NCP-APIGW-API-KEY-ID': configs.clova_id,
        'X-NCP-APIGW-API-KEY': configs.clova_secret
    }

    data = {
        'speaker': 'vara',
        'speed': '0',
        'text': text,
        'volume': '0',
        'pitch': '0',
        'format': 'wav',
        'emotion': emotion,
        'emotion_strength': strength,
    }

    response = requests.post(url, headers=headers, data=data)
    save_wav(response.content, filename)


def save_wav(audio, path):
    if not path.endswith('.wav'):
        path += '.wav'

    with open(path, 'wb') as f:
        f.write(audio)

    return audio
