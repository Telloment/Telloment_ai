from fastapi import APIRouter
import features.voice.clone_voice as Clone
import features.voice.text_to_speech as TTS

router = APIRouter(prefix="/voice")


@router.get('/', tags=["voice"])
async def voice():
    return {"message": "Voice API"}


@router.put('/{user_id}', tags=["voice"])
async def clone_voice(user_id: str, audio_path: str):
    Clone.clone_voice(user_id, audio_path)
    return {"result": "success"}


@router.get('/{user_id}/speech', tags=["voice"])
async def text_to_speech(user_id: str, text: str):
    TTS.text_to_speech(user_id, text, language='KR')
    return {"message": "text to speech success"}
