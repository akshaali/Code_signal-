"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
"""

def longestDigitsPrefix(inputString):
    import re
    prefix = inputString.split(' ')[0]
    if not prefix or prefix.isdigit():
        return prefix
    elif prefix[0].isdigit():
        s = re.split('[a-z]+', inputString)
        return s[0]
    return ''

