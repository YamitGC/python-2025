from fastapi import FastAPI, Depends
from security import authenticate

app = FastAPI()

@app.get("/")
def public_route():
    return {"message": "Bienvenido a nuestra API pública sin contraseña"}


@app.get("/private")
def private_route(username: str = Depends(authenticate)):
    return {"message": f"Bienvenido a tu área privada, {username}!"}