import asyncio
import websockets

async def receive_mp3(websocket, path):
    try:
        with open("received_file.mp3", "wb") as file:
            while True:
                data = await websocket.recv()
                if not data:
                    break
                file.write(data)
    except websockets.exceptions.ConnectionClosed:
        pass

start_server = websockets.serve(receive_mp3, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
