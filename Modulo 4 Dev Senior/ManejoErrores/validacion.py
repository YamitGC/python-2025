edad = input("Ingrese su edad: ")

if edad.isdigit() and int(edad) > 0:
    print(f"Usted tiene {edad} años")
else:
    print("Ingrese un numero valido")

