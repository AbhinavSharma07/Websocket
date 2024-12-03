import asyncio
import websockets

async def handle_client(websocket, path):
    print("A client connected!")
    async for message in websocket:
        print(f"Received from client: {message}")
        await websocket.send(f"Echo: {message}")

start_server = websockets.serve(handle_client, "localhost", 8765)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server)
    print("Server started on ws://localhost:8765")
    asyncio.get_event_loop().run_forever()
