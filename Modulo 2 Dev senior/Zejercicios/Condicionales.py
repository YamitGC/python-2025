x = int(input("Ingresa el primer valor: "))
y = int(input("Ingresa el segundo valor: "))

def multiplicacion(x,y):
    return x * y 

resultado = (multiplicacion(x,y))

print(resultado)

if resultado > 99 :
    print("El resultado tiene mas de 3 digitos")
    
elif resultado > 999:
    print("El resultado tiene mas de 4 digitos")
    
else:
    print("El resultado tiene menos de dos digitos")