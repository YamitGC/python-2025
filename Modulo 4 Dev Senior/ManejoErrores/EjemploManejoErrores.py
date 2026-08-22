try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10 / numero
except ValueError:
    print("Ingrese un numero valido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print("Fin del programa")

