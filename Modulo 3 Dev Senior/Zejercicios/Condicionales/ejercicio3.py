peso_paquete = int(input("Ingrese el peso del paquete: "))
distancia_envio = int(input("Ingrese la distancia del envio: "))


if peso_paquete <= 2:
    if distancia_envio <= 100:
        print("Costo de envio: 5$")
    else:
        print("Costo de envio: 10$")
            
            
elif peso_paquete > 2 and peso_paquete <= 5:
    if distancia_envio <= 100:
        print("Costo de envio 8$")
    else:
        print("Costo de envio 15$")
            
            
elif peso_paquete > 5:
    if distancia_envio <= 100:
        print("Costo de envio 12$")
    else:
        print("Costo de envio 25$")
          
            
            
            
            
        
    
    