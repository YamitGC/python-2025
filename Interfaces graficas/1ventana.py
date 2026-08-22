import tkinter as tk

"""
Creamos un objeto llamado ventana de la clase tk,
ya que hace parte de la libreria tkinter debemos poner donde esta ubicada
"""
ventana = tk.Tk()

#Con .title() agregamos el titulo a la ventana
ventana.title("Primera ventana")

#Con .geometry() se le dan las dimenciones a la ventana y lo que se suma es las cordenadas para saber donde aparece
ventana.geometry("800x500+300+100")

#Con .resizable() le podemos dar permisos para que pueda modificar el tamaño de la ventana
#ventana.resizable(width=False, height=False)

#Con .minsize() le podemos decir el minimo que la ventana se puede minimizar
ventana.minsize(width=300, height=200)

#Con .maxsize() le podemos dar el maximo que la ventana se puede expandir
ventana.maxsize(width=1200, height=800)

#Con .configure() o config() le podemos dar el color a la ventana, ademas que la palabra background se puede abreviar como bg
ventana.config(bg="lightblue")


#mainloop() es el bucle principal del programa, sirve para ejecular la ventana
ventana.mainloop()