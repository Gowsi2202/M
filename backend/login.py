from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
import datetime
from database import db  # Import from database.py

# Initialize APIRouter
login = APIRouter()

# Secret key for encoding JWT tokens
SECRET_KEY = "123456789"  # Change this to a secure key
ALGORITHM = "HS256"  # Algorithm for JWT encoding

class LoginRequest(BaseModel):
    username: str
    password: str

@login.post("/login")
async def login_user(request: LoginRequest):
    user = await db.users.find_one({"username": request.username})
    
    if user is None:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Replace this with proper password validation
    if request.password != user.get("password"):  # Replace with hashed password comparison
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Create a JWT token
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    token = jwt.encode(
        {"sub": request.username, "role": user.get("role"), "exp": expiration}, 
        SECRET_KEY, 
        algorithm=ALGORITHM
    )

    return {"status": "Logged in", "token": token, "role": user.get("role")}
