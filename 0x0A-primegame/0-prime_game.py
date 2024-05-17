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
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    if ... in nums:
        return None

    def filter_primes(max_n):
        """
            Filter prime numbers: Returns a list of prime numbers
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(max_n ** 0.5) + 1):
            if is_prime[start]:
                for i in range(start * start, max_n + 1, start):
                    is_prime[i] = False
        primes_list = []
        for i, prime in enumerate(is_prime):
            if prime:
                primes_list.append(i)
        return primes_list

    max_number = max(nums)
    primes_list = filter_primes(max_number)
    prime_set = set(primes_list)
    
    def result(n):
        """
           Returns Result name of winner
        """
        numbers = set(range(1, n + 1))
        current_player = 0 
        
        while True:
            available_prime = None
            for p in primes_list:
                if p in numbers:
                    available_prime = p
                    break
            
            if available_prime is None:
                return 1 - current_player
            
            to_remove = set(range(available_prime, n + 1, available_prime))
            numbers.difference_update(to_remove)
            
            current_player = 1 - current_player
    results = {n: result(n) for n in set(nums)}
    
    maria_wins = sum(1 for n in nums if results[n] == 0)
    ben_wins = sum(1 for n in nums if results[n] == 1)
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
