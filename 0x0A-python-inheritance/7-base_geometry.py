#!/usr/bin/python3
"""BaseGeometry class with methods."""


class BaseGeometry:
    """Class with area method and integer validation."""

    def area(self):
        """Raise exception for unimplemented method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value as positive integer.
        Raises TypeError or ValueError on failure.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
