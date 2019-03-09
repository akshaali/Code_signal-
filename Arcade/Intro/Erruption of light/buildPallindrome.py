"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""
def buildPalindrome(st):
    st2 = st
    for i in range(len(st)):
        if checkpall(st[i:]):
            if i == 0:
                return st
            else :    
                ans = list(st)+list(st[:i][::-1])
                return ''.join(ans)
            
def checkpall(st1):
    if st1 == st1[::-1]:
        return True 
    else : 
        return False
