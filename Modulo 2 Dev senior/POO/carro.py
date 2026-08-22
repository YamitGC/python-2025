class Coche:
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.velocidad = 0  # la velocidad inicial es 0

    def acelerar(self):
        self.velocidad += 200  # incrementa la velocidad en 10 unidades

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10  # disminuye la velocidad en 10, pero sin que sea negativa

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Año: {self.año}")
        print(f"Velocidad actual: {self.velocidad} km/h")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo", 2020)

# Usar los métodos
mi_coche.acelerar()  # acelera el coche
mi_coche.acelerar()  # acelera el coche nuevamente
mi_coche.frenar()    # frena el coche
mi_coche.mostrar_info()  # muestra la información del coche
