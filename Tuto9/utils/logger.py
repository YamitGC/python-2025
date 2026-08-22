import logging

class Registrador:
    
    def __init__(self):
        logging.basicConfig(
            filename='registros.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )

    def registrar(self, mensaje, nivel = 'INFO'):
        
        if nivel == 'ERROR':
            logging.error(mensaje)
        else:
            logging.info(mensaje)
        print(f'[{nivel}] {mensaje}')
