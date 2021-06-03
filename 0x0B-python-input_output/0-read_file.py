#!/usr/bin/python3
"""
Module 0-read_file

Read a file and print its contents to stdout
"""


def read_file(filename=""):
    """Read a file and print its contents to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
