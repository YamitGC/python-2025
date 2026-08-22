import random

def Prueba_Covid19():
    
    if edad >= 0 and edad < 6:
       random.choices([True,False], weights=[35,65], k=1)[0]
    elif edad >= 6 and edad < 14:
        random.choices([True,False], weights=[30,70], k=1)[0]
    elif edad >= 14 and edad < 18:
        random.choices([True,False], weights=[30,70], k=1)[0]
    elif edad >= 18 and edad < 30: 
        random.choices([True,False], weights=[35,65], k=1)[0]
    elif edad >= 30 and edad < 50: 
        random.choices([True,False], weights=[40,60], k=1)[0]
    elif edad >= 50 and edad < 100:
        random.choices([True,False], weights=[50,50], k=1)[0]
    elif edad >= 100 and edad < 130:
        random.choices([True,False], weights=[100,0], k=1)[0]
    else:
        print("Error, edad incorrecta.")
                                                

edad = int(input("Ingresa una edad del 0 al 130: "))

if  edad >= 100 and edad <= 130:
    resultado = Prueba_Covid19()
    print(f"Para la edad {edad}, el resultado es {resultado} para su prueba de Covid-19")
    

    