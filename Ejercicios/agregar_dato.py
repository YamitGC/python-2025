import random

def juego_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    
    print("Bienvenido al juego de piedra, papel o tijeras.")
    usuario = input("Elige una opción (piedra, papel o tijeras): ").lower()
    
    if usuario not in opciones:
        print("Opción no válida. Por favor, elige piedra, papel o tijeras.")
        return
    
    programa = random.choice(opciones)
    
    print(f"Tú elegiste: {usuario}")
    print(f"El programa eligió: {programa}")
    
    if usuario == programa:
        print("¡Es un empate!")
    elif (usuario == "piedra" and programa == "tijeras") or \
         (usuario == "tijeras" and programa == "papel") or \
         (usuario == "papel" and programa == "piedra"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Ejecutar el juego
juego_piedra_papel_tijeras()
