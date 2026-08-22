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
sumador = 0
def sumador_numeros():
    global sumador
    sumador += 1
    numero["text"] = sumador
    
restador = 0
def restador_numeros():
    global restador
    restador -= 1
    numero["text"] = restador
    

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
                   text="CONTAR +1",
                   font=("consolas", 20, "bold"),
                   bg="lightgrey", fg="black",
                   relief=tk.GROOVE, bd=10,
                   padx=20, pady=20,
                   command=sumador_numeros
                   )
contar_aumento.pack()

### WIDGET PRINCIPAL DEL BOTON, CONTADOR -1 ###
contar_descenso = tk.Button(ventana,
                   text="CONTAR -1",
                   font=("consolas", 20, "bold"),
                   bg="lightgrey", fg="black",
                   relief=tk.GROOVE, bd=10,
                   padx=20, pady=20,
                   command=restador_numeros
                   )
contar_descenso.pack()
                   
                   
                   
            

### BUCLE PRINCIPAL DEL PROGRAMA ###
ventana.mainloop()