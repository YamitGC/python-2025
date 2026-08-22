from jose import jwt
from jose.exceptions import JWTError
from fastapi import HTTPException

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Invalid token")
    
token_ejemplo = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3VhcmlvMTIzIiwiZXhwIjoxNzU0NDQ5MDA0fQ.pAiu2LvJrQORWCmyrRyCEj7ZXxuR9eEfZcA4zj1K5mI"
    
try:
    contenido = verify_token(token_ejemplo)
    print("Token válido:", contenido)
except ValueError as e:
    print("Error al verificar el token:", str(e))