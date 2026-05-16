# Usa imagen oficial de Python.
FROM python:3.11

# Define carpeta de trabajo.
WORKDIR /app

# Copia dependencias.
COPY requirements.txt .

# Instala librerías necesarias.
RUN pip install -r requirements.txt

# Copia todos los archivos.
COPY . .

# Ejecuta FastAPI con Uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]