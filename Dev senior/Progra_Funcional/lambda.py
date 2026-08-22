"""

#Ejemplo 1

x = lambda a : a + 10

print(x(5))

#Es lo mismo que:

def cualquiera(a):
    return a+10
    
print(cualquiera(5))

# Ejemplo 2

x = lambda a, b : a * b
print(x(5,6))



def x(a,b):
    return a*b

print(x(5,6))
"""

x = lambda a,b,c : a + b + c
print(x(5,6,2))



def x(a,b,c):
    return a+b+c

print(x(5,6,2))


