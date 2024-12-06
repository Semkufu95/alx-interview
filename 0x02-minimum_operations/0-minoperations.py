#!/usr/bin/python3
"""
A module to calculate minimu operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve
    exactly n 'H' characters.
    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if n
    is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
