import os

from src.xml_lib import *


def test_if_input_xml_file_exist():
    assert os.path.isfile(os.path.abspath('samples/input/test_data.xml')) is True


def test_if_input_xml_file_has_correct_structure():
    assert validate('samples/input/test_data.xml', 'samples/input/test_data.xsd') is True


def test_if_output_xml_file_exist():
    assert os.path.isfile(os.path.abspath('samples/output/output_test_data.xml')) is True


def test_if_output_xml_file_has_correct_structure():
    assert validate('samples/output/output_test_data.xml', 'samples/input/test_data.xsd') is True


def test_if_output_json_file_exist():
    assert os.path.isfile(os.path.abspath('samples/output/output_test_data.json')) is True


def test_if_json_file_content_is_correct():
    assert compare_xml('samples/output/output_test_data.xml', 'samples/output/output_json_to_xml_test_data.xml') is ''
