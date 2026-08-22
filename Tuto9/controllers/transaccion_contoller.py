from dataclasses import dataclass
from models.transaccion import Transaccion
from utils.logger import Registrador

@dataclass
class GestionTransacciones:
    
    transacciones: list
    registrador: Registrador
    
    def crear_transaccion(self, datos): # Datos del objeto
        
        try:
            if datos is None:
                raise ValueError('Datos incompletos')
            
            nueva = Transaccion(*datos)
            self.transacciones.append(nueva)
            self.registrador.registrar(f'Transaccion creada: {nueva}')
            return 

        except ValueError as e:
            #print(f'ERROR. Error de validacion {e}')
            self.registrador.registrar(f'Error de validacion: {str(e)}', 'ERROR')
            return False
        
        except Exception as e:
            #print(f'ERROR {e}')
            self.registrador.registrar(f'Error inesperado: {str(e)}', 'ERROR')
            return False
            
    def leer_transacciones(self):
        self.registrador.registrar('Consultando todas las transacciones')
        return self.transacciones.copy()

