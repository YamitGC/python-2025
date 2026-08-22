from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel 
from typing import List

app = FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    
clientes_db: List[Cliente] = []
contador_id = 1

@app.post("/clientes", response_model=Cliente)
def crear_cliente(cliente: Cliente):
    global contador_id
    cliente.id = contador_id
    clientes_db.append(cliente)
    contador_id += 1
    return cliente

@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes_db

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, cliente_actualizado: Cliente):
    for index, cliente in enumerate(clientes_db):
        if cliente.id == cliente_id:
            clientes_db[index] = cliente_actualizado
            cliente_actualizado.id = cliente_id
            return cliente_actualizado
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.delete("/clientes/{cliente_id}", response_model=Cliente)
def eliminar_cliente(cliente_id: int):
    for index, cliente in enumerate(clientes_db):
        if cliente.id == cliente_id:
            eliminado = clientes_db.pop(index)
            return eliminado
    raise HTTPException(status_code=404, detail="Cliente no encontrado")