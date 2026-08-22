from .cargarDatos import CargarDatos

class ControllerControl:
    def __init__(self):
        self.cargar_datos = CargarDatos()
        self.df_control = self.cargar_datos.get_df_control()

    def registrar_control(self, placa, tipoVehiculo, fechaIngreso, fechaSalida, totalPagar):
        self.df_control = self.df_control._append({'placa': placa, 'tipoVehiculo': tipoVehiculo, 'fechaIngreso': fechaIngreso, 'fechaSalida': fechaSalida, 'totalPagar': totalPagar}, ignore_index=True)
