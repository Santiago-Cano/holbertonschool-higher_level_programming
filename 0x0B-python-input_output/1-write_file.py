#!/usr/bin/python3

"""
Module 1-write_file
Write a string to a text file and return the number of characters written
"""


def write_file(filename="", text=""):
    """Write a string to a text file, return number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
