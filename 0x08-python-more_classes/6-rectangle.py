#!/usr/bin/python3
"""Module for the Rectangle class definition."""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Parameters:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle's width.

        Parameters:
            value (int): The width value.

        Raises:
            TypeError: If width isn't an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the rectangle's height.

        Parameters:
            value (int): The height value.

        Raises:
            TypeError: If height isn't an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the rectangle's perimeter.

        Returns:
            Zero if width or height is zero, else the perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle with '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """String representation for recreating the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
