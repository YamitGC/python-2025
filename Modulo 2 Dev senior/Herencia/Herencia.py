class Animal:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        
    # Metodo clase padre, Animal  
    def hablar(self):
        print("El animal hace un sonido")
        
# Herencia, Perro heredando la clase animal       
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)    
        self.raza = raza
        
    # Metodo clase perro
    
    def hablar(self):
        print(f"{self.nombre} dice: ¡guau!")
        
mi_perro = Perro("Rex", 3, "pincher")

print(mi_perro.nombre)
print(mi_perro.edad)
print(mi_perro.raza)

mi_perro.hablar()