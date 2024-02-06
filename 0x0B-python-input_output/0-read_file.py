#!/usr/bin/python3
"""
This module provides a function to read and print text
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
    filename (str): The name of the file to read.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end ="")
