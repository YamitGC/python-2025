import tkinter as tk
import sys


### VENTANA DEL PROGRAMA ###
ventana = tk.Tk()
ventana.title("Botones")
#ventana.geometry("800x500+300+100")
ventana.minsize(width=200, height=300)
"""
↑↑↑ PARA TENER EN CUENTA

Si se quitan las dimenciones a la ventana, 
el widget se ajusta automaticamente al contenido
de los widgets

"""
### FUNCIONES ###
contador = 0
def cuenta_numeros():
    global contador
    contador += 1
    numero["text"] = contador

### TITULO DEL PROGRAMA ###
titulo = tk.Label(ventana,
                  text="CONTADOR",
                  font=("consolas", 20, "bold"),
                  bg="lightgreen", fg="darkblue",
                  relief=tk.GROOVE,
                  padx=40, pady=20
                  )
titulo.pack()

### LABEL DEL NUMERO ###
numero = tk.Label(ventana,
                  text="0",
                  font=("consolas", 48, "bold"),
                  bg="darkgreen", fg="lightblue",
                  relief=tk.GROOVE,
                  padx=20, pady=20
                  )
numero.pack()

### WIDGET PRINCIPAL DEL BOTON, CONTADOR +1 ###
contar_aumento = tk.Button(ventana,
                   text="CONTAR",
                   font=("consolas", 20, "bold"),
                   bg="lightgrey", fg="black",
                   relief=tk.GROOVE, bd=10,
                   padx=20, pady=20,
                   command=cuenta_numeros
                   )
contar_aumento.pack()

salir = tk.Button(ventana,
                  text="SALIR",
                  font=("consolas", 20, "bold"),
                  bg="darkred", fg="white",
                  relief=tk.GROOVE, bd=10,
                  padx=20, pady=10,
                  command=sys.exit
                  )
salir.pack()


### BUCLE PRINCIPAL DEL PROGRAMA ###
ventana.mainloop()
