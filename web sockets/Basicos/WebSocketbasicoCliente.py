import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hola, servidor!")
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(hello())
