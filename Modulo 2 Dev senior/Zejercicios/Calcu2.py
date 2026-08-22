from os import system

def limpiar_pantalla():
    system("cls")

opcion = int(input("Menú: \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division \n 5.Salir\n "))

n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo valor: "))

if opcion == 1:
    print("El resultado de la suma es", n1 + n2)
    
elif opcion == 2:
    print("El resultado de la resta es", n1 - n2)
    
elif opcion == 3:
    print("El resultado de la multiplicacion es", n1 * n2)
    
elif opcion == 4:
    print("El resultado de la division es", n1 / n2)

elif opcion == 5:
    print("Gracias por usar.")
    
else:
    limpiar_pantalla()
    print("Error, numero fuera de limites.")
    
    

