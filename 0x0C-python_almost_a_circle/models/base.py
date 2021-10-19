#!/usr/bin/python3
"""Contains Base class, which will function as the base of all other classes"""


class Base:
    """ Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of Base class

        Args:
             id: id of each instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
