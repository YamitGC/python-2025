# Minijuego para adivinar un numero del 1 al 100 con la libreria random.
from random import *

# Input pidiendo su nombre y print para darte la bievenida al juego.
nombre = input("Ingresa tu nombre: ")
print(f"hola {nombre}, Bienvenid@ al juego de adivina el número.\nadivina el numero del 1 al 100 para ganar.")

# Dandole el rango de numeros para adivinar, en este caso del 1 al 100.
numero_random = randint(1, 100)
intentos = 1


# Acá un bucle para darle a entender que tenemos 10 intentos, si se acaban esos 10 intentos se acaba el Minijuego.
# Dentro del bucle se encuentran condicionales fundamentales para hacer funcionar el código.
while intentos <= 10:
    
    
    numero = int(input("Ingrese el numero: "))
    
    if intentos == 10:
        print(f"{nombre}, perdiste, todo este tiempo el numero era {numero_random}, suerte para la próxima.")
        break
    
    elif numero < 1 or numero > 100:
        print("Numero digitado fuera de rango.")
        intentos += 1
        continue
    
    elif numero < numero_random:
        print(f"El {numero} es menor que el numero que debes advinar. Intentos completados: {intentos}")
        intentos += 1
        continue
        
    elif numero > numero_random:
        print(f"El {numero} es mayor que el numero que debes advinar. Intentos completados: {intentos}")
        intentos += 1
        continue
    
    else:
        print(f"Felicidades el {numero} es el numero correcto, Has ganado el juego.")
    break



"""elif abs(numero - numero_random) <= 5:
        print(f"El {numero} cerca del numero correcto. Sigue intentado")
        intentos +=1
        continue"""

    