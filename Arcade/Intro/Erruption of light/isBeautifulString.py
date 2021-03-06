"""
A string is said to be beautiful if each letter of the alphabet appears at most as many times as than the previous letter; ie: b occurs no more times than a; c occurs no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.
"""

def isBeautifulString(inputString):
    new = sorted(set(inputString))
    li = []
    for i,j in enumerate('abcdefghijklmnopqrstuvwxyz'):
        li.insert(i,inputString.count(j))
    li_sorted = sorted(li)
    print(li_sorted,li)
    if li_sorted[::-1] == li:
        return True
    return False

