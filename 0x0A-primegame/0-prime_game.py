#!/usr/bin/python3

"""
Determines the overall winner of a series of prime number games
"""


def isWinner(x, nums):
    """
    Determines the overall winner of a series of prime number games.

      x (int): The number of rounds to be played.
      nums (list of int): A list of integers where each integer represents
                the upper limit of the range of numbers (1 to n)
                to be used in each game.

      str: The name of the overall winner ("Maria" or "Ben"). If there is no
         winner (i.e., both players win an equal number of games), returns
         None.

    The game rules are as follows:
    - Two players, Maria and Ben, take turns choosing a prime number from the
      remaining list of numbers from 1 to n.
    - After choosing a prime number, all multiples of that prime number are
      removed from the list.
    - The player who cannot make a move loses the game.
    - The function simulates x rounds of the game and determines the overall
      winner based on the number of games won by each player.
    """

    def is_prime(num):
        """
        Determine if a given number is a prime number.

        Args:
          num (int): The number to check for primality.

        Returns:
          bool: True if the number is prime, False otherwise.

        A prime number is a natural number greater than 1 that
        has no positive divisors other than 1 and itself.
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        """
        Simulates a game where two players, Maria and Ben,
        take turns removing numbers from a list of integers from 1 to n.
        The player who cannot make a move loses the game.

        The rules are as follows:
        - Players take turns choosing a prime number from the remaining list.
        - After choosing a prime number, all multiples of that prime number
        are removed from the list.
        - The game continues until no prime numbers are left in the list.

        Args:
          n (int): The upper limit of the range of numbers (1 to n) to be
          used in the game.

        Returns:
          int: The winner of the game. 0 if Maria wins, 1 if Ben wins.
        """
        remaining = list(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        while True:
            prime_found = False
            for num in remaining:
                if is_prime(num):
                    prime_found = True
                    prime = num
                    break
            if not prime_found:
                return 1 - turn  # The player who cannot move loses
            remaining = [num for num in remaining if num % prime != 0]
            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
