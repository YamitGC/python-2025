def procesar_pedido(codigo_producto, cantidad):
    try:
        
        if not codigo_producto.isalnum():
            raise ValueError("El codigo del producto debe ser alfanumerico")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser superior a cero")
        
        precio_unitario = 100
        total = precio_unitario * cantidad
        
    except ValueError as e:
        print(f"Error al procesar el pedido {e}")
    else:
        print(f"Pedido procesado exitosamente. El total a pagar es : ${total: .2f}")
    finally:
        print("Operación finalizada. Registro actualizado")

if __name__ == "__main__":
    procesar_pedido("ABC123", 2)
    procesar_pedido("#####", 12)        
    procesar_pedido("GHJ1239", -10)   
    procesar_pedido("GHJ1239", 10.30) 