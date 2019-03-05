""""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

""""
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    l = len(inputArray)
    new_array = []
    for i in range(l):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray
    

