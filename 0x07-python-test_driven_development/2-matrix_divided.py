#!/usr/bin/python3
"""
Module 2-matrix_divided contains one function:
matrix_divided(matrix, div)
"""
def matrix_divided(matrix, div):
    """ matrix_divided returns a new matrix containing
    all elements from matrix divided by div

    Args:
        matrix: matrix to divide. must have equal-length rows
        div: divisor. must be int != 0
    """
    if type(matrix) is not list or len(matrix) < 2:
        raise TypeError("matrix must be a matrix (list of lists)" \
                        " of integers/floats")
    for line in matrix:
        if type(line) is not list:
            raise TypeError("matrix must be a matrix (list of " \
                            "lists) of integers/floats")
        if len(line) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have" \
                            " the same size")
        for i in line:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of " \
                                "lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    return[[round(i / div, 2) for i in line] for line in matrix]
