from controller import docentesController
from menu.validaciones import *

def solicitar_datos_docente(modificar=False):
    if not modificar:
        while True:
            numero_documento = input("Ingrese el número de documento: ")
            if validar_documento(numero_documento):
                break
            print("Documento inválido. Solo números.")
    else:
        numero_documento = input("Ingrese el número de documento del docente a modificar: ")

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
        email = input("Ingrese el email: ")
        if validar_email(email):
            break
        print("Email inválido, formato ejemplo: 'usuario@ejemplo.com'.")

    while True:
        telefono = input("Ingrese el teléfono: ")
        if validar_telefono(telefono):
            break
        print("Teléfono inválido. Solo números.")

    especialidad = input("Ingrese la especialidad: ")

    return numero_documento, nombre, apellido, email, telefono, especialidad

def menuDocentes():
    while True:
        print("\n--- Menú de Docentes ---")
        print("1. Crear Docente")
        print("2. Mostrar Docentes")
        print("3. Buscar Docente por Documento")
        print("4. Modificar Docente")
        print("5. Eliminar Docente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = solicitar_datos_docente()
            docentesController.crear_docente(*datos)
        elif opcion == "2":
            docentesController.mostrar_docentes()
        elif opcion == "3":
            numero_documento = input("Ingrese el número de documento del docente: ")
            docentesController.mostrar_docente_por_documento(numero_documento)
        elif opcion == "4":
            datos = solicitar_datos_docente(modificar=True)
            docentesController.modificar_docente(*datos)
        elif opcion == "5":
            numero_documento = input("Ingrese el número de documento del docente a eliminar: ")
            docentesController.eliminar_docente(numero_documento)
        elif opcion == "6":
            print("Saliendo del menú de docentes.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")