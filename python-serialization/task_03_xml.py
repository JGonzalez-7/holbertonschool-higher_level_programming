#!/usr/bin/env python3
"""
XML serialization and deserialization module.

Provides:
- serialize_to_xml(dictionary, filename)
- deserialize_from_xml(filename)
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save to file.

    Args:
        dictionary (dict): Dictionary to serialize
        filename (str): Output XML file name
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)

    except (OSError, TypeError):
        return None


def deserialize_from_xml(filename):
    """
    Deserialize XML file into a Python dictionary.

    Args:
        filename (str): Input XML file name

    Returns:
        dict: Reconstructed dictionary
        None: If error occurs
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = child.text

        return result

    except (FileNotFoundError, ET.ParseError, OSError):
        return None
