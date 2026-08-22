"""
Primera infancia sea de cero a 5 años
infancia entre 6 y 13 años
adolecencia entre 14 y 17 años
mayor a 18 y menor a 115 adulto
else edad incorrecta
"""

edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad < 6:
    print("primera infancia")
    print("es un pequeño bebé")

elif edad >= 6 and edad < 14:
    print("infancia")
elif edad >=14 and edad < 18:
    print("adolecente")
elif edad >= 18 and edad < 116:
    print("adulto")
else:
    print("edad incorrecta")