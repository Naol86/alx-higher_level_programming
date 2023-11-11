#!/usr/bin/python3
"""this is base class"""


class Base:
    """
    A class that keeps track of the number of objects created
    and assigns a unique ID to each object.

    Fields:
    - id: The unique ID assigned to each object.

    Methods:
    - __init__(self, id=None): The constructor of the class.
    Initializes the object with a unique ID.
    If an ID is provided as an argument, it assigns that ID to the object.
    Otherwise, it increments the static variable __nb_objects
    and assigns the incremented value as the ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor of the class. Initializes the object with a unique ID.
        If an ID is provided as an argument, it assigns that ID to the object.
        Otherwise, it increments the static variable __nb_objects and assigns
        the incremented value as the ID.

        Parameters:
        - id (int, optional): The ID to assign to the object. If not provided,
        a unique ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
