"""Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno."""

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
        
class Moto(Fabrica):
    def caracteristicas(self):
        print(f"La moto tiene {self.llantas} llantas, es de color {self.color} y cuesta {self.precio}$.")
        
class Carro(Fabrica):
    def caracteristicas(self):
        print(f"El carro tiene {self.llantas} llantas, es de color {self.color} y cuesta {self.precio}$.")
        
moto = Moto("2",(input("Ingrese el color de su moto: ")), 10000 )
moto.caracteristicas()

carro = Carro("4",(input("Ingrese el color de su carro: ")), 80000)
carro.caracteristicas()