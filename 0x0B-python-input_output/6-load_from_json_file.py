#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import sys
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)


save = __import__('5-save_to_json_file').save_to_json_file

items = load_from_json_file()

my_list = []

my_list.extend(sys.argv[1:])
