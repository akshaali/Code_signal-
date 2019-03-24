"""
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.
"""
def isSmooth(arr):
    n = len(arr)
    if n % 2 != 0:
        mid = arr[int((n-1)/2)]
        if mid == arr[0] and mid == arr[-1]:
            return True
    if n % 2 == 0:
        mid = arr[int(n/2)-1] + arr[int(n/2)]
        if mid == arr[0] and mid == arr[-1]:
            return True
    return False

