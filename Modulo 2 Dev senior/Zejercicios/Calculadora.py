from os import system

def suma(a,b):
    return a + b
        
def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def limpiar_pantalla():
    system("cls")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))


while True:
    
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    opcion = int(input("Ingrese una opcion (1-5): "))
    
    if opcion > 0 and opcion < 6:

        if opcion == 1:
            limpiar_pantalla()
            print("El resulado de la suma es", suma(a,b))
            
        elif opcion == 2:
            limpiar_pantalla()
            print("El resulado de la resta es", resta(a,b))
        
        elif opcion == 3:
            limpiar_pantalla()
            print("El resulado de la multiplicacion es", multiplicacion(a,b))
        
        elif opcion == 4:
            limpiar_pantalla()
            print("El resulado de la division es", division(a,b))
            
        
            
        elif opcion == 5:
            limpiar_pantalla()
            print("Gracias por usar la calculadora.")
            break
    else:
        limpiar_pantalla()
        ("Error. Opcion erronea.")
        

            
        
            
            
    
            
            
        
    
    
    
    
