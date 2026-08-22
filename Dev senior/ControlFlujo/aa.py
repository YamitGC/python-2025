"""
licencia = 16
edad = int(input("Ingrese su edad: ")) # -> Devuelve String

if edad > 0:
    if edad >= licencia:
        print('Tienes permiso para conducir')
    if edad < licencia:
        print('No tienes permiso para conducir')    
else:
    print('Error ! Digite un numero valido')
"""
# And = y  not = negacion or = o 

habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en python y tener conocimientos de inglés")
elif not sabe_python and habla_ingles:
    print("Para postularte debes saber python")
else:
    print("Para postularte necesitas saber ingles")
    


"""
Cumples con los requisitos para postularse
Para postularte, necesitas saber programar en python y tener conocimientos de inglés
Para postularte necesitas saber ingles 
Para postularte debes saber python
"""