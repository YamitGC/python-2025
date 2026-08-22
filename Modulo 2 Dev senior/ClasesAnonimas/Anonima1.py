def saludar(self):
    print(f"Hola, mi nombre es {self.nombre}")
    
Persona = type("persona", (object,), {
    "nombre" : "juan",  # Atributo de la clase
    "saludar": saludar # funcion de la clase
})

# Creamos una instancia de la clase anonima
persona_objeto = Persona()

# Llamamos la clase objeto
persona_objeto.saludar()