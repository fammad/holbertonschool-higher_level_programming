#!/usr/bin/python3
"""This creates class Square that defines a square by: (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification) """


class Square:
    """This class repesent a Square"""
    def __init__(self, size):
        self.__size = size
