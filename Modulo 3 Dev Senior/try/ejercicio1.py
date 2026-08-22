"""try:
    x = 10 / 0

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
"""

try:
    numero = int(input("Por favor, ingrese un número: "))
    resultado = 10 / numero
    
except ValueError:
    print("Error: Debe ingresar un número entero.")
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    
except Exception as e:
    print(f"Error inesperado: {e}")
    
    