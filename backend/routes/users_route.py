import os
from typing import Optional
from fastapi import APIRouter, UploadFile, File, Form


router = APIRouter()


@router.get("/test")
def get_user(token: str):
    return "test"



