#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
"""
"""

class Square(Rectangle):
    """ Square class

    Attributes:
        size (obj:`int`): side length
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init method for square

        Args:
            size: side length
            x: x offset
            y: y offset
            id: id for object, or none
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str replacement for square
        """
        return (
            "[Square] (" + str(self.id) + ") " +
            str(self.x) + "/" + str(self.y) +
            " - " + str(self.width)
            )

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """ updates a square with new values
        """
        allowed = ['id', 'size', 'x', 'y']
        if args:
            for att, arg in zip(allowed, args):
                setattr(self, att, arg)
        elif kwargs:
            for att, arg in kwargs.items():
                if att in allowed:
                    setattr(self, att, arg)

    def to_dictionary(self):
        """ returns a dictionary representation of a square
        for json encoding
        """
        return {
            k.replace("_Rectangle__", "").replace(
                "_Square__", ""
            ): v for k, v in self.__dict__.items()
            if k not in ["_Rectangle__width", "_Rectangle__height"]
        }
