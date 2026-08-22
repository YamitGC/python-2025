class Experimento:
    def __init__(self, nombre, fecha, tipo, resultados):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.resultados = resultados

class ExperimentoModel:
    def __init__(self):
        self.experimentos = []

    def agregar(self, experimento):
        self.experimentos.append(experimento)

    def obtener_todos(self):
        return self.experimentos

    def buscar_por_nombre(self, nombre):
        for exp in self.experimentos:
            if exp.nombre == nombre:
                return exp
        return None

    def eliminar(self, nombre):
        self.experimentos = [exp for exp in self.experimentos if exp.nombre != nombre]