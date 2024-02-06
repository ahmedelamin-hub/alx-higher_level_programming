#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


def save_to_json_file(my_obj, filename):
    """Saves a Python object as a JSON string in a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))

def load_from_json_file(filename):
    """Loads a Python object from a JSON string in a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

if __name__ == "__main__":
    import sys
    import json
    import os

    filename = 'add_item.json'

    # Load existing list if file exists, else create new list
    if os.path.isfile(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)
