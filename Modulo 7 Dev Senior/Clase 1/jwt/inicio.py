from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def crear_token(datos: dict, expiracion: int = 30):
    to_encode = datos.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Invalid token")
    
datos_usuario = {
    "sub": "usuario123",
    "rol": "admin"
}

token_generado = crear_token(datos_usuario)
print("Token generado:", token_generado)

try:
    payload = verificar_token(token_generado)
    print(f"Token verificado, payload => {payload}")
except ValueError as e:
    print(str(e))