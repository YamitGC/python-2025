from fastapi import FastAPI, Depends
from security import authenticate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenido a nuestra app de rutas protegidas"}

@app.get("/dashboard")
def read_dashboard(current_user: dict = Depends(authenticate)):
    return {
        "message": f"Bienvenido al dashboard, {current_user['username']}!",
        "roles": current_user['roles']
    }
    
@app.get("/admin_only")
def read_admin_area(current_user: dict = Depends(authenticate)):
    if "admin" not in current_user['roles']:
        return {"ERROR": "Acceso restringido solo para roles de Administrador"}
    return {"message": f"Bienvenido al área de administración, {current_user['username']}!"}
