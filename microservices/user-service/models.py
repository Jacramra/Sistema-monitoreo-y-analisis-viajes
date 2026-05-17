# Importa tipos SQLAlchemy.
from sqlalchemy import Column, Integer, String

# Importa Base ORM.
from db import Base

# Modelo de tabla users.
class User(Base):

    # Nombre de tabla PostgreSQL.
    __tablename__ = "users"

    # ID autoincremental.
    id = Column(Integer, primary_key=True, index=True)

    # Nombre usuario.
    name = Column(String)

    # Correo usuario.
    email = Column(String)