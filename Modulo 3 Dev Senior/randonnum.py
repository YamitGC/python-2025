from random import *


nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}, bienvenid@ al Juego de Adivina el numero del 1 al 80 !\n Solo tienes 10 intentos')

numero_random = randint(1, 80) # Se genera el numero aleatorio en ese rango 1 al 80
intentos = 1

while intentos <= 10:
    
    numero = int(input('Ingrese el numero: '))

    if intentos == 10: 
        print(f"fallaste en todo {nombre}, era {numero_random} todo este tiempo")
        break
    
    if numero < 1 or numero > 80:
        print("El numero debe de estar 1 y 80. Intenta de nuevo")
        intentos += 1
        continue
    
    elif numero < numero_random:
        print(f'El numero {numero} es menor al que debes adivinar. Sigue intentando.')
        intentos += 1
        continue
    
    elif numero > numero_random:
        print(f'El numero {numero} es mayor al que debes adivinar. Sigue intentando')
        intentos += 1
        continue
    
    #elif numero == numero_random:
    else:
        print(f'FELICIDADES {nombre}\nHa adivinado el numero: {numero}')
    break
