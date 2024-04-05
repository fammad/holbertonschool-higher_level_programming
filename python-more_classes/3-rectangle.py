#!/usr/bin/python3
"""A rectangle Class Module for task 3"""


class Rectangle:
    """A class with methods and attributes"""

    def __init__(self, width=0, height=0):
        """Object initializadion values"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area"""
        return self.width * self.height

    def perimeter(self):
        """Calcualates the perimeter of the object"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle based on of its width and height"""
        return ((self.width * "#" + '\n') * self.height).strip('\n')