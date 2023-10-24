#!/usr/bin/python3
"""oop learning day 1"""


class Square:
    """this is a square class"""

    def __init__(self, size=0, position=(0, 0)):
        if type(position) != tuple or (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = position
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=None):
        if value is not None:
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or (value[0] > 0 or value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        pos = self.__position
        p1 = pos[0]
        p2 = pos[1]
        if self.__size == 0:
            print()
        else:
            for i in range(p2):
                print()
            for i in range(self.__size):
                for h in range(p1):
                    print('_', end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
