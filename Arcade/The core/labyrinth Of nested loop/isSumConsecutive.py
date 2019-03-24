"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.
"""
def isSumOfConsecutive2(n):
    result = 0;
    for i in range(1,n):
        num = n
        sub = i
        while (num > 0):
            num -= sub
            sub += 1
        if (num==0):
            result += 1
    return result
