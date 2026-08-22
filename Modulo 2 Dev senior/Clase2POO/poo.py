# Definir la clase de Persona
class Persona:
    # Método constricutor  
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Método para saludar
    def saludar(self):
       print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años")

# Crear un objeto de la clase Persona       
persona1 = Persona("Juan", 25)

# Usar el método del objeto
persona1.saludar()