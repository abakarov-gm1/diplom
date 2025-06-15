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
    return get_all_entrant()


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
# manager2 = ConnectionManager()
#

@app.websocket("/ws/{chat_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int, token: str):
    await manager.connect(websocket)

    try:

        groups = abakarov()
        entrant = get_all_entrant()
        is_russian = 0
        is_english = 0

        for i in entrant:
            if i.snils == 'true':
                is_russian += 1
            else:
                is_english += 1

        # data = [
        #     {
        #         "id": item.id,
        #         "comment": item.comment,
        #         "number_places": item.number_places,
        #         "count_pod": len(item.groups),
        #         "zach_pod": 0,
        #         "all_count_entrant": len(entrant),
        #         "all_count_russian": is_russian,
        #         "all_count_english": is_english
        #     }
        #     for item in groups]
        data = []

        all_number_places = 0
        all_applications = 0
        all_status_enrolled = 0
        all_status_refusal = 0
        count_egpy = 0
        count_not_egpy = 0

        for item in groups:
            all_number_places += item.number_places
            all_applications += len(item.groups)

            if type(item.groups) is list:
                for group in item.groups:
                    if group.is_ovo:
                        count_egpy += 1
                    elif group.is_ovo is False:
                        count_not_egpy += 1

                    if group.status_id == 19:
                        all_status_enrolled += 1
                    elif group.status_id in [15, 14, 10, 12]:
                        all_status_refusal += 1

            elif type(item.groups) is dict:
                if item.is_ovo:
                    count_egpy += 1
                elif item.is_ovo is False:
                    count_not_egpy += 1

                if item.status_id == 19:
                    all_status_enrolled += 1
                elif item.status_id in [15, 14, 10, 12]:
                    all_status_refusal += 1

            data.append(
                {
                    "id": item.id,
                    "comment": item.comment,
                    "number_places": item.number_places,
                    "count_pod": len(item.groups),
                    "zach_pod": 0,
                    "all_count_entrant": len(entrant),
                    "all_count_russian": is_russian,
                    "all_count_english": is_english,
                    "all_number_places": all_number_places,
                    "all_applications": all_applications,
                    "all_status_refusal": all_status_refusal,
                    "all_status_enrolled": all_status_enrolled,
                    "count_not_egpy": count_not_egpy,
                    "count_egpy": count_egpy
                }
            )

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

