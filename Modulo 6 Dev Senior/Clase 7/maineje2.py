from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Dict

app = FastAPI()

class Libro(BaseModel):
    id: int
    titulo: str = Field(..., min_length=2)
    autor: str = Field(..., min_length=3)
    ano_publicacion: int = Field(..., gt=0)
    genero: str = Field(..., min_length=3)
    isbn: str = Field(..., min_length=10, max_length=13)
    tapa: str = Field(..., min_length=3)

    @field_validator("titulo")
    def validar_titulo(cls, v):
        if not v:
            raise ValueError("El título no puede estar vacío")
        return v

Biblioteca_db: Dict[int, Libro] = {}
id_counter = 0

@app.get("/")
def root():
    return {"mensaje": "Bienvenidos a la Biblioteca!"}

@app.post("/libros/")
def agregar_libro(libro: Libro):
    global id_counter
    id_counter += 1
    Biblioteca_db[id_counter] = libro
    return {"id": id_counter, "libro": libro}

@app.get("/libros/")
def obtener_libros():
    return Biblioteca_db

@app.get("/libros/{libro_id}")
def obtener_libro(libro_id: int):
    if libro_id not in Biblioteca_db:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return Biblioteca_db[libro_id]

@app.put("/libros/{libro_id}")
def actualizar_libro(libro_id: int, libro: Libro):
    if libro_id not in Biblioteca_db:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    Biblioteca_db[libro_id] = libro
    return {"mensaje": "Libro actualizado exitosamente!"}

@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    if libro_id not in Biblioteca_db:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    del Biblioteca_db[libro_id]
    return {"mensaje": "Libro eliminado exitosamente!"}