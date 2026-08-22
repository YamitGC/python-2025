from models.experimento import Experimento, ExperimentoModel
from views.experimento_view import ExperimentoView


class ExperimentoController:
    def __init__(self):
        self.model = ExperimentoModel()
        self.view = ExperimentoView()

    def ejecutar(self):
        while True:
            self.view.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_experimento()
            elif opcion == "2":
                self.ver_experimentos()
            elif opcion == "3":
                self.actualizar_resultado()
            elif opcion == "4":
                self.generar_informe()
            elif opcion == "5":
                self.eliminar_experimento()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

    def agregar_experimento(self):
        nombre, fecha, tipo, resultados = self.view.pedir_datos_experimento()
        exp = Experimento(nombre, fecha, tipo, resultados)
        self.model.agregar(exp)
        print("Experimento agregado exitosamente.")

    def ver_experimentos(self):
        self.view.mostrar_experimentos(self.model.obtener_todos())

    def actualizar_resultado(self):
        nombre = input("Nombre del experimento a actualizar: ")
        exp = self.model.buscar_por_nombre(nombre)
        if exp:
            nuevos_resultados = input("Nuevos resultados: ")
            exp.resultados = nuevos_resultados
            print("Resultados actualizados.")
        else:
            print("No encontrado.")

    def eliminar_experimento(self):
        nombre = input("Nombre del experimento a eliminar: ")
        self.model.eliminar(nombre)
        print("Experimento eliminado.")

    def generar_informe(self):
        # Puedes implementar la lógica de informe aquí
        print("Función de informe no implementada.")