from pydantic import BaseModel
from typing import Optional

class ProductoEntrante(BaseModel):
    id: int
    nombre: str
    precio: float
    cantidad: int = 0
    descripcion: Optional[str] = None
    disponible: bool = True

class ProductoSaliente(BaseModel):
    id: int
    nombre: str
    precio_total: float
    estado: str
    fecha_salida: str
    destinatario: str