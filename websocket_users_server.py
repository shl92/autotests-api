import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"
        for i in range(1, 6):
            await websocket.send(f"{i} {response}")


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
