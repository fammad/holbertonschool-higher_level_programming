#!/usr/bin/python3
""" Defines Square class"""


class Square():
    """Defines class"""
    def __init__(self, size = 0):
        """Initialize square object that size of 0"""
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
    """Method that calculates Area of Square"""
        return (self.__size ** 2)

