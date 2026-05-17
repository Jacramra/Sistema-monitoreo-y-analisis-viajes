# Framework FastAPI.
from fastapi import FastAPI

# Base de datos.
from db import SessionLocal, engine

# Modelos ORM.
import models

# Crear tablas automáticamente.
models.Base.metadata.create_all(bind=engine)

# Crear aplicación.
app = FastAPI()

# Endpoint principal.
@app.get("/")
def home():

    return {
        "message": "Trip Service Running with PostgreSQL"
    }

# Obtener viajes.
@app.get("/trips")
def get_trips():

    db = SessionLocal()

    trips = db.query(models.Trip).all()

    return trips

# Crear viaje.
@app.post("/trips")
def create_trip(trip: dict):

    db = SessionLocal()

    new_trip = models.Trip(
        city=trip["city"],
        distance=trip["distance"],
        duration=trip["duration"],
        price=trip["price"]
    )

    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)

    return {
        "message": "Trip created successfully",
        "trip": {
            "id": new_trip.id,
            "city": new_trip.city,
            "distance": new_trip.distance,
            "duration": new_trip.duration,
            "price": new_trip.price
        }
    }