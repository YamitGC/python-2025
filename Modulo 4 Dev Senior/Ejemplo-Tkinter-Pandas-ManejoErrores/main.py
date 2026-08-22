import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    return ruta_archivo

def crear_csv_por_defecto():
    df = pd.DataFrame(columns=["Nombre", "Edad", "Ciudad"])
    df.to_csv("datos.csv", index=False)
    return "datos.csv"

def mostar_mensaje_exito():
    messagebox.showinfo("Exito", "Archivo cargado correctamente")

def mostar_mensaje_error(e):
    messagebox.showerror("Error", f"Error al cargar el archivo: {e}")

def cargar_csv():

    try:
        ruta_archivo = seleccionar_archivo()

        if not ruta_archivo:
            ruta_archivo = crear_csv_por_defecto()

        df = pd.read_csv(ruta_archivo)
        df.to_csv("datos.csv", index=False)
        mostar_mensaje_exito()

    except Exception as e:
        mostar_mensaje_error(e)
        

#Interfaz grafica
root = tk.Tk()
root.title("Carga de Archivos CSV")
root.geometry("400x300")


tk.Button(root, text="Cargar CSV", command=cargar_csv).pack(pady=20)
resultado_var = tk.StringVar()
tk.Label(root, textvariable=resultado_var).pack(pady=10)

root.mainloop()
