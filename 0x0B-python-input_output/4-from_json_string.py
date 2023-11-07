#!/usr/bin/python3
"""this get json object"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string into a JSON object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        dict: The parsed JSON object from the input string.
    """
    return json.loads(my_str)
