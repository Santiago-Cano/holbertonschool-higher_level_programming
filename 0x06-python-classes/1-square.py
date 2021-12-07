#!/usr/bin/python3

"""1-square
A square class with an empty size private attribute
"""


class Square:
    """ Class Square
     Args:
        size: Size of a square
    """
    def __init__(self, size):
        """ Initializes square object and size
        Attributes:
            __size: Size of a square
        """
        self.__size = size
