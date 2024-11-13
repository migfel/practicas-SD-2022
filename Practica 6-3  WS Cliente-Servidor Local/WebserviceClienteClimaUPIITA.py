import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:8080'

def obtener_temperatura(pais):
    url = f'{url_base}/temperature/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Temperatura en {pais}: {data["temperature"]:.2f}°C'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso
paises = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]
for pais in paises:
    resultado = obtener_temperatura(pais)
    print(resultado)
