#!/usr/bin/python3
"""this is base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            if list_objs is None:
                json.dump([], file)
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json.dump(list_dicts, file)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1) # type: ignore
            else:
                new = cls(1)
            new.update(**dictionary) # type: ignore
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
