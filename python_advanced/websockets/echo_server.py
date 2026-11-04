#!/usr/bin/env python3
"""
Minimal WebSocket echo server.
"""
import asyncio

import websockets


async def connection_handler(websocket):
    """
    Send back every text message received on this connection.
    """
    async for message in websocket:
        await websocket.send(message)


async def main():
    """
    Start the server on localhost:8765 and keep it running.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
