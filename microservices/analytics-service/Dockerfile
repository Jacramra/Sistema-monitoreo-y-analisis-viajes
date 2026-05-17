# Imagen Python.
FROM python:3.11

# Carpeta trabajo.
WORKDIR /app

# Copiar requirements.
COPY requirements.txt .

# Instalar dependencias.
RUN pip install -r requirements.txt

# Copiar archivos.
COPY . .

# Ejecutar FastAPI.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]