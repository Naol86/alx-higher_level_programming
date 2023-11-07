#!/usr/bin/python3
"""this is obj to a txt"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj (any): The object to be saved to the JSON file.
        filename (str): The name of the file to which the object will be saved.

    Returns:
        None

    Example:
        # Saving a dictionary to a JSON file
        data = {"name": "John", "age": 30}
        save_to_json_file(data, "output.json")
        # The contents of data will be written to output.json in JSON format

        # Saving a list to a JSON file
        data = [1, 2, 3, 4, 5]
        save_to_json_file(data, "output.json")
        # The contents of data will be written to output.json in JSON format
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
