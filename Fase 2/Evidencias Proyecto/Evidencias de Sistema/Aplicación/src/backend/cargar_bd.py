import pandas as pd
from sqlalchemy import create_engine

# 1. Leer el archivo limpio que generó tu script anterior
df_limpio = pd.read_csv('ventas_limpio_sql.csv')

# 2. Configurar la conexión al SQL Server en Docker (Puerto 1434)
# Utilizamos el usuario 'sa' y la contraseña que pusiste en el docker-compose
conexion_str = (
    "mssql+pyodbc://sa:Capstone2026.Seguro!@localhost,1434/master"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

try:
    print("Conectando a la base de datos en Docker...")
    engine = create_engine(conexion_str)
    
    # 3. Subir los datos. Se creará una tabla llamada 'Historial_Ventas'
    # if_exists='replace' borrará la tabla y la creará de nuevo cada vez que ejecutes el script
    df_limpio.to_sql('Historial_Ventas', con=engine, if_exists='replace', index=False)
    
    print("¡Éxito! Los datos limpios se insertaron correctamente en SQL Server.")

except Exception as e:
    print(f"Ocurrió un error al conectar: {e}")