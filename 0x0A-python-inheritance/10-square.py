#!/usr/bin/python3
"""this is square"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Inherits from the Rectangle class and adds functionality
    specific to squares.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        self.integer_validator("size", size)
        if size > 0:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
