#!/usr/bin/env python3
"""
WebSocket unicast server: each reply goes only to its sender.
"""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """
    Register the client, reply 'U:' + message to the sender only,
    and unregister the client when the connection ends.
    """
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():cd ~/holbertonschool-core-engineering/python_advanced/websockets
python3 -m http.server 5500
    """
    Start the server on localhost:8765 and keep it running.
    """
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
