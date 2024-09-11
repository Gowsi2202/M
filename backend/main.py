import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login import login
from register import register
from admin import admin  # Import admin routes
from user import user
from database import db  # Import from database.py
from starlette.staticfiles import StaticFiles as StaticFiles  # noqa

app = FastAPI()

frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")

app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router=login)
app.include_router(router=register)
app.include_router(router=admin) # Include admin routes
app.include_router(router=user)

@app.get("/", tags=["root"])
async def greet():
    return {"Hello, World...!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)