import asyncio
import websockets

async def connect_to_server():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to the server!")
        while True:
            message = input("Enter a message to send to the server: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Response from server: {response}")

if __name__ == "__main__":
    asyncio.run(connect_to_server())
