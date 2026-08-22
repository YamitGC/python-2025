from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(
    filename="response.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a mi nueva API"}

@app.get("/divide")
def divide(x: int, y: int):
    try:
        resultado = x / y
        logging.info(f"División exitosa: {x} / {y} = {resultado}")
        return {"resultado": resultado}
    except ZeroDivisionError:
        logging.error("Error de división por cero")
        raise HTTPException(status_code=400, detail="No se puede dividir por cero")