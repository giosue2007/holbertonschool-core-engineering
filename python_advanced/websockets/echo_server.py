#!/usr/bin/env python3
"""WebSocket server that sends back every message it receives."""
import asyncio

import websockets


async def echo(websocket, path=None):
    """Send each message received from a client back to that client."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the server on localhost:8765 and keep it running forever."""
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
