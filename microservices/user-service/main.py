# FastAPI framework.
from fastapi import FastAPI

# Prometheus metrics.
from prometheus_fastapi_instrumentator import Instrumentator

# SQLAlchemy session.
from sqlalchemy.orm import Session

# Base de datos.
from db import SessionLocal, engine

# Modelos ORM.
import models

# ==============================
# PROMETHEUS
# ==============================
from prometheus_fastapi_instrumentator import Instrumentator

# Crea tablas automáticamente.
models.Base.metadata.create_all(bind=engine)

# Crea aplicación FastAPI.
app = FastAPI()

# =====================================================
# ACTIVAR MÉTRICAS PROMETHEUS
# =====================================================
Instrumentator().instrument(app).expose(app)

# ==============================
# ACTIVAR METRICS
# ==============================
Instrumentator().instrument(app).expose(app)

# Endpoint principal.
@app.get("/")
def home():

    return {
        "message": "User Service Running with PostgreSQL"
    }

# Obtener usuarios.
@app.get("/users")
def get_users():

    # Crea sesión DB.
    db = SessionLocal()

    # Consulta usuarios.
    users = db.query(models.User).all()

    return users

# Crear usuario.
@app.post("/users")
def create_user(user: dict):

    # Sesión DB.
    db = SessionLocal()

    # Crear objeto ORM.
    new_user = models.User(
        name=user["name"],
        email=user["email"]
    )

    # Guardar en PostgreSQL.
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }