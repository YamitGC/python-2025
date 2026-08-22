"""crear un programa para gestionar estudiantes
que les puedas poner notas, agregar nuevos 
estudiantes y sacarles el promedio"""

lista_notas = []   
lista_estudiantes = []    

while True: 
        
       
    estudiantes = input("Ingresa nombres estudiantes (escriba 'hecho' para terminar): ")
    if estudiantes.lower() == "hecho":
        break
       
    lista_estudiantes.append(estudiantes)
       
while True:
        
    notas = input("Ingrese las notas (escriba 'hecho' para terminar): ")
    if notas.lower() == "hecho":
            break
    try:
        
        numero = float(notas)
        lista_notas.append(numero)
    
    except ValueError:
        print("Eso no es un numero.")
        
if lista_notas:
    promedio = sum(lista_notas) / len(lista_notas)
    print(f"Las notas son: {lista_notas}")
    print(f"El promedio de las notas es: {promedio}")
        
        

 
        
  
        
        
        
        

    