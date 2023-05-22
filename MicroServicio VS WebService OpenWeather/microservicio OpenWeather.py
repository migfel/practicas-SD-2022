import requests
city = 'Mexico'  # Inserta el nombre de la ciudad de la cual se quiere saber la temperatura 

def get_temperature():
    api_key = '152b1599f3e42d9d0f559bf3cf348a2b'  # Inserta  tu API KEY  OpenWeatherMap 
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    temperature = data['main']['temp']
    return temperature

if __name__ == '__main__':
    temperature = get_temperature()
    print(f'La temperatura en la  ciudad {city} es: {temperature}°C')
