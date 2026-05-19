# ==========================================================
# IMPORTA FASTAPI
# ==========================================================

from fastapi import FastAPI

# ==========================================================
# IMPORTA FUNCIONES DE SPARK
# ==========================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# ==========================================================
# CREA LA API
# ==========================================================

app = FastAPI()

# ==========================================================
# CREA SESIÓN SPARK
# ==========================================================

spark = SparkSession.builder \
    .appName("AnalyticsService") \
    .getOrCreate()

# ==========================================================
# DATASET DE VIAJES
# ==========================================================

data = [
    ("Cali", 12.5, 25, 18000),
    ("Bogota", 20.0, 40, 35000),
    ("Medellin", 8.0, 15, 12000),
    ("Cali", 15.0, 30, 25000),
    ("Bogota", 10.0, 18, 15000),
    ("Cali", 7.0, 12, 10000),
    ("Medellin", 22.0, 50, 42000),
    ("Bogota", 18.0, 35, 30000),
    ("Cali", 11.0, 20, 17000),
    ("Medellin", 14.0, 28, 21000)
]

# ==========================================================
# COLUMNAS DEL DATAFRAME
# ==========================================================

columns = ["city", "distance", "duration", "price"]

# ==========================================================
# CREA DATAFRAME SPARK
# ==========================================================

df = spark.createDataFrame(data, columns)

# ==========================================================
# ENDPOINT PRINCIPAL
# ==========================================================

@app.get("/")
def home():

    return {
        "message": "Analytics Service Running"
    }

# ==========================================================
# RESUMEN ANALÍTICO
# ==========================================================

@app.get("/analytics/summary")
def analytics_summary():

    # Cuenta viajes.
    total_trips = df.count()

    # Calcula promedio precio.
    average_price = df.select(avg("price")).collect()[0][0]

    # Agrupa viajes por ciudad.
    trips_by_city = (
        df.groupBy("city")
        .count()
        .collect()
    )

    # Convierte resultado a JSON.
    city_results = []

    for row in trips_by_city:

        city_results.append({
            "city": row["city"],
            "trips": row["count"]
        })

    # Retorna resultado final.
    return {
        "total_trips": total_trips,
        "average_price": average_price,
        "trips_by_city": city_results
    }