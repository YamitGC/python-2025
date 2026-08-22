#Fromkeys

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

claves = ["a", "b", "c"]

diccionario2 = dict.fromkeys(claves)
#print(diccionario2)

#Setdefault()---------------------------------------------

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

diccionario.setdefault("Nombre" , "Manuel")
#print(diccionario)

#Update()--------------------------------------------------

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

diccionario.update({"Telefono": 31040301201, "Identifiacion": 1002149124})
diccionario.update({"nombre": "Maria", "edad": 20})
#print(diccionario)

# TUPLE
# enumerate()------------------------------------------------

tupla = (1,2,3,4,5)
for i, valor in enumerate(tupla):
    print(f"Indice: {i}, valor: {valor}")