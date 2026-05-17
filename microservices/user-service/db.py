# Importa herramientas SQLAlchemy.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de conexión PostgreSQL.
#
# postgres-db:
# nombre del servicio Docker Compose.
DATABASE_URL = "postgresql://admin:admin123@postgres-db:5432/mobility_db"

# Crea motor de conexión.
engine = create_engine(DATABASE_URL)

# Crea sesiones para consultas.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos ORM.
Base = declarative_base()