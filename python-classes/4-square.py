#!/usr/bin/python3
""" Defines Square class"""


class Square():
    """Defines class"""
    def __init__(self, size = 0):
        """Initialize square object that size of 0"""
        self.__size = size

    @property
    def size(self):
        """Getter method that returns private atribute __size"""
        return self.__size
    @size_setter
    def size(self, value):
        if isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
