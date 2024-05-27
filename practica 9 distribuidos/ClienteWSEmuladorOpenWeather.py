import requests

def get_weather(city):
    try:
        response = requests.get(f'http://localhost:5000/weather?city={city}')
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Could not retrieve weather data"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

if __name__ == '__main__':
    city = input("Enter city name: ")
    weather = get_weather(city)
    if "error" in weather:
        print(weather["error"])
    else:
        print(f"The weather in {city} is {weather['description']} with a temperature of {weather['temperature']}°C")
