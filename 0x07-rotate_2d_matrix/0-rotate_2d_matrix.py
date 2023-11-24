#!/usr/bin/python3
""" Module for Rotate 2D Matrix
"""


def transpose_matrix(matrix, n):
    """transpose_matrix
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """reverse_matrix
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix
    """
    n = len(matrix)
    # print(n)

    transpose_matrix(matrix, n)
    reverse_matrix(matrix)

    return matrix
