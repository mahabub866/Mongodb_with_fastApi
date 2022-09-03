from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
app = FastAPI()

@app.get('/')
async def index():
    return {"message": "Hello, world"}
