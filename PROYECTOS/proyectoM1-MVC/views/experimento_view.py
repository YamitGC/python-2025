class ExperimentoView:
    @staticmethod
    def mostrar_menu():
        print("Menu de opciones:")
        print("1. Agregar Experimento")
        print("2. Ver Experimentos")
        print("3. Actualizar Resultado")
        print("4. Generar Informe")
        print("5. Eliminar Experimento")
        print("6. Salir")

    @staticmethod
    def pedir_datos_experimento():
        nombre = input("Ingrese el nombre del experimento: ")
        fecha = input("Ingrese la fecha (DD-MM-AAAA): ")
        tipo = input("Ingrese el tipo (Química, Biología, Física): ")
        resultados = input("Ingrese los resultados (números separados por comas): ")
        return nombre, fecha, tipo, resultados

    @staticmethod
    def mostrar_experimentos(experimentos):
        if not experimentos:
            print("No hay experimentos registrados.")
            return
        for exp in experimentos:
            print("-" * 20)
            print(f"Nombre: {exp.nombre}")
            print(f"Fecha: {exp.fecha}")
            print(f"Tipo: {exp.tipo}")
            print(f"Resultados: {exp.resultados}")
            print("-" * 20)