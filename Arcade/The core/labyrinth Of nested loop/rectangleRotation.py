"""

A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example

For a = 6 and b = 4, the output should be
rectangleRotation(a, b) = 23.

The following picture illustrates the example, and the 23 points are marked green.
"""
import math
def rectangleRotation(a, b):
    count = 0
    k = math.radians(45)
    x1 = (a//2)*(math.cos(k))-(b//2)*(math.sin(k))
    y1 = (a//2)*(math.sin(k))+(b//2)*(math.cos(k))
    for i in range(-200,200):
        for j in range(-200,200):
            if((i-j+(y1-x1)>= 0) and (i-j-(y1-x1)<=0) and (i+j+(y1+x1)>=0 )and (i+j-(y1+x1)<=0)):
               count += 1
    return count
