lista= ["andres", "nicolas", "juan", "carlos", "felipe", "rodrigo", "mateo", "alberto", "cesar", "sebastian"]
def validacion():
    while True:
        try:
            #numero=int(numero)
            longitud = len(lista)
            numero = int(input("ingrese indice: ") )
            if not numero:
                
                raise ValueError (" debe de ser un numero entero.")
            
            if numero > longitud:
                raise IndexError (f"fuera del rango de la lista. Debe ser entre {", ".join(lista.index(numero))}")
            
            
            
            else:
                
                valor= lista[numero]
                print(f"entrada exitosa el indice ingresado es: {numero} y su valor es: {valor}")
                break
        except ValueError as error:
            print(f"Error de tipo: {error}")   
        except IndexError as error:
            print(f"Error de tipo: {error}")        
            
validacion ()