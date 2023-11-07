#!/usr/bin/python3
"""this is the file reading"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints them to the console.

    Args:
        filename (str, optional): The name of the file to be
        read. If no filename is provided, an empty string will be used.

    Returns:
        None

    Example:
        read_file("example.txt")

    This code will read the contents of the file named "example.txt"
    and print them to the console.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
