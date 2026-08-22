import logging

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers= [
                        logging.FileHandler("Errores.log"),
                        logging.StreamHandler()
                        ]
)

try:
    with open("archivo.csv", "r") as file:
        data = file.readline()
        
except FileNotFoundError:
    logging.error("ERROR. El archivo no existe.")
    data = None
    
else:
    logging.info("El archivo fue leido con exito.")
    
finally:
    if data:
        data.close()
    
