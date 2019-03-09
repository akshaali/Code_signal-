"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
"""

def deleteDigit(n):
    n1 = list(str(n))
    l = len(n1)
    li = ['' for i in range(l)]
    #print(li)
    for j in range(l):
        temp = (n1)
        print(temp)
        temp =  temp[:j] + temp[j+1:]
        li[j] = ''.join(temp)
    #print(li)
    return int(max(li))
