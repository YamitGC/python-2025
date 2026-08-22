"""La primera debe ser Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad).
La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. El programa
debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona."""

class Universidad():
    def __init__(self, nombreUNI):
        self.nombreUNI = nombreUNI
        
    
class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad
        
class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El estudiante {self.nombre} de {self.edad} años estudia en la universidad {self.nombreUNI} y su especialidad es {self.especialidad}")
        
persona=Estudiante("Hardvard")
persona.carrera("Ingeniería mecatronica")
persona.datos("Mike", 19)

    
        
