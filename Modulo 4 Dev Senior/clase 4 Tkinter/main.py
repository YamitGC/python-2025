import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import os

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if ruta_archivo:
        resultado_var.set(ruta_archivo)
    else:
        resultado_var.set("No se selecciono ningun archivo")
        
def crear_csv_por_defecto():
        df = pd.DataFrame(columns=["Nombre", "Edad", "Ciudad"])
        df.to_csv("datos.csv", index=False)
        resultado_var.set("Archivo creado correctamente")

def mostrar_mensaje_exito():
    messagebox.showinfo("Exito", "Archivo cargado correctamente")
    
def mostrar_mensaje_error(e):
    messagebox.showerror("Error", "Error al cargar el archivo")

def cargar_csv():
    
    try:
        ruta_archivo = seleccionar_archivo()
        
        if not ruta_archivo:
           ruta_archivo = crear_csv_por_defecto()
            
        df = pd.read_csv(ruta_archivo)
        df.to_csv("datos.csv", index=False)
        mostrar_mensaje_exito()
        
    except Exception as e:
        mostrar_mensaje_error(e)
        
#Interfaz de usuario
ventana = tk.Tk()
ventana.title("Gestion de Archivos CSV")
ventana.geometry("300x200")

tk.Button(ventana, text="Cargar CSV", command=cargar_csv).pack(pady=20)
resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var).pack(pady=20)

ventana.mainloop()


        
        
        
      
    
        
        

