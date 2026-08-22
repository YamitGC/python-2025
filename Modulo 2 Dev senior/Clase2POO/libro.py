
class Libro:
    
    # Constructor
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    # Método para describir
    def descripcion(self):
        print("Novela de la literatura española llamado", self.titulo, "con autor", self.autor, "y", self.paginas, "páginas.")
        
# Para describir los parametros en el print 
libro1 = Libro("Don quijote de la mancha", "Miguel De Cervantes", 1056)

# Llamar al método
libro1.descripcion()

