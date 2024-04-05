#!/usr/bin/python3
"""A rectangle Class Module"""


class Rectangle:
    """A class with methods and attributes"""

    def __init__(self, width=0, height=0):
        """Object initializadion values"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width=value

    @property
    def height(self):
        return self.__height

    @setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height=value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width or self.height == 0:
            return 0
        else:
            return 2* (self.width+self.height)