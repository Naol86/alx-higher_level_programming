#!/usr/bin/python3
"""this is a class that check for list"""


class MyList(list):
    """inherit list"""
    def print_sorted(self):
        print(sorted(self))
