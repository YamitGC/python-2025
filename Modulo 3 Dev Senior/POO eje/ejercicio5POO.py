"""Crea un programa que permita gestionar diferentes tipos de vehículos por ejemplo, coches,
motos y camiones Cada vehículo tendrá atributos comunes como marca,
modelo y velocidad máxima, pero cada tipo de vehículo tendrá comportamientos particulares,
como el cálculo del consumo de combustible en función de su tipo."""


class Vehiculo:
    def init(self, marca, modelo, vel_max, consumo):
        self.marca = marca
        self.modelo = modelo
        self.vel_max = vel_max
        self.consumo = consumo

    def mostrar_datos(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nVelocidad Máxima: {self.vel_max} km/h\nConsumo: {self.consumo}\n")

class Carro(Vehiculo):
    pass

class Moto(Vehiculo):
    pass

class Camion(Vehiculo):
    pass


carro = Carro("Ferrari", "F40", 340, "30L/100Km")
carro.mostrar_datos()

moto = Moto("Yamaha", "DT 175", 201, "5L/100Km")
moto.mostrar_datos()

camion = Camion("Kenworth", "T600", 163, "20L/100Km")
camion.mostrar_datos()

        
        
    
    
    
    
    
    
        
    
        