from database.base import Base, engine
from models.tarea import Tarea

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")
    
if __name__ == "__main__":
    init_db()