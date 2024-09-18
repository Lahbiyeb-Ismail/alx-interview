#!/usr/bin/python3

"""
Determine the minimum number of coins needed to make a given total.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make a given total.

    Args:
      coins (list of int): A list of the values of the available coins.
      total (int): The total amount of money to make change for.

    Returns:
      int: The minimum number of coins needed to make the total,
      or -1 if it is not possible to make the total with the
      given coins.

    Example:
      >>> makeChange([1, 2, 5], 11)
      3
      >>> makeChange([2], 3)
      -1
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
