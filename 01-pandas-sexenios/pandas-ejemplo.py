# Importar las librerias
from sqlalchemy import Column,Date, Numeric, Integer, String, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
import pandas as pd

# Informacion de la conexión a la base de datos de postgreSQL
USER = "uriel"
PASSWORD = "12345"
HOST = "localhost"
PORT = "5432"
DB_NAME = "escuela_db"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Creating a Database Connection

# SQLAlchemy creates database connections using create_engine() function. This function takes a
# connection URL and returns an engine object, which manages the connection between Python and the database.


engine = create_engine(DATABASE_URL)

# Declarar la base para los modelos
Base = declarative_base()


#  Definir la clase (tabla 'cotizaciones')
class Calificaciones(Base):
  __tablename__ = "calificaciones"

  id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
  alumno_id  = Column(Integer)
  materia_id = Column(Integer)
  calificacion = Column(Numeric(precision=5, scale=2))


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

#  Crear una sesión para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

mi_query = session.query(Calificaciones).filter(Calificaciones.materia_id ==5)
df = pe,read_sql(mi_query.statement, session.bind)
session.close()


#sentencia = text("SELECT * FROM cotizaciones;")
#resultado = session.execute(sentencia)




# Cerrar sesión
session.close()


datos = pd.DataFrame(resultado.fetchall(), columns=resultado.keys())

media = df['calificaciones'].astype(float).mean()
varianza = df['calificaciones'].astype(float).var()
desviacion_estandar = df['calificaciones'].astype(float).std()




