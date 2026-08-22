import psycopg2 

# Establecer  la conexión a la base de datos

conexion = psycopg2.connect(
    host="localhost",
    database="Academia",
    user="postgres",
    password="admin",
    port="5432"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Insertar datos
insert_query = """INSERT INTO empleados (nombre, puesto,salario) VALUES (%s, %s, %s)"""

nombre = input("Ingrese el nombre del empleado: ")
puesto = input("Ingrese el puesto del empleado: ")
salario = input("Ingrese el salario del empleado: ")

emplado_data = (nombre, puesto, salario)

cursor.execute(insert_query, emplado_data)
conexion.commit()
