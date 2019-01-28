#!/usr/bin/python3
"""
module contains 1 class:
    Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ rectangle class - inherits from Base

    Attributes:
        width (obj:`int`): width of rectangle
        height (obj:`int`): height of rectangle
        x (obj:`int`): x offset of rectangle
        y (obj:`int`): y offset of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """ str method replacement for Rectangle
        """
        return (
            "[Rectangle] (" + str(self.id) + ") " +
            str(self.__x) + "/" + str(self.__y) + " - " +
            str(self.__width) + "/" + str(self.__height)
        )

    def int_validator(self, key, value):
        """ simple value validator with error handling

        Args:
            key: key to return errors with
            value: value to check
        """
        if type(value) is not int:
            raise TypeError(key + " must be an integer")
        elif key is "width" or key is "height":
            if value <= 0:
                raise ValueError(key + " must be > 0")
        elif key is "x" or key is "y":
            if value < 0:
                raise ValueError(key + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_validator("y", value)
        self.__y = value

    def area(self):
        """ returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle in "#"s
        """
        if self.__y > 0:
            print("\n" * (self.__y), end="")
        for c in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ updates the values of a rectangle's attributes
        """
        allowed = ['id', 'width', 'height', 'x', 'y']
        if args:
            for att, arg in zip(allowed, args):
                setattr(self, att, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in allowed:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation of a
        rectangle for json encoding
        """
        return {k.replace(
            "_Rectangle__", ""
        ): v for k, v in self.__dict__.items()}
