"""class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        
try:
    raise ErrorPersonalizado("Este es un ejemplo de error personalizado.")
except ErrorPersonalizado as e:
    print(f"Se capturo un error: {e}")"""
    
import logging

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers= [
                        logging.FileHandler("Errores.log"),
                        logging.StreamHandler()
                        ]
)

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error(f"Error capturado: {e}")