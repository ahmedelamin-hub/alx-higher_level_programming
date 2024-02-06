#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys

def append_new_items(file_name, new_items):
    """Appends new items to the list stored in the specified file."""
    current_items = load_list_from_file(file_name)
    current_items.extend(new_items)
    save_to_json_file(current_items, file_name)

def load_list_from_file(file_name):
    """Loads a list from a file, returning an empty list if the file doesn't exist."""
    try:
        return load_from_json_file(file_name)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    new_items = sys.argv[1:]
    append_new_items("add_item.json", new_items)
