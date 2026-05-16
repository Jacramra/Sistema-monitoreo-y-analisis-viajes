# Importa FastAPI para crear APIs y microservicios.
from fastapi import FastAPI

# Crea la aplicación FastAPI.
app = FastAPI()

# Lista temporal donde se almacenarán usuarios.
# Por ahora no usamos base de datos.
users = []

# Endpoint principal para verificar que el servicio funciona.
@app.get("/")
def home():

    # Retorna un mensaje simple.
    return {"message": "User Service Running"}

# Endpoint para obtener todos los usuarios registrados.
@app.get("/users")
def get_users():

    # Retorna la lista completa de usuarios.
    return users

# Endpoint para crear un nuevo usuario.
@app.post("/users")
def create_user(user: dict):

    # Agrega el usuario recibido a la lista.
    users.append(user)

    # Retorna mensaje de éxito y datos del usuario.
    return {
        "message": "User created successfully",
        "user": user
    }