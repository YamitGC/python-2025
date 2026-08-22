import logging



# Niveles de Loggin
# Debug
# Info
# Warning
# Error
# Critical

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s %(message)s")

logging.debug("Este es un mensahe de debug")
logging.info("Este es un mensaje informativo")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de ERROR")
logging.critical("Esto es un mensaje SERIO que puede detener el software...")
                   
