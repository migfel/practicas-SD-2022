import socket
import requests

def obtener_clima(ciudad):
    api_key = 'tu_api_key_de_OpenWeatherMap'  # Reemplaza con tu API Key de OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    response = requests.get(url)
    datos_clima = response.json()
    return datos_clima['weather'][0]['description']

def servidor_openweather():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 8000))
    servidor.listen(1)

    print("Servidor OpenWeather iniciado en el puerto 8000...")

    while True:
        conn, addr = servidor.accept()
        print(f"Conexión establecida desde {addr}")

        ciudad = conn.recv(1024).decode()
        clima = obtener_clima(ciudad)
        conn.send(clima.encode())

        conn.close()

if __name__ == "__main__":
    servidor_openweather()
