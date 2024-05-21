from fastapi import APIRouter, BackgroundTasks
import features.voice.clone_voice as Clone
import features.voice.text_to_speech as TTS
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/voice")


@router.get('/', tags=["voice"])
async def voice():
    return {"message": "Voice API"}


@router.post('/{user_id}', tags=["voice"], status_code=202)
async def clone_voice(user_id: str, background_tasks: BackgroundTasks, audio_file: UploadFile = File(...)):
    audio_path = f"resources/{user_id}"
    audio_name = "voice_rec.wav"
    os.makedirs(f"{audio_path}", exist_ok=True)
    with open(f"{audio_path}/{audio_name}", "wb") as audio:
        audio.write(audio_file.file.read())

    background_tasks.add_task(Clone.clone_voice, user_id=user_id, audio_path=f"{audio_path}/{audio_name}")
    return {
        "result": "accepted"
        , "key": key
    }


@router.get('/{user_id}/speech', tags=["voice"], response_class=FileResponse)
async def text_to_speech(user_id: str, text: str):
    TTS.text_to_speech(user_id, text)
    return {"message": "text to speech success"}
