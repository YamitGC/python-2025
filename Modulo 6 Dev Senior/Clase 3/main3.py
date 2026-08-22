from pydantic import BaseModel, Field

class Automovil(BaseModel):
    model: str = Field(..., min_length=1)
    year: int = Field(..., gt=1885, lt=2026)
    color: str = Field(..., min_length=3)
    type: str = Field(..., min_length=3)
    horsepower: int = Field(..., ge=0)
    torque: int = Field(..., ge=0)

