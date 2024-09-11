from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from login import login
from register import register


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




client = AsyncIOMotorClient("mongodb://localhost:27017/")

app.include_router(router=login)
app.include_router(router=register)


def get_db():
    return client["Railway_System"]



