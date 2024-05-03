from fastapi import APIRouter, BackgroundTasks
import features.voice.clone_voice as Clone
import features.voice.text_to_speech as TTS

router = APIRouter(prefix="/voice")


@router.get('/', tags=["voice"])
async def voice():
    return {"message": "Voice API"}


@router.put('/{user_id}', tags=["voice"], status_code=202)
async def clone_voice(user_id: str, audio_path: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(Clone.clone_voice, user_id=user_id, audio_path=audio_path)
    return {"result": "accepted"}


@router.get('/{user_id}/speech', tags=["voice"])
async def text_to_speech(user_id: str, text: str):
    TTS.text_to_speech(user_id, text, language='KR')
    return {"message": "text to speech success"}
