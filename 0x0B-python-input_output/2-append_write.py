#!/usr/bin/python3
"""
Module 2-append_write

Append a string to the end of a text file, return number of characters added
"""


def append_write(filename="", text=""):
    """Appends string to end of text file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
