"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:
https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/bishop.jpg?_tm=1551432802825
Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.

"""

def bishopAndPawn(bishop, pawn):
    if (abs(ord(bishop[0]) - ord(pawn[0])) == abs(ord(bishop[1]) - ord(pawn[1]))):
        return True
    return False
    
    

