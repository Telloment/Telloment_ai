from fastapi import APIRouter

router = APIRouter()
path = "/voice"

@router.get(path, tags=["voice"])
async def voice():
    return {"message": "Voice API"}