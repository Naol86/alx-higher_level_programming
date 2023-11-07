#!/usr/bin/python3
"""this is appending in a file"""


def append_write(filename="", text=""):
    """
    Opens the specified file in append mode and writes the
    given text to the file.

    Args:
        filename (str, optional): The name of the file to be opened.
        Defaults to an empty string.
        text (str, optional): The text to be written to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "+a", encoding='utf-8') as file:
        return file.write(text)
