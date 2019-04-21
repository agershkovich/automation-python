import os

from src.xml_lib import *


# env_from_csv = read_csv('samples/input/env.csv')
#
# input_xml_file = env_from_csv[0][1]
# output_xml_file = env_from_csv[1][1]
# input_csv_file = env_from_csv[2][1]
# index_of_child = int(env_from_csv[3][1])
# output_json_file = env_from_csv[4][1]
# input_xsd_file = env_from_csv[5][1]
# output_json_to_xml_file = env_from_csv[6][1]


def main():
    tree = get_tree_of_xml_file(os.path.isfile(os.path.abspath('samples/input/test_data.xml')))
    root = tree.getroot()
    child = root[1]
    data_from_csv = read_csv(os.path.isfile(os.path.abspath('samples/input/input_data.csv')))

    for previous_value_from_xml in child:
        for new_value_from_csv in data_from_csv:
            if previous_value_from_xml.tag == new_value_from_csv[0]:
                previous_value_from_xml.text = new_value_from_csv[1]

    tree.write(os.path.isfile(os.path.abspath('samples/output/output_test_data.xml')))

    tree.write(os.path.isfile(os.path.abspath('samples/output/output_test_data.xml')), xml_declaration=True,
               encoding='UTF-8')

    xml_to_json(os.path.isfile(os.path.abspath('samples/output/output_test_data.xml')),
                os.path.isfile(os.path.abspath('samples/output/output_test_data.json')))

    json_to_xml(os.path.isfile(os.path.abspath('samples/output/output_test_data.json')),
                os.path.isfile(os.path.abspath('samples/output/output_json_to_xml_test_data.xml')))

    if __name__ == "__main__":
        main()
