try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10 / numero
    
except ValueError:
    print("Error: Ingrese un numero valido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except Exception as e:
    print(f"Ocurrio un error: {e}")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Fin del programa")

    



