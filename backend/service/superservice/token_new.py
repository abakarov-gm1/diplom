import json
import os
import sys
import base64
import time

import requests
import urllib3

from .application import get_full_applications
from repositories.Competition_repository import add_competition_bulk

from repositories.entrant_repository import add_all_entrant
from repositories.application_repositories import add_applications_from_super_service
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# from new_session import session_key
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from repositories.entity_repository import EntityRepository
from config import redis_client
from .parse_xml import convert_xml_json

url = "https://vo-online-test.citis.ru:8100/api/token/new"
url_own = "https://vo-online-test.citis.ru:8100/api/token/own/get"


def get_payload(action, entity_object):
    for i in entity_object.actions:
        if i.action == action:
            bs = base64.b64encode(i.payload.encode("utf-8")).decode("utf-8")
            return bs


def decode_payload_base64(payload_base64):
    decoded_bytes = base64.b64decode(payload_base64)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str


def get_xml_entity(action: str, entity: str, flag):
    j = EntityRepository()
    entity_object = j.get_entity(entity)

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

    try:
        own_data = response.json()
        own_d = {"IdJwt": own_data["IdJwt"]}

        time.sleep(own_data["DelaySeconds"])

        resp_own = requests.post(url_own, headers=headers, json=own_d, verify=False)

        if resp_own == {}:
            return "Данных нет"

        r = resp_own.json()

        payload_base = r["payload_base64"]

        c = convert_xml_json(decode_payload_base64(payload_base))

        if entity == "ApplicationList" and flag:
            add_applications_from_super_service(c["SuccessResultList"]['Application'])
            return {"Message": "success"}

        if entity == "ApplicationList" and flag and action == "GetDirect":
            get_full_applications(c["SuccessResultList"]['Application'])
            return {"Message": "success"}

        if entity == "CompetitionList" and flag:
            add_competition_bulk(c['SuccessResultList']['Competition'])
            return {"Message": "success"}

        if entity == "EntrantList" and flag:
            add_all_entrant(c['SuccessResultList']['Entrant'])

        return c

    except Exception as e:
        return {"message_error": e}


