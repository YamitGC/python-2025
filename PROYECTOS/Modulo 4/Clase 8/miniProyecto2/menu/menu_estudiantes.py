from controller import estudiantesController
from menu.validaciones import *

def solicitar_datos_estudiante(modificar=False):
    if not modificar:
        while True:
            numero_documento = input("Ingrese el número de documento: ")
            if validar_documento(numero_documento):
                break
            print("Documento inválido. Solo números.")
    else:
        numero_documento = input("Ingrese el número de documento del estudiante a modificar: ")

    while True:
        nombre = input("Ingrese el nombre: ")
        if validar_nombre(nombre):
            break
        print("Nombre inválido. Solo letras.")

    while True:
        apellido = input("Ingrese el apellido: ")
        if validar_nombre(apellido):
            break
        print("Apellido inválido. Solo letras.")

    while True:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        if validar_fecha(fecha_nacimiento):
            break
        print("Fecha inválida. Formato correcto: YYYY-MM-DD.")

    while True:
        email = input("Ingrese el email: ")
        if validar_email(email):
            break
        print("Email inválido.")

    while True:
        telefono = input("Ingrese el teléfono: ")
        if validar_telefono(telefono):
            break
        print("Teléfono inválido. Solo números.")

    return numero_documento, nombre, apellido, fecha_nacimiento, email, telefono

def menuEstudiantes():
    while True:
        print("\n--- Menú de Estudiantes ---")
        print("1. Crear Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Buscar Estudiante por Documento")
        print("4. Modificar Estudiante")
        print("5. Eliminar Estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = solicitar_datos_estudiante()
            estudiantesController.crear_estudiante(*datos)
        elif opcion == "2":
            estudiantesController.mostrar_estudiantes()
        elif opcion == "3":
            id_estudiante = input("Ingrese el número de documento del estudiante: ")
            estudiantesController.mostrar_estudiante(id_estudiante)
        elif opcion == "4":
            datos = solicitar_datos_estudiante(modificar=True)
            estudiantesController.modificar_estudiante(*datos)
        elif opcion == "5":
            numero_documento = input("Ingrese el número de documento del estudiante a eliminar: ")
            estudiantesController.eliminar_estudiante(numero_documento)
        elif opcion == "6":
            print("Saliendo del menú de estudiantes.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")