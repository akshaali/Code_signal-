"""
Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).
"""
def leastFactorial(n):
    k = 1
    for i in range(1,n+1):
        k *=i
        if n > k and n < k*(i+1):
            return k*(i+1)
        if n == k :
            return k
        


