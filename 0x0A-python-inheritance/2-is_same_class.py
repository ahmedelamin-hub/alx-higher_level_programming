#!/usr/bin/python3
"""Defines a function that checks an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Check if an object is exaxtly of the specified class.

    Args:
    obj (object): The object to check.
    a_class (type): The class to match the type of obj.

    Returns:
    bool: True otherwise False.
    """
    return type(obj) is a_class
