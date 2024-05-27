import socket

def cliente_geonames(lugar):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 9000))

    cliente.send(lugar.encode())
    descripcion = cliente.recv(1024).decode()
    print(f"Descripción de {lugar}: {descripcion}")

    cliente.close()

if __name__ == "__main__":
    lugar = input("Ingrese el nombre del lugar para obtener la descripción: ")
    cliente_geonames(lugar)
