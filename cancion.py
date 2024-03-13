import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura las credenciales de autenticación
client_id = ''
client_secret = ''

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_song(query):
    # Busca una canción
    result = sp.search(q=query, limit=1)

    # Muestra el nombre de la primera canción encontrada
    if result['tracks']['items']:
        track_name = result['tracks']['items'][0]['name']
        return track_name
    else:
        return "No se encontraron canciones con ese nombre."

if __name__ == "__main__":
    # Ejemplo de búsqueda
    query = 'Happy'
    track_name = search_song(query)
    print("La primera canción encontrada es:", track_name)
