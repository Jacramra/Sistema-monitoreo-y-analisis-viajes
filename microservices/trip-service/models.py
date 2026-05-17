# Tipos SQLAlchemy.
from sqlalchemy import Column, Integer, String, Float

# Base ORM.
from db import Base

# Tabla trips.
class Trip(Base):

    __tablename__ = "trips"

    # ID viaje.
    id = Column(Integer, primary_key=True, index=True)

    # Ciudad.
    city = Column(String)

    # Distancia.
    distance = Column(Float)

    # Duración.
    duration = Column(Float)

    # Precio.
    price = Column(Float)