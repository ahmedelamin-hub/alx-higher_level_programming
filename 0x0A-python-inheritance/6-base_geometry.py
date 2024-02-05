#!/usr/bin/python3
"""Defines the class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Class with unimplemented area method."""

    def area(self):
        """Raises an exception with a message."""
        raise Exception("area() is not implemented")
