class Carro:
    
    def __init__(self, marca, modelo, año, color, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo
        
    def mostrar_informacion(self):
        print(f"El {self.marca} {self.modelo} del año {self.año} es de color {self.color} y es de tipo {self.tipo} \n")
        
    class Motor:
        
        def __init__(self, combustible, potencia, cilindrada):
            self.combustible = combustible
            self.potencia = potencia
            self.cilindrada = cilindrada
            
        def info_motor(self):
            print(f"""Caracteristicas del motor:
combustible: {self.combustible} 
caballos de fuerza: {self.potencia}HP 
cilindrada: {self.cilindrada}L""")
            
mi_vehiculo = Carro("Renault", "Sandero", 2022, "Gris", "Hatchback")
        
mi_motor = mi_vehiculo.Motor("Gasolina", 111, 1.6)

mi_vehiculo.mostrar_informacion()
mi_motor.info_motor()

