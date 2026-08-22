# FUNCIONES -------------------

def add_Student_List(nombre_estudiante, correo, cedula):
        
    estudianteList = []
    estudianteList.append(nombre_estudiante)
    estudianteList.append(correo)
    estudianteList.append(cedula)
    return estudianteList

def edit_Student_List(listaEstudiante: list, indice, valor):
    
    
    
    if indice < len(listaEstudiante):
        listaEstudiante[indice] = valor
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante

def eliminar_Por_Indice_Estudiante(listaEstudiante: list, indice):
    
    if indice < len(listaEstudiante):
        listaEstudiante = listaEstudiante.pop(indice)
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante


while True:
    print("Menu Academia")
    print("1. Agregar")
    print("2. Leer")
    print("3.Eliminar")
    print("4. Operaciones")
    print("5. Comparacion")
    print("Salir")
    
    opcion = input("Elige una opcion (1-6): ")
    
    if opcion == "6":
        print("Adios !")
        break
    
    if opcion == "1":
        print(add_Student_List)