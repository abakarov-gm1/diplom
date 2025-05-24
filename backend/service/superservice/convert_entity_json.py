import xml.etree.ElementTree as Et
from .parse_xml import convert_xml_json


def convert_entity_json(entity, string_convert):

    if entity in ['CompetitionList', 'DictionaryValueList', 'EducationalProgramList', 'CampaignEventList']:
        return convert_xml_json(string_convert)




