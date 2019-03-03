""""

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
                      
                      
"""""

def addBorder(picture):
    length = len(picture)
    pic = len(picture[0])
    final = []
    final.append(str(pic*'*'+'**'))
    for s in range(length) :
        final.append(str('*'+picture[s]+'*'))
    final.append(str(pic*'*'+'**'))
    '\n'.join(final)
    return final
