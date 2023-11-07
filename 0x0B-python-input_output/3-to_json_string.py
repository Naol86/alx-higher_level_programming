#!/usr/bin/python3
"""this is a file to change in json"""

import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON string representation.

    Args:
        my_obj: The object to be converted.

    Returns:
        A JSON string representation of the input object.

    Example:
        obj = {"name": "John", "age": 30}
        json_str = to_json_string(obj)
        print(json_str)
        # Output: {"name": "John", "age": 30}
    """
    return json.dumps(my_obj)
