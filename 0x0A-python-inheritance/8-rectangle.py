#!/usr/bin/python3
"""geometry class"""


class BaseGeometry():
    """
    A base class that provides a blueprint for other geometry classes.

    Methods:
        area(): Raises an exception indicating that it is not implemented.
        integer_validator(name, value):
        Validates if a given value is an integer and
        if it is greater than zero.

    """

    def __init__(self, width, height):
        """
        Initializes a BaseGeometry object with the
        given width and height values.

        Args:
            width (int): The width of the geometry object.
            height (int): The height of the geometry object.

        Returns:
            None

        Raises:
            ValueError: If the width or height is not a positive integer.
        """

        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Raises:
            Exception: Indicates that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a given value is an
        integer and if it is greater than zero.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
