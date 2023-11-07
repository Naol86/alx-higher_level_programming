#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a new string after a specified search string in a text file.

    Args:
        filename (str): The name of the text file to be modified.
        search_string (str): The text to search for in the file.
        new_string (str): The text to be inserted after the search string.

    Returns:
        None. Modifies the specified text file directly.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
