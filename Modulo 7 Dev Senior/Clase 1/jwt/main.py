from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256" # Crea un token JWT con el algoritmo HS256 pivado. RS256 es más seguro pero requiere una clave privada y pública.
data = {
    "sub": "usuario123",
    "exp": datetime.now(timezone.utc) + timedelta(hours=1)  # El token expira en 1 hora
}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

print(f"\nToken:", token)