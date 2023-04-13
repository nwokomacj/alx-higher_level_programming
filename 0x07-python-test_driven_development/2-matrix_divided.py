#!/usr/bin/python3
"""This module will divide all elements in a matrix"""


def matrix_divided(matrix, div):
    """A function that divides all element of a matrix
    Args:
        matrix: A list of lists of integers or floats
        div: The divisor, must be an integer or float
    Returns:
        A new matrix which is the result of the division
    Raises:
        TypeError: When the matrix is not a list of lists of integers or floats
        TypeError: When each row is not of equall size
        TypeError: When div is neither integer or float
        ZeroDivisionError: When div is equall to zero
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []

    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        new_matrix.append(new_row)

    return(new_matrix)
