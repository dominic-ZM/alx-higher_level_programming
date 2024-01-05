#!/usr/bin/python3

"""Defines a square class based on 3-square.py"""


class Square:
    """square class definition"""
    def __init__(self, size=0):
        """constructor with private variable"""
        self.__size = size

    @property
    def size(self):
        """property representing length of square's side"""
        return self.__size

    @size.setter
    def size(self, value):
        """size's corresponding setter with value checking"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a method to calculate area and return it"""
        return self.__size * self.__size
