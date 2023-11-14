#!/usr/bin/python3

from attr import validate
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle shape.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The id of the rectangle.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle object with the given width, height,
        x-coordinate, y-coordinate, and id.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle.Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        self.validator("width", width)
        self.validator("height", height)
        self.validator("x", x)
        self.validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError("{} must be >= 0".format(name))
        return True

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.
        """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.
        """
        self.validator('height', value)
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
            value (int): The new x-coordinate of the rectangle.
        """
        self.validator('x', value)
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle.

        Args:
            value (int): The new y-coordinate of the rectangle.
        """
        self.validator('y', value)
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for i in kwargs:
                if i == "width":
                    self.__width = kwargs[i]
                elif i == "height":
                    self.__height = kwargs[i]
                elif i == "x":
                    self.__x = kwargs[i]
                elif i == "y":
                    self.__y = kwargs[i]
                elif i == "id":
                    self.id = kwargs[i]
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def to_dictionary(self):
        tem = {'id': self.id, 'width': self.__width,
               'height': self.__height, 'x': self.__x, 'y': self.__y}
        return tem
