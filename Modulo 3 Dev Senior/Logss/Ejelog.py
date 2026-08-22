import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s %(message)s")

logging.debug("Mensaje de debug")
logging.info("Mensaje de informacion")
logging.warning("Este es un mensaje de Warning")
logging.error("Esto es un mensaje de error")
logging.critical("Esto es un mensaje de critical")