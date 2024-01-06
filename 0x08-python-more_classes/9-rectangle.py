#!/usr/bin/python3

"""Defines a rectangle class based on 0-rectangle.py"""


class Rectangle:
    """Definition of rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """called when creating an instance"""
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Called when object is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

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

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        if isinstance(self.print_symbol, str):
            top_side = self.print_symbol * self.__width
        else:
            top_side = str(self.print_symbol) * self.__width
        if self.__height == 1:
            rectangle = top_side
        elif self.__height == 2:
            rectangle = f"{top_side}\n{top_side}"
        else:
            side = f"{top_side}\n"
            rectangle = f"{top_side}\n{side * (self.__height - 2)}{top_side}"
        return rectangle

    def __repr__(self):
        """Returns a string representation that can create a new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
