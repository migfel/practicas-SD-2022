import socket

host = '127.0.0.1'  # '0.0.0.0' para escuchar en todas las interfaces
port = 12345        # Puerto de escucha

# Configura el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print("Esperando conexión...")

# Acepta la conexión y recibe el archivo
conn, addr = server_socket.accept()
client_ip = addr[0]  # IP del cliente
print(f"Conexión desde: {addr}")

# Define el nombre del archivo con la IP del cliente
file_name = f"archivo_recibido_{client_ip.replace('.', '_')}.dat"  # Reemplaza puntos en la IP por guiones bajos
print(f"Guardando archivo como: {file_name}")

# Recibe y guarda el archivo
with open(file_name, "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

conn.close()
print("Archivo recibido y renombrado correctamente.")

