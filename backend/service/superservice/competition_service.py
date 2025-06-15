import base64
import json
import time

import requests
from repositories.Competition_repository import get_all_competition
from config import redis_client
from service.superservice.parse_xml import convert_xml_json

url = "https://vo-online-test.citis.ru:8100/api/token/new"
url_own = "https://vo-online-test.citis.ru:8100/api/token/own/get"


def decode_payload_base64(payload_base64):
    decoded_bytes = base64.b64decode(payload_base64)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str


def xsd_xml_schema(id_competition):
    return f'''<PackageData>
  <CompetitiveGroupList>
    <CompetitiveGroup>
      <IdObject>6050</IdObject>
      <IdCompetition>{id_competition}</IdCompetition>
    </CompetitiveGroup>
  </CompetitiveGroupList>
</PackageData>'''


token_header = {
        "Action": "GetAll",
        "Entity": "CompetitiveGroupList",
        "Ogrn": "1020502629180",
        "Kpp": "057201001"
    }

header_str = json.dumps(token_header)
token_header_base64 = base64.b64encode(header_str.encode("utf-8")).decode("utf-8")


def base64_payload(xml):
    bs = base64.b64encode(xml.encode("utf-8")).decode("utf-8")
    return bs


def generate():
    for competition in get_all_competition():
        data = {
            "payload_base64": base64_payload(xsd_xml_schema(competition.id)),
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
            print(competition.id)
            print(c)

        except Exception as e:
            return {"message_error": e}




