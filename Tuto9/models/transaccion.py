"""
Gestor de gastos

Clase
El proyecto debe permitir agregar un -tipo- de transaccion sea gasto o ingreso
Debe especificarse que -categoria- es: Salario, salud, transporte, regalo, otros
-fecha- DD/MM/YY
-Monto-

Cada transaccion debe agregar a una lista, para luego en un menu interactivo el usuario pueda
escoger ver sus movimientos o transacciones

"""
from dataclasses import dataclass

@dataclass
class Transaccion:
    tipo: str
    categoria: str
    fecha: str
    monto: float
    
    """
    Metodo __str__
    """
    def __str__(self):
        return f'Tipo de transaccion: {self.tipo}, Categoria: {self.categoria}, Monto: {self.monto} el {self.fecha}.'
    
    