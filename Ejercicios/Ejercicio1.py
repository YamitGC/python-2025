lista_notas = []

# Ciclo para ingresar números
while True:
    notas = input("Ingresa un número (o 'fin' para terminar): ")
    
    if notas.lower() == 'fin':
        break

    try:
        # Convertimos la entrada a número (puede ser float o int)
        numero = float(notas)
        lista_notas.append(numero)
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

# Calculamos el promedio si hay al menos un número
if lista_notas:
    promedio = sum(lista_notas) / len(lista_notas)
    print("Los números ingresados son:", lista_notas)
    print("El promedio es:", promedio)
else:
    print("No ingresaste ningún número.")