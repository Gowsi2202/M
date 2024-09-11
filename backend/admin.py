from fastapi import APIRouter, Depends, HTTPException
from dependencies import verify_token  # Import the token verification function

admin = APIRouter()

@admin.get("/admin-data")
async def get_admin_data(username: str = Depends(verify_token)):
    _, role = username  # Extract the role from the token
    if role != "admin":
        raise HTTPException(status_code=403, detail="Access forbidden: Admins only")
    # Access the protected admin data here
    return {"message": f"Hello {username}, this is protected admin data."}
