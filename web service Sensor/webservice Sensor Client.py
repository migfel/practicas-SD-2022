import requests

# URL del servidor donde se ejecuta el web service
BASE_URL = "http://127.0.0.1:5000/sensor/status"

def get_sensor_data():
    try:
        # Realizar la petición GET al servidor
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            data = response.json()
            status = data.get("status")
            if status == 1:
                print("Presencia detectada!")
            else:
                print("No se detecta presencia.")
        else:
            print(f"Error al conectar al servidor: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Consultar el estado del sensor
    get_sensor_data()
