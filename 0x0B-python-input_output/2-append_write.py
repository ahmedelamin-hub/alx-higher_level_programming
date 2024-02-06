#!/usr/bin/python3
"""
This module provides a function to append a string
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
    filename (str): The name of the file to append to.
    text (str): The text to append to the file.

    Returns:
    int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
