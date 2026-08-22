from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int
    
usuario = Usuario(nombre="Juan", edad=30)
print(usuario)