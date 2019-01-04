#!/usr/bin/python3
class Square:
    """ Square is a class that defines a square

    Attributes:
        size (obj:`int`): size of square
        area (obj:`int`): area of square

    """

    def __init__(self, size=0):
        """ Init function for square class

        Args:
            size (obj:`int`): for size attribute
            area (obj:`int`): size squared

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
