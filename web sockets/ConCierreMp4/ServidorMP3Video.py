import asyncio
import websockets
from websockets.exceptions import ConnectionClosedOK

async def handle_client(websocket, path, file_name):
    try:
        with open(file_name, 'wb') as file:
            while True:
                data = await websocket.recv()
                if not data:
                    break
                file.write(data)
    except ConnectionClosedOK:
        pass  # La conexión se cerró de manera ordenada

    print(f"Archivo {file_name} recibido. Conexión cerrada.")
    print("Servidor esperando conexiones...")


async def server(websocket, path):
    print(f"Conexión establecida desde: {websocket.remote_address}")

    await handle_client(websocket, path, 'archivo_video_recibido.mp4')

if __name__ == "__main__":
    start_server = websockets.serve(server, "localhost", 5555, max_size=None)

    print("Servidor esperando conexiones...")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
