#!/usr/bin/python3

"""Creates square based on 1-square.py"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        """constructor with value checking"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
