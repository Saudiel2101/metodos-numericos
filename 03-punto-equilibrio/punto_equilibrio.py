import math
from datetime import date
from sqlalchemy import Column, Date, Integer, Numeric, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Credenciales y Conexión TCP/IP
USER = "saudiel"
PASS = "12345"  # Tu contraseña de PostgreSQL
HOST = "localhost"
PORT = "5432"
DB_NAME = "sexenio_db"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# -------------------------------------------------------------
# 2. DEFINIR 'Base' AQUÍ (Esto es lo que te faltaba antes de la clase)
# -------------------------------------------------------------
Base = declarative_base()


# 3. Mapeo de la Tabla
class Sexenio(Base):
  __tablename__ = "sexenio"

  id = Column(Integer, primary_key=True)
  fecha = Column(Date, nullable=False)
  determinacion = Column(Numeric(10, 4))
  publicacion_dof = Column(Numeric(10, 4))
  para_solventar = Column(Numeric(10, 4))


# 4. Crear Sesión
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# 5. Consulta de datos (Ajusta la fecha según tus registros)
fecha_inicio = date(2012, 1, 1)
fecha_fin = date(2024, 12, 31)

cotizaciones = (
    session.query(Sexenio)
    .filter(Sexenio.fecha.between(fecha_inicio, fecha_fin))
    .filter(Sexenio.para_solventar.isnot(None))
    .order_by(Sexenio.fecha)
    .all()
)

session.close()

# 6. Extracción y Cálculo Estadístico
lista_cotizaciones = [float(c.para_solventar) for c in cotizaciones]

print(f"Registros encontrados: {len(lista_cotizaciones)}")

if not lista_cotizaciones:
  print("¡Lista vacía! Verifica el rango de fechas.")
  exit()


def calcular_media_de(lista):
  return sum(lista) / len(lista)


def obtener_varianza_de(lista, poblacional=False):
  n = len(lista)
  if n < 2 and not poblacional:
    return 0
  media = calcular_media_de(lista)
  suma_cuadrados = sum((x - media) ** 2 for x in lista)
  return suma_cuadrados / n if poblacional else suma_cuadrados / (n - 1)


def obtener_desviacion_estandar(lista, poblacional=False):
  return math.sqrt(obtener_varianza_de(lista, poblacional))


media = calcular_media_de(lista_cotizaciones)
varianza = obtener_varianza_de(lista_cotizaciones)
desviacion = obtener_desviacion_estandar(lista_cotizaciones)

print("-------------------------------------")
print(f"Media: {media:.4f}")
print(f"Varianza: {varianza:.6f}")
print(f"Desviación Estándar: {desviacion:.6f}")
