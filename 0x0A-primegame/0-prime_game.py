#!/usr/bin/python3
"""
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
"""


def isWinner(x, nums):
    """
        Return: name of the player that won the most rounds
    """

    if ... in nums:
        return None

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        """
        Return: name of the player that won the most rounds
        """
        if n < 2:
            return None

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] ^ 1

            if is_prime(i):
                dp[i] = 1

        return "Ben" if dp[n] == 1 else "Maria"

    winners = [calculate_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
