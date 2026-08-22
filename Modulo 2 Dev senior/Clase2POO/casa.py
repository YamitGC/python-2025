class Casa:
    
    def __init__(self, color, pisos):
        self.color = color
        self.pisos = pisos
        pass
    
    def caracteristicas(self):
        print("La casa es de color", self.color, "y tiene", self.pisos,"pisos")
        
casa1 = Casa("blanco", 2)

casa1.caracteristicas()