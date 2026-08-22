import pandas as pd

class CargarDatos:
    def __init__(self):
        self.df_vehiculos = pd.read_csv('controller/data/vehiculos.csv',sep=';')
        self.df_control = pd.read_csv('controller/data/control.csv', sep=';')

    def get_df_vehiculos(self):
        return self.df_vehiculos
    
    def get_df_control(self):
        return self.df_control

    def guardar_df_vehiculos(self, df_vehiculos):
        df_vehiculos.to_csv('controller/data/vehiculos.csv', sep=';', index=False)

    def guardar_df_control(self, df_control):
        df_control.to_csv('controller/data/control.csv', sep=';', index=False)



