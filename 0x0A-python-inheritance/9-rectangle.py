#!/usr/bin/python3
"""Defines Rectangle class inheriting from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Representation of a rectangle."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()."""
        return f"[Rectangle] {self.__width}/{self.__height}"
