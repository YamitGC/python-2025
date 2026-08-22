class Carro:
    
    def conducir(self):
        print("El vehiculo se esta menejando")
       
class Bicicleta:
    def conducir(self):
        print("La bicicleta se está pedaleando")
        
class Vehiculofactory:
    @staticmethod
    def crear_vehiculo(tipo):
        if tipo == "Carro":
            return Carro()
        elif tipo == "Bicicleta":
            return Bicicleta()
        else:
            ValueError("Tipo de vehiculo no reconocido")
            
vehiculo1 = Vehiculofactory.crear_vehiculo("Carro")
vehiculo1.conducir()

vehiculo2=Vehiculofactory.crear_vehiculo("Bicicleta")
vehiculo2.conducir()