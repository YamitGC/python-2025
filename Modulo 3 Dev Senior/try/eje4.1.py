import logging
import psycopg2

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers= [
                        logging.FileHandler("ErroresPsycopg2.log"),
                        logging.StreamHandler()
                        ]
)

try:
    conn = psycopg2.connect("dbname = empresa user = admin password = 123")
    
except psycopg2.OperationalError as e:
    logging.error(f"Error de conexion contra la BD: {e}")