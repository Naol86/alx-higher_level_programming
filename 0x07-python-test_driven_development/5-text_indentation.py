#!/usr/bin/python3
"""
printing text
"""


def text_indentation(text):
    """"
    print text using 2 space after . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    check = ['.', '?', ":"]
    for i in text:
        print(i, end="")
        if i in check:
            print()
            print()
