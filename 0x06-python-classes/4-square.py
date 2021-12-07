#!/usr/bin/python3

""" 4-square
Defines class Square with private attribute size and public attribute area
Gets and sets size
"""


class Square:
    """ Class Square
    Args:
        size: size of a square
    """

    def __init__(self, size=0):
        """ Initialization of a Square
        Attributes:
            __size: size of a square, defaults to 0 if no args
        """

        if type(size)is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Gets size attribute
        Returns:
            __size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets size attribute
        Raises:
            TypeError(size must be an integer)
            ValueError(size must be >= 0)
        """
        if type(value)is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates area of a square
        Returns:
            Area of a square
        """
        return (self.__size ** 2)
