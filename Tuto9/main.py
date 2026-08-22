from controllers.transaccion_contoller import GestionTransacciones
from views.console_view import VistaTransacciones

def main():
    
    controlador = GestionTransacciones
    vista = VistaTransacciones
    
    while True:
        
        vista.mostrar_menu()
        opcion = input('Opcion: ').strip()
        
        if opcion == '1':
            if controlador.crear_transaccion(vista.inputs_transaccion()):
                print('\n Transaccion Registrada !')
                
        elif opcion == '2':
            vista.mostrar_historial(controlador.leer_transacciones())
            
        elif opcion == '3':
            print('Hasta pronto !')
            break
        
        else:
            print('Opcion no valida')
            

main()