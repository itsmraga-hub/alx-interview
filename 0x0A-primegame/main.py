#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
print("Winner: {}".format(isWinner(-1, [10])))
print("Winner: {}".format(isWinner(100, [...])))
print("Winner: {}".format(isWinner(10000, [...])))

