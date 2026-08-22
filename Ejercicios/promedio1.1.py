def sacar_promedio():

    lista_num = []

    while True:
        numeros = input("Ingresa los numeros (digite 'fin' para terminar): ")
    
        if numeros.lower() == "fin":
           break
    
        try:
           numero = float(numeros)
           lista_num.append(numero)
    
        except ValueError:
           print("Error, ingresa un numero valido")
        
    if lista_num:
        promedio = sum(lista_num) / len(lista_num)
        print(f"Los numeros ingresados son {lista_num}")
        print(f"El promedio de la lista es {promedio}")
    else:
        print("Error no ingresaste ningun dato.")
        
if __name__ == "__main__":
    sacar_promedio()
