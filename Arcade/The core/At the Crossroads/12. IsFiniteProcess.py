"""
def extraNumber(a, b, c):
    if a==b:
        return c
    if a==c:
        return b
    if b==c:
        return a


"""

def isInfiniteProcess(a, b):
    if a > b :
        return True
    if a < b:
        p = b-a
        if a %2 == 0 and b % 2 != 0 and p % 2 != 2:
            return True 
        if a %2 != 0 and b % 2 == 0 and p % 2 != 2:
            return True
        if a%2 !=0 and b%2 != 0 and p%2 != 0:
            return True
    return False
