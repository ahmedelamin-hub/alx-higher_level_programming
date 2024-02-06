#!/usr/bin/python3
"""Funct for JSON."""
import json


def save_to_json_file(my_obj, filename):
    """JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
