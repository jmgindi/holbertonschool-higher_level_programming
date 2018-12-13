#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in range(len(matrix)):
        square_matrix.append([i ** 2 for i in matrix[row]])

    return square_matrix
