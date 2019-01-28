"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.
"""



def addTwoDigits(n):
    n = str(n)
    return int(n[0])+int(n[1])

