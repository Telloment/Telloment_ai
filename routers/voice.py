from fastapi import APIRouter, BackgroundTasks
import features.voice.clone_voice as Clone
import features.voice.text_to_speech as TTS

router = APIRouter(prefix="/voice")


@router.get('/', tags=["voice"])
async def voice():
    return {"message": "Voice API"}


@router.put('/{user_id}', tags=["voice"], status_code=202)
async def clone_voice(user_id: str, audio_path: str, background_tasks: BackgroundTasks):
    key = Clone.get_key(user_id)
    background_tasks.add_task(Clone.clone_voice, user_id=user_id, key=key, audio_path=audio_path)
    return {
        "result": "accepted"
        , "key": key
    }


@router.get('/{user_id}/speech', tags=["voice"])
async def text_to_speech(user_id: str, key: str, text: str):
    TTS.text_to_speech(user_id, key, text)
    return {"message": "text to speech success"}
