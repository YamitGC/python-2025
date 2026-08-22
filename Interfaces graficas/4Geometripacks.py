import tkinter as tk

ventana = tk.Tk()

### CREACION DE WIDGETS ###

rotulo1 = tk.Label(ventana,
                   text="Primer Widget",
                   font=("consolas", 20, "bold"),
                   bg= "lightgreen", fg="darkblue"
                   )
rotulo1.pack()

rotulo2 = tk.Label(ventana,
                   text="Tercer Widget",
                   font=("consolas", 36, "bold"),
                   bg= "lightgreen", fg="darkblue"
                   )
rotulo2.pack(side=tk.LEFT)

rotulo3 = tk.Label(ventana,
                   text="Tercer Widget",
                   font=("consolas", 30, "bold"),
                   bg= "lightgreen", fg="darkblue"
                   )
rotulo3.pack(side=tk.RIGHT)



ventana.mainloop()