import asyncio
import websockets

# WebSocket Server
async def websocket_server(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {e}")

# WebSocket Client
async def websocket_client():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to server")
            while True:
                message = input("Enter a message to send to the server: ")
                if message.lower() == "exit":
                    print("Exiting...")
                    break
                await websocket.send(message)
                response = await websocket.recv()
                print(f"Response from server: {response}")
    except Exception as e:
        print(f"Error: {e}")

# Main Function to Run Server and Client
async def main():
    # Start server
    server = websockets.serve(websocket_server, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(server)

    # Run client
    await websocket_client()

if __name__ == "__main__":
    asyncio.run(main())
