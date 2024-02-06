#!/usr/bin/python3
"""function for JSON file-read."""
import json


def load_from_json_file(filename):
    """json that Python object from file."""
    with open(filename) as f:
        return json.load(f)
