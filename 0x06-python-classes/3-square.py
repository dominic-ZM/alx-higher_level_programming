#!/usr/bin/python3

"""Creates a square class based on 2-square.py"""


class Square:
    """square definition"""
    def __init__(self, size=0):
        """constructor with value checking"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method to calculate and return area"""
        return self.__size * self.__size
