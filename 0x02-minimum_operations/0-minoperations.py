#!/usr/bin/python3
"""
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given a
    number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
"""

def minOperations(n):
    """
        minimum operations solution done returning the number of operations
    """
    if n <= 1:
        return 0
    
    # Initialize factors and operations
    factors = []
    operations = 0
    
    # Find factors of n
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # Calculate the sum of factors
    for factor in factors:
        operations += factor
    
    return operations
