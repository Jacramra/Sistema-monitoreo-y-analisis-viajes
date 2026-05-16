# Importa FastAPI para construir el microservicio.
from fastapi import FastAPI

# Crea la aplicación FastAPI.
app = FastAPI()

# Lista temporal para almacenar viajes.
# Más adelante puede conectarse a PostgreSQL.
trips = []

# Endpoint principal para verificar estado del servicio.
@app.get("/")
def home():

    return {
        "message": "Trip Service Running"
    }

# Endpoint para obtener todos los viajes registrados.
@app.get("/trips")
def get_trips():

    return trips

# Endpoint para registrar un nuevo viaje.
@app.post("/trips")
def create_trip(trip: dict):

    # Agrega viaje a la lista.
    trips.append(trip)

    return {
        "message": "Trip created successfully",
        "trip": trip
    }