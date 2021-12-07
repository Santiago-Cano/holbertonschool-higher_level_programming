#!/usr/bin/python3

""" 6-square
Defines class Square with private attribute size and public attribute area
Gets and sets size
Prints a square to stdout using '#'
"""


class Square:
    """ Class Square
    Args:
        size: size of a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization of a Square
        Attributes:
            __size: size of a square, defaults to 0 if no args
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Gets position attribute
        Returns:
            __position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Sets position attribute
        Raises:
            TypeError(position must be a tuple of 2 positive integers)
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) for i in value) and
                all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates area of a square
        Returns:
            Area of a square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints a square to stdout using '#'
        """
        if self.__size != 0:
            for j in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print("{}{}".format(" " * self.__position[0],
                                    "#" * self.__size))
            else:
                print("")
