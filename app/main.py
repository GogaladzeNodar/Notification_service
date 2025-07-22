from fastapi import FastAPI
from app.api.notification import router 

app = FastAPI()

app.include_router(router) 

@app.get("/")
async def root():
    return {"message": "Notifier is alive"}