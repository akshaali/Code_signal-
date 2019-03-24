"""
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
"""
def isPower(n):
    for j in range(1,21):
        for i in range(2,9):
            if n == j**i:
                return True
    return False 

