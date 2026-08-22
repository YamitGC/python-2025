class Pajaro():
    
    #Atributos de la clase - Caracteristicas
    alas = True
    color = "Azul"
   
    
    #Constructor
    def __init__(self,color,pico):
        self.color = color
        self.pico = pico
        
piolin = Pajaro("amarillo", "Largo")
print(piolin)

canario = Pajaro("Rojo", "Corto")
print(canario.pico)

print(f"El Canario es de color {canario.color} y su pico es {canario.pico}")
print(f"Piolin es de color {piolin.color} y su pico es {piolin.pico}")