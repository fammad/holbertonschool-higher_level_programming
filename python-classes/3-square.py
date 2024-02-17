#!/usr/bin/python3
"""This defines a class of Square"""


class Square():
    """Define Square Class"""
    def __init__(self, size=0):
        """Initialization values for Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defines given Square area"""
        return self.__size ** 2

