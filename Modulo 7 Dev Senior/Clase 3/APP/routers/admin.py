from fastapi import APIRouter, Depends
from auth.roles import require_role, get_current_user

router = APIRouter()

@router.get("/admin-data")
def get_admin_data(current_user: dict = Depends(require_role("admin"))):
    return {"msg": "Datos solo de administradores"}