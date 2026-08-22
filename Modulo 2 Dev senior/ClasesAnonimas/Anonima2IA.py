def crear_formulario(campos):
    # Creamos una clase anónima, donde los campos proporcionados serán atributos
    formulario = type('Formulario', (object,), {campo: "" for campo in campos})
    return formulario

# Lista de campos que queremos en el formulario
campos = ['nombre', 'edad', 'email']

# Creamos el formulario utilizando la lista de campos
Formulario = crear_formulario(campos)

# Creamos una instancia del formulario
formulario_obj = Formulario()

# Asignamos valores a los campos
formulario_obj.nombre = "Carlos"
formulario_obj.edad = "30"
formulario_obj.email = "carlos@example.com"

# Mostramos los valores de los campos
print(f"Nombre: {formulario_obj.nombre}")
print(f"Edad: {formulario_obj.edad}")
print(f"Email: {formulario_obj.email}")
