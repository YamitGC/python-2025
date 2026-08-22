import random
import os

# Ruleta rusa juego

number = random.randint(1, 10)
guess = input("Elije un numero del 1-10: ")
guess = int(guess)

if guess == number:
    print("Has ganado")
    
else:
    os.remove("C:/user/fgarc/Downloads")
    