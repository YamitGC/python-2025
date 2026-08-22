# Paso 1: Estructura de datos para almacenar los registros
historial = []

# Paso 2: Función para agregar datos
def agregar_dato():
    nombre = input("Introduce el nombre: ")
    edad = input("Introduce la edad: ")
    historial.append({'nombre': nombre, 'edad': edad})
    print("Dato agregado exitosamente.\n")

# Paso 3: Función para modificar datos
def modificar_dato():
    mostrar_historial()
    try:
        indice = int(input("Selecciona el índice del dato a modificar: "))
        if 0 <= indice < len(historial):
            nombre = input("Introduce el nuevo nombre: ")
            edad = input("Introduce la nueva edad: ")
            historial[indice] = {'nombre': nombre, 'edad': edad}
            print("Dato modificado exitosamente.\n")
        else:
            print("Índice fuera de rango.\n")
    except ValueError:
        print("Por favor, ingresa un número válido.\n")

# Paso 4: Función para borrar datos
def borrar_dato():
    mostrar_historial()
    try:
        indice = int(input("Selecciona el índice del dato a borrar: "))
        if 0 <= indice < len(historial):
            del historial[indice]
            print("Dato borrado exitosamente.\n")
        else:
            print("Índice fuera de rango.\n")
    except ValueError:
        print("Por favor, ingresa un número válido.\n")

# Paso 5: Función para mostrar historial de datos
def mostrar_historial():
    if historial:
        print("\nHistorial de datos:")
        for i, registro in enumerate(historial):
            print(f"{i}. Nombre: {registro['nombre']}, Edad: {registro['edad']}")
    else:
        print("No hay datos en el historial.\n")

# Paso 6: Función principal para mostrar el menú
def menu():
    while True:
        print("Menú:")
        print("1. Agregar dato")
        print("2. Modificar dato")
        print("3. Borrar dato")
        print("4. Mostrar historial")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_dato()
        elif opcion == '2':
            modificar_dato()
        elif opcion == '3':
            borrar_dato()
        elif opcion == '4':
            mostrar_historial()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
