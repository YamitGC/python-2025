class Coche:
    
    # Constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    # Método para la informacion 
    def informacion(self):
        print("El", self.marca, self.modelo, "del año", self.año, "es un muy bonito auto icono de los muscle car americanos.")
        
# Crear la descripcion del auto
coche1 = Coche("Ford", "Mustang", 1968)

# Llamar para que imprima
coche1.informacion()