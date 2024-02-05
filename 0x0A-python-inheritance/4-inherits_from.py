#!/usr/bin/python3
"""Function to check object inheritance."""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a subclass of a_class.

    Args:
    obj: The object to check.
    a_class: The reference class.

    Returns:
    True if obj is an instance of a subclass False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
