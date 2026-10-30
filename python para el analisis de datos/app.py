import math
from sqlalchemy import Column,Date, Numeric, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date



# 1. Crear el motor de conexión (remplaza usuario, password, host y base_datos)
USER = "metodos"
PASSWORD = "12345678"
HOST = "localhost"
PORT = "5432"
DB_NAME = "metodos_db"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# 2. Declarar la base para los modelos
Base = declarative_base()


# 3. Definir la clase (tabla 'cotizacion')
class Cotizacion(Base):
  __tablename__ = "cotizacion"

  id = Column(Integer, primary_key=True, index=True)
  fecha = Column(Date, nullable=False)
  cotizacion = Column(Numeric(precision=10, scale=4))


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# 4. Crear una sesión para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Ejemplo de inserción (Crear)
#nueva_cotizacion = Cotizacion(fecha="24-09-2026", cotizacion="25")
#session.add(nueva_cotizacion)
#session.commit()


fecha_inicio = date(2026, 1, 1)
fecha_fin = date(2026, 12, 31)

cotizaciones_2026 = (
    session.query(Cotizacion)
    .filter(Cotizacion.fecha.between(fecha_inicio, fecha_fin))
    .all()
)



# Cerrar sesión
session.close()

lista_cotizaciones = []




for cotizacion in cotizaciones_2026:
    # Accedemos a las propiedades del objeto directamente
    print(f"cotizacion: {cotizacion.cotizacion}")
    lista_cotizaciones.append(cotizacion.cotizacion)
    
print("-------------------------------------\n")

print(f"cotizaciones: {lista_cotizaciones}")


def calcular_media_de (lista):
  n = len(lista)
  media = sum(lista) / n
  return media

def obtener_varianza_de (lista, poblacional=False):
  n = len(lista)

  # 1. Validar que tengamos datos suficientes
  if n < 2 and not poblacional:
    return 0
  if n == 0:
    return 0

  # 2. Calcular la media (promedio)
  media = calcular_media_de(lista)

  # 3. Calcular la suma de las diferencias al cuadrado
  # (valor - media) ** 2 para cada elemento
  suma_cuadrados = sum((x - media) ** 2 for x in lista)

  # 4. Dividir según el tipo de varianza
  if poblacional:

    return suma_cuadrados / n  # Divide por N
  else:
    return suma_cuadrados / (n - 1)  # Divide por N - 1


def obtener_desviacion_estandar(lista, poblacional=False):
  desviacion_estandar = obtener_varianza_de (lista)
  return  math.sqrt(desviacion_estandar)

varianza = obtener_varianza_de(lista_cotizaciones, False)
desviacion = obtener_desviacion_estandar(lista_cotizaciones, False)

print(f"La varianza es: {varianza}")
print(f"La desvicion estandar es: {desviacion}")
