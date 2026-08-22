def validar_num():
    while True:
        try:
            numero = float(input("Ingrese el numero: "))
            print(numero)
            break
        except ValueError:
            print("Numero no valido")
    
validar_num()
            
        