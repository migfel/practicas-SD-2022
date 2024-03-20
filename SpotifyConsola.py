
#El código no utiliza OAuth directamente en el sentido de que no solicita acceso a la cuenta del usuario para realizar operaciones en su nombre. 
#En su lugar, utiliza el flujo de "Credenciales del cliente" proporcionado por la API de Spotify.


#OAuth se utiliza cuando la aplicación necesita acceder a recursos protegidos en nombre de un usuario específico.
#Las "Credenciales del Cliente" se utilizan cuando la aplicación necesita acceder a recursos que no requieren la identidad específica de un usuario, como datos públicos o globales.



#Este código funciona como sigue: 
#configura las credenciales de autenticación de Spotify, crea un objeto Spotify, 
#define una función para buscar canciones en Spotify 
#y realiza una búsqueda de ejemplo de una canción con el título "Now". 
#Si se encuentra una canción, imprime su nombre.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #clase sque e utiliza para autenticar las solicitudes a la API de Spotify mediante el flujo de credenciales del cliente.

# Configura las credenciales de autenticación
client_id = ''
client_secret = ''

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)#Se crea un objeto Spotify 

def search_song(query):
    # Busca una canción
    result = sp.search(q=query, limit=1)

    # Muestra el nombre de la primera canción encontrada
    if result['tracks']['items']:
        track_name = result['tracks']['items'][0]['name']
        return track_name
    else:
        return "No se encontraron canciones con ese nombre."

if __name__ == "__main__":#Esto verifica si el script está siendo ejecutado directamente o importado como un módulo.
#Si es ejecutado directamente, se realizará una búsqueda de ejemplo de una canción con el título "Now" y se imprimirá el nombre de la canción encontrada.
    # Ejemplo de búsqueda
    query = 'Now'
    track_name = search_song(query)
    print("La primera canción encontrada es:", track_name)
