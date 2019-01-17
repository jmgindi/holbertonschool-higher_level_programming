#!/usr/bin/python3
"""
module contains 1 class:
    Square
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Square inherits from rectangle. Its width and height
    must be the same, and together are held in size
    """

    def __init__(self, size):
        """ init method for square

        Args:
            size (obj:`int`): side length of square
        """
        self.integer_validator("size", size)
        super(Rectangle, self).__init__()
        self.__size = self._Rectangle__width = self._Rectangle__height = size

    def area(self):
        """ returns the area of a square
        """
        return self.__size ** 2
