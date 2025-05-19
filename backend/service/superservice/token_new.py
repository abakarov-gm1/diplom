import json
import os
import sys
import base64
import requests
# from new_session import session_key
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from repositories.entity_repository import EntityRepository
from config import redis_client

url = "https://vo-online-test.citis.ru:8100/api/token/new"
url_own = "https://vo-online-test.citis.ru:8100/api/token/own/get"


# token_header = {
#     "Action": entity_object.action,
#     "Entity": entity_object.entity,
#     "Ogrn": entity_object.ogrn,
#     "Kpp": entity_object.kpp
# }
#
# header_str = json.dumps(token_header)
# token_header_base64 = base64.b64encode(header_str.encode("utf-8")).decode("utf-8")
#
#
# payload = entity_object.payload
# payload_base64 = base64.b64encode(payload.encode("utf-8")).decode("utf-8")
#
#
# headers = {
#     "accept": "application/json",
#     "Token-Header": token_header_base64,
#     "Session-Key": redis_client.get("session-key"),
#     "Content-Type": "application/json"
# }
#
# data = {
#     "payload_base64": payload_base64,
#     "signature_base64": "string"
# }
#
#
# response = requests.post(url, headers=headers, json=data, verify=False)
# own_data = response.json()


def get_payload(action, entity_object):
    for i in entity_object.actions:
        if i.action == action:
            bs = base64.b64encode(i.payload.encode("utf-8")).decode("utf-8")
            return bs


def decode_payload_base64(payload_base64):
    decoded_bytes = base64.b64decode(payload_base64)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str


def get_xml_entity(action: str, entity: str):
    j = EntityRepository()
    entity_object = j.get_entity("CompetitionList")

    token_header = {
        "Action": action,
        "Entity": entity_object.entity,
        "Ogrn": entity_object.ogrn,
        "Kpp": entity_object.kpp
    }
    header_str = json.dumps(token_header)
    token_header_base64 = base64.b64encode(header_str.encode("utf-8")).decode("utf-8")

    data = {
        "payload_base64": get_payload(action, entity_object),
        "signature_base64": "string"
    }

    headers = {
        "accept": "application/json",
        "Token-Header": token_header_base64,
        "Session-Key": redis_client.get("session-key"),
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    own_data = response.json()
    own_d = {"IdJwt": own_data["IdJwt"]}

    headers_own = {
        "accept": "application/json",
        "Session-Key": redis_client.get("session-key"),
        "Content-Type": "application/json"
    }
    resp_own = requests.post(url_own, headers=headers, json=own_d, verify=False)
    r = resp_own.json()
    payload_base = r["payload_base64"]

    return decode_payload_base64(payload_base)
