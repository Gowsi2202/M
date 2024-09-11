from fastapi import APIRouter, Depends, HTTPException
from dependencies import verify_token  # Import the token verification function

user = APIRouter()

@user.get("/user-data")
async def get_user_data(username: str = Depends(verify_token)):
    _, role = username  # Extract the role from the token
    if role != "user":
        raise HTTPException(status_code=403, detail="Access forbidden: Users only")
    # Access the protected user data here
    return {"message": f"Hello {username}, this is protected user data."}
