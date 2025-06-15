import os
from datetime import datetime
import requests
import xmltodict
from config import redis_client
from .parse_xml import convert_xml_json
from repositories.Direction_repository import get_add_directions_bulk
from repositories.EducationLevel_repository import get_add_education_level_bulk
from repositories.Competition_status_repository import add_status_competition

url = "https://vo-online-test.citis.ru:8100/api/cls/get"
headers = {
    "Content-Type": "application/json",
    "Session-Key": redis_client.get("session-key")
}


def cls_get(cls):
    data = {
        "ogrn": "1020502629180",
        "kpp": "057201001",
        "cls": cls
    }
    response = requests.post(url, headers=headers, json=data, verify=False)

    xml_dict = xmltodict.parse(response.text)

    if cls == "DirectionCls":
        get_add_directions_bulk(xml_dict['PackageData']['DirectionCls'])
        return {"message": "success"}

    if cls == 'EducationLevelCls':
        get_add_education_level_bulk(xml_dict['PackageData']['EducationLevelCls'])
        return {"message": "success"}

    if cls == 'CompetitiveGroupStatusCls':
        add_status_competition(xml_dict['PackageData']['CompetitiveGroupStatusCls'])

    return xml_dict

