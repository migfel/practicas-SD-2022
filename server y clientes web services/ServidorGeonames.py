import socket
import requests

def obtener_descripcion_lugar(lugar):
    username = 'tu_usuario_de_Geonames'  # Reemplaza con tu nombre de usuario de Geonames
    url = f'http://api.geonames.org/wikipediaSearchJSON?q={lugar}&maxRows=1&username={username}'
    response = requests.get(url)
    datos_lugar = response.json()
    if 'geonames' in datos_lugar and datos_lugar['geonames']:
        return datos_lugar['geonames'][0]['summary']
    else:
        return "No se encontró una descripción para este lugar."

def servidor_geonames():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 9000))
    servidor.listen(1)

    print("Servidor Geonames iniciado en el puerto 9000...")

    while True:
        conn, addr = servidor.accept()
        print(f"Conexión establecida desde {addr}")

        lugar = conn.recv(1024).decode()
        descripcion = obtener_descripcion_lugar(lugar)
        conn.send(descripcion.encode())

        conn.close()

if __name__ == "__main__":
    servidor_geonames()
