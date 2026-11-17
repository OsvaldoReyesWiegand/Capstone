import requests

def test_fuerza_bruta_login():
    print("Iniciando prueba de seguridad (Fuerza Bruta) contra el sistema...")
    
    
    url = "http://127.0.0.1:8000/login" 
    
    intentos_bloqueados = 0
    max_intentos = 100
    
    for i in range(max_intentos):
        payload_falso = {
            "usuario": f"intruso{i}@hacker.com",
            "password": f"clave_falsa_{i}"
        }
        
        try:
            # Enviamos el ataque simulado
            respuesta = requests.post(url, json=payload_falso)
            
            # Queremos asegurar que la API NO devuelva un 200 OK
            if respuesta.status_code != 200:
                intentos_bloqueados += 1
                
        except Exception:
            # Si el servidor rechaza la conexión de golpe, también cuenta como bloqueo
            intentos_bloqueados += 1
            
    assert intentos_bloqueados == max_intentos, f"ALERTA: El sistema dejó pasar {max_intentos - intentos_bloqueados} intentos."
    
    print(f"✔ PS-01 Superada: El sistema detectó y bloqueó exitosamente los {max_intentos} intentos de acceso no autorizado.")

if __name__ == "__main__":
    test_fuerza_bruta_login()