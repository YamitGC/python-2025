# 1.crear una lista de 10 valores, el usuario debe ingresar una clave para entrar a los valores de la lista

def llamar_valor():
    
   numeros = ["Pan", "Fresas", "Carne", "Pescado", "Leche", "Papa", "Lechuga", "Garbanzo", "Azucar", "Galleta"]
   
   while True:
       try:
           indice = int(input("Ingresa el indice de la lista que quieras acceder: "))
           print(f"El elemento en la posicion {indice} es {numeros[indice]}")
           break
       
       except ValueError:
           print("Debe ingresae un numero entero")
           
       except IndexError:
           print(f"Error. El indice esta fuera de rango {len(numeros)} elementos")
           
llamar_valor()
       
       

                