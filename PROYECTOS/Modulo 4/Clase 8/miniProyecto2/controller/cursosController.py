from models import cursosModel
from views import cursosView

def mostrar_cursos():
    """Mostrar la lista de cursos."""
    cursos = cursosModel.consultarCursos()
    if cursos:
        cursosView.mostrar_cursos(cursos)
    else:
        print("No hay cursos registrados.")

def mostrar_curso_por_docente(numero_documento):
    """Mostrar los cursos dictados por un docente específico."""
    cursos = cursosModel.consultarCursoPorDocente(numero_documento)
    if cursos:
        cursosView.mostrar_curso_por_docente(cursos)
    else:
        print("No hay cursos registrados para este docente.")
        
def crear_curso(nombre_curso, descripcion, creditos, numero_documento):
    """Crear un nuevo curso."""
    if cursosModel.crear(nombre_curso, descripcion, creditos, numero_documento):
        print("Curso creado exitosamente.")
    else:
        print("Error al crear el curso.")

def modificar_curso(id_curso, nombre_curso, descripcion, creditos, numero_documento):
    """Modificar un curso existente."""
    if cursosModel.actualizar(id_curso, nombre_curso, descripcion, creditos, numero_documento):
        print("Curso modificado exitosamente.")
    else:
        print("Error al modificar el curso.")

def eliminar_curso(id_curso):
    """Eliminar un curso existente."""
    if cursosModel.eliminar(id_curso):
        print("Curso eliminado exitosamente.")
    else:
        print("Error al eliminar el curso.")
