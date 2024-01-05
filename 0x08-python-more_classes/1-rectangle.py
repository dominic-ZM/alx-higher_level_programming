#!/usr/bin/python3

"""Defines a rectangle class based on 0-rectangle.py"""


class Rectangle:
    """Definition of rectangle class"""
    def __init__(self, width=0, height=0):
        """called when creating an instance"""
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height, after validating it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width, after validating it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
