from fastapi import FastAPI, HTTPException, status 
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict

app = FastAPI()

# Modelo de entrada Post/Put
class RecursoCreate(BaseModel):
    nombre: str = Field(..., min_length=4, max_length=20)
    descripcion: Optional[str] = Field(None, max_length=200)


class RecursoResponse(RecursoCreate):
    item_id: int = Field(..., gt=0) 
    
class UsuarioCreate(BaseModel):
    nombre: str = Field(..., min_length=5, max_length=20)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    edad : int = Field(..., gt=0, lt=100)
    
class UsuarioResponse(UsuarioCreate):
    usuario_id: int = Field(..., gt=0)

# Base de datos simulada
db_recursos: List[Dict] = []
next_recurso_id = 1

db_usuarios: List[Dict] = []
next_usuario_id = 1

@app.get("/")
def root():
    return {"message": "Uso de pydantic, HTTTPException, Field y JSONResponse"}

@app.post("/recursos/", response_model=RecursoResponse, status_code=status.HTTP_201_CREATED)
def crear_recurso(recurso: RecursoCreate):
    global next_recurso_id
    new_item = recurso.model_dump()
    new_item["item_id"] = next_recurso_id
    db_recursos.append(new_item)
    next_recurso_id += 1
    
    new_item_2 = RecursoResponse(**new_item)
    response_content ={
        "message": "Recurso creado exitosamente",
        "recurso": new_item_2.model_dump()
    }
    return JSONResponse(content=response_content, status_code=status.HTTP_201_CREATED)

@app.get("/recursos/")
def get_all_recursos():
    if not db_recursos:
        raise HTTPException(status_code=404, detail="No hay recursos disponibles")
    return db_recursos

@app.get("/recursos/{item_id}", response_model=RecursoResponse)
def read_recurso(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="ID de recurso inválido. Debe ser mayor que 0")    
    for item in db_recursos:
        if item["item_id"] == item_id:
            return RecursoResponse(**item)
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@app.put("/recursos/{item_id}", response_model=RecursoResponse)
def update_recurso(item_id: int, recurso: RecursoCreate):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="ID de recurso inválido. Debe ser mayor que 0")
    for index, item in enumerate(db_recursos):
        if item["item_id"] == item_id:
            updated_item = recurso.model_dump()
            updated_item["item_id"] = item_id
            db_recursos[index] = updated_item
            return RecursoResponse(**updated_item)
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@app.delete("/recursos/{item_id}")
def delete_recurso(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="ID de recurso inválido. Debe ser mayor que 0")
    for index, item in enumerate(db_recursos):
        if item["item_id"] == item_id:
            del db_recursos[index]
            return JSONResponse(content={"message": "Recurso eliminado exitosamente"}, status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Recurso no encontrado")
