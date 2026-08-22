

while True:
    
    calificacion = int(input("Ingrese su calificacion: "))

    if calificacion < 0 or calificacion > 100:
        print("Calificacion no valida")
        
        
    elif calificacion in range(90,101):
        print("Su califiacion es: A")
        break
       
       
    elif calificacion in range(80,90):
        print("Su calificacion es: B")
        break
       
    elif calificacion in range(70,80):
        print("Su calificacion es: C")
        break
        
    elif calificacion in range(60,70):
        print("Su calificacion es: D")
        break
        
    else:
        print("Su calificacion es: F")
        break
    

        
        
       