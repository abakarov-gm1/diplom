import os
from typing import Optional
from fastapi import APIRouter
from service.superservice.new_session import get_session
from config import redis_client
from service.superservice.token_new import get_xml_entity

router = APIRouter()


@router.get("/new/session")
def get_user():
    if redis_client.get("session-key") is not None:
        return redis_client.get("session-key")
    return get_session()


@router.get("/token/new")
def new_token(action: str, entity: str):
    return get_xml_entity(action, entity)


