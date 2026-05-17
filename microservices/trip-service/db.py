# Herramientas SQLAlchemy.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Conexión PostgreSQL.
DATABASE_URL = "postgresql://admin:admin123@postgres-db:5432/mobility_db"

# Motor de conexión.
engine = create_engine(DATABASE_URL)

# Sesiones SQLAlchemy.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base ORM.
Base = declarative_base()