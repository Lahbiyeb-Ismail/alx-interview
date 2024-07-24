#!/usr/bin/python3

"""
Generate Pascal's triangle up to the given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
      n (int): The number of rows to generate in Pascal's triangle.

    Returns:
      list: A list of lists representing Pascal's triangle.

    Example:
      >>> pascal_triangle(5)
      [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    result = [[1]]

    for _ in range(n - 1):
        tempList = [0] + result[-1] + [0]
        newRow = []
        for j in range(len(result[-1]) + 1):
            newRow.append(tempList[j] + tempList[j + 1])

        result.append(newRow)

    return result
