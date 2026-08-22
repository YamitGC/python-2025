from random import *
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s %(message)s",
                    filename="adivina.log",
                    filemode="w")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s %(message)s")
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

"""
Reparticion de obligaciones

- Jaime
- Carlos
- Andres **2
- Yamit

Objetivo:
1. Implementar las excepciones necesarias al proyecto. 
2. Implementar logs con un archivo .log - Yamit
3. Modularizar las validaciones en funciones - Andres Andrade
4. Hacer pruebas de las funciones con Unittest - Andres Osorio

"""

nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}, bienvenid@ al Juego de Adivina el numero del 1 al 100 !\n Solo tienes 10 intentos')

numero_random = randint(1, 100) # Se genera el numero aleatorio en ese rango 1 al 100
intentos = 0
    
while intentos <= 10:
    
    try:
        
        numero = input('Ingrese el numero: ')
        intentos += 1
        
        if numero.isalpha():
            raise ValueError (f"Se adivinara es un numero, no es permitido letras.")
        if not numero.strip():
            raise ValueError('No se ingreso ningun numero') #Validacion para no permitir vacios o espacios
        
        numero = int(numero)
        if numero.__float__():
            raise ValueError ("El numero ingresado es flotante. debe ser un numero entero.")
        if intentos == 10:
            logging.info(f"ERROR. Fallaste en todo {nombre}, era {numero_random} todo este tiempo")
            break
        
        if numero < 1 or numero > 100:
            
            logging.error(f"Error. El numero {numero} no está en el rango (1-100). Intenta de nuevo. Intentos: {10 - intentos} restantes")
            continue
        
        elif numero < numero_random:
            logging.info(f'El numero {numero} es menor al que debes adivinar. Sigue intentando. Intentos: {10 - intentos} restantes') 
            continue
        
        elif numero > numero_random:
            logging.info(f'El numero {numero} es mayor al que debes adivinar. Sigue intentando. Intentos: {10 - intentos} restantes')
            continue
        
        #elif numero == numero_random:
        else:
            logging.info(f'FELICIDADES {nombre}\nHa adivinado el numero: {numero}')
            break
        
    except (ValueError) as e:
        logging.error(f'De tipo: {e}')