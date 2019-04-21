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
    tree = get_tree_of_xml_file(input_xml_file)
    root = tree.getroot()
    child = root[index_of_child]
    data_from_csv = read_csv(input_csv_file)

    for previous_value_from_xml in child:
        for new_value_from_csv in data_from_csv:
            if previous_value_from_xml.tag == new_value_from_csv[0]:
                previous_value_from_xml.text = new_value_from_csv[1]

    tree.write(output_xml_file)

    tree.write(output_xml_file, xml_declaration=True, encoding='UTF-8')

    xml_to_json(output_xml_file, output_json_file)

    json_to_xml(output_json_file, output_json_to_xml_file)


if __name__ == "__main__":
    main()
