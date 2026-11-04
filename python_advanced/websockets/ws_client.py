#!/usr/bin/env python3
"""
Minimal WebSocket client: sends one message and prints the reply.
"""
import asyncio

import websockets

URI = "ws://localhost:8765"
MESSAGE = "Hello WebSocket"


async def connect_and_send(uri: str, text: str) -> str:
    """
    Connect to uri, send text once, receive one reply,
    close the connection and return the reply as a str. 
    """
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
    return str(response)


async def main():
    """
    Send the demo message to the echo server and print the reply.
    """
    response = await connect_and_send(URI, MESSAGE)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
