from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="nombre del producto")
    price: float = Field(000, gt=0, description="precio del producto")
    description: str | None = Field(default=None, max_length=200, description="descripción del producto")
    stock: int = Field(..., gt=0, le=1000, description="cantidad en stock")

    @field_validator("name")
    def validar_nombre(cls, v):
        if not v:
            raise ValueError("El nombre no puede estar vacío")
        return v

fake_db: Dict[int, Item] = {}
id_counter = 1

@app.get("/")
def root():
    return {"mensaje": "Bienvenidos!"}

@app.post("/items/")
def create_item(item: Item):
    global id_counter
    id_counter += 1
    fake_db[id_counter] = item
    return {"id": id_counter, "item": item}

@app.get("/items/")
def read_items():
    return fake_db

@app.get("/items/{item_id}")
def get_items(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = updated_item
    return {"mensaje": "Item actualizado", "item": updated_item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = fake_db.pop(item_id)
    return {"mensaje": "Item eliminado con éxito", "item": deleted}