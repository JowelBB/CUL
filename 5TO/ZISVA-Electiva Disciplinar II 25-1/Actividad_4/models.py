from sqlalchemy import Column, Integer, String
from db_config import Base

class Products(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)
    descripcion = Column(String(255), index=True)
    precio = Column(Integer)
    categoria_id = Column(Integer)

class Categories(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)