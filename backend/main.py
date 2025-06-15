import json

from fastapi import FastAPI
from repositories.Competition_repository import abakarov
from repositories.entrant_repository import get_all_entrant
from routes.users_route import router as users_router
from routes.superservice_route import router as super_router
import os
from typing import List
from starlette.responses import HTMLResponse, JSONResponse
from fastapi import Request, HTTPException, WebSocket, WebSocketDisconnect, Header
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(users_router, prefix="/auth")
app.include_router(super_router, prefix="/super-service")


@app.get("/")
def main():
    return "Backend is working !!!"


@app.get("/entrant")
def get_entrants():
    get_all_entrant()


@app.get("/test")
def get_abakarov():
    return abakarov()


class ConnectionManager:

    def __init__(self):
        self.active_connections: List[WebSocket] = list()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_file(self, file):
        for connection in self.active_connections:
            await connection.send_bytes(file)


manager = ConnectionManager()


@app.websocket("/ws/{chat_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int, token: str):
    await manager.connect(websocket)

    try:

        groups = abakarov()

        data = [
            {
                "id": item.id,
                "comment": item.comment,
                "number_places": item.number_places,
                "count_pod": len(item.groups),
                "zach_pod": 0
            }
            for item in groups]
        await websocket.send_text(json.dumps(data))

        while True:
            try:

                data = await websocket.receive()

            except Exception as e:
                print(e, ".../disconnected")
                manager.disconnect(websocket)
                return

    except WebSocketDisconnect as e:
        print(f"Client disconnected with code: {e.code}, reason: {e.reason}")
        manager.disconnect(websocket)

    except Exception as e:
        print(e, "message.user => not found")
        manager.disconnect(websocket)
