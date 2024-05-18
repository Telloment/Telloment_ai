import requests
import env_vars
import os

url = 'https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts'


def tts(text: str, filename: str):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-NCP-APIGW-API-KEY-ID': client_id,
        'X-NCP-APIGW-API-KEY': client_secret
    }

    data = {
        'speaker': 'nara',
        'speed': '0',
        'text': text,
        'volume': '0',
        'pitch': '0',
        'format': 'wav'
    }

    response = requests.post(url, headers=headers, data=data)
    save_wav(response.content, filename)


def save_wav(audio, path):
    if not path.endswith('.wav'):
        path += '.wav'

    with open(path, 'wb') as f:
        f.write(audio)

    return audio
