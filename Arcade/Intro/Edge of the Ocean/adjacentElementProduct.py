""""

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

""""


def adjacentElementsProduct(inputArray):
    i = len(inputArray)
    Multiple = inputArray[0]*inputArray[1]
    for a in range(0,i-1) :
        Multiple_temp = inputArray[a]*inputArray[a+1]
        if Multiple_temp > Multiple :
            Multiple = Multiple_temp
    return Multiple
