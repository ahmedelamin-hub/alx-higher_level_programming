#!/usr/bin/python3
"""Defines an objec function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj (object): The object to look up attributes and methods for.

    Returns:
    list: A list of strings, each string being an attribute or method name.
    """
    return dir(obj)
