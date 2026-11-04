#!/usr/bin/env python3
"""
WebSocket server that validates each message before responding.
"""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


def validate(message):
    """
    Return the response for a message:
    'ERR:EMPTY' if it is empty after stripping whitespace,
    otherwise 'OK:' followed by the original message.
    """
    if len(message.strip()) == 0:
        return "ERR:EMPTY"
    return f"OK:{message}"


async def connection_handler(websocket):
    """
    Validate every text message received on this connection
    and send back the result, keeping the connection open.
    """
    try:
        async for message in websocket:
            await websocket.send(validate(message))
    except ConnectionClosed:
        pass


async def main():
    """
    Start the server on localhost:8765 and keep it running.
    """
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
