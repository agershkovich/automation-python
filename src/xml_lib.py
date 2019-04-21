import csv
import json

import xmltodict
from lxml import etree
from xmldiff import main, formatting


def get_tree_of_xml_file(input_file_path):
    return etree.parse(input_file_path)


def validate(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


def read_csv(file_path):
    with open(file_path, 'r') as data:
        csv_list = list(csv.reader(data))

    return csv_list


def xml_to_json(xml_file_path, json_file_path):
    f = open(xml_file_path)
    xml_content = f.read()
    x = xmltodict.parse(xml_content)
    j = json.dumps(x, indent=2)
    output_file = open(json_file_path, 'w')
    output_file.write(j)


def json_to_xml(json_file, xml_new_file):
    with open(json_file, 'r') as f:
        jsonString = f.read()

    xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)

    with open(xml_new_file, 'w') as f:
        f.write(xmlString)


def compare_xml(observed, expected):
    formatter = formatting.DiffFormatter()
    diff = main.diff_files(observed, expected, formatter=formatter)
    return diff


env_from_csv = read_csv('samples/input/env.csv')

input_xml_file = env_from_csv[0][1]
output_xml_file = env_from_csv[1][1]
input_csv_file = env_from_csv[2][1]
index_of_child = int(env_from_csv[3][1])
output_json_file = env_from_csv[4][1]
input_xsd_file = env_from_csv[5][1]
output_json_to_xml_file = env_from_csv[6][1]
