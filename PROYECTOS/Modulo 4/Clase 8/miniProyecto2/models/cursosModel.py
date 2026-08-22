from database import conectar_db, cerrar_db, ejecutar_consulta, confirmar_cambios

def crear(nombre_curso, descripcion, creditos, id_docente):
    """Crea un nuevo curso."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "INSERT INTO cursos (nombre_curso, descripcion, creditos, id_docente) VALUES (%s, %s, %s, %s);"
            ejecutar_consulta(conexion, consulta, (nombre_curso, descripcion, creditos, id_docente))
            confirmar_cambios(conexion)
            return True
    finally:
        cerrar_db(conexion)
    return False

def consultarCursos():
    """Consulta todos los cursos."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT c.id_curso, c.nombre_curso, c.descripcion, c.creditos, d.nombre AS nombre_docenente, d.apellido as apellido_docente FROM cursos c JOIN docentes d ON c.id_docente = d.id_docente;"
            resultados = ejecutar_consulta(conexion, consulta)
            return resultados
    finally:
        cerrar_db(conexion)
        
# Consulta un curso por el id del docente
def consultarCursoPorDocente(numero_documento):
    """Consulta un curso por el id del docente."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT c.nombre_curso, c.descripcion, c.creditos, d.nombre AS nombre_docenente, d.apellido as apellido_docente FROM cursos c JOIN docentes d ON c.id_docente = d.id_docente WHERE d.numero_documento = %s;"
            resultados = ejecutar_consulta(conexion, consulta, (numero_documento,))
            return resultados
    finally:
        cerrar_db(conexion)

def actualizar(id_curso, nombre_curso, descripcion, creditos, id_docente):
    """Actualiza un curso existente."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "UPDATE cursos SET nombre_curso = %s, descripcion = %s, creditos = %s, id_docente = %s WHERE id_curso = %s;"
            ejecutar_consulta(conexion, consulta, (nombre_curso, descripcion, creditos, id_docente, id_curso))
            confirmar_cambios(conexion)
            return True
    finally:
        cerrar_db(conexion)
    return False

def eliminar(id_curso):
    """Elimina un curso por su ID."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "DELETE FROM cursos WHERE id_curso = %s;"
            ejecutar_consulta(conexion, consulta, (id_curso,))
            confirmar_cambios(conexion)
            return True
    finally:
        cerrar_db(conexion)
    return False
