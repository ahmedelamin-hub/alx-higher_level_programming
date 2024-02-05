#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry."""


class Rectangle(BaseGeometry):
    """A representation of a rectangle."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
