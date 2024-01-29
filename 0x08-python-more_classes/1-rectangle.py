#!/usr/bin/python3

class Rectangle:
    # Constructor method for Rectangle class with optional width and height
    def __init__(self, width=0, height=0):
        # Initialize the rectangle with provided width and height
        # The setter methods below are used for validation
        self.width = width
        self.height = height

    # Getter method for width attribute
    @property
    def width(self):
        # Returns the value of the private width attribute
        return self.__width

    # Setter method for width attribute
    @width.setter
    def width(self, value):
        # Check if the provided value is an integer
        if type(value) != int:
            raise TypeError("width must be an integer")
        # Check if the provided value is greater than or equal to 0
        if value < 0:
            raise ValueError("width must be >= 0")
        # Set the private width attribute to the provided value
        self.__width = value

    # Getter method for height attribute
    @property
    def height(self):
        # Returns the value of the private height attribute
        return self.__height

    # Setter method for height attribute
    @height.setter
    def height(self, value):
        # Check if the provided value is an integer
        if type(value) != int:
            raise TypeError("height must be an integer")
        # Check if the provided value is greater than or equal to 0
        if value < 0:
            raise ValueError("height must be >= 0")
        # Set the private height attribute to the provided value
        self.__height = value
