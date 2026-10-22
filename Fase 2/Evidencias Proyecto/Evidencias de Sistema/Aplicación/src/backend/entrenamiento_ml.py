import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Conectar a SQL Server en Docker (Puerto 1434)
conexion_str = "mssql+pyodbc://sa:Capstone2026.Seguro!@localhost,1434/master?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(conexion_str)

print("Extrayendo datos desde SQL Server...")
df = pd.read_sql("SELECT * FROM Historial_Ventas", engine)

# 2. Ingeniería de Características (Preparar datos para la IA)
# Convertimos la fecha en variables numéricas que la IA pueda entender
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.month
df['Dia'] = df['Fecha'].dt.day

# Convertimos las categorías de texto a columnas numéricas (One-Hot Encoding)
df = pd.get_dummies(df, columns=['Categoria'])

# Separamos las variables predictoras (X) de lo que queremos predecir (y)
X = df.drop(['Fecha', 'ID_Producto', 'Cantidad'], axis=1)
y = df['Cantidad']

# 3. Entrenamiento del Modelo de Machine Learning
print("Entrenando algoritmo Random Forest...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 4. Evaluación y KPI
predicciones = modelo.predict(X_test)
error_mae = mean_absolute_error(y_test, predicciones)

print("--------------------------------------------------")
print("¡Modelo de Machine Learning entrenado con éxito!")
print(f"KPI de Precisión (MAE): {error_mae:.2f} unidades")
print("--------------------------------------------------")