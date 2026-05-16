# Usa una imagen oficial de Python versión 3.11.
FROM python:3.11

# Define la carpeta de trabajo dentro del contenedor.
# Todo se ejecutará dentro de /app.
WORKDIR /app

# Copia el archivo requirements.txt desde tu PC al contenedor.
COPY requirements.txt .

# Instala las dependencias necesarias del proyecto.
# En este caso FastAPI y Uvicorn.
RUN pip install -r requirements.txt

# Copia todos los archivos del proyecto al contenedor.
COPY . .

# Comando que inicia el microservicio.
# uvicorn ejecuta FastAPI.
#
# main:app
# -> main = archivo main.py
# -> app = objeto FastAPI()
#
# --host 0.0.0.0
# permite que el servicio sea accesible desde fuera del contenedor.
#
# --port 8000
# define el puerto del microservicio.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]