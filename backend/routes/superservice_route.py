import os
from typing import Optional
from fastapi import APIRouter
from service.superservice.new_session import get_session
from service.superservice.cls_data import cls_get
from config import redis_client
from service.superservice.token_new import get_xml_entity

from service.superservice.competition_service import generate

router = APIRouter()


@router.get("/new/session")
def get_user():
    if redis_client.get("session-key") is not None:
        return redis_client.get("session-key")
    return get_session()


@router.get("/token/new")
def new_token(action: str, entity: str, flag: Optional[bool] = False):
    return get_xml_entity(action, entity, flag)


@router.get("/get/cls")
def get_cls(cls: str):
    return cls_get(cls)


@router.get("/update/competition")
def update():
    return generate()



