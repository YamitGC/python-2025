# crud_simple.py

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

productos = []
ultimo_id = 0

def crear_producto(nombre, precio):
    global ultimo_id
    ultimo_id += 1
    nuevo_producto = Producto(ultimo_id, nombre, precio)
    productos.append(nuevo_producto)
    print(f"Producto '{nuevo_producto.nombre}' creado con ID: {nuevo_producto.id}")

def leer_producto(id):
    for producto in productos:
        if producto.id == id:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: ${producto.precio:.2f}")
            return
    print(f"No se encontró ningún producto con el ID: {id}")

def actualizar_producto(id, nuevo_nombre, nuevo_precio):
    for producto in productos:
        if producto.id == id:
            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio
            print(f"Producto con ID {id} actualizado a Nombre: '{nuevo_nombre}', Precio: ${nuevo_precio:.2f}")
            return
    print(f"No se encontró ningún producto con el ID: {id}")

def eliminar_producto(id):
    global productos
    productos = [producto for producto in productos if producto.id != id]
    print(f"Producto con ID {id} eliminado.")

# Ejemplo de uso
crear_producto("Laptop", 1200.50)
crear_producto("Mouse", 25.00)
leer_producto(1)
actualizar_producto(1, "Laptop Gamer", 1500.00)
leer_producto(1)
eliminar_producto(2)
leer_producto(2)