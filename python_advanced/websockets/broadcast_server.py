#!/usr/bin/env python3
"""
WebSocket broadcast server: each message goes to every connected client.
"""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(text):
    """
    Send text to every connected client.
    Clients whose connection is closed are removed and skipped.
    """
    for client in list(connected_clients):
        try:
            await client.send(text)
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """
    Register the client, broadcast 'B:' + each message it sends
    to all connected clients, and unregister it when it leaves.
    """
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """
    Start the server on localhost:8765 and keep it running.
    """
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
