import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
from tkinter import messagebox

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

def search_and_display():
    query = entry.get()
    track_name = search_song(query)
    messagebox.showinfo("Canción encontrada", f"La primera canción encontrada es: {track_name}")

# Crear la ventana principal
root = tk.Tk()
root.title("Buscar canción")

# Crear y posicionar la etiqueta
label = tk.Label(root, text="Introduce el nombre de la canción:")
label.pack()

# Crear y posicionar la entrada de texto
entry = tk.Entry(root)
entry.pack()

# Crear y posicionar el botón de búsqueda
search_button = tk.Button(root, text="Buscar", command=search_and_display)
search_button.pack()

# Ejecutar el bucle de eventos de la ventana
root.mainloop()
