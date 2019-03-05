""""
Given a string, replace each of its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
""""

def alphabeticShift(inputString):
    new_str = []
    for i, r in enumerate(inputString):
        if ord(r) == 122:
            new_str.insert(i, chr(97))
        else:
            f = ord(r) + 1
            new_str.insert(i, chr(f))
    return ''.join(new_str)

