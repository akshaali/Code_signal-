""""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.


"""""

def palindromeRearranging(inputString):
    l = len(inputString)
    b = []
    tolerance = 0
    for i in range(l):
        if inputString[i] not in b:
            if inputString.count(inputString[i])%2 != 0:
                if inputString.count(inputString[i]) == 1:
                    tolerance +=1
                elif inputString.count(inputString[i])%2 == 1:
                    tolerance +=1
        b.append(inputString[i])
    if tolerance > 1:
        return False
    return True
        
