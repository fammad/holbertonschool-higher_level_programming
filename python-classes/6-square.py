#!/usr/bin/python3
"""Defines Square class"""


class Square:
    """Represents a square with size and position attributes.

    Attributes:
        size (int): The size of the square (non-negative integer).
        position (tuple): The position of the square's top-left corner (x, y
                             coordinates), both of which must be non-negative integers.

    Raises:
        TypeError: If the size or any position coordinate is not an integer.
        ValueError: If the size is negative or any position coordinate is negative.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square object.

        Args:
            size (int): The initial size of the square (default: 0).
            position (tuple): The initial position of the square's top-left corner
                             (default: (0, 0)).
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""

        return self.__size ** 2

    def my_print(self):
        """Prints a representation of the square using "#" characters at its position."""

        if self.__size == 0:
            print()
        else:
            x, y = self.__position
            print(" " * x, end="")
            for i in range(self.__size):
                print("#" * self.__size, end="")
                if i < self.__size - 1 and y > 0:
                    print()
                print()
