# Sistema de Monitoreo y Análisis de Viajes

Proyecto académico basado en arquitectura de microservicios para la gestión y monitoreo de viajes utilizando tecnologías modernas de backend, contenedores y observabilidad.

---

# Tecnologías Utilizadas

- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- Prometheus
- Grafana
- Apache Spark
- PySpark

---

# Arquitectura del Proyecto

El sistema está compuesto por tres microservicios principales:

## user-service
Gestiona usuarios del sistema.

## trip-service
Gestiona viajes y registros de movilidad.

## analytics-service
Realiza análisis de datos usando Apache Spark y expone métricas analíticas.

---

# Estructura del Proyecto

```text
Sistema-monitoreo-y-analisis-viajes/
│
├── microservices/
│   ├── user-service/
│   ├── trip-service/
│   └── analytics-service/
│
├── monitoring/
│   └── prometheus.yml
│
├── analytics/
│   ├── dataset/
│   └── spark-job.py
│
├── docs/
│
├── docker-compose.yml
│
├── README.md
│
└── .gitignore
```

---

# Ejecución del Proyecto

## Construir y levantar contenedores

```bash
docker compose up --build
```

---

# Servicios Disponibles

## User Service

http://localhost:8000

### Endpoints

- GET /users
- POST /users
- GET /metrics

---

## Trip Service

http://localhost:8001

### Endpoints

- GET /trips
- POST /trips
- GET /metrics

---

## Analytics Service

http://localhost:8002

### Endpoints

- GET /analytics/summary
- GET /metrics

---

# Herramientas de Monitoreo

## Prometheus

http://localhost:9090

Prometheus recolecta métricas de los microservicios.

---

## Grafana

http://localhost:3000

Grafana permite visualizar dashboards y métricas en tiempo real.

### Credenciales por defecto

- Usuario: admin
- Contraseña: admin

---

# Métricas Monitoreadas

- Total de requests HTTP
- Tiempo de respuesta
- Uso de memoria
- Métricas de procesos Python
- Estado de servicios

---

# Docker Containers

El sistema utiliza los siguientes contenedores:

- postgres-db
- user-service
- trip-service
- analytics-service
- prometheus
- grafana

---

# Funcionalidades Implementadas

- Arquitectura basada en microservicios
- Persistencia de datos con PostgreSQL
- Contenedores Docker
- Comunicación entre servicios
- Métricas Prometheus
- Dashboards Grafana
- Procesamiento analítico con Spark

---

# Evidencias

Las evidencias del funcionamiento del sistema se encuentran en la carpeta:

```text
docs/
```

---

# Autor

Proyecto desarrollado para la asignatura de Redes e Infraestructura.