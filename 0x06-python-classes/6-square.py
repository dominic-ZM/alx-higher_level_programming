#!/usr/bin/python3

"""Creates a square class based on 5-square.py"""


class Square:
    """square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor with private variable"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property representing length of square's side"""
        return self.__size

    @property
    def position(self):
        """property representing where to offset when printing"""
        return self.__position

    @size.setter
    def size(self, value):
        """corresponding setter for size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """corresponding setter for position property"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(elem, int) and elem > 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """function to calculate and return area of square"""
        return self.__size * self.__size

    def my_print(self):
        """a function to print the square"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for _ in range(self.__position[1]):
                    print()
            for x in range(self.__size):
                if self.__position[0] > 0:
                    for _ in range(self.__position[0]):
                        print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
