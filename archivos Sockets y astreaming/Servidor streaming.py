import asyncio

async def send_file_streaming(file_path, host, port):
    reader, writer = await asyncio.open_connection(host, port)
    print(f"Conectado a {host}:{port}")

    try:
        with open(file_path, 'rb') as file:
            file_size = str(len(file.read())).encode()
            writer.write(file_size + b'\n')  # Enviar tamaño del archivo
            file.seek(0)  # Volver al inicio del archivo

            while chunk := file.read(64 * 1024):  # Leer en fragmentos de 64 KB
                writer.write(chunk)
                await writer.drain()  # Asegurarse de enviar datos antes de continuar

        print("Archivo enviado.")
    finally:
        writer.close()
        await writer.wait_closed()

# Configuración del cliente
asyncio.run(send_file_streaming("archivo.bin", "192.168.1.101", 5000))
