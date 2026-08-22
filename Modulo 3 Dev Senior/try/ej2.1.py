import logging

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers= [
                        logging.FileHandler("Errores.log"),
                        logging.StreamHandler()
                        ]
)


try:
    entero = int(input("Ingresa un numero entero: "))
    
except ValueError as e:
    logging.error(f"Error capturado: {e}")
    
else:
    logging.info(f"El numero entero es: {entero}")
    

    