#!/usr/bin/python3
"""2-square.py Defines a Square class with size atributes"""


class Square():
    """This Class represent a Square with fixed size
    Atributes:
    __size(int) - size of Square which initialized as 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
