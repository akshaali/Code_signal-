"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.
"""



def largestNumber(n):
    p = 0
    for i in range(n):
        if i != n-1:
            p += 9*(10**(n-i-1))
        if i == n-1:
            p +=9
    return p
        

