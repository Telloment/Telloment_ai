# from fastapi import APIRouter
# from features import emotion
#
# router = APIRouter()
# path = "/emotion"
#
#
# @router.get(path, tags=["emotion"])
# async def get_emotion(text: str):
#     (emo, n) = emotion.get_emotion(text)
#     return {
#         "emotion": emo,
#         "score": n,
#     }
