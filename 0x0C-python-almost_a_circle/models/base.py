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
        """
        Convert a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be
            converted into a JSON string.

        Returns:
            str: A JSON string representing the input list of dictionaries.

        Example:
            >>> list_dicts = [{'id': 1, 'name': 'John'},
            {'id': 2, 'name': 'Jane'}]
            >>> result = Base.to_json_string(list_dicts)
            >>> print(result)
            '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved to the JSON file.

        Returns:
            None

        Raises:
            None

        Example Usage:
            # Create a list of objects
            objs = [obj1, obj2, obj3]

            # Call the save_to_file method
            Base.save_to_file(objs)
        """
        file_name = str(cls.__name__) + ".json"
        with open(file_name, 'w') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string into a list of dictionaries.

        Args:
            json_string (str): A JSON str representing a list of dictionaries.

        Returns:
            list: A list of dictionaries representing the parsed JSON string.

        Example:
            json_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
            result = Base.from_json_string(json_string)
            print(result)
            # Output: [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class based on a dictionary of attributes.

        Args:
            **dictionary: A dictionary containing the attributes and their
            values for the new instance of the class.

        Returns:
            The newly created instance of the class with the attributes set
            according to the values in the dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
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
