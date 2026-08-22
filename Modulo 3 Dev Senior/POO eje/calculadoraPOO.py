"""Realizar un programa en el cual se declaren dos valores
enteros por teclado utilizando el método __init__.Calcular 
después la suma, resta, multiplicación y división. Utilizar 
un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora."""

class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def suma(self):
        resultado = self.num1 + self.num2
        print(f"El resultado de {self.num1} + {self.num2} = {resultado}")
        
    def resta(self):
        resultado = self.num1 - self.num2
        print(f"El resultado de {self.num1} - {self.num2} = {resultado}")
        
    def multiplicacion(self):
        resultado = self.num1 * self.num2
        print(f"El resultado de {self.num1} x {self.num2} = {resultado}")
        
    def division(self):
        resultado = self.num1 / self.num2
        print(f"El resultado de {self.num1} ÷ {self.num2} = {resultado}")
            
        
operacion1 = Calculadora(10, 40)
operacion1.suma()

operacion2 = Calculadora(20, 40)
operacion2.resta()

operacion3 = Calculadora(58, 4)
operacion3.multiplicacion()

operacion4 = Calculadora(10, 1238951)
operacion4.division()
    