x = int(input("Ingrese la cantidad $(COL): "))

def COL_to_USD(x):
    return x * 0.00023   #Precio del dolar 21/01/25

print(COL_to_USD(x),"USD")
