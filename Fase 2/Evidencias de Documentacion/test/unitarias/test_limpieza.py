import os
import pandas as pd

def test_dataset_sintetico():
    print("Iniciando prueba unitaria de limpieza y carga de datos...")
    
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_actual, '..', '..', 'ventas_cliente_sucio.csv')
    ruta_csv = os.path.abspath(ruta_csv)
    
    assert os.path.exists(ruta_csv), f"ERROR: El archivo CSV no se encuentra en {ruta_csv}"
    
    df = pd.read_csv(ruta_csv)
    assert not df.empty, "ERROR: El dataset está vacío."
    assert len(df) == 1000, f"ERROR: Se esperaban 1000 registros, pero hay {len(df)}."
    
    print("✔ PU-01 Superada: CSV validado correctamente con 1000 registros estructurados.")

if __name__ == "__main__":
    test_dataset_sintetico()