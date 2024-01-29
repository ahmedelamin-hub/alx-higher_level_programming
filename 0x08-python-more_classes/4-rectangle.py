#!/usr/bin/python3
"""Module for the Rectangle class definition."""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Parameters:
            width (int): The width of the rectangle (defaults to 0).
            height (int): The height of the rectangle (defaults to 0).
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
            TypeError: If the width is not an integer.
            ValueError: If the width is negative.
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
            TypeError: If the height is not an integer.
            ValueError: If the height is negative.
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
            Zero if either width or height is zero,
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable representation of the Rectangle.

        Returns:
            The string representation of the rectangle using '#' characters,
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation for recreation

        Returns:
            String that can be used with eval() to create a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
