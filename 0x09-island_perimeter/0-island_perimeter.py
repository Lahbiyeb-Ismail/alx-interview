#!/usr/bin/python3

"""
Calculate the perimeter of an island represented by
1s in a grid of 0s and 1s.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by
    1s in a grid of 0s and 1s.

    Args:
      grid (List[List[int]]): A 2D list representing the
      grid where 1s are land and 0s are water.

    Returns:
      int: The perimeter of the island.

    The function iterates through each cell in the grid.
    For each land cell (1), it checks its four
    neighboring cells (up, down, left, right).
    If a neighboring cell is water (0) or out of bounds,
    it contributes to the perimeter.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check up
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check down
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
