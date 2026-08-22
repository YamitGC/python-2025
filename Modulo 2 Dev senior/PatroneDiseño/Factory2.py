# Producto concreto
class Carro:
    def obtener_tipo(self):
        return "Carro"
    
# Creador concreto (la fábrica)
class FabricaCarro:
    def crear_vehiculo(self):
        return Carro()
    
# Cliente
def cliente():
    # El cliente solo usa la fábrica para crear un carro
    fabrica = FabricaCarro()  # Fábrica que crea carro
    vehiculo = fabrica.crear_vehiculo()  # Crea el carro
    print(f"Se ha creado un vehículo de tipo: {vehiculo.obtener_tipo()}")
    
# Ejecutar cliente
cliente()
    