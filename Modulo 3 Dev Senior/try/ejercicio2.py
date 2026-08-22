try:
    archivo = open("datos.csv" "r")
    contenido = archivo.read()
    
except FileNotFoundError:
    print("Error: El archivo no existe")
    archivo = None
    
else:
    print("El archivo fue leido con exito")
    
finally:
    if archivo:
        archivo.close()
    
    else:
        print("Recuerda que si el archivo no existe => no lo puedo cerrar...")
    