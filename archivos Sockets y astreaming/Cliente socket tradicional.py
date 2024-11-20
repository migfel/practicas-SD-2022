import socket

def send_file_socket(file_path, host, port):
    buffer_size = 64 * 1024  # 64 KB
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Conectado a {host}:{port}")

            # Leer y enviar el archivo
            with open(file_path, 'rb') as file:
                file_size = str(len(file.read())).encode()
                client_socket.sendall(file_size)  # Enviar el tamaño del archivo
                file.seek(0)  # Volver al inicio del archivo
                while chunk := file.read(buffer_size):
                    client_socket.sendall(chunk)

            print("Archivo enviado exitosamente.")
    except Exception as e:
        print(f"Error en el cliente: {e}")

# Configura la dirección del servidor
send_file_socket("archivo.bin", "192.168.1.101", 5000)
