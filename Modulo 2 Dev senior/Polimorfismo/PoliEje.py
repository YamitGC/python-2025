class Vehiculo: 
    def __init__(self,marca):
        self.marca= marca
        
    def mostrar_info(self):
        print(f"Vehiculo de la marca {self.marca}")
        
class Carro(Vehiculo):
    def mostrar_info(self):
        print(f"Coche de la marca {self.marca}")
        
class Moto(Vehiculo):
    def mostrar_info(self):
        print(f"Moto de la marca {self.marca}")
    
# Usando polimorfismo
Vehiculos = [Carro("toyota"), Moto("yamaha")]

for vehiculo in Vehiculos:
    vehiculo.mostrar_info()
    