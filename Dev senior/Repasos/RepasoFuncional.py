num1 = 5
num2 = 5
suma = num1 + num2

def sumaFuncionTradicional(num1, num2):
    return num1 + num2 

"""sumaFuncional = lambda a,b  : a + b
print(sumaFuncional(5,5))
print(sumaFuncionTradicional(10,10))"""

numeros = [1,2,3,4,5]
resultado = list(map(lambda x: x * 2, numeros))
"""print(resultado)
print(type(resultado))"""

palabras = ["Hola como estas"]
mayusculas = lambda x: x.upper()
resultado = list(map(mayusculas, palabras))
"""print(resultado)"""

numeros = [1,2,3,4,5, 1233, 1291, 232, 251, 252, 12, 94, 123, 1000]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
"""print(numeros_pares)"""


import functools

numeros = ["Juan", "Ana", "Manuel", "Felipe"]
numeros_reduce = functools.reduce(lambda x, y: x + y, numeros)
print(numeros_reduce)