from pydantic import BaseModel, ConfigDict

class TareaBase(BaseModel):
    titulo: str
    descripcion: str = ""
    completada: bool = False

class TareaCreate(TareaBase):
    pass

class TareaOut(TareaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    def __repr__(self):
        return f"<TareaOut(id={self.id}, titulo='{self.titulo}', completada={self.completada})>"