def tipoExperimento():
    
    while True:
        opciones = ["Quimico", "Fisico", "Biologico"]
    
        experimento = input("Ingresa el tipo de experimento (Quimico, Fisico, Biologico): ").lower()
    
        if experimento not in opciones:
           print("Error, digite uno de los tres experimentos.")
        else:
            print(f"Tipo de experimento {experimento}")
        break


       
        
     
    

    
tipoExperimento()
    