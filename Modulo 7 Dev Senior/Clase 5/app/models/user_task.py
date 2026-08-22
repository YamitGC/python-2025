from sqlalchemy import Column, Integer, String, Boolean
from database.session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    #enable, disable, unable
    is_active = Column(Boolean, default=True)
