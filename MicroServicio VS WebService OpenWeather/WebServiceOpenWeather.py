from flask import Flask, jsonify #
import requests #Importamos las bibliotecas necesarias:



app = Flask(__name__)# Creamos una instancia de la aplicación Flask:

city = 'Mexico'  #Nombre de la Ciudad donde quieres saber la temperatura

@app.route('/temperatura')# Definimos una ruta /temperatura 
#utilizando el decorador @app.route. Cuando se acceda a esta ruta, se ejecutará la función get_temperature:



def get_temperatura():
    api_key = ''  # ITU API KEY  OpenWeatherMap 
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric' #Construimos la URL de la API de OpenWeatherMap 
    #utilizando la clave de la API y el nombre de la ciudad:

    response = requests.get(url)# Realizamos una solicitud GET a la URL de la API utilizando la biblioteca requests:

    data = response.json()#Extraemos los datos JSON de la respuesta:


    
    temperatura = data['main']['temp'] #Obtenemos la temperatura actual de los datos utilizando la estructura de los datos JSON devueltos por la API de OpenWeatherMap:


    return jsonify({'la temperatura es': data}) #Devolvemos la temperatura como una respuesta JSON utilizando jsonify de Flask:


#Pverificamos si el archivo está siendo ejecutado directamente y luego ejecutamos la aplicación Flask:


if __name__ == '__main__':
    app.run()
 
