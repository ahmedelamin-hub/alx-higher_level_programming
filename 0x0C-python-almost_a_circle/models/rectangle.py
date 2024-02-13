#!/usr/bin/python3
"""Module for Rectangle class."""


from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle that inherits Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
            x (int, optional): The x coordinate
            y (int, optional): The y coordinate
            id (int, optional): The id of the object
        Raises:
            TypeError: width,height not an int.
            ValueError: If width or height <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise Typeerror("width must be an integer")
        if <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise Typeerror("height must be an integer")
        if value <= 0:
            raise Valuerror("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise Typeerror("x must be an integer")
        if value <= 0:
            raise Valueerror("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise Typeerror("y must be an integer")
        if value <= 0:
            raise Valueerror("y must be > 0")
        self.__y = value
