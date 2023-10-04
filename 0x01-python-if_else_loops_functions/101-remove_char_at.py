#!/usr/bin/python3

def remove_char_at(str, n):
    if n < len(str) - 1:
        str = str[: n] + str[n + 1:]
    return str
