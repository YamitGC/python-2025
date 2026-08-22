from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.tarea import TareaCreate, TareaOut
from crud import tarea as crud_tarea
from database.session import get_db

router = APIRouter()

@router.post("/", response_model=TareaOut)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crud_tarea.crear_tarea(db, tarea)

@router.get("/", response_model=list[TareaOut])
def listar_tareas(db: Session = Depends(get_db)):
    return crud_tarea.listar_tareas(db)

@router.get("/{tarea_id}", response_model=TareaOut)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud_tarea.obtener_tarea(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.put("/{tarea_id}", response_model=TareaOut)
def actualizar_tarea(tarea_id: int, tarea: TareaCreate, db: Session = Depends(get_db)):
    tarea_actualizada = crud_tarea.actualizar_tarea(db, tarea_id, tarea)
    if tarea_actualizada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_actualizada

@router.delete("/{tarea_id}", response_model=TareaOut)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea_eliminada = crud_tarea.eliminar_tarea(db, tarea_id)
    if tarea_eliminada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_eliminada