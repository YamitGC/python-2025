from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

items = {}

class Item(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    impuesto: Optional[float] = None
    
# Rutas (definición de endpoints)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de clase 2 (Items)"}

@app.get("/items/")
def get_all_items():
    if not items:
        raise HTTPException(status_code=404, detail="No hay items disponibles")
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"item_id": item_id, "item": items[item_id]}

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"mensaje": "Item creado", "item_id": item_id, "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    items[item_id] = item
    return {"mensaje": "Item actualizado", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del items[item_id]
    return {"mensaje": f"Item {item_id} eliminado"}