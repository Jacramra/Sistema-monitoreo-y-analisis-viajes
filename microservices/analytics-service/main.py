# ==========================================================
# IMPORTAR FASTAPI
# ==========================================================

from fastapi import FastAPI

# ==========================================================
# IMPORTAR PROMETHEUS
# ==========================================================

from prometheus_fastapi_instrumentator import Instrumentator

# ==========================================================
# IMPORTAR SPARK
# ==========================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# ==========================================================
# CREAR APP FASTAPI
# ==========================================================

app = FastAPI()

# ==========================================================
# ACTIVAR MÉTRICAS
# ==========================================================

Instrumentator().instrument(app).expose(app)

# ==========================================================
# ENDPOINT PRINCIPAL
# ==========================================================

@app.get("/")
def home():

    return {
        "message": "Analytics Service Running"
    }

# ==========================================================
# ENDPOINT ANALÍTICO
# ==========================================================

@app.get("/analytics/summary")
def analytics_summary():

    # Crear sesión Spark.
    spark = SparkSession.builder \
        .appName("Analytics Service") \
        .getOrCreate()

    # Leer dataset CSV.
    df = spark.read.csv(
        "../../analytics/dataset/trips_data.csv",
        header=True,
        inferSchema=True
    )

    # ======================================================
    # MÉTRICAS
    # ======================================================

    total_trips = df.count()

    avg_price = df.select(
        avg("price")
    ).collect()[0][0]

    city_data = (
        df.groupBy("city")
        .count()
        .collect()
    )

    cities = []

    for row in city_data:

        cities.append({
            "city": row["city"],
            "trips": row["count"]
        })

    spark.stop()

    return {

        "total_trips": total_trips,

        "average_price": avg_price,

        "trips_by_city": cities
    }