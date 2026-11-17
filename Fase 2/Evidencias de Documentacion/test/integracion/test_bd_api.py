import requests

def test_conexion_api():
    print("Iniciando prueba de integración con la API Predictiva...")
    
    url = "http://127.0.0.1:8000/calcular_compras/"
    payload = {
        "categoria": "Zapatillas",
        "mes_futuro": 12,
        "stock_actual": 20
    }
    
    try:
        respuesta = requests.post(url, json=payload)
        assert respuesta.status_code == 200, f"Error HTTP: {respuesta.status_code}"
        
        datos = respuesta.json()
        assert "sugerencia_compra" in datos, "La respuesta no contiene el cálculo de la IA."
        
        print("✔ PI-01 Superada: API responde correctamente (HTTP 200) y devuelve la predicción.")
    except Exception as e:
        print(f"Error de conexión. Asegúrese de que la API esté encendida. Detalle: {e}")

if __name__ == "__main__":
    test_conexion_api()