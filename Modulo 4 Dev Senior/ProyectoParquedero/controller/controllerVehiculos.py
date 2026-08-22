from .cargarDatos import CargarDatos
from .controllerControl import ControllerControl
from datetime import datetime

class ControllerVehiculos:
    def __init__(self):
        self.cargar_datos = CargarDatos()
        self.df_vehiculos = self.cargar_datos.get_df_vehiculos()
        self.df_control = self.cargar_datos.get_df_control()
        self.controller_control = ControllerControl()

    def cargar_vehiculo(self, placa, tipoVehiculo, fechaIngreso):
        try:
            if not self.df_vehiculos['placa'].str.contains(placa).any():
                self.df_vehiculos = self.df_vehiculos._append({'id': len(self.df_vehiculos) + 1, 'placa': placa, 'tipoVehiculo': tipoVehiculo, 'fechaIngreso': fechaIngreso, 'estado': True}, ignore_index=True)
                self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
                return True
            else:
                return "Placa ya existe"
        except Exception as e:
            return "Error al cargar vehiculo"

    def obtener_vehiculos(self):
        return self.df_vehiculos
    
    def obtener_vehiculo(self, placa):
        vehiculo = self.df_vehiculos[self.df_vehiculos['placa'] == placa]
        if not vehiculo.empty:
            vehiculo_dict = vehiculo.iloc[0].to_dict()
            # Convertir fechaIngreso a datetime si es string
            if isinstance(vehiculo_dict['fechaIngreso'], str):
                vehiculo_dict['fechaIngreso'] = datetime.strptime(vehiculo_dict['fechaIngreso'], '%Y-%m-%d %H:%M:%S.%f')
            return vehiculo_dict
        return None
    
    def modificar_placa(self, id, placa):
        try:
            if self.df_vehiculos['id'].str.contains(id).any():
                self.df_vehiculos = self.df_vehiculos.loc[self.df_vehiculos['id'] == id, 'placa'] = placa
                self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
                return True
            else:
                return "Vehiculo no encontrado"
        except Exception as e:
            return "Error al modificar placa"

    def salida_vehiculo(self, placa, tipoVehiculo, fechaIngreso, tarifa):
        try:
            vehiculo = self.df_vehiculos[self.df_vehiculos['placa'] == placa]
            if not vehiculo.empty:
                # Actualizar estado del vehículo
                self.df_vehiculos.loc[self.df_vehiculos['placa'] == placa, 'estado'] = False
                self.cargar_datos.guardar_df_vehiculos(self.df_vehiculos)
                
                # Asegurar que fechaIngreso sea datetime
                if isinstance(fechaIngreso, str):
                    fechaIngreso = datetime.strptime(fechaIngreso, '%Y-%m-%d %H:%M:%S.%f')
                
                # Calcular tiempo y total a pagar
                fechaSalida = datetime.now()
                tiempo_estacionado = (fechaSalida - fechaIngreso).total_seconds() / 3600  # Convertir a horas
                totalPagar = tarifa * tiempo_estacionado
                
                # Registrar en el control
                self.controller_control.registrar_control(placa, tipoVehiculo, fechaIngreso, fechaSalida, totalPagar)
                return True
            else:
                return "Vehículo no encontrado"
        except Exception as e:
            return f"Error al registrar salida: {str(e)}"
        
    
