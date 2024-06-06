import requests
from fastapi import HTTPException
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
        'speed': '2',
        'text': text,
        'volume': '0',
        'pitch': '0',
        'alpha': '2',
        'format': 'wav',
        'emotion': emotion,
        'emotion_strength': strength,
    }

    response = requests.post(url, headers=headers, data=data)
    if 200 <= response.status_code < 300:
        save_wav(response.content, filename)
    else :
        raise HTTPException(
            status_code=400,
            detail="parameter가 잘못되었습니ㄷ"
        )


def save_wav(audio, path):
    if not path.endswith('.wav'):
        path += '.wav'

    with open(path, 'wb') as f:
        f.write(audio)

    return audio
