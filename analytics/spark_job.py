# ==========================================================
# IMPORTACIÓN DE SPARK
# ==========================================================

# SparkSession es el punto de entrada principal de Spark.
from pyspark.sql import SparkSession

# ==========================================================
# CREAR SESIÓN SPARK
# ==========================================================

# Inicializa aplicación Spark.
spark = SparkSession.builder \
    .appName("Trip Analytics") \
    .getOrCreate()

# ==========================================================
# CARGAR DATASET CSV
# ==========================================================

# Lee archivo CSV.
df = spark.read.csv(
    "dataset/trips_data.csv",
    header=True,
    inferSchema=True
)

# ==========================================================
# MOSTRAR DATOS
# ==========================================================

print("\nDATASET ORIGINAL:")
df.show()

# ==========================================================
# TOTAL DE VIAJES
# ==========================================================

total_trips = df.count()

print(f"\nTotal de viajes: {total_trips}")

# ==========================================================
# PROMEDIO DE PRECIO
# ==========================================================

from pyspark.sql.functions import avg

avg_price = df.select(
    avg("price")
).collect()[0][0]

print(f"\nPromedio precio: {avg_price}")

# ==========================================================
# AGRUPAR POR CIUDAD
# ==========================================================

city_stats = df.groupBy("city").count()

print("\nViajes por ciudad:")
city_stats.show()

# ==========================================================
# VIAJE MÁS COSTOSO
# ==========================================================

max_price_trip = df.orderBy(
    df.price.desc()
)

print("\nViaje más costoso:")
max_price_trip.show(1)

# ==========================================================
# FINALIZAR SPARK
# ==========================================================

spark.stop()