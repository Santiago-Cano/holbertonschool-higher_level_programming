#!/usr/bin/python3

""" 2-square
Defines class Square with private attribute size
"""


class Square:
    """ Class Square

    Args:
        size: size of a square
    """
    def __init__(self, size=0):
        """ Initialization of Square

        Attributes:
            __size: size of a square, defaults to 0 if not passed an argument
        """
        if type(size)is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
