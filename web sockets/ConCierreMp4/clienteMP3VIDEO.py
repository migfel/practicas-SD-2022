import asyncio
import websockets

async def client(file_path, uri):
    async with websockets.connect(uri) as websocket:
        with open(file_path, 'rb') as file:
            data = file.read()
            await websocket.send(data)

if __name__ == "__main__":
    file_path = "video.mp4"
    server_uri = "ws://localhost:5555"

    asyncio.get_event_loop().run_until_complete(client(file_path, server_uri))
