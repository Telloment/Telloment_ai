from fastapi import FastAPI
# from routers.emotion import router as emotion_router
# from routers.voice import router as voice_router

app = FastAPI()
# app.include_router(emotion_router, prefix="/v1")
# app.include_router(voice_router, prefix="/v1")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
