"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.

"""
import numpy
def digitsProduct(product):
    if len(str(product)) == 1 and product > 0:
        return product 
    for x in range(10,10000):
        l = list(int(s) for s in str(x))
        num = numpy.prod(l)
        if num == product:
            return int("".join(str(p) for p in l )) 
    return(-1)
                
