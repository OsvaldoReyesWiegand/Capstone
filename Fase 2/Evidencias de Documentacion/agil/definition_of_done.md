# Definición de Terminado (Definition of Done - DoD)

**Proyecto Capstone:** Sistema Predictivo de Demanda y Optimización de Inventario

**Empresa / Cliente:** Mundo Bags SpA

**Metodología:** Scrum (Ágil)

## Propósito

La **Definición de Terminado (DoD)** establece el conjunto riguroso de criterios de calidad, técnicos y metodológicos que una Historia de Usuario (HU) o entregable debe cumplir obligatoriamente para ser considerado oficial y formalmente como **"Terminado" (Done)** al finalizar cada Sprint. Su cumplimiento garantiza la robustez del sistema y evita deuda técnica.

## Criterios de Aceptación Globales (DoD)

Para que cualquier incremento del producto en el proyecto de Mundo Bags SpA reciba el estado de *Terminado*, debe satisfacer los siguientes pilares de calidad:

### 1. Control de Versiones e Integridad de Código (Git / GitHub)

* [ ] El código fuente asociado a la Historia de Usuario se encuentra desarrollado, probado y fusionado (**merged**) en la rama principal (`main`) o de integración del repositorio oficial de GitHub.
* [ ] No existen conflictos de integración pendientes.
* [ ] Se aplicó estrictamente el principio de menor privilegio: **ninguna credencial sensible, clave secreta o contraseña de base de datos** se encuentra hardcodeada ni expuesta en el código fuente (gestión exclusiva mediante `.env` y `.gitignore`).

### 2. Persistencia y Gestión de Datos (SQL Server sobre Docker)

* [ ] El pipeline ETL en Python (`archivo.py`) procesa el dataset histórico asegurando un **100% de integridad estructural** (eliminación de nulos y conversión de negativos a positivos mediante `abs()`).
* [ ] La carga masiva de datos (`cargar_bd.py`) migra de forma exitosa y sin pérdida de filas los registros depurados hacia el **Esquema en Estrella** de SQL Server 2022 ejecutándose en el contenedor Docker (Puerto 1434).
* [ ] Los volúmenes persistentes locales (`sqlserver_data`) se encuentran configurados correctamente en el archivo `docker-compose.yml`.

### 3. Aseguramiento de Calidad y Pruebas (QA Lead)

* [ ] Las **Pruebas Unitarias** correspondientes (ej. `PU-01` para manejo de nulos y `PU-02` para normalización) han sido ejecutadas y validadas con estado **Aprobado**.
* [ ] Las **Pruebas de Integración** (`PI-01`, `PI-02`, `PI-03`) demuestran una comunicación fluida y sin interrupciones entre el script de Python, el contenedor Docker de SQL Server y los endpoints de la API de FastAPI.
* [ ] Se cuenta con respaldos visuales de consola o capturas de terminal que validan la correcta ejecución de los scripts.

### 4. Validación Analítica y de Machine Learning

* [ ] El modelo de Machine Learning (**Random Forest Regressor**) cumple con el umbral de rendimiento establecido para el proyecto.
* [ ] El error formal de predicción ha sido medido y verificado en consola, alcanzando un **MAE (Mean Absolute Error)** $\le 25$ **unidades** (documentado formalmente en $24,11$ **unidades** por prenda).
* [ ] El archivo binario serializado (`.joblib`) se genera y carga correctamente en memoria durante la ejecución del backend.

### 5. Validación Funcional y de Negocio (UAT)

* [ ] Las interfaces gráficas interactivas desarrolladas en **Streamlit** operan sin errores de renderizado en el navegador web local (`http://localhost:8501`).
* [ ] Las reglas de negocio de reabastecimiento ($\text{Sugerencia} = \max(0, \text{Demanda Proyectada} - \text{Stock Actual})$) y las alertas visuales semaforizadas (Rojo para Stock Crítico) se calculan y visualizan de forma correcta.
* [ ] El incremento ha sido revisado y validado en las ceremonias periódicas con el equipo y representantes de **Mundo Bags SpA**.

### 6. Documentación Técnica

* [ ] La funcionalidad, script o componente desarrollado cuenta con su respectiva actualización en la documentación técnica del proyecto (Manual Técnico, Informe de Requerimientos o Documento de Arquitectura).

*Aprobado por el equipo de desarrollo para el ciclo iterativo del proyecto Capstone — Duoc UC.*