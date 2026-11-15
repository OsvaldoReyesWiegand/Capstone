from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime

app = FastAPI(title="API Predictiva - Capstone", description="Lógica de reabastecimiento textil")

# Cargar el modelo de Inteligencia Artificial entrenado
try:
    modelo_rf = joblib.load('modelo_random_forest.joblib')
except:
    print("Atención: No se encontró el archivo del modelo. Ejecute entrenamiento_ml.py primero.")

class SolicitudPrediccion(BaseModel):
    categoria: str
    mes_futuro: int
    stock_actual: int

@app.post("/calcular_compras/")
def calcular_reabastecimiento(datos: SolicitudPrediccion):
    
    # 1. Preparar los datos tal como los aprendió la IA
    # El modelo espera ver: Mes, Dia, Categoria_Pantalones, Categoria_Poleras, Categoria_Polerones, Categoria_Zapatillas
    
    # Iniciamos todas las categorías en 0
    cat_pantalones = 0
    cat_poleras = 0
    cat_polerones = 0
    cat_zapatillas = 0
    
    # Activamos con 1 solo la categoría que pidió el cliente
    categoria_solicitada = datos.categoria.capitalize()
    if categoria_solicitada == "Pantalones": cat_pantalones = 1
    elif categoria_solicitada == "Poleras": cat_poleras = 1
    elif categoria_solicitada == "Polerones": cat_polerones = 1
    elif categoria_solicitada == "Zapatillas": cat_zapatillas = 1

    # Construimos la fila matemática para la IA (asumiendo día 1 del mes para la proyección)
    datos_entrada = pd.DataFrame([{
        "Mes": datos.mes_futuro,
        "Dia": 1,
        "Categoria_Pantalones": cat_pantalones,
        "Categoria_Poleras": cat_poleras,
        "Categoria_Polerones": cat_polerones,
        "Categoria_Zapatillas": cat_zapatillas
    }])

    # 2. Ejecutar la Predicción Real
    prediccion_ia = int(modelo_rf.predict(datos_entrada)[0])

    # 3. Lógica de Reabastecimiento
    cantidad_a_comprar = prediccion_ia - datos.stock_actual
    
    if cantidad_a_comprar < 0:
        cantidad_a_comprar = 0
        alerta = "Sobrestock: No requiere compras."
    elif cantidad_a_comprar == 0:
        alerta = "Stock equilibrado."
    else:
        alerta = f"Stock Crítico: Comprar {cantidad_a_comprar} unidades."

    return {
        "categoria_analizada": datos.categoria,
        "mes_proyectado": datos.mes_futuro,
        "demanda_predicha_ia": prediccion_ia,
        "stock_en_bodega": datos.stock_actual,
        "sugerencia_compra": cantidad_a_comprar,
        "estado_alerta": alerta
    }