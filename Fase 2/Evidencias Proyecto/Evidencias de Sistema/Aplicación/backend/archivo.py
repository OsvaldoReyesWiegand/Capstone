import pandas as pd

def limpiar_datos(ruta_archivo):
    # 1. Extraer
    df = pd.read_csv(ruta_archivo)
    total_inicial = len(df)
    
    # 2. Transformar (Limpieza)
    # Eliminar filas con valores nulos
    df_limpio = df.dropna(subset=['Cantidad']).copy()
    
    # Convertir negativos a positivos (asumiendo error de tipeo)
    df_limpio['Cantidad'] = df_limpio['Cantidad'].abs()
    
    # Eliminar outliers absurdos (ej. más de 500 unidades en un día normal)
    df_limpio = df_limpio[df_limpio['Cantidad'] < 500]
    
    total_final = len(df_limpio)
    registros_corregidos = total_inicial - total_final
    
    # 3. Cargar (Exportar)
    df_limpio.to_csv('ventas_limpio_sql.csv', index=False)
    
    return total_inicial, registros_corregidos, total_final

if __name__ == "__main__":
    inicial, corregidos, final = limpiar_datos('ventas_cliente_sucio.csv')
    print(f"ETL Finalizado. Iniciales: {inicial} | Descartados/Corregidos: {corregidos} | Finales: {final}")