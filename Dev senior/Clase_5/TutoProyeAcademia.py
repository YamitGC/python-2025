#Simulacion de una academia

# Crear, editar y eliminar

# FUNCIONES -----------------

# Crear, editar y eliminar

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
    

# INPUTS ----------------------

student_name = input("Ingrese el nombre del estudiante: ")
email = input("Ingrese el correo del estudiante: ")
id_number = int(input("Ingrese el cedula del estudiante: "))


# LLAMADO DE FUNCIONES --------------------------------------

StudentList = add_Student_List(student_name, email, id_number)
print("\nLista de estudiantes:", StudentList, "\n")

index = int(input("Ingrese donde esta ubicado el valor a modificar: "))
new_Email = input("Ingrese el nuevo correo del estudiante: ")
edit_Student_List(StudentList, index, new_Email)
print("\nLista de estudiantes MODIFICADA:", StudentList, "\n")


"""print(eliminar_Por_Indice_Estudiante(StudentList, 2))
print(StudentList)"""

