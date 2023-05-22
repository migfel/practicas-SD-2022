import json
from tabulate import tabulate

# Estructura JSON
json_data = '''
{
    "base": "stations",
    "clouds": {
        "all": 47
    },
    "cod": 200,
    "coord": {
        "lat": 15.0646,
        "lon": 120.7198
    },
    "dt": 1684785357,
    "id": 1699805,
    "main": {
        "feels_like": 32.6,
        "grnd_level": 1009,
        "humidity": 86,
        "pressure": 1010,
        "sea_level": 1010,
        "temp": 27.84,
        "temp_max": 27.84,
        "temp_min": 27.84
    },
    "name": "Mexico",
    "sys": {
        "country": "PH",
        "id": 8152,
        "sunrise": 1684790833,
        "sunset": 1684837242,
        "type": 1
    },
    "timezone": 28800,
    "visibility": 10000,
    "weather": [
        {
            "description": "scattered clouds",
            "icon": "03n",
            "id": 802,
            "main": "Clouds"
        }
    ],
    "wind": {
        "deg": 47,
        "gust": 1.98,
        "speed": 1.4
    }
}
'''

# Cargar el JSON en un diccionario
data = json.loads(json_data)

# Convertir el diccionario en una lista de tuplas para la tabla
table_data = [(key, value) for key, value in data.items()]

# Imprimir la tabla
print(tabulate(table_data, headers=["Campo", "Valor"], tablefmt="grid"))
