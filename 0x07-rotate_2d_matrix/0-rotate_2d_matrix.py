#!/usr/bin/env python3
'''
A module to rotate a 2d matrix
'''

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    :param matrix: 2D list representing the matrix
    """
    n = len(matrix)
    # Step 1: Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

        
