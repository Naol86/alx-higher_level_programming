#!/usr/bin/python3
"""this is square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape.

    Inherits properties and methods from the `Rectangle` class.
    Overrides the `__str__` method to provide a custom string representation.
    Adds a `size` property and setter method to manipulate the width
    and height of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object with the given size, x and y
        coordinates, and id.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The unique identifier of the square object.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square object.

        Returns:
            str: The string representation of the square object.
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If the value is not a positive integer.

        Returns:
            None
        """
        Square.validator(self, "width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of a square object.

        Args:
            *args: Variable-length argument list that can contain the
            square's id, width, height, x, and y in that order.
            **kwargs: Variable-length keyword argument list that can
            contain the square id, width, height, x, and y as key-value pairs.

        Returns:
            None

        Example Usage:
            square = Square(5)  # Create a square object with size 5
            square.update(1, 10, 20)  # Update the square's id, width,
            height, x, and y using positional arguments
            print(square)  # Output: [Square] (1) 10/20 - 10

            square.update(id=2, size=7, y=15)  # Update the square's id,
            width, height, and y using keyword arguments
            print(square)  # Output: [Square] (2) 10/15 - 7
        """
        if len(args) == 0:
            for i in kwargs:
                setattr(self, i, kwargs[i])
        else:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
                if i == "id":
                    self.id = kwargs[i]
                elif i == "size":
                    self.width = self.height = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """
        Returns a dictionary representation of the object's attributes.

        Returns:
            dict: A dictionary with keys 'id', 'size', 'x', and 'y'
            representing the object's attributes.
        """
        tem = {'id': self.id, 'size': self.width,
               'x': self.x, 'y': self.y}
        return tem
