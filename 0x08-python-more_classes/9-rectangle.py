#!/usr/bin/python3
"""Module for the Rectangle class definition."""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

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
        """String representation of the rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """String representation for recreating the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines the bigger rectangle based on the area.

        Parameters:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Returns:
            The bigger rectangle, or rect_1 if both are equal in area.

        Raises:
            TypeError: If either of rect_1 or rect_2 is not an instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width and heigh

        Parameters:
            size (int): The size of the sides of the square.

        Returns:
            A new Rectangle instance with width and height equal to size.
        """
        return cls(size, size)
