class Animal:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hablar(self):
        print("El animal hace un sonido")
        
    def informacion1(self):
        print(f"El animal se llama {self.nombre} y tiene {self.edad} años")
        
class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__( nombre, edad)
        self.raza = raza
        
    def hablar(self):
        print(f"{self.nombre} maulla.")
        
    def ronronear(self):
        print(f"{self.nombre} está ronroneando")
        
    def informacion(self):
        print(f"{self.nombre} tiene {self.edad} años y es de raza {self.raza}.")
        
gato = Gato( "Pepe", 3, "Gato naranja")

gato.informacion1()
gato.hablar()
gato.ronronear()
gato.informacion()




