""""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
""""

def commonCharacterCount(s1, s2):
    count = 0
    for ch1 in s1 :
        line = s2[:]
        for ch2 in line :
            if ch1 == ch2:
                s2 = s2.replace(ch2,'',1)
                count += 1
                break
    return count
            
