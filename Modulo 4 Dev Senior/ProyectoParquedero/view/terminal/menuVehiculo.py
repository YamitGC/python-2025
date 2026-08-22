from controller.controllerVehiculos import ControllerVehiculos
import datetime

class MenuVehiculo:

    def __init__(self):
        self.controller_vehiculos = ControllerVehiculos()

    def mostrar_menu(self):
        while True:
            print("1. Ingresar vehiculo")
            print("2. Ver vehiculos")
            print("3. Salida vehiculo")
            print("4. Salir ")   
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.ingresar_vehiculo()
            elif opcion == "2":
                self.ver_vehiculos()
            elif opcion == "3":
                self.salida_vehiculo()
            elif opcion == "4":
                print("Saliendo...")    
                break
            else:
                print("Opcion invalida")

    def ingresar_vehiculo(self):
        placa = input("Ingrese la placa del vehiculo: ")
        tipoVehiculo = input("Ingrese el tipo de vehiculo: ")
        fechaIngreso = datetime.datetime.now()
        self.controller_vehiculos.cargar_vehiculo(placa, tipoVehiculo, fechaIngreso)

    def ver_vehiculos(self):
        vehiculos = self.controller_vehiculos.obtener_vehiculos()
        print(vehiculos)

    def salida_vehiculo(self):
        placa = input("Ingrese la placa del vehiculo: ")
        vehiculo = self.controller_vehiculos.obtener_vehiculo(placa)

        if not vehiculo:
            print("Vehículo no encontrado")
            return

        tipoVehiculo = vehiculo['tipoVehiculo']
        fechaIngreso = vehiculo['fechaIngreso']
        
        if tipoVehiculo == "Carro":
            tarifa = 1000
        elif tipoVehiculo == "Moto":
            tarifa = 500
        else:
            print("Tipo de vehiculo no valido")
            return

        resultado = self.controller_vehiculos.salida_vehiculo(placa, tipoVehiculo, fechaIngreso, tarifa)
        
        if resultado is True:
            print("Salida de vehículo registrada exitosamente")
        else:
            print(f"Error al registrar salida: {resultado}")


