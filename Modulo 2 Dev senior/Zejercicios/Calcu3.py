import tkinter as tk


ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, width=20)
entrada.grid(row=0, column=0, columnspan=4)

def boton_click(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

fila = 1
columna = 0

for boton in botones:
    tk.Button(ventana, text=boton, width=5, height=2, command=lambda valor=boton: boton_click(valor)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()