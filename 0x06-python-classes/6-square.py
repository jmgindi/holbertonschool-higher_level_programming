#!/usr/bin/python3
class Square:
    """Square is a class that defines a square

    Attributes:
        size (obj:`int`): size of square
        area (obj:`int`): area of square
        position (obj:`int`): offset of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Init function for square class

        Args:
            size (obj:`int`): for size attribute
            position (obj:`int`): for position attribute
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Area calculates the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """returns size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """modifies size of a square

        Args:
            value (obj:`int`): value to modify size to
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        """
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or value[0] < 0 or\
           type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of two integers")
        self.__position = value

    def my_print(self):
        """prints the square in hashes
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print((" " * self.__position[0]) + ('#' * self.__size))
