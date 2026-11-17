# Sistema Predictivo de Demanda y Optimización de Inventario 

Este proyecto es una solución integral orientada al Edge Computing para una tienda retail textil en Viña del Mar. Utiliza Machine Learning para predecir la demanda futura de prendas basándose en el historial de ventas, optimizando el reabastecimiento de inventario y evitando el sobrestock.

##  Arquitectura del Sistema (Tech Stack)
- **Base de Datos:** SQL Server 2022 (Dockerizado)
- **Procesamiento (ETL):** Pandas y SQLAlchemy
- **Backend / API:** FastAPI + Uvicorn
- **Machine Learning:** Random Forest (Scikit-Learn + Joblib)
- **Frontend / Dashboard:** Streamlit

##  Estructura del Proyecto
El ecosistema se divide en contenedores y microservicios locales:
* `docker-compose.yml`: Orquestación del motor de base de datos.
* `src/backend/`: Scripts de limpieza ETL, entrenamiento del modelo IA (`entrenamiento_ml.py`) y la API predictiva (`api_reabastecimiento.py`).
* `src/frontend/`: Panel interactivo para el cliente (`app_web.py`) con control de acceso por sesión.

##  Despliegue Rápido (Quick Start)

1. **Clonar repositorio e instalar dependencias:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   pip install -r requirements.txt