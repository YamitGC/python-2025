from fastapi import Depends, HTTPException
from auth.security import get_current_user

def require_role(requiered_role: str):
    def role_dependency(user: dict = Depends(get_current_user)):
        if user["role"] != requiered_role:
            raise HTTPException(status_code=403, detail="Acceso denegado")
        return user
    return role_dependency