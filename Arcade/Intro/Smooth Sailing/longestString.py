""""

Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

""""

def allLongestStrings(inputArray):
    r = len(inputArray)
    longest_length = 0
    long_array = []
    list(long_array)
    for i in range(r):
        if len(inputArray[i])>longest_length:
            longest_length = len(inputArray[i])
    for j in range(r):
            if len(inputArray[j]) == longest_length:
                long_array.append(inputArray[j])
    return long_array
                
            
