import socket

def cliente_openweather(ciudad):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 8000))

    cliente.send(ciudad.encode())
    clima = cliente.recv(1024).decode()
    print(f"El clima en {ciudad} es: {clima}")

    cliente.close()

if __name__ == "__main__":
    ciudad = input("Ingrese el nombre de la ciudad para obtener el clima: ")
    cliente_openweather(ciudad)
