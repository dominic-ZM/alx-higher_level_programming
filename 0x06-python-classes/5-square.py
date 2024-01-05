#!/usr/bin/python3

"""Creates a square class based on 4-square.py"""


class Square:
    """square class definition"""
    def __init__(self, size=0):
        """constructor with private variable"""
        self.__size = size

    @property
    def size(self):
        """property corresponding to length of square side"""
        return self.__size

    @size.setter
    def size(self, value):
        """corresponding setter for size property with value checking"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a function to calculate area and return it"""
        return self.__size * self.__size

    def my_print(self):
        """a function to print the square using '#'"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
