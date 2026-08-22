class Animal:
    
    def __init__(self, accion, nombre, edad):
        self.accion = accion
        self.nombre = nombre
        self.edad = edad
        
    def hablar(self):
        print("El animal hace un sonido")
        
class Gato(Animal):
    def __init__(self, accion, nombre, edad, raza):
        super().__init__(accion, nombre, edad)
        self.raza = raza
        
    def ronronear(self):
        print(f"{self.accion} ")
    