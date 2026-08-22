from fastapi import APIRouter, Depends
from auth.security import get_current_user

router = APIRouter()

@router.get("/datos-usuario")
def get_user_data(current_user: dict = Depends(get_current_user)):
    return {"user": current_user["user"], "role": current_user["role"]}