import requests
city = 'Mexico'  # Inserta el nombre de la ciudad de la cual se quiere saber la temperatura 

def get_temperatura():
    api_key = '152b1599f3e42d9d0f559bf3cf348a2b'  # Inserta  tu API KEY  OpenWeatherMap 
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    temperatura = data['main']['temp']
    return temperatura

if __name__ == '__main__': #Para que la aplicacion se ejecute cuando es llamada directamente, 
    #si este programa es llamado como modulo en otro programa entonces la variable __name__ no tendra el valor de main y no se ejecutara 
    temperatura = get_temperatura()
    print(f'La temperatura en la  ciudad {city} es: {temperatura}°C')
