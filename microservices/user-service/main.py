# FastAPI framework.
from fastapi import FastAPI

# SQLAlchemy session.
from sqlalchemy.orm import Session

# Base de datos.
from db import SessionLocal, engine

# Modelos ORM.
import models

# Crea tablas automáticamente.
models.Base.metadata.create_all(bind=engine)

# Crea aplicación FastAPI.
app = FastAPI()

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