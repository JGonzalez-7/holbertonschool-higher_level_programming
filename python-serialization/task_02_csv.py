#!/usr/bin/env python3
"""
Convert CSV data into JSON format.

Reads a CSV file using DictReader,
converts rows into dictionaries,
and writes the data to data.json.

Returns:
    True if successful
    False if an error occurs
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file data into JSON format and save to data.json.

    Args:
        filename (str): Path to the input CSV file.

    Returns:
        bool: True if conversion successful, False otherwise.
    """
    try:
        data_list = []

        with open(filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error):
        return False
