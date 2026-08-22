import tkinter as tk

ventana = tk.Tk()
#Acá las caracteristicas de la ventana
ventana.title("Widgets")
ventana.geometry("800x500+300+100")
ventana.minsize(width=300, height=200)
ventana.maxsize(width=1000, height=800) 
ventana.config(background="lightblue")


### Creacion de widgets ###
titulo = tk.Label(ventana,
                  text="TITULO DE LA APLICACIÓN\n SEGUNDA LINEA\n TERCERA LINEA", #Coloca textos en la ventana
                  font=("consolas", 20, "bold"), #Tipo de letra y tamaño
                  bg="white", #Color de donde irán los textos
                  foreground="black", #Color de las letras
                  padx=1000, pady=20, #Modificar el espacio del titulo
                  #width=40, height=3,  #<-- esta es otra forma de decir padx=, pady= pero sin cordenadas, este es con espacios
                  anchor=tk.CENTER, #Para decir donde colocar el texto
                  justify=tk.LEFT, #Sirve para decir donde colocar las demas lineas (segunda linea, tercera, cuarta etc.)
                  relief=tk.GROOVE, #Esto es para poner bordes a los titulos
                  border=10 #Tamaño del borde
                  )
#Para ejecutar el titulo
titulo.pack()


ventana.mainloop()