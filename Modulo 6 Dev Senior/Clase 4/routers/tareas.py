from fastapi import APIRouter
from models import TareaEntrada, TareaSaliente

router = APIRouter()

tareas_db = []
id_actual = 1

@router.post("/tareas", response_model=TareaSaliente)
def crear_tarea(tarea: TareaEntrada):
    global id_actual
    nueva_tarea = TareaSaliente(id=id_actual,
                                titulo=tarea.titulo,
                                descripcion=tarea.descripcion,
                                completado=False
                                )
    tareas_db.append(nueva_tarea)
    id_actual += 1
    return nueva_tarea

@router.get("/tareas", response_model=list[TareaSaliente])
def listar_tareas():
    return tareas_db

@router.put("/tareas/{tarea_id}", response_model=TareaSaliente)
def actualizar_tarea(tarea_id: int, tarea_actualizada: TareaEntrada):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            tarea.titulo = tarea_actualizada.titulo
            tarea.descripcion = tarea_actualizada.descripcion
            return tarea
    return {"error": "Tarea no encontrada"}

@router.delete("/tareas/{tarea_id}", response_model=dict)
def eliminar_tarea(tarea_id: int):
    global tareas_db
    tareas_db = [tarea for tarea in tareas_db if tarea.id != tarea_id]
    return {"mensaje": "Tarea eliminada correctamente"}




