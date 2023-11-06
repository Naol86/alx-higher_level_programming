#!/usr/bin/python3
"""geometry class"""


class BaseGeometry():
    """
    A base class for other geometry classes.

    Methods:
    - area(): Raises an exception indicating that it is not implemented.
    """

    def area(self):
        """
        Raises:
            Exception: Indicates that the method is not implemented.

        This method is meant to be overridden in the
        derived classes to calculate the area of the specific geometry.
        """
        raise Exception("area() is not implemented")
