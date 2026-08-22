
# Sirve para garantizar que sea si o si mover

from abc import ABC , abstractmethod

class Vehiculo_interface(ABC):
    
    @abstractmethod
    def mover(self):
        pass
    
class Carro(Vehiculo_interface):
    def mover(self):
        print("El carro se esta conduciendo por carretera")
        
class Bicicleta(Vehiculo_interface):
    def mover(self):
        print("La bicicleta va en la cicloruta")
        
vehiculos = [Carro(), Bicicleta()]

for vehiculo in vehiculos:
    vehiculo.mover()