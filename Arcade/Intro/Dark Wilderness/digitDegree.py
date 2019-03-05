"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.

"""

def digitSum(num):
    return sum([int(char) for char in str(num)])
def digitDegree(n):
    if n/10 ==0:
        return 0
    counter = 0
    while int(n/10) != 0:
        n = digitSum(n)
        counter +=1
    return counter
        
    
    

