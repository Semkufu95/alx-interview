#!/usr/bin/python3
"""
An algortihm to print pascahal's triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        # Create a new row based on the previous row
        prev_row = triangle[-1]
        # New row starts and ends with 1
        new_row = [1]
        for j in range(1, len(prev_row)):
            # Sum two adjacent numbers from the previous row
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
