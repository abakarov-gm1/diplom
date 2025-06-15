import asyncio
import base64
import json
import time
import httpx
from repositories.Competition_repository import get_all_competition
from config import redis_client
from service.superservice.parse_xml import convert_xml_json

from repositories.CompetitionGroup_repository import get_competition_group_id_array, add_group_competition

url = "https://vo-online-test.citis.ru:8100/api/token/new"
url_own = "https://vo-online-test.citis.ru:8100/api/token/own/get"


def decode_payload_base64(payload_base64: str) -> str:
    decoded_bytes = base64.b64decode(payload_base64)
    return decoded_bytes.decode('utf-8')


def xsd_xml_schema(id_competition: int) -> str:
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


def base64_payload(xml: str) -> str:
    return base64.b64encode(xml.encode("utf-8")).decode("utf-8")


async def generate():
    async with httpx.AsyncClient(verify=False) as client:
        cg_all = get_competition_group_id_array()
        for competition in get_all_competition():

            if competition.id in cg_all:
                continue

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

            try:
                # Первый запрос
                response = await client.post(url, headers=headers, json=data)
                response.raise_for_status()
                own_data = response.json()

                # Ожидание перед вторым запросом
                await asyncio.sleep(own_data["DelaySeconds"])

                # Второй запрос
                own_d = {"IdJwt": own_data["IdJwt"]}
                resp_own = await client.post(url_own, headers=headers, json=own_d)
                resp_own.raise_for_status()

                r = resp_own.json()
                if not r:
                    print(f"Для конкурса {competition.id} данных нет")
                    continue

                payload_base = r["payload_base64"]
                decoded_data = decode_payload_base64(payload_base)
                c = convert_xml_json(decoded_data)

                print(competition.id)
                print(c)

                if c.get("SuccessResultList") is None:
                    continue

                cg = c["SuccessResultList"]["CompetitiveGroup"]
                if type(cg) is list:
                    for i in cg:
                        add_group_competition(
                            competition_id=i['IdCompetition'],
                            application_id=i['IdApplication'],
                            direction_id=i['IdDirection'],
                            status_id=i['IdStatus'],
                            is_ovo=True if i.get('IsOovo', '') == 'true' else False,
                            education_form_id=i['IdEducationForm'],
                            place_type_id=i['IdPlaceType']
                        )

                elif type(cg) is dict:
                    add_group_competition(
                        competition_id=cg['IdCompetition'],
                        application_id=cg['IdApplication'],
                        direction_id=cg['IdDirection'],
                        status_id=cg['IdStatus'],
                        is_ovo=True if cg.get('IsOovo', '') == 'true' else False,
                        education_form_id=cg['IdEducationForm'],
                        place_type_id=cg['IdPlaceType']
                    )

            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred for competition {competition.id}: {e}")
            except Exception as e:
                print(f"Error processing competition {competition.id}: {e}")



