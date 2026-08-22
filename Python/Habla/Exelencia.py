def calculadora():
     # Solicitar al usuario que ingrese dos numeros
    num1= float(input("ingrese el primer numero: "))
    num2= float(input("ingrese el segundo numero: "))

    # Mostrar las operaciones disponibles 
    print("operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    # Solicitar al usuario que elija una ecuación
    Operacion = input("Elije una operación (1/2/3/4): ")