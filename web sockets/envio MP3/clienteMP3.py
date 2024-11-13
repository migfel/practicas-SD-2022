import asyncio
import websockets

async def send_mp3(file_path):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                await websocket.send(chunk)

asyncio.get_event_loop().run_until_complete(send_mp3("your_file.mp3"))
