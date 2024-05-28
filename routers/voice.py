from fastapi import APIRouter, BackgroundTasks, HTTPException
import features.voice.clone_voice as Clone
import features.voice.text_to_speech as TTS
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os
from features.checker import is_wav
from pydantic import BaseModel

router = APIRouter(prefix="/voice")


# @router.get('/', tags=["voice"])
# async def voice():
#     return {"message": "Voice API"}
class CloneRequest(BaseModel):
    emotion: str
    strength: int


@router.post('/{user_id}', tags=["voice"], status_code=202)
async def clone_voice(user_id: str, background_tasks: BackgroundTasks, audio_file: UploadFile = File(...)):
    if not is_wav(audio_file.file.read()):
        raise HTTPException(status_code=400, detail="Not a wav format ")

    audio_path = f"resources/{user_id}"
    audio_name = "temp.wav"
    os.makedirs(f"{audio_path}", exist_ok=True)
    with open(f"{audio_path}/{audio_name}", "wb") as audio:
        audio.write(audio_file.file.read())

    background_tasks.add_task(Clone.clone_voice, user_id=user_id, audio_path=f"{audio_path}/{audio_name}")
    return {
        "result": "accepted"
    }


@router.get('/{user_id}/speech', tags=["voice"])
async def text_to_speech(user_id: str, text: str, emotion: str, strength: int) -> FileResponse:
    path = TTS.text_to_speech(user_id, text, emotion, strength)
    return FileResponse(path, media_type='audio/wav', filename='output.wav')
