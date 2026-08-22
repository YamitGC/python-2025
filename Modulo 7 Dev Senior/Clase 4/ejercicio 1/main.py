from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

class Recurso(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    
db: List[Dict] = []
next_id = 1

@app.get("/")
def root():
    return {"message": "Bienvenido a mi app web"}

@app.post("/recurso/")
def create_recurso(recurso: Recurso):
    global next_id
    new_item = recurso.model_dump()
    new_item["id"] = next_id
    db.append(new_item)
    next_id += 1
    print(f"Recurso recibido con éxito{new_item}")
    return {"mensaje": "Recurso creado exitosamente", "data": new_item}

@app.get("/recurso/")
def get_all_items():
    return {"recursos": db}

@app.get("/recurso/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=422, detail="ID inválido")
    for item in db:
        if item["id"] == item_id:
            return {"recurso": item}
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@app.delete("/recurso/{item_id}")
def delete_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=422, detail="ID inválido")
    for i, item in enumerate(db):
        if item["id"] == item_id:
            db.pop(i)
            return {"mensaje": "Recurso eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Recurso no encontrado")
