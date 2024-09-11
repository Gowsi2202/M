from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import db  # Import from database.py

register = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    password: str
    aadhar: str
    role: str = "user"  # Default role is 'user'

@register.post("/register")
async def register_user(request: RegisterRequest):
    if request.role not in ["user", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    existing_user = await db.users.find_one({"username": request.username})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Save user data
    new_user = {
        "username": request.username,
        "password": request.password,  # Replace with hashed password
        "aadhar": request.aadhar,
        "role": request.role
    }
    result = await db.users.insert_one(new_user)

    return {"status": "Registered"}
