#!/usr/bin/python3
"""this is more on class """


class Rectangle:
    """start working on class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def print(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        ans = ""
        if self.__width == 0 or self.__height == 0:
            return ans
        for i in range(self.__height):
            ans += "#" * self.__width
            if i != self.__height - 1:
                ans += "\n"
        return ans

    def __repr__(self):
        ans = f"Rectangle({self.__width}, {self.__height})"
        return ans

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
