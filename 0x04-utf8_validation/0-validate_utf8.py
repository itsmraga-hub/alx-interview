#!/usr/bin/python3
"""
    Write a method that determines if a given data set represents a
    valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to
handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    num_bytes = 0

    for byte in data:
        binary = bin(byte)[2:].rjust(8, '0')

        if num_bytes == 0:
            if binary[0] == '0':
                continue
            elif binary[:3] == '110':
                num_bytes = 1
            elif binary[:4] == '1110':
                num_bytes = 2
            elif binary[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            if binary[:2] == '10':
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
