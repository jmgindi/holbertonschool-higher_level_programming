#!/usr/bin/python3
"""
Module 1-rectangle contains one class: Rectangle
"""


class Rectangle:
    """ Rectangle defines a rectangle

    Attributes:
        width (obj:`int`): width of rectangle
        height (obj:`int`): height of rectangle
        number_of_instances (obj:`int`): num of
            instances of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init for Rectangle class

        Args:
            width (obj:`int`): width of rectangle
            height (obj:`int`): height of rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ modifies width of rectangle

        Args:
            value (obj:`int`): value for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ modifies height of rectangle

        Args:
            value (obj:`int`): value for height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle
        if width or height is 0, perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ string representation function
        prints rectangle with hashes
        """
        rect_string = []
        for h in range(self.__height):
            for w in range(self.__width):
                rect_string.append(str(self.print_symbol))
            rect_string.append("\n")
        del rect_string[-1]
        return ''.join(rect_string)

    def __repr__(self):
        """ returns a string that can be used to
        create another instance of Rectangle
        """
        return ("Rectangle(width={:d}, height={:d})"
                .format(self.__width, self.__height))

    def __del__(self):
        """ prints "Bye rectangle..." when a rectangle
        is deleted
        """
        print("Bye Rectangle...")
        Rectangle.number_of_instances -= 1
