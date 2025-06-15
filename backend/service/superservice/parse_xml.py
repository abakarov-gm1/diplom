import json
import xml.etree.ElementTree as Et


def xml_to_dict(elem):
    children = list(elem)
    if not children:
        return elem.text
    result = {}
    for child in children:
        key = child.tag
        value = xml_to_dict(child)
        if key in result:
            if not isinstance(result[key], list):
                result[key] = [result[key]]
            result[key].append(value)
        else:
            result[key] = value
    return result


def convert_xml_json(xml_data):
    root = Et.fromstring(xml_data)
    data_dict = xml_to_dict(root)

    json_data = json.dumps(data_dict, ensure_ascii=False, indent=2)
    data = json.loads(json_data)
    return data

