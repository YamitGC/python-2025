from utils.logger import Registrador
from dataclasses import dataclass

@dataclass
class VistaTransacciones:
    
    registrador: Registrador
    
    @staticmethod
    def mostrar_menu():
        print('\n Gestor de Gastos')
        print('1. Registrar transaccion')
        print('2. Ver historial')
        print('3. Salir')
        
    def inputs_transaccion(self):
        
        try:
            #Validaciones PENDIENTE -------------
            tipo = input('Tipo (gasto/ingreso): '.strip().lower())
            if tipo not in ['ingreso', 'gasto']:
                raise ValueError (f'Tipo de transaccion {tipo} no valido. (gasto/ingreso)')
            
            categoria = input('Categoria: (salario, comida, hogar) '.strip().lower())
            
            if categoria  not in ['salario', 'comida', 'hogar']:
                raise ValueError(f'Opcion de categoria {categoria} no valido.')
            
            fecha = input('Fecha: (DD/MM/AA) '.strip())
            
            monto = float(input('Monto: '))
            if monto < 0:
                raise ValueError("Ingresa un monto.")
            
            return tipo, categoria, fecha, monto
        
        except Exception as e:
            self.registrador.registrar(f'Error inesperado: {str(e)}', 'ERROR')
            return None
        
    @staticmethod
    def mostrar_historial(transacciones):
        print('\n----- HISTORIAL -----')
        for contador, t in enumerate(transacciones, 1):
            print(f'{contador}. {t}')
            
            
            
                
    
        
    


