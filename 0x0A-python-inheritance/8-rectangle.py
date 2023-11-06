#!/usr/bin/python3
"""this is inheritance from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle and provides functionalities
    for initializing the width and height of the rectangle
    and validating that they are integers.

    Example Usage:
    rectangle = Rectangle(5, 10)
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle object with the given width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
