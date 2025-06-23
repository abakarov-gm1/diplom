import asyncio
import json

from fastapi import FastAPI

from repositories.application_repositories import get_all_applications
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


# @app.get('/applications')
# def get_applications():
#     return get_all_applications()


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


async def get_all_entrants():

    entrant = get_all_entrant()
    is_russian = 0
    is_english = 0

    for i in entrant:
        if i.snils == 'true':
            is_russian += 1
        else:
            is_english += 1

    return entrant, is_russian, is_english


async def get_applications():
    application = await asyncio.to_thread(get_all_applications)
    # registration_data = [{"registration_data": i.registration_date} for i in application]
    registration_data = [
        {"registration_data": i.registration_date.isoformat()}  # Преобразуем дату в строку
        for i in application
        if hasattr(i, 'registration_date') and i.registration_date is not None  # Проверяем наличие даты
    ]
    return application, registration_data


@app.websocket("/ws/{chat_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int, token: str):
    await manager.connect(websocket)

    try:
        task_entrants = asyncio.create_task(get_all_entrants())  # async
        task_groups = asyncio.to_thread(abakarov)  # sync

        entrant, is_russian, is_english = await task_entrants
        applications, registration_data = await get_applications()
        groups = await task_groups

        data_sent_frontend = []

        all_number_places = 0
        all_applications = 0
        all_status_enrolled = 0
        all_status_refusal = 0
        count_egpy = 0
        count_not_egpy = 0

        for item in groups:
            all_number_places += item.number_places
            all_applications += len(item.groups)
            zach = 0

            for group in item.groups:
                if group.is_ovo:
                    count_egpy += 1
                elif group.is_ovo is False:
                    count_not_egpy += 1

                if int(group.status_id) == 19:
                    zach += 1
                    all_status_enrolled += 1
                elif int(group.status_id) in [15, 14, 10, 12]:
                    all_status_refusal += 1

            data_sent_frontend.append(
                {
                    "id": item.id,
                    "comment": item.comment,
                    "number_places": item.number_places,
                    "count_pod": len(item.groups),
                    "zach_pod": zach,
                    "all_count_entrant": len(entrant),
                    "all_count_russian": is_russian,
                    "all_count_english": is_english,
                    "all_number_places": all_number_places,
                    "all_applications": len(applications),
                    "all_status_refusal": all_status_refusal,
                    "all_status_enrolled": all_status_enrolled,
                    "count_not_egpy": count_not_egpy,
                    "count_egpy": count_egpy
                }
            )
        response = {
            "table_data": data_sent_frontend,
            "registration_data": registration_data
        }

        await websocket.send_text(json.dumps(response))

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


