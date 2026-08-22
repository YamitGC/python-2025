matricula_Fecha = input("Ingrese la fecha de matricula (DD/MM/AAAA): ")


dia, mes, anio = matricula_Fecha.split("/")

if len(dia) == 2 and len(mes) == 2 and len(anio) == 4:    # Cantidad exacta de digitos
    if dia.isdigit() and mes.isdigit() and anio.isdigit():   # Validar si por terminal nos entregan NUMEROS
        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(anio) <= 2025:  # Validar rangos de los numeros
            print("Fecha valida.")
        else:
            print("Fecha INVALIDA. El dia, mes o año es invalido")
    else:
        print("Fecha INVALIDA. Los valores de la fecha no son numericos")
else: 
    print("Fecha INVALIDA. Fuera del rango de las fechas")
    
print(matricula_Fecha)
            