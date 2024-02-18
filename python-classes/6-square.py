#!/usr/bin/python3
""" Defines Square class"""


class Square():
    """Defines class"""
    def __init__(self, size = 0, position=(0, 0)):
        """Initialize square object that size of 0"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method that returns private atribute __size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set value for position"""
        if not (isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], int) and value[0] >= 0
                and isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range (self.__position[1]):
                print()

            for i in range (self.size):
                for j in range (self.position):
                    print(" ", sep = "", end = "")
                for k in range (self.size):
                    print("#", sep = '', end = '')
                print()
