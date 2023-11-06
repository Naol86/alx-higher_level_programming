#!/usr/bin/python3
"""geometry class"""


class BaseGeometry():
    """
    A base class that provides a blueprint for other geometry classes.

    Methods:
        area(): Raises an exception indicating that it is not implemented.
        integer_validator(name, value): Validates if a
        given value is an integer and if it is greater than zero.

    """

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
