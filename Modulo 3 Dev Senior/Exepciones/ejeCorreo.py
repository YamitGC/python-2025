# 1.crear una lista de 10 valores, el usuario debe ingresar una clave para entrar a los valores de la lista

# 2. Descripción: Escribe un programa que solicite al usuario
# ingresar un correo electrónico y valide que tenga un formato válido
# (por ejemplo, que contenga un "@" y un "."). Maneja las excepciones si el formato no es válido


"""def validar_correo(correo): 
    
    if not re.search("@", correo) and not re.search(".", correo):
        raise ValueError("Error. El correo debe tener al menos un arroba(@) y un punto(.).")
    
    if not re.search("."):
        raise ValueError("Error. El correo debe tener al menos un punto(.).")"""
        
def validar_correo(correo):
    if "@" not in correo or "." not in correo:
        raise ValueError("Error. El correo debe tener al menos un arroba y un punto.")
    return True

def perdir_correo():
    while True:
        try:
            correo = input("Ingresa tu correo: ")
            validar_correo(correo)
            print(correo)
            break
        except ValueError:
            print("Error. El correo debe tener al menos un arroba y un punto.")
            
perdir_correo()
            
            
            
        
                
    