#!/usr/bin/python3
"""
A module to calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    Function to calculate perimeter of an island
    Args: grid (The perimeter of whole area)
    """
    perimeter = 0
    heights = len(grid)
    widths = len(grid[0]) if heights > 0 else 0

    for height in range(heights):
        for width in range(widths):
            if grid[height][width] == 1:
                perimeter += 4

                # Check cells for row and columns
                if height > 0 and grid[height - 1][width] == 1:
                    perimeter -= 1
                if height < heights - 1 and grid[height + 1][width] == 1:
                    perimeter -= 1
                if width > 0 and grid[height][width - 1] == 1:
                    perimeter -= 1
                if width < widths - 1 and grid[height][width + 1] == 1:
                    perimeter -= 1

    return perimeter
