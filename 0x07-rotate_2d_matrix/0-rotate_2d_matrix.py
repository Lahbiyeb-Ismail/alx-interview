#!/usr/bin/python3

"""
Rotate a given 2D matrix in-place by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix in-place by 90 degrees clockwise.

    Args:
      matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
      None: The function modifies the input matrix in-place.
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # swapping mat[i][j] and mat[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        left_index = 0
        right_index = len(matrix[i]) - 1

        while left_index <= right_index:
            temp = matrix[i][left_index]
            matrix[i][left_index] = matrix[i][right_index]
            matrix[i][right_index] = temp

            left_index += 1
            right_index -= 1
