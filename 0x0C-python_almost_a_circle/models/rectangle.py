#!/usr/bin/python3
""" Contains Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of Rectangle class

        Args:
             width: width of the rectangle instance
             height: height of the rectangle instance
             x: horizontal axis of the rectangle
             y: vertical axis of the rectangle
             id: id of each instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of a Rectangle Instance """
        return self.width * self.height

    def display(self):
        """Prints a representation of a Rectangle Instance using # to stdout"""

        for h in range(self.height):
            for w in range(self.width):
                print("#", end="")
            print("")
