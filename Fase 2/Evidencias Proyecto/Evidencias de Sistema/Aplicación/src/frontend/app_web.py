import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuración de la página
st.set_page_config(page_title="Sistema Predictivo - Capstone", layout="wide")

# 1. SISTEMA DE LOGIN (Cumple requisito de Seguridad PS-01)
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    # Pantalla de inicio de sesión
    st.title("🔒 Acceso Seguro - Panel Mayorista")
    st.markdown("Ingrese sus credenciales de administrador para acceder a la plataforma.")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        
        if st.button("Iniciar Sesión", type="primary", use_container_width=True):
            # Credenciales del cliente
            if usuario == "cliente" and password == "textil2026":
                st.session_state.autenticado = True
                st.rerun() # Recarga la página para mostrar el dashboard
            else:
                st.error("❌ Credenciales incorrectas. Intente nuevamente.")
else:
    # 2. EL DASHBOARD (Solo visible si el login es exitoso)
    st.title("📊 Panel Predictivo de Demanda y Reabastecimiento")
    st.markdown("Sistema integral de Inteligencia Artificial para el rubro textil en Viña del Mar.")
    
    # Botón para cerrar sesión
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
        
    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("⚙️ Configurar Proyección")
        
        # Categorías en mayúscula para que coincidan exacto con tu base de datos
        categoria = st.selectbox("Categoría de Producto", ["Polerones", "Zapatillas", "Poleras", "Pantalones"])
        mes = st.slider("Mes a proyectar (1=Ene, 12=Dic)", 1, 12, 6)
        stock = st.number_input("Stock actual en bodega", min_value=0, value=20)
        
        if st.button("Ejecutar Lógica de Reabastecimiento", type="primary"):
            url = "http://127.0.0.1:8000/calcular_compras/"
            datos = {"categoria": categoria, "mes_futuro": mes, "stock_actual": stock}
            
            try:
                respuesta = requests.post(url, json=datos)
                if respuesta.status_code == 200:
                    resultado = respuesta.json()
                    st.success("✅ Predicción completada con éxito")
                    
                    st.metric("Demanda Proyectada por IA", f"{resultado['demanda_predicha_ia']} unidades")
                    st.metric("Stock Restante", f"{resultado['stock_en_bodega']} unidades")
                    st.metric("Sugerencia de Compra", f"{resultado['sugerencia_compra']} unidades")
                    
                    if "Crítico" in resultado['estado_alerta']:
                        st.error(f"⚠️ {resultado['estado_alerta']}")
                    else:
                        st.info(f"✅ {resultado['estado_alerta']}")
                else:
                    st.error("Error al procesar los datos con la API.")
            except Exception as e:
                st.error("Error de conexión. Asegúrese de que la API esté encendida.")

    with col2:
        st.subheader(f"📈 Curva Histórica Real: {categoria}")
        st.write("Análisis extraído directamente desde el Data Warehouse (SQL Server).")
        
        try:
            # Conexión directa a tu SQL Server en Docker
            conexion_str = "mssql+pyodbc://sa:Capstone2026.Seguro!@localhost,1434/master?driver=ODBC+Driver+17+for+SQL+Server"
            engine = create_engine(conexion_str)
            
            # Consulta SQL para sumar todas las ventas de la prenda seleccionada agrupadas por mes
            query = f"""
            SELECT MONTH(Fecha) as Mes_Num, SUM(Cantidad) as Ventas_Totales 
            FROM Historial_Ventas 
            WHERE Categoria = '{categoria}' 
            GROUP BY MONTH(Fecha) 
            ORDER BY Mes_Num
            """
            df_grafico = pd.read_sql(query, engine)
            
            # Reemplazar números de mes por nombres para el gráfico
            meses_nombres = {1:'Ene', 2:'Feb', 3:'Mar', 4:'Abr', 5:'May', 6:'Jun', 7:'Jul', 8:'Ago', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dic'}
            df_grafico['Mes'] = df_grafico['Mes_Num'].map(meses_nombres)
            
            if not df_grafico.empty:
                fig = px.bar(df_grafico, x="Mes", y="Ventas_Totales", 
                             text="Ventas_Totales",
                             title=f"Volumen de ventas mensuales de {categoria}",
                             template="plotly_white")
                fig.update_traces(marker_color="#1f77b4", textposition="outside")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No hay datos históricos para esta categoría.")
                
        except Exception as e:
            st.error("Error conectando a SQL Server. Asegúrate de que Docker esté corriendo.")