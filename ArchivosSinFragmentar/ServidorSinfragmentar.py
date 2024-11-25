import socket
host = '127.0.0.1' # '0.0.0.0' Escucha en todas las interfaces
port = 12345      # Puerto de escucha
# Configura el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print("Esperando conexión...")
# Acepta la conexión y recibe el archivo
conn, addr = server_socket.accept()
print(f"Conexión desde: {addr}")
with open("archivo_recibido", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)
conn.close()
print("Archivo recibido.")

