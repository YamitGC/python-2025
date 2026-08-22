from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database.session import get_db
from services.auth_service import create_user, authenticate_user, create_access_token, get_current_user
from schemas.user_task import UserCreate, UserOut, Token
from models.user_task import User

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if len(user.username) < 4 or len(user.username) > 20:
        raise HTTPException(status_code=400, detail="Invalid username length")
    if len(user.password) < 6 or len(user.password) > 20:
        raise HTTPException(status_code=400, detail="Invalid password length")
    if user.role not in ["admin", "user"]:
        raise HTTPException(status_code=400, detail="Invalid role")
    return create_user(user, db)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username, "role": user.role}, db)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/admin")
def admin_route(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return {"message": f"Welcome to the admin panel, {current_user.username}!"}