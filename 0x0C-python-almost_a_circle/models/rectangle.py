#!/usr/bin/python3
"""this is a rectangle class"""
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
        """
        Returns a string representation of the Rectangle object.

        The string representation includes the id, x-coordinate,
        y-coordinate, width, and height of the rectangle.

        Returns:
            A string representation of the Rectangle object in the
            format "[Rectangle] (id) x/y - width/height".
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def validator(self, name, value):
        """
        Validate the values of the attributes in the Rectangle class.

        Args:
            name (str): The name of the attribute to be validated.
            value (int): The value of the attribute to be validated.

        Returns:
            bool: True if the attribute value is valid.

        Raises:
            TypeError: If the attribute value is not an integer.
            ValueError: If the attribute value does not meet
            the specified conditions.

        Example Usage:
            rect = Rectangle(5, 3, 2, 1)
            rect.validator("width", 5)  # No error
            rect.validator("width", "abc")  # Raises TypeError
            rect.validator("width", -5)  # Raises ValueError
        """
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
        """get area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """
        Prints a visual representation of the rectangle
        shape using the '#' character.

        Example Usage:
        rect = Rectangle(5, 3, 2, 1)
        rect.display()
        Output:
            #####
            #####
            #####

        Inputs: None

        Flow:
        1. Prints a number of empty lines equal to the
            y-coordinate of the rectangle.
        2. For each row of the rectangle (height), it prints
            a number of spaces equal to the x-coordinate of the rectangle.
        3. Within each row, it prints a number of '#' characters
            equal to the width of the rectangle.
        4. After printing each row, it moves to the next line.

        Outputs: None
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        Update the attributes of a rectangle object.

        Args:
            *args: Positional arguments. The first argument is
            the id of the rectangle, followed by the width, height, x,
            and y values in that order.
            **kwargs: Keyword arguments. The attributes to be updated
            can be passed as keyword arguments. The available attributes
            are width, height, x, y, and id.

        Returns:
            None

        Example Usage:
            rect = Rectangle(5, 3, 2, 1)
            rect.update(10, 7, x=4, y=2)
            print(rect.width)  # Output: 10
            print(rect.height)  # Output: 7
            print(rect.x)  # Output: 4
            print(rect.y)  # Output: 2
        """
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
        """return a dict of rectangle"""
        tem = {'id': self.id, 'width': self.__width,
               'height': self.__height, 'x': self.__x, 'y': self.__y}
        return tem
