#!/usr/bin/python3
"""Function to check if an object is an instance or subclass."""


def is_kind_of_class(obj, a_class):
    """
    Determine if obj is an instance or subclass of a_class.

    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance,False otherwise.
    """
    return isinstance(obj, a_class)
