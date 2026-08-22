"""
edad = 3

if edad >= 18:
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")
"""
"""
sexo = input("Dijite el sexo: ")
if sexo == "M":
    print("Masculino.")
elif sexo == "F":
    print("Femenino.")
else:
    print("Otro.")
"""
"""
Primera infancia sea de cero a 5 años
infancia entre 6 y 13 años
adolecencia entre 14 y 17 años
mayor a 18 y menor a 120 adulto
else edad incorrecta
"""
edad = int(input("Ingrese su edad: "))
if edad < 6:
    print("primera infancia")
elif edad >=6 and edad < 14:
    print("Infancia")
elif edad >=14 and edad < 17:
    print("adolecencia")
elif edad >= 18 and edad < 120:
    print ("Adulto")
else: 
    print("Edad incorrecta")
