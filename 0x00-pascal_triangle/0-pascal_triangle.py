#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the
        Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
