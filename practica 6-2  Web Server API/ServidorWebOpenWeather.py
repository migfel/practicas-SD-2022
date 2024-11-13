import http.server
import socketserver
import requests

# Tu API Key de OpenWeatherMap
API_KEY = "tu api "

# Función para obtener datos meteorológicos
def obtener_datos_meteorologicos(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            return f"Temperatura: {temperatura:.2f}°C<br>Condiciones Climáticas: {condiciones_climaticas}"
        else:
            return "Datos meteorológicos no disponibles."
    except Exception as e:
        return f"Error: {str(e)}"

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/weather/'):
            ciudad = self.path[9:]
            resultado = obtener_datos_meteorologicos(ciudad)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(resultado.encode())
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090 para openweathermap")
    httpd.serve_forever()
