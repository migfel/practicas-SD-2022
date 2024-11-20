import socket

def receive_file_socket(host, port, save_path):
    buffer_size = 64 * 1024  # 64 KB
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"Servidor escuchando en {host}:{port}")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Conexión desde {addr}")

                # Leer tamaño del archivo
                file_size = int(conn.recv(1024).decode())
                received_size = 0

                # Recibir datos en fragmentos
                with open(save_path, 'wb') as file:
                    while received_size < file_size:
                        chunk = conn.recv(buffer_size)
                        if not chunk:
                            break
                        file.write(chunk)
                        received_size += len(chunk)

                print("Archivo recibido y guardado.")
    except Exception as e:
        print(f"Error en el servidor: {e}")

# Configuración del servidor
receive_file_socket("0.0.0.0", 5000, "archivo_recibido.bin")
