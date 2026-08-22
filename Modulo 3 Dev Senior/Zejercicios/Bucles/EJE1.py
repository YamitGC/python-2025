"""pedirle al usuario que ingrese numeros y sumar todos los números
y se tiene que dejar de pedir datos cuando el usuario digite 0 
o un número negativo. después mostrar la suma en pantalla."""

suma = 0

while True:
    numero = int(input("Ingresa un numero: "))
    
    if numero <= 0:
        break
    
    suma += numero
  
print(f"La suma totald de los numeros es {numero}")
    
    