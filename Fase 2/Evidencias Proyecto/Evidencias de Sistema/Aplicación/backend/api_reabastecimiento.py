from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Predictiva - Capstone", description="Lógica de reabastecimiento textil")

# Estructura de los datos que la página web le enviará a la API
class SolicitudPrediccion(BaseModel):
    categoria: str
    mes_futuro: int
    stock_actual: int

@app.post("/calcular_compras/")
def calcular_reabastecimiento(datos: SolicitudPrediccion):
    # ---------------------------------------------------------
    # Aquí en el futuro conectaremos el modelo Random Forest real.
    # Por ahora, para el Sprint 1, simulamos la respuesta del algoritmo 
    # para armar la arquitectura y probar la Lógica de Reabastecimiento.
    # ---------------------------------------------------------
    
    # Simulación de predicción del modelo basada en el mes
    prediccion_ia = 0
    if datos.categoria.lower() == "zapatillas":
        prediccion_ia = 150 if datos.mes_futuro in [11, 12, 1, 2] else 60
    elif datos.categoria.lower() == "polerones":
        prediccion_ia = 200 if datos.mes_futuro in [5, 6, 7, 8] else 40
    else:
        prediccion_ia = 100

    # Lógica de Reabastecimiento (La regla de negocio)
    cantidad_a_comprar = prediccion_ia - datos.stock_actual
    
    # Si la cantidad es negativa (hay sobrestock), no comprar nada
    if cantidad_a_comprar < 0:
        cantidad_a_comprar = 0
        alerta = "Sobrestock: No requiere compras."
    elif cantidad_a_comprar == 0:
        alerta = "Stock equilibrado."
    else:
        alerta = f"Stock Crítico: Comprar {cantidad_a_comprar} unidades."

    # La respuesta final que la API le enviará a la página web
    return {
        "categoria_analizada": datos.categoria,
        "mes_proyectado": datos.mes_futuro,
        "demanda_predicha_ia": prediccion_ia,
        "stock_en_bodega": datos.stock_actual,
        "sugerencia_compra": cantidad_a_comprar,
        "estado_alerta": alerta
    }