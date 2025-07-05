import base64
import os

import requests
from config import redis_client


def encoded_data():
    file_path = os.path.join(os.path.dirname(__file__), "data.txt")
    with open(file_path, "r") as file:
        s = base64.b64encode(file.read().encode())
        return s.decode("utf-8")


def encode_signed_file_to_base64():
    file_path = os.path.join(os.path.dirname(__file__), "07_signed_data.p7s")

    with open(file_path, "rb") as file:
        file_data = file.read()
        return base64.b64encode(file_data).decode("utf-8")


encoded_signed_file_content = encode_signed_file_to_base64()
encoded_data = encoded_data()


headers = {
    "Token-header": encoded_data,
    "Content-Type": "application/json"
}

data = {
    "signature_base64": encoded_signed_file_content,
}


def get_session():
    response = requests.post(
        "https://vo-online-test.citis.ru:8100/api/session/new",
        json=data,
        headers=headers,
        verify=False
    )
    resp = response.json()
    redis_client.set("session-key", resp["Session-Key"], ex=39600)
    return resp["Session-Key"]
