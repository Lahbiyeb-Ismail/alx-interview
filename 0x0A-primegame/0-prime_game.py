#!/usr/bin/python3

""" Determines the winner of a prime number game between Maria and Ben """


def find_primes(num):
    """
    Finds all prime numbers up to a given number.

    Args:
      num (int): The upper limit (inclusive) to find prime numbers.

    Returns:
      List[int]: A list of prime numbers up to the specified limit.
    """
    primes = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, num + 1) if primes[p]]
    return prime_numbers


def isWinner(x, nums):
    """
    Determines the winner of a prime number game between Maria and Ben.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): List of integers representing the upper limit
    for each round.

    Returns:
    str: The name of the player with the most wins ("Maria" or "Ben").
       Returns None if there is a tie or if the input is invalid.
    """
    if not x or not nums:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        primes = find_primes(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
