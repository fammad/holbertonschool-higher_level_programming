#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle():
    """Rectangle class with atributes and methods"""

    def __init__(self, width=0, height=0):
        """private __width and __height atributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) != True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")        
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) != True:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
