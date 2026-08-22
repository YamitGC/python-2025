class Persona:
    
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        profesion = profesion
        
    def cumpleaños(self):
        self.edad += 1
        
    def cambiar_profesion(self, nueva_profesion):
        self.profesion = nueva_profesion
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Profesion: {self.profesion}")
        
persona1 = Persona("Diomedes", "35", "cantante")

persona1.mostrar_info()
    