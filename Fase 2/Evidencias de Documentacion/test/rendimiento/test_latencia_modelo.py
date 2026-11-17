import time
import joblib
import pandas as pd
import os

def test_latencia_ia():
    print("Iniciando prueba de rendimiento del modelo Random Forest...")
    
    # Sube dos carpetas hasta la raíz del proyecto
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_modelo = os.path.join(directorio_actual, '..', '..', 'modelo_random_forest.joblib')
    ruta_modelo = os.path.abspath(ruta_modelo)
    
    assert os.path.exists(ruta_modelo), f"ERROR: El archivo .joblib no existe en {ruta_modelo}"
    
    modelo = joblib.load(ruta_modelo)
    
    # Matriz de prueba
    datos_entrada = pd.DataFrame([{
        "Mes": 12, "Dia": 1,
        "Categoria_Pantalones": 0, "Categoria_Poleras": 0,
        "Categoria_Polerones": 0, "Categoria_Zapatillas": 1
    }])
    
    inicio = time.time()
    _ = modelo.predict(datos_entrada)
    fin = time.time()
    
    latencia = fin - inicio
    
    assert latencia < 1.0, f"Error: La latencia es demasiado alta ({latencia} segundos)."
    
    print(f"✔ PR-01 Superada: El modelo procesó la matriz en {latencia:.4f} segundos (Cumple SLA < 1s).")

if __name__ == "__main__":
    test_latencia_ia()