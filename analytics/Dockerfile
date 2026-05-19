# ==========================================================
# IMAGEN BASE PYTHON
# ==========================================================

# Usa Python 3.11 oficial.
FROM python:3.11

# ==========================================================
# DIRECTORIO INTERNO DEL CONTENEDOR
# ==========================================================

# Carpeta donde trabajará la app.
WORKDIR /app

# ==========================================================
# COPIA DEPENDENCIAS
# ==========================================================

# Copia requirements.txt al contenedor.
COPY requirements.txt .

# Instala librerías necesarias.
RUN pip install -r requirements.txt

# ==========================================================
# COPIA TODO EL PROYECTO
# ==========================================================

# Copia archivos de analytics.
COPY . .

# ==========================================================
# EJECUCIÓN FASTAPI
# ==========================================================

# Inicia FastAPI con Uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]