"""
Reversing an array can be a tough task, especially for a novice programmer. Mary just started coding, so she would like to start with something basic at first. Instead of reversing the array entirely, she wants to swap just its first and last elements.

Given an array arr, swap its first and last elements and return the resulting array.

Example

For arr = [1, 2, 3, 4, 5], the output should be
firstReverseTry(arr) = [5, 2, 3, 4, 1].
"""
def firstReverseTry(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return(arr[::-1])
    else:
        b = arr[0]
        arr[0] = arr[-1]
        arr[-1] = b 
        return arr
        

