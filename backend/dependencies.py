from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from database import db  # Import from database.py
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    role: str

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # Placeholder token verification and user fetching logic
    user = await db.users.find_one({"username": "example_user"})  # Replace with actual user lookup
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return User(username=user["username"], role=user["role"])

def require_role(required_role: str):
    async def role_checker(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker




SECRET_KEY = "123456789"  # Should be the same as used in login
ALGORITHM = "HS256"  # Should be the same as used in login

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return username, role
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

