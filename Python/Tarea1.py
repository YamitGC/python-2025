n = int(input("Ingresa un numero del 1 al 10: "))

if 1 <= n <= 10:
    print(f"Tabla de multiplicar de {n}: ")
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
        
else: 
    print("Error, el número debe ser entre el 1 y el 10")

