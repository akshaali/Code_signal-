"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

"""

def valid(cell):
    if len(cell)>2:
        return False
    try:
        if cell[0] not in ['a','b','c','d','e','f','g','h']:
            return False
        if int(cell[1]) not in range(1,9):
            return False
    except:
        return False
    return True
def chessKnight(cell):
    a = 0
    if not valid(cell):
        return 0
    check1 = chr(ord(cell[0])+1) + str((int(cell[1])+2))
    if valid(check1):
        a +=1
    check2 = chr(ord(cell[0])+2) + str((int(cell[1])+1))
    if valid(check2):
        a +=1
    check3 = chr(ord(cell[0])+2) + str((int(cell[1])-1))
    if valid(check3):
        a +=1
    check4 = chr(ord(cell[0])-1) + str((int(cell[1])+2))
    if valid(check4):
        a +=1
    check5 = chr(ord(cell[0])-2) + str((int(cell[1])+1))
    if valid(check5):
        a +=1
    check6 = chr(ord(cell[0])+1) + str((int(cell[1])-2))
    if valid(check6):
        a +=1
    check7 = chr(ord(cell[0])-1) + str((int(cell[1])-2))
    if valid(check7):
        a +=1
    check8 = chr(ord(cell[0])-2) + str((int(cell[1])-1))
    if valid(check8):
        a +=1
    return a 
