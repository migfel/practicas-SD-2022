import requests

URL = "http://127.0.0.1:8080/microsensor"

def check_sensor():
    """Consulta el estado del sensor en el servidor"""
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            status = data.get("sensor_status")
            if status == 1:
                print("Presencia detectada por el sensor.")
            else:
                print("No se detecta presencia.")
        else:
            print(f"Error: {response.status_code} al conectar con el servidor.")
    except Exception as e:
        print(f"Error al intentar acceder al servidor: {e}")

if __name__ == '__main__':
    check_sensor()
