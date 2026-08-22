def llamar_valores():
    
    comida = ["Jugo", "Gaseosa", "Papas", "Galletas", "Pan"]
    
    while True:
        try:
            indice = input("Ingrese el indice de la comida a obtener: ")
            print(f"El elemento en la posicion de {indice} está en el {comida[indice]}")
            break
        
        except ValueError:
            print("Error. Debe ingresar numero entero")
            
        except ValueError:
            print(f"El indice debe estar entre el rango disponible {len(comida)}")
            
llamar_valores()