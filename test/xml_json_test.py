import os

from src.xml_lib import *


def test_if_input_xml_file_exist():
    assert os.path.isfile(os.path.abspath(input_xml_file)) is True


def test_if_input_xml_file_has_correct_structure():
    assert validate(input_xml_file, input_xsd_file) is True


def test_if_output_xml_file_exist():
    assert os.path.isfile(os.path.abspath(output_xml_file)) is True


def test_if_output_xml_file_has_correct_structure():
    assert validate(output_xml_file, input_xsd_file) is True


def test_if_output_json_file_exist():
    assert os.path.isfile(os.path.abspath(output_json_file)) is True


def test_if_json_file_content_is_correct():
    assert compare_xml(output_xml_file, output_json_to_xml_file) is ''
