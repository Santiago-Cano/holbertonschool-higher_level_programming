#!/usr/bin/python3
""" Contains Square Class """

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of Square class

        Args:
            size: size of square instance
            x: horizontal axis of the square instance
            y: vertical axis of the square instance
            id: id of the square instance
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ Size setter """
        self.width = size
        self.height = size

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Updates instance attributes according to arguments passed"""
        if len(args) != 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Returns the dictionary representation of a square instance """
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y

        return dict
