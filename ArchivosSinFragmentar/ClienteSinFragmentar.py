import socket
host = '127.0.0.1'  # Cambia por la IP del servidor receptor
port = 12345          # Mismo puerto que el servidor
# Configura el socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Conectado al servidor.")
# Envía el archivo
with open("Video1.mp4", "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)
print("Archivo enviado.")
client_socket.close()
