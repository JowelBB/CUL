from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#   Datos para conexion a la bd, credneciales y config
DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/mi_api"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()