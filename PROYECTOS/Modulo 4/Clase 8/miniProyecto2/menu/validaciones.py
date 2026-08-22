import re

# --------- Validaciones para estudiantes y docentes -----------------------------------

def validar_documento(doc):
    """Valida que el documento solo contenga números."""
    return doc.isdigit()

def validar_nombre(nombre):
    """Valida que el nombre solo contenga letras."""
    return nombre.isalpha()

def validar_fecha(fecha):
    """Valida que la fecha tenga el formato YYYY-MM-DD."""
    return bool(re.match(r"\d{4}-\d{2}-\d{2}$", fecha))

def validar_email(email):
    """Valida que el email tenga un formato básico correcto."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def validar_telefono(telefono):
    """Valida que el teléfono solo contenga números."""
    return telefono.isdigit()

# ---------- Validaciones para cursos -----------------------------------

def validar_descripcion(descripcion):
    return len(descripcion) > 0

def validar_creditos(creditos):
    return creditos.isdigit() and 0 < int(creditos) <= 10

def validar_id_docente(id_docente):
    return id_docente.isdigit()