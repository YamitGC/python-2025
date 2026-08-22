class ErrorDePago(Exception):
    pass

class PasarelaDePago:
    @staticmethod
    def procesar_pago(numero_tarjeta, monto):
        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("El número de la tarjeta no es valido. Debe iniciar en 4")
        if monto <= 0:
            raise ErrorDePago("El monto de la compra debe ser superior a cero")
        if len(numero_tarjeta) != 16:
            raise ErrorDePago("El número de la tarjeta debe tener 16 digitos")
        
        return f"El pago de ${monto} fue procesado con exito."
    
def proceso_pago_cliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f"Iniciando el proceso de pago de {nombre_cliente}...")
        resultado = PasarelaDePago.procesar_pago(numero_tarjeta, monto)
    except ErrorDePago as e:
        print(f"Error al procesar el pago: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    else: 
        print(resultado)
    finally:
        print("El registro de la transacción finalizo.")

if __name__ == "__main__":
    proceso_pago_cliente("Juan", "4134039356733728", 300)