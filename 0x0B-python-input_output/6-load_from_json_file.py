#!/usr/bin/python3
"""create an object from a file"""

import json


def load_from_json_file(filename: str) -> dict:
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        dict: The loaded JSON object.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contents are not valid JSON.
    """
    with open(filename, "r") as file:
        return json.load(file)
