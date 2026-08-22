class Coche:
    
  
    def __init__(self, marca, modelo, year):
        self.__marca = marca
        self.__modelo = modelo
        self.__year = year
        
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_year(self):
        return self.__year
    
    def set_year(self, newyear):
        self.__year = newyear
        

    
veh = Coche("Ferrari", "F40", 1990)

print("Bienvenido a la exposicion de autos clasicos, este es un", veh.get_marca(), veh.get_modelo(),"Del año", veh.get_year())

veh.set_year(1992)

print("El nuevo año del vehiculo es", veh.set_year())
