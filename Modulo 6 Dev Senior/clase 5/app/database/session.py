from sqlalchemy.orm import sessionmaker
from database.base import engine

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Nos permite crear una sesión local para interactuar con la base de datos

def get_db():
    db = LocalSession()
    try:
        yield db
    except Exception as e:
        db.rollback()
        print(f"Error en la sesión de la base de datos: {e}")
    finally:
        db.close()