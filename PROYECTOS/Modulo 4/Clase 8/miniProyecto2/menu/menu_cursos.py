from controller import cursosController, docentesController
from menu.validaciones import *
    
def solicitar_datos_cursos(modificar=False):
    if not modificar:
        while True:
            nombre_curso = input("Ingrese el nombre del curso: ")
            if validar_nombre(nombre_curso):
                break
            print("Nombre inválido. Solo letras.")

    while True:
        descripcion = input("Ingrese la descripción del curso: ")
        if validar_descripcion(descripcion):
            break
        print("Descripción inválida.")

    while True:
        creditos = input("Ingrese los créditos del curso: ")
        if validar_creditos(creditos):
            break
        print("Créditos inválidos. 10 créditos máximo o solo numeros.")

    while True:
        numero_documento = input("Ingrese el número de documento del docente: ")
        if validar_id_docente(numero_documento):
            break
        print("Número de documento inválido. Solo números.")

    while True:
        id_docente = input("Ingrese el ID del docente: ")
        if docentesController.existe_docente(id_docente):
                break
        print("El docente no existe. Ingrese un ID válido.")

    return nombre_curso, descripcion, creditos, id_docente

def menuCursos():
    while True:
        print("\n--- Menú de Cursos ---")
        print("1. Crear Curso")
        print("2. Mostrar Cursos")
        print("3. Buscar Curso por Docente")
        print("4. Modificar Curso")
        print("5. Eliminar Curso")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = solicitar_datos_cursos()
            cursosController.crear_curso(*datos)
        elif opcion == "2":
            cursosController.mostrar_cursos()
        elif opcion == "3":
            numero_documento = input("Ingrese el número de documento del docente: ")
            cursosController.buscar_curso_por_docente(numero_documento)
        elif opcion == "4":
            datos = solicitar_datos_cursos(modificar=True)
            cursosController.modificar_curso(*datos)
        elif opcion == "5":
            id_curso = input("Ingrese el ID del curso a eliminar: ")
            cursosController.eliminar_curso(id_curso)
        elif opcion == "6":
            print("Saliendo del menú de cursos.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")