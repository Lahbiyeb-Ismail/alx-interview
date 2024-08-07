#!/usr/bin/python3


"""
Function that calculates the minimum number
of operations required to reach a given number.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations
    required to reach a given number.

    Args:
      n (int): The target number.

    Returns:
      int: The minimum number of operations required.

    Examples:
      >>> minOperations(6)
      9
      >>> minOperations(12)
      16
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
