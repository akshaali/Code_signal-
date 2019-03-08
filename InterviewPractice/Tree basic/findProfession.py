"""
Consider a special family of Engineers and Doctors. This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.

Example

For level = 3 and pos = 3, the output should be
findProfession(level, pos) = "Doctor".
"""

def findProfession(level, pos):
    """
    Level 1: E
    Level 2: ED
    Level 3: EDDE
    Level 4: EDDEDEED
    Level 5: EDDEDEEDDEEDEDDE 
    
    Level input is not necessary because first elements are the same
    The result is based on the count of 1's in binary representation of position-1
    If position is even, then Engineer; Else Doctor
    """
    bits  = bin(pos-1).count('1')
    if bits%2 == 0: 
        return "Engineer"
    else:
        return "Doctor"

    
    
