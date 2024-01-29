#!/usr/bin/python3
"""Module for the Rectangle class definition."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """Constructs a Rectangle object with specified width and height.

        Parameters:
            width (int): The initial width of the rectangle (defaults to 0).
            height (int): The initial height of the rectangle (defaults to 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Parameters:
            value (int): The value to set the width to.

        Raises:
            TypeError: Raised if the width is not an integer.
            ValueError: Raised if the width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Parameters:
            value (int): The value to set the height to.

        Raises:
            TypeError: Raised if the height is not an integer.
            ValueError: Raised if the height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            Zero if either width or height is zero"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
