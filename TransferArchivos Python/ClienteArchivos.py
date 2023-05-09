import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('texto.txt', 'rb') as f:
        data = f.read()
    s.sendall(data)
    print('Archivo enviado')
