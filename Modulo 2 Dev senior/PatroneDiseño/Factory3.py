class Camisetas:
    
    def obtener_tipos(self):
        return "Camisetas"
    
class FabricaCamisetas:
    def fabricar_camiseta(self):
        return Camisetas()
    
def cliente():
    fabrica = FabricaCamisetas()
    camiseta = fabrica.fabricar_camiseta()
    print(f"Se ha creado una ropa tipo: {camiseta.obtener_tipos()}")
    
cliente()